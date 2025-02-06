import requests
import numpy as np
import cv2
from PIL import Image
import io

# Roboflow API details
API_KEY = "zIH1xZbDAKnDSb2cXv77"
MODEL_ID = "underwater-marine-species/6"
API_URL = f"https://detect.roboflow.com/{MODEL_ID}"

def run_inference(image: Image.Image, confidence_threshold: float = 0.4):
    """
    Runs object detection using Roboflow API and returns the processed image with detections.

    Args:
        image (PIL.Image): The uploaded image.
        confidence_threshold (float): Minimum confidence for detections (0.0 - 1.0).

    Returns:
        tuple: (processed_image, detections)
            - processed_image (np.ndarray): Image with bounding boxes drawn.
            - detections (list of dict): Detection results with labels, confidence scores, and bounding boxes.
    """
    
    # Convert PIL Image to bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="JPEG")
    img_bytes = img_bytes.getvalue()

    # Send request to Roboflow API
    response = requests.post(
        API_URL,
        params={"api_key": API_KEY, "confidence": confidence_threshold * 100},  # Convert to percentage
        files={"file": img_bytes},
        headers={"Accept": "application/json"}
    )

    # Parse response
    if response.status_code != 200:
        raise RuntimeError(f"❌ Error from Roboflow API: {response.text}")

    result = response.json()

    # Extract detections
    detections = []
    for prediction in result.get("predictions", []):
        detections.append({
            "class": prediction["class"],
            "confidence": round(prediction["confidence"], 2),
            "bounding_box": [
                prediction["x"] - prediction["width"] / 2,  # x_min
                prediction["y"] - prediction["height"] / 2,  # y_min
                prediction["x"] + prediction["width"] / 2,  # x_max
                prediction["y"] + prediction["height"] / 2   # y_max
            ]
        })

    # Convert PIL Image to OpenCV format for drawing
    image_cv = np.array(image)
    image_cv = cv2.cvtColor(image_cv, cv2.COLOR_RGB2BGR)

    # Draw bounding boxes
    for det in detections:
        x_min, y_min, x_max, y_max = map(int, det["bounding_box"])
        cv2.rectangle(image_cv, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        label = f"{det['class']} ({det['confidence']})"
        cv2.putText(image_cv, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Convert back to RGB for Streamlit
    processed_image = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)

    return processed_image, detections
