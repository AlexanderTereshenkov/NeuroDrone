from ultralytics import YOLO

model = YOLO("model/yolo11n.pt")

model.train(data="D:\PyProjects\datasets\pig_dataset\custom_data.yaml", epochs=2, imgsz=640, device="cpu")

model.val()