🕵️ Fake Job Detection Using Machine Learning & Deep Learning
📌 Project Overview

Fake job postings have become a serious problem on online recruitment platforms, deceiving job seekers into financial scams and identity theft.
This project aims to automatically detect fraudulent job postings using a hybrid machine learning and deep learning approach, combining textual information and structured job attributes.

The system classifies job postings as Legitimate or Fake with high accuracy and provides a probability score indicating fraud risk.

🎯 Problem Statement

Online job portals are increasingly targeted by scammers who post fake job advertisements. Manual verification is slow, error-prone, and not scalable.
Hence, there is a need for an intelligent automated system that can analyze job postings and flag fraudulent ones.

📂 Dataset Description

Dataset Name: Fake Job Postings Dataset

Source: Kaggle

Total Records: ~17,880 job postings

Target Variable:

fraudulent →

0 : Legitimate Job

1 : Fake Job

Key Features:

Job title & description

Location, department, industry

Employment type, experience, education

Company logo presence

Telecommuting availability

Salary details

Benefits & requirements

The dataset is highly imbalanced, with fake jobs forming only ~5% of the total data.

⚙️ Feature Engineering
🅰 Text Features

TF-IDF (Term Frequency–Inverse Document Frequency)

Used for traditional ML models

Converts job descriptions into numerical vectors

Tokenization & Padding

Used for the LSTM deep learning model

Converts text into integer sequences of fixed length

🅱 Structured Features

Salary statistics (min, max, average)

Text length features

Binary indicators:

Company logo presence

Telecommuting

Salary missing

Department missing

Categorical features:

Location

Industry

Employment type

Experience & education level

🧠 Models Implemented
Machine Learning Models

Logistic Regression

Random Forest

XGBoost

Support Vector Machine (SVM)

Deep Learning Model

LSTM (Long Short-Term Memory)

Captures contextual and sequential patterns in job descriptions

🔗 Hybrid Model (Final Model)

A hybrid ensemble model combining:

Random Forest (Structured Data)

LSTM (Text Data)

This approach leverages:

The interpretability of ML models

The semantic understanding of deep learning

⚖️ Handling Class Imbalance

SMOTE (Synthetic Minority Over-sampling Technique)

Class Weighting in ML models

These techniques ensure better recall for fake job detection.

📊 Model Evaluation Metrics
📈 Hybrid Model Performance (RF + LSTM)
Metric	Value
Accuracy	98.41%
Precision	95.31%
Recall	70.52%
F1 Score	81.06%
ROC-AUC	98.45%
Classification Summary:

Very high accuracy on legitimate jobs

Strong precision for fake jobs (low false positives)

Improved recall compared to standalone models

🌐 Web Interface

A Streamlit-based web application allows users to:

Enter job details

Submit job postings

Get instant predictions:

Legitimate Job ✅

Fake Job 🚨

View fraud probability score

▶️ How to Run the Project
1️⃣ Clone Repository
git clone https://github.com/Polu-Soneesh-Reddy/Fake-Job-Detection.git
cd Fake-Job-Detection

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Web App
streamlit run app.py

🚀 Future Scope

Deployment on cloud platforms (AWS / GCP)

Browser extension for real-time job verification

Integration with company verification APIs

Use of transformer models (BERT, RoBERTa)

Multilingual fake job detection

Network analysis of scam recruiters

📚 Technologies Used

Python

Pandas, NumPy

Scikit-learn

TensorFlow / Keras

Imbalanced-learn (SMOTE)

Streamlit

Git & GitHub

👨‍💻 Author

Polu Soneesh Reddy
Machine Learning Enthusiast | Data Science Student

⭐ Conclusion

This project demonstrates how combining machine learning, deep learning, and feature engineering can effectively detect fraudulent job postings.
The hybrid approach significantly improves performance and makes the system suitable for real-world deployment.
