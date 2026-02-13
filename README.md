# Python 3.11

project/
 ├─ app.py
 ├─ faces/              ← 치매노인 사진 500장 (jpg/png)
 ├─ data/
 │   └─ db.npy          ← 최초 실행 시 자동 생성
 └─ templates/
     └─ index.html


# multi_face/faces
 faces
  ├─Nomuheon(폴더명 영문사용할것/폴더)
      └─1.jpg
      └─2.jpg
      └─3.jpg
      
# pyinstaller
- ALTS
   ├─apps.py
   ├─apps.speck
   ├─data(folder)
   ├─faces(folder)

- C:\Users\owner\AppData\Local\Programs\Python\Python311\python.exe -m PyInstaller --onefile --add-data "templates;templates" --add-data "faces;faces" --add-data "data;data" apps.py

- ImportError: Unable to import dependency onnxruntime.
   - C:\Users\owner\AppData\Local\Programs\Python\Python311\python.exe -m pip install onnxruntime
     
- http://127.0.0.1:5000
- C:\Users\owner\Desktop\ALTS

- pyinstaller --noconfirm --onedir ^
--collect-all onnxruntime ^
--collect-all insightface ^
--add-data "templates;templates" ^
--add-data "models;models" ^
apps.py
