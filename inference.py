import torch
import numpy as np
import cv2
from PIL import Image
from ultralytics import YOLO

# Path to your trained YOLO model weights
MODEL_PATH = "/Users/kanikawarman/Desktop/Projects/Marine/V5/detect 2/train/weights/best.pt"

# Load YOLOv8 model
try:
    model = YOLO(MODEL_PATH)
except Exception as ex:
    raise RuntimeError(f"❌ Unable to load model. Check the path: {MODEL_PATH}\nError: {ex}")

def run_inference(image: Image.Image, confidence_threshold: float = 0.4):
    """
    Runs object detection on an image using YOLOv8 and returns the processed image with bounding boxes.

    Args:
        image (PIL.Image): The uploaded image.
        confidence_threshold (float): Minimum confidence for detections (0.0 - 1.0).

    Returns:
        tuple: (processed_image, detections)
            - processed_image (np.ndarray): Image with bounding boxes drawn.
            - detections (list of dict): Detection results with labels, confidence scores, and bounding boxes.
    """
    if not isinstance(image, Image.Image):
        raise ValueError("Input should be a PIL Image.")

    # Run YOLO inference
    results = model.predict(image, conf=confidence_threshold)
    
    # Extract detected boxes
    boxes = results[0].boxes
    detections = []

    for box in boxes:
        class_id = int(box.cls.item())  # Get class ID
        class_name = model.names[class_id]  # Get class name (e.g., "Eel")
        detections.append({
            "class": class_name,  # Store class name
            "label": int(box.cls.item()),  # Class ID (convert to label if needed)
            "confidence": round(box.conf.item(), 2),  # Store confidence
            "bounding_box": box.xyxy.tolist()  # Bounding box coordinates
        })

    # Draw bounding boxes on the image
    processed_image = results[0].plot()[:, :, ::-1]  # Convert from BGR to RGB for Streamlit

    return processed_image, detections
