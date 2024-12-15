from ultralytics import YOLO

model = YOLO("model/yolo11n.pt")

results = model(['img/cat.jpg'], conf=.80, save=True)