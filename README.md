# **Marine Species Object Detection 🌊🐠**  

<!-- One-glance header block -->
<p align="left">
  <a href="https://www.python.org/"><img alt="Python 3.10+" src="https://img.shields.io/badge/Python-3.10%2B-blue"></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/github/license/kanikawarman/Marine-object-detection"></a>
  <a href="https://github.com/kanikawarman/Marine-object-detection/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/kanikawarman/Marine-object-detection?style=social"></a>
  <a href="https://github.com/kanikawarman/Marine-object-detection/commits/main"><img alt="Last commit" src="https://img.shields.io/github/last-commit/kanikawarman/Marine-object-detection"></a>
  <!-- Update the notebook path if different -->
  <a href="https://colab.research.google.com/github/kanikawarman/Marine-object-detection/blob/main/train.ipynb">
    <img alt="Open in Colab" src="https://colab.research.google.com/assets/colab-badge.svg">
  </a>
  <!-- If you have a public Streamlit app, put its URL below; otherwise keep only the local run command in README -->
  <a href="https://YOUR-STREAMLIT-APP-URL">
    <img alt="Open in Streamlit" src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg">
  </a>
</p>


### **Overview**  
This project focuses on detecting marine species in underwater environments using **YOLOv8** and deep learning techniques. The model is trained on a **custom-curated dataset** and optimized for real-world aquatic conditions.  

🔹 **Live Demo:** [Streamlit App](https://underwater-marine-object-detection.streamlit.app/)

🔹 **Research Paper:** [Available in this repository](https://github.com/kanikawarman/Marine-object-detection/blob/main/objectID_yolov8.pdf)

🔹 **Dataset:** Hosted on [Roboflow](https://app.roboflow.com/california-state-university-east-bay-wkf0d/underwater-marine-species/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true)

---

## **1️⃣ Features**  
✅ Object detection for multiple marine species: Eel, Fish, Jellyfish, Lobster, Lionfish   
✅ Optimized for underwater environments  
✅ Pretrained YOLOv8 model with fine-tuned weights  
✅ Ready-to-use inference (weights available via external link)  
✅ Open for further training on custom datasets  

---

## **2️⃣ Model Details**  
- **Model Used:** YOLOv8m
- **Framework:** Ultralytics (built on PyTorch)  
- **Training Platform:** Kaggle (free GPU)  
- **Dataset:** Custom dataset curated from multiple sources  
- **Best Weights:** Available via external link (since GitHub limits file size)  

---

## **3️⃣ Installation & Setup**  

### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/kanikawarman/Marine-object-detection.git
cd Marine-object-detection
```

### **Step 2: Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **Step 3: Run Inference**  
```bash
python detect.py --weights path_to_best_weights.pt --source your_image.jpg
```  
*(Download `best.pt` from the provided external [link](https://app.roboflow.com/california-state-university-east-bay-wkf0d/underwater-marine-species/6) before running inference.)*  

---

## **4️⃣ Training the Model**  
If you want to train the model from scratch using your dataset, follow the script available in `train.py`:  
```bash
python main.py --data dataset.yaml --weights yolov8.pt --epochs 50
```  
Modify the `dataset.yaml` file to point to your custom dataset on **Roboflow**.  

---

## **5️⃣ Results & Evaluation**  
📌 **Model Performance:** 

<img width="1018" alt="Screenshot 2025-02-24 at 16 59 36" src="https://github.com/user-attachments/assets/34102990-ccdf-4bb2-b5c8-8ec0046c1970" />

![confusion_matrix](https://github.com/user-attachments/assets/d76c5ee0-926f-46c1-a725-f51116621f49)


![val_batch1_pred](https://github.com/user-attachments/assets/c0df09dd-63c1-4816-b88c-a27b20bf7f15)


## **6️⃣ How to Use the Model?**  
- **For Direct Inference:** Download `best.pt` from the external link and use it.  
- **For Custom Use:** Fine-tune the model using your dataset and the provided training scripts.  

---

## **7️⃣ Live Demo (Streamlit App) 🎯**  
Try the model in action via our **[Streamlit App](https://underwater-marine-object-detection.streamlit.app/)** where you can upload images and test marine species detection in real time.  

---

## **8️⃣ Contribution & Acknowledgments**  
Contributions are welcome! If you use this work, consider citing or linking back.  
