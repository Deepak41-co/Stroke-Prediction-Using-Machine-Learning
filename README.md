# 🧠 Stroke Prediction using Machine Learning
## 📌 Project Overview

This project builds a machine learning classification pipeline to predict the likelihood of stroke occurrence using patient health-related features.

The workflow includes data preprocessing, handling class imbalance, feature selection, model training, evaluation, and deployment using Streamlit.

## 🎯 Objective

To develop and evaluate machine learning models capable of predicting stroke risk and deploy the best-performing model as an interactive web application.

## 📂 Dataset

The dataset contains structured healthcare data with the following features:

Gender

Age

Hypertension

Heart disease

Ever married

Work type

Residence type

Average glucose level

BMI

Smoking status

Stroke (target variable)

*Target Variable*: 

0 → No Stroke

1 → Stroke

The dataset is imbalanced, with significantly fewer stroke cases.

## 🛠 Technologies & Libraries Used

Python

pandas

numpy

scikit-learn

imbalanced-learn

joblib

Streamlit

## 🔎 Project Workflow
1️⃣ *Data Exploration*

Loaded dataset and inspected structure

Checked missing values

Performed exploratory data analysis

Visualized class distribution

Examined feature relationships using correlation analysis

2️⃣ *Data Preprocessing*

Handled missing values (BMI column treatment)

Encoded categorical variables

Scaled numerical features

Split dataset into training and testing sets

3️⃣ *Handling Class Imbalance*

Applied SMOTE (Synthetic Minority Oversampling Technique)

Resampled training data only

Improved recall performance for minority (stroke) class

4️⃣ *Feature Selection*

Used SelectKBest with statistical scoring

Selected top contributing features for modeling

5️⃣ *Model Training & Comparison*

The following models were trained and evaluated:

Logistic Regression

Decision Tree Classifier

Random Forest Classifier

K-Nearest Neighbors

Support Vector Classifier

Bernoulli Naive Bayes

6️⃣ *Model Evaluation*

Models were evaluated using:

Accuracy

Precision

Recall

F1-score

ROC-AUC Score

Classification Report

Special attention was given to performance on the minority (Stroke = 1) class.

## 🚀 Model Deployment

The final trained model was saved using joblib and deployed as a web application using Streamlit.

*Deployed link*:https://stroke-prediction-using-machine-learning.streamlit.app/ 

