import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# Load dataset
df = pd.read_csv(
    r"C:\Users\ROHITH\Desktop\Campus Placement Analytics & Salary Forecasting System\data\placement_data.csv"
)

# Clean column names FIRST
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# ----------- CORRECT SALARY CLEANING (BEFORE NUMERIC CONVERSION) -----------

def clean_salary(x):
    if isinstance(x, str):
        return re.sub(r'[^\d]', '', x)  # keep only digits
    return x

df['salary'] = df['salary'].apply(clean_salary)

# Convert salary & year to numeric
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df['year'] = pd.to_numeric(df['year'], errors='coerce')

# Drop invalid rows AFTER cleaning
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)

print(df.head())
print(df.info())

# ------------------ DAY 2 PLOTS ------------------

plt.figure()
df['salary'].hist(bins=20)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Count")
plt.show()

plt.figure()
df.groupby('region')['salary'].mean().plot(kind='bar')
plt.title("Average Salary by Region")
plt.xlabel("Region")
plt.ylabel("Average Salary")
plt.show()

plt.figure()
df['name_of_company'].value_counts().head(10).plot(kind='bar')
plt.title("Top Recruiting Companies")
plt.xlabel("Company")
plt.ylabel("Number of Offers")
plt.show()

plt.figure()
df.groupby('year')['salary'].mean().plot()
plt.title("Salary Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Average Salary")
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

rf = RandomForestRegressor(
    n_estimators=300,
    max_depth=12,
    min_samples_leaf=5,
    random_state=42,
    n_jobs=-1
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

print("Random Forest MAE:", mean_absolute_error(y_test, rf_pred))
print("Random Forest R2:", r2_score(y_test, rf_pred))

importances = pd.Series(rf.feature_importances_, index=X.columns)
importances.sort_values().plot(kind='barh')
plt.title("Feature Importance in Salary Prediction")
plt.show()


# Copy dataset for ML
ml_df = df.copy()

# Encode categorical features
le_company = LabelEncoder()
le_college = LabelEncoder()
le_region = LabelEncoder()

ml_df['name_of_company'] = le_company.fit_transform(ml_df['name_of_company'])
ml_df['college_name'] = le_college.fit_transform(ml_df['college_name'])
ml_df['region'] = le_region.fit_transform(ml_df['region'])

X = ml_df[['name_of_company', 'college_name', 'region', 'year']]
y = ml_df['salary']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
