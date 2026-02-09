import os, cv2, numpy as np
from flask import Flask, render_template, request, jsonify
from flask import send_from_directory
from insightface.app import FaceAnalysis

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FACE_DIR = os.path.join(BASE_DIR, "faces")
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "db.npy")

os.makedirs(DATA_DIR, exist_ok=True)

app = Flask(__name__)

# =========================
# 얼굴 인식 엔진 (CPU)
# =========================
face_app = FaceAnalysis(providers=['CPUExecutionProvider'])
face_app.prepare(ctx_id=0)

def get_embedding(img_path):
    img = cv2.imread(img_path)
    if img is None:
        return None

    faces = face_app.get(img)
    if not faces:
        return None

    # 첫 번째 얼굴 사용
    emb = faces[0].embedding

    # ✅ 벡터 정규화 (코사인 유사도 정확도 향상)
    norm = np.linalg.norm(emb)
    if norm == 0:
        return None

    emb = emb / norm
    return emb

# =========================
# 최초 1회: DB 생성
# =========================
def build_db():
    db = {}
    for f in os.listdir(FACE_DIR):
        path = os.path.join(FACE_DIR, f)
        emb = get_embedding(path)
        if emb is not None:
            db[f] = emb
    np.save(DB_PATH, db)
    return db

if os.path.exists(DB_PATH):
    db = np.load(DB_PATH, allow_pickle=True).item()
else:
    db = build_db()

# =========================
# 웹 화면
# =========================
@app.route("/")
def index():
    return render_template("index.html")

# =========================
# 얼굴 비교 API
# =========================
@app.route("/compare", methods=["POST"])
def compare():
    global db
    db = build_db()   # 🔥 매 요청마다 DB 재생성
    file = request.files["photo"]
    temp_path = os.path.join(DATA_DIR, "input.jpg")
    file.save(temp_path)

    input_emb = get_embedding(temp_path)
    if input_emb is None:
        return jsonify([])

    results = []
    for name, emb in db.items():
        score = float(np.dot(input_emb, emb))
        if score >= 0.7:   # 🔥 70% 이상만 통과
            results.append((name, score))

    results.sort(key=lambda x: x[1], reverse=True)
    top = results[:5]

    response = []
    for name, score in top:
        response.append({
            "name": name,
            "score": round(score * 100, 1),
            "image": f"/faces/{name}"
        })

    return jsonify(response)

# =========================
# 사진 제공
# =========================
@app.route("/faces/<path:filename>")
def face_image(filename):
    return send_from_directory(FACE_DIR, filename)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
