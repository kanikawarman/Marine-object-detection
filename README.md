# **Marine Species Object Detection 🌊🐠**  

### **Overview**  
This project focuses on detecting marine species in underwater environments using **YOLOv8** and deep learning techniques. The model is trained on a **custom-curated dataset** and optimized for real-world aquatic conditions.  

🔹 **Live Demo:** [Streamlit App](https://underwater-marine-object-detection.streamlit.app/)  
🔹 **Research Paper:** Available in this repository  
🔹 **Dataset:** Hosted on [Roboflow](https://app.roboflow.com/california-state-university-east-bay-wkf0d/underwater-marine-species/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true)

---

## **1️⃣ Features**  
✅ Object detection for multiple marine species : Eel, Fish, Jellyfish, Lobster, Lionfish
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
python train.py --data dataset.yaml --weights yolov8.pt --epochs 50
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
