import streamlit as st
import requests
import base64
import io
from PIL import Image
from io import BytesIO
import os
from PIL import Image
from inference import run_inference
import PIL.Image

# Set page title and layout
st.set_page_config(page_title="Marine Species Detection", page_icon="🐠", layout="wide")

# Apply Custom CSS for Gradient Background & Layering
st.markdown(
    """
    <style>
        /* Main Page Background Gradient */
        .stApp {
            background: linear-gradient(to bottom, #005599, #0077cc, #0099ff) !important;
            background-size: cover;
            height: 100vh;
            padding: 0px;
        }

        /* Sidebar Styling - Darker Contrast */
        section[data-testid="stSidebar"] {
            background: linear-gradient(to bottom, #002244, #003366, #004488) !important; /* Darker shade */
            color: white !important;
            border-right: 3px solid #005599;
        }

        /* Ensure Sidebar Text is White */
        section[data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Fix Black Bar at the Top */
        .st-emotion-cache-1r0z55i, .st-emotion-cache-6qob1r {
            background: linear-gradient(to right, #004488, #005599) !important;
            color: white !important;
        }

        /* Ensure the deploy button is visible */
        .stDeployButton {
            color: white !important;
        }
        
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <style>
        /* Override the default Streamlit background */
        body {
            background-color: #003366 !important;  /* Deep ocean blue */
        }

        /* Background gradient for the entire app */
        .stApp {
            background: linear-gradient(to bottom, #001a33, #003366, #005599) !important;
            background-size: cover;
            height: 100vh;
            padding: 0px;
        }

        /* Sidebar Styling - Applying Gradient */
        section[data-testid="stSidebar"] {
            background: linear-gradient(to bottom, #002244, #003366, #004488) !important; /* Dark to lighter blue */
            color: white !important;
            border-right: 2px solid #005599;
        }

        /* Ensure all text in the sidebar is visible */
        section[data-testid="stSidebar"] * {
            color: white !important;
        }
        
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.markdown(
    """
    <style>
        /* Sidebar Container */
        section[data-testid="stSidebar"] {
            padding: 20px !important;
        }

        /* Upload Section */
        .upload-box {
            border: 2px dashed white; 
            padding: 15px;
            text-align: center;
            border-radius: 10px;
            background-color: rgba(255, 255, 255, 0.1);
        }

        /* Center Detect Button */
        .stButton>button {
            display: block;
            margin: 0 auto;
            width: 100%;
            background-color: #ff6600;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)




# Title Section
st.markdown("<h1 style='text-align: center; color: white;'>🐠 Underwater Marine Species Detection 🦞</h1>", unsafe_allow_html=True)

# Project Description
st.markdown(
    """
    <p style="text-align: center; font-size: 16px; color: #e0e0e0;">
    🌊 This AI-powered tool detects and identifies various marine species, including <span style='color:#ff6600;'>🦞 Lobsters</span>, <span style='color:#ff6600;'>🐠  Fish</span>,  
    <span style='color:#ff6600;'> 🐡  Lionfish</span>, <span style='color:#ff6600;'> 🦐  Eels</span>,  
    and <span style='color:#ff6600;'> 🦑  Jellyfish</span>. <br>
    It leverages deep learning for accurate object detection, helping in marine research and conservation efforts.
    </p>
    """,
    unsafe_allow_html=True
)

# Instructions
st.markdown("<p style='text-align: center; font-size: 16px; color: white;'>Upload an image and click 'Detect Objects' to detect marine life.</p>", unsafe_allow_html=True)

# Collapsible Tech Stack
with st.expander("🔍 **Project Details & Tech Stack**"):
    st.markdown(
        """
        - **Built Using**: Python, Streamlit, YOLOv8, Roboflow API  
        - **Model**: Object detection with deep learning  
        - **Data Source**: Publicly available marine datasets  
        - **Developer**: [Kanika Warman](https://www.linkedin.com/in/kanika-warman/) 🔗

          ---
        🌊 **What Can You Detect?**  
        - **🦞 Lobster**,  **🐠 Fish**,  **🦐 Eel**,  **🦑 Jellyfish**,  **🐡 Lionfish**  

         ---
        🚀 **Future Improvements**:  
        - Expanding to detect **more marine species**  
        - Enhancing accuracy with **better training datasets** and **fine-tuning models**

        """
    )

# Sidebar
with st.sidebar:
    # ---- 🖼️ Image Upload Section ----
    st.markdown("### 📸 Upload Your Image")

    # Stylish Upload Box (Functional & Styled)
    st.markdown(
    """
    <style>
        /* Upload Box Styling */
        div[data-testid="stFileUploader"] {
            border: 2px dashed white !important;
            padding: 20px;
            text-align: center;
            border-radius: 10px;
            background-color: rgba(0, 102, 204, 0.2);  /* Light Blue */
        }

        /* Styling for Drag & Drop Text */
        div[data-testid="stFileUploader"] label {
            font-size: 18px !important;  /* Bigger Text */
            font-weight: bold !important;
            color: white !important;
            text-align: center;
        }

        /* Optional: Add Icon Before Text */
        div[data-testid="stFileUploader"] label::before {
            content: "📂 ";  /* File Icon */
            font-size: 20px;
        }

        /* Center & Style Browse Files Button */
        div[data-testid="stFileUploader"] button {
            display: block;
            margin: 10px auto;  /* Centering */
            background-color: #ff6600 !important;  /* Match Detect Objects */
            color: white !important;
            font-weight: bold;
            border-radius: 8px;
            padding: 8px;
            font-size: 16px;
        }
    </style>
    """, 
    unsafe_allow_html=True
    )

    # File Upload Section
    uploaded_file = st.file_uploader("Upload an image or video", type=["png", "jpg", "jpeg", "gif", "mp4"])

# Initialize session state variables
if "detect_clicked" not in st.session_state:
    st.session_state["detect_clicked"] = False

if uploaded_file:
    image = Image.open(uploaded_file)  # Open the uploaded image

    if not st.session_state.detect_clicked:  # Show image only if detect is NOT clicked
        col1, col2, col3 = st.columns([1, 2, 1])  # Centering the image

        with col2:
            st.image(image, caption="Uploaded Image", width=450)

        # # Button to start detection
        # detect_button = st.button("🔍 Detect Objects", key="detect")
        
        # "Detect Objects" button
        if st.button("🔍 Detect Objects"):
            st.session_state.detect_clicked = True  # Set flag to True (hides initial image)
            st.rerun()  # Refresh the app to update layout

    # If detect is clicked, show both images side by side
    if st.session_state.detect_clicked:
        with st.spinner("Running detection..."):
            processed_image, detections = run_inference(image)

        # Dummy function to simulate detection (replace with actual model)
            def detect_objects(img):
                return img  # Placeholder, should return processed image with detections

            detected_image = detect_objects(image)  # Get processed image

            # Display side-by-side images
            col1, col2 = st.columns(2)

            # Show original image in first column
            with col1:
                st.image(image, caption="📸 Original Image", use_container_width=True)

            # Show detected image in second column
            with col2:
                if processed_image is not None:
                    st.image(processed_image, caption="🎯 Predicted Results", use_container_width=True)
                else:
                    st.error("⚠️ Failed to process image.")

            # Expandable section for detection results
            with st.expander("📋 Detection Results:"):
                if detections:
                    for det in detections:
                        st.write(f"🔹 **Class:** {det['class']}")
                        # st.write(f"🔹 **Class:** {det['class']} (Label: {det['label']})")
                        st.write(f"🎯 **Confidence:** {det['confidence'] * 100:.2f}%")
                        st.write(f"📍 **Bounding Box:** {det['bounding_box']}")
                        st.markdown("---")
                else:
                    st.write("⚠️ No objects detected.")

else:
    # If no image is uploaded, show sample images
    # Path to your images folder (relative path for flexibility)
    IMAGE_FOLDER = os.path.join(os.getcwd(), "sample_images")

    # Check if folder exists
    if not os.path.exists(IMAGE_FOLDER):
        st.error(f"❌ Error: The folder '{IMAGE_FOLDER}' was not found!")
        st.stop()


    # Get list of image filenames
    image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith((".png", ".jpg", ".jpeg"))]

    # Sort for consistency
    image_files.sort()

    # Handle case when no images exist
    if not image_files:
        st.warning("⚠️ No sample images found in the folder!")
        st.stop()

    # 🔹 Custom-styled header (smaller font, centered)
    st.markdown(
        """
        <h3 style="text-align: center; font-size: 22px;">🐚 Sample Detections</h3>
        <p style="text-align: center; font-size: 16px; color: #666;">Explore how our model detects marine species!</p>
        """,
        unsafe_allow_html=True,
    )

    # Create a grid (2x3 or 3x3 depending on images)
    cols_per_row = 3
    num_images = len(image_files)
    rows = (num_images // cols_per_row) + (1 if num_images % cols_per_row else 0)

    # Display images in grid format
    for i in range(rows):
        cols = st.columns(cols_per_row)  # Create columns for a row
        for j in range(cols_per_row):
            img_index = i * cols_per_row + j
            if img_index < num_images:  # Ensure we don't go out of bounds
                img_path = os.path.join(IMAGE_FOLDER, image_files[img_index])
                image = Image.open(img_path)
                cols[j].image(image, caption=f"🔍 {image_files[img_index]}", use_container_width=True)