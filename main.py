from fastapi import FastAPI, File, UploadFile
from PIL import Image
import torch
import io

app = FastAPI()

# Load the YOLOv5n model (nano version) from PyTorch Hub
# 'force_reload=True' ensures we get the latest cache
model = torch.hub.load('ultralytics/yolov5', 'yolov5n', pretrained=True)

@app.get("/")
def home():
    return {"message": "YOLOv5 Nano API is running!"}

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    # 1. Read the image file
    image_bytes = await file.read()
    img = Image.open(io.BytesIO(image_bytes))

    # 2. Pass image to model
    results = model(img)

    # 3. Return results as JSON (bounding boxes, labels, confidence)
    # results.pandas().xyxy[0] returns a nice DataFrame, we convert to JSON dict
    return results.pandas().xyxy[0].to_dict(orient="records")