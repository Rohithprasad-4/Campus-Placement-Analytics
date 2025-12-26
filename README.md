# Campus Placement Data Analysis & Salary Prediction

## 📌 Project Overview

This project analyzes campus placement data to uncover salary trends and identify key factors influencing compensation outcomes across companies, regions, and academic years. It demonstrates an end-to-end data science workflow, combining data cleaning, exploratory data analysis (EDA), and regression-based modeling to generate practical, data-driven insights.

The project emphasizes real-world data handling, insight extraction, and interpretable modeling rather than purely theoretical analysis.

---

## 🎯 Objectives

- Analyze salary distributions and trends in campus placements  
- Identify key drivers influencing placement salaries  
- Build and compare baseline and tree-based regression models  
- Interpret results to derive actionable insights from placement data  

---

## 📊 Dataset

- Campus placement dataset with **200+ records**

### Key Attributes
- Recruiting Company  
- College  
- Placement Region  
- Placement Year  
- Salary (raw text format with currency symbols)  

> Salary values required preprocessing due to inconsistent formatting and noise.

---

## 🧹 Data Preprocessing

- Standardized column names for consistency  
- Cleaned salary values by removing currency symbols and text artifacts  
- Converted relevant fields to numeric formats  
- Removed incomplete and invalid records  

These steps ensured high-quality data suitable for analysis and modeling.

---

## 📈 Exploratory Data Analysis (EDA)

Key analyses included:

- Salary distribution across placements  
- Regional comparison of average salary offers  
- Identification of top recruiting companies  
- Salary trends across multiple placement years  

EDA provided valuable context and insights prior to model development.

---

## 🤖 Modeling Approach

### Baseline Model
- **Linear Regression**
- Established a baseline for salary prediction performance  

### Improved Model
- **Random Forest Regressor**
- Captured non-linear relationships between features  
- Improved predictive performance and interpretability  

---

## 📏 Evaluation Metrics

- Mean Absolute Error (MAE)  
- R² Score  

---

## 🔑 Key Insights

- Recruiting company and region are the strongest predictors of salary  
- Salary distributions vary significantly across regions  
- Tree-based models outperform linear baselines for real-world salary data  

---

## 🛠 Tools & Technologies

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-learn  

---

## ⚠ Limitations & Future Work

- Academic performance and skill-level features were unavailable  
- Inclusion of internship experience and role-level data could improve results  
- Advanced encoding and feature engineering may further enhance performance  

---

## ✅ Summary

This project highlights the practical application of data science techniques to real-world placement data, focusing on data quality, exploratory analysis, and interpretable modeling to extract meaningful insights.
