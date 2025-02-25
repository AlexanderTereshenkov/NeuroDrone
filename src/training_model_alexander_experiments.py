from ultralytics import YOLO

model = YOLO("model/yolo11n.pt")

model.train(data="D:\PyProjects\datasets\dataset_v1.v1i.yolov11\data.yaml", epochs=100, imgsz=640, device=0, workers=0)

model.val()