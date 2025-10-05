# AI Phishing Email Detector

## Table of Contents
- [Description](#description)  
- [Functionalities](#functionalities)  
- [Features](#features)  
- [Requirements](#requirements)   
- [How to Use](#how-to-use)  
- [Model & Dataset](#model--dataset)  
- [Evaluation](#evaluation)  
- [Screenshots](#screenshots)  
- [Author](#author)  


---

## Description
**AI Phishing Email Detector** is a machine learning project that identifies whether an email is a phishing attempt or legitimate. It analyzes email text (subject + body, optionally headers) to predict a phishing probability and flags suspicious messages.  
The project aims to provide a user-friendly tool to test phishing detection and understand phishing patterns.

---

## Functionalities
- Load and preprocess email text data.  
- Train and evaluate classification models (e.g., TF-IDF + Logistic Regression).  
- Predict whether an email is phishing or legitimate.  
- Save and load trained models.  
- Evaluate model performance with metrics like accuracy, precision, recall, F1-score.  
- Command-line or script-based testing for single emails or batch files.  

---

## Features
- Text preprocessing: lowercasing, HTML tag removal, punctuation removal, stopword removal.  
- TF-IDF feature extraction.  
- Train and save models for later prediction.  
- Predict individual emails or CSV datasets.  
- Basic logging of predictions and evaluation results.  

---

## Requirements
- Python 3.8+  
- Libraries:
  ```bash
  numpy
  pandas
  scikit-learn
  joblib
  nltk
  matplotlib  # optional for plots
  flask      # optional for web demo
## How to Use
1. Prepare your dataset CSV with columns: `subject`, `body`, `label`.  
2. Train the model using `train.py`.  
3. Evaluate on a test set using `evaluate.py`.  
4. Use `predict.py` to test individual emails or batch files.  
5. Review metrics to understand model performance.  

---

## Model & Dataset
- **Model:** TF-IDF + Logistic Regression (baseline, interpretable)  
- **Dataset:** Public phishing datasets (e.g., Enron, Nazario) or curated datasets  
- **Preprocessing:** Lowercasing, punctuation removal, stopwords removal, URL/email replacement, optional stemming/lemmatization  

---

## Evaluation
- Accuracy  
- Precision, Recall, F1-score  
- Confusion Matrix  

---

## Screenshots

![screeshot]()

---

## Author
**Harshita Patil**



