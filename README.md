Campus Placement Data Analysis & Salary Prediction
📌 Project Overview

This project analyzes campus placement data to identify salary trends and key factors influencing compensation outcomes across companies, regions, and academic years. It covers the complete data analysis workflow, including data cleaning, exploratory data analysis (EDA), and baseline predictive modeling for salary estimation.

The emphasis is on data quality, insight generation, and model interpretability using real-world placement records.

🎯 Objectives

Analyze salary distributions in campus placements

Identify factors influencing placement salary outcomes

Build and compare baseline and tree-based regression models

Interpret model results in a real-world campus hiring context

📊 Dataset

Campus placement dataset containing 200+ records

Key attributes:

name_of_company — Recruiting organization

college_name — Institution where placement occurred

region — Placement location

year — Placement year

salary — Offered salary (raw text format with currency symbols)

The salary field required preprocessing due to inconsistent formatting and text noise.

🧹 Data Preparation

Key preprocessing steps:

Standardized column names for consistency

Cleaned salary values by removing currency symbols and text artifacts

Converted relevant fields to numeric formats

Removed incomplete and invalid records

These steps ensured the dataset was suitable for analysis and modeling.

📈 Exploratory Data Analysis (EDA)

The analysis focused on:

Distribution of salary offers

Average salary comparison across regions

Identification of top recruiting companies

Salary trends across multiple placement years

EDA insights helped explain observed salary variations prior to model building.

🤖 Modeling Approach
Baseline Model

Linear Regression

Used to establish a performance baseline

Limited effectiveness due to categorical features and non-linear patterns

Improved Model

Random Forest Regressor

Better captured non-linear relationships and feature interactions

Improved predictive performance and interpretability

Aligned more closely with real-world placement behavior

📏 Evaluation Metrics

Model performance was evaluated using:

Mean Absolute Error (MAE)

R² Score

🔑 Feature Importance Insights

Feature importance analysis from the Random Forest model indicated:

Recruiting company and region had the strongest influence on salary

College and placement year showed secondary effects

These findings align with common campus hiring patterns.

📌 Key Observations

A small number of companies account for a large share of campus hiring

Salary offers vary significantly across regions

Linear models struggle with placement salary prediction

Tree-based models better capture real-world salary structures

🛠 Tools & Technologies

Python

Pandas

Matplotlib

Scikit-learn

⚠ Limitations & Future Work

Academic performance metrics (CGPA) were unavailable

Internship experience and skill-level data could improve predictions

Advanced encoding techniques may further enhance model performance

✅ Summary

This project demonstrates an end-to-end data analysis and machine learning workflow using real-world campus placement data. It highlights the importance of data preprocessing, exploratory analysis, and model interpretation when addressing practical salary prediction problems.
