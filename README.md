Campus Placement Analytics & Salary Forecasting


Project Overview

This project analyzes historical campus placement data to understand salary trends across recruiting companies, regions, and academic years.
It also applies machine learning techniques to estimate salary outcomes based on past placement patterns.

The primary focus of this work is data quality, exploratory analysis, and model reasoning, rather than maximizing prediction accuracy.


Objectives

Analyze salary distributions in campus placements
Identify factors influencing placement salary outcomes
Build baseline and improved machine learning models for salary prediction
Interpret model results in a real-world placement context


Dataset

The dataset consists of campus placement records with the following attributes:
name_of_company – Recruiting organization
college_name – Institution where placement occurred
region – Location of the placement
year – Year of placement
salary – Offered salary (raw format with currency symbols)
The raw salary field required cleaning due to inconsistent formatting.


Data Preparation
Key preprocessing steps included:
Standardizing column names
Cleaning salary values by removing currency symbols and text noise
Converting relevant fields to numeric formats
Removing incomplete or invalid records
These steps ensured the dataset was suitable for analysis and modeling.


Exploratory Data Analysis
The analysis focuses on:
Distribution of salary offers
Average salary comparison across regions
Identification of top recruiting companies
Salary trends over multiple placement years

These insights help explain observed salary variations before applying machine learning models.



Modeling Approach

Baseline Model: Linear Regression
Linear Regression was used as a baseline to evaluate how well a simple model performs on placement data.
Due to the presence of categorical and non-linear patterns, its performance was limited.

Improved Model: Random Forest Regressor
A Random Forest model was applied to better capture non-linear relationships and interactions between features such as company, region, and college.
This approach provided improved predictive performance and better alignment with real-world placement behavior.

Evaluation Metrics
Model performance was evaluated using:
Mean Absolute Error (MAE)
R² Score


Feature Importance

Feature importance analysis from the Random Forest model indicates that:
Recruiting company and region have the strongest influence on salary
College and placement year contribute secondary effects
These results are consistent with typical campus hiring patterns.


Key Observations

A small number of companies account for a large portion of campus hiring
Salary offers vary significantly by region
Simple linear models struggle with placement salary prediction
Tree-based models better capture real-world salary structures


Tools and Technologies

Python
Pandas
Matplotlib
Scikit-learn

Limitations and Future Work

Academic performance metrics such as CGPA were not available
Internship experience and skill-level data could further improve predictions
More advanced encoding techniques may enhance model performance


Conclusion

This project demonstrates a complete machine learning workflow using real-world campus placement data, with an emphasis on data cleaning, exploratory analysis, and model interpretation.
The results highlight both the challenges and practical considerations involved in predicting placement salaries.
