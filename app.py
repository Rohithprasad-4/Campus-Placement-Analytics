import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


st.set_page_config(page_title="Campus Placement Salary Predictor", layout="wide")

st.title("🎓 Campus Placement Analytics & Salary Prediction")

# ---------------------------
# LOAD DATA
# ---------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("data/placement_data.csv")

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    def clean_salary(x):
        if isinstance(x, str):
            return re.sub(r'[^\d]', '', x)
        return x

    df['salary'] = df['salary'].apply(clean_salary)
    df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
    df['year'] = pd.to_numeric(df['year'], errors='coerce')

    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)

    return df


df = load_data()

st.subheader("Dataset Preview")
st.dataframe(df.head())

# ---------------------------
# VISUALIZATIONS
# ---------------------------

st.subheader("Salary Distribution")

fig1, ax = plt.subplots()
df['salary'].hist(bins=20, ax=ax)
ax.set_title("Salary Distribution")
ax.set_xlabel("Salary")
ax.set_ylabel("Count")
st.pyplot(fig1)


st.subheader("Average Salary by Region")

fig2, ax = plt.subplots()
df.groupby('region')['salary'].mean().plot(kind='bar', ax=ax)
st.pyplot(fig2)


st.subheader("Top Recruiting Companies")

fig3, ax = plt.subplots()
df['name_of_company'].value_counts().head(10).plot(kind='bar', ax=ax)
st.pyplot(fig3)


st.subheader("Salary Trend Over Years")

fig4, ax = plt.subplots()
df.groupby('year')['salary'].mean().plot(ax=ax)
st.pyplot(fig4)


# ---------------------------
# MACHINE LEARNING MODEL
# ---------------------------

ml_df = df.copy()

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

rf = RandomForestRegressor(
    n_estimators=300,
    max_depth=12,
    min_samples_leaf=5,
    random_state=42
)

rf.fit(X_train, y_train)

pred = rf.predict(X_test)

st.subheader("Model Performance")

st.write("MAE:", mean_absolute_error(y_test, pred))
st.write("R2 Score:", r2_score(y_test, pred))


# ---------------------------
# SALARY PREDICTION UI
# ---------------------------

st.sidebar.header("Predict Salary")

company = st.sidebar.selectbox(
    "Company", df['name_of_company'].unique()
)

college = st.sidebar.selectbox(
    "College", df['college_name'].unique()
)

region = st.sidebar.selectbox(
    "Region", df['region'].unique()
)

year = st.sidebar.number_input(
    "Year", min_value=2010, max_value=2030, value=2024
)

if st.sidebar.button("Predict Salary"):

    input_data = pd.DataFrame({
        "name_of_company": [le_company.transform([company])[0]],
        "college_name": [le_college.transform([college])[0]],
        "region": [le_region.transform([region])[0]],
        "year": [year]
    })

    prediction = rf.predict(input_data)

    st.success(f"💰 Predicted Salary: ₹{int(prediction[0]):,}")