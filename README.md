# Python 3.11
# python 3.10 is safer when using InsightFace  
  3.11 introduced internal ABI changes.
  PyInstaller sometimes fails to bundle ONNX correctly.
  
# face_app.get 오류: 'NoneType' object has no attribute 'shape'
  onnxruntime_providers_cpu.dll 검토

  pip uninstall onnxruntime -y
  pip install onnxruntime==1.24.1

##  
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
      

# ALTS
   ├─apps.py
   ├─apps.speck
   ├─data(folder)
   ├─faces(folder)
   ├─templates(folder)

  
# pyinstaller
- C:\Users\owner\Desktop\ALTS
- pyinstaller --noconfirm --onedir ^
--collect-all onnxruntime ^
--collect-all insightface ^
--add-data "templates;templates" ^
--add-data "models;models" ^
apps.py

# pyinstaller 결과
 ALTS
   ├─apps.py
   ├─apps.speck
   ├─data(folder)
   ├─faces(folder)
   ├─templates(folder)
   ├─build(folder)
   ├─dist(folder)
       ├─apps
          ├─_internsl
          └─apps.exe
          ├─faces(복사 생성)
          ├─data(apps.exe 실행시 생성됨)




 
