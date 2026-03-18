import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# =====================
# CONFIG
# =====================
st.set_page_config(page_title="HR Analytics Dashboard", layout="wide")

st.title("📊 Executive HR Analytics Dashboard")
st.markdown("Dashboard interaktif untuk analisis faktor-faktor yang mempengaruhi employee attrition.")

# =====================
# LOAD DATA
# =====================
@st.cache_data
def load_data():
    return pd.read_csv('employee_data.csv')

df = load_data()

# =====================
# DATA CLEANING
# =====================
df['Attrition'] = df['Attrition'].apply(lambda x: 1 if str(x).lower() == 'yes' else 0)

# Mapping kategori biar tidak angka
if 'WorkLifeBalance' in df.columns:
    df['WorkLifeBalance'] = df['WorkLifeBalance'].map({
        1: "Poor",
        2: "Fair",
        3: "Good",
        4: "Excellent"
    })

if 'JobLevel' in df.columns:
    df['JobLevel'] = df['JobLevel'].map({
        1: "Entry Level",
        2: "Mid Level",
        3: "Senior Level",
        4: "Manager",
        5: "Executive"
    })

# =====================
# FILTER (INI YANG DIMINTA REVIEWER)
# =====================
st.sidebar.header("Filter Data")

df_filtered = df.copy()

if 'Department' in df.columns:
    dept = st.sidebar.selectbox("Department", sorted(df['Department'].dropna().unique()))
    df_filtered = df_filtered[df_filtered['Department'] == dept]

if 'Gender' in df.columns:
    gender = st.sidebar.selectbox("Gender", sorted(df_filtered['Gender'].dropna().unique()))
    df_filtered = df_filtered[df_filtered['Gender'] == gender]

# =====================
# KPI
# =====================
total_employees = len(df_filtered)
attrition_rate = (df_filtered['Attrition'].sum() / total_employees) * 100

# =====================
# MODEL (HIGH RISK)
# =====================
high_risk_pct = 0

try:
    model = joblib.load("model/model.pkl")

    X = df_filtered.drop(columns=['Attrition', 'EmployeeCount', 'EmployeeId', 'StandardHours', 'Over18'], errors='ignore')

    for c in X.columns:
        if not pd.api.types.is_numeric_dtype(X[c]):
            X[c] = LabelEncoder().fit_transform(X[c].astype(str))

    preds = model.predict_proba(X)[:, 1]
    high_risk_pct = (np.sum(preds > 0.5) / total_employees) * 100

except:
    rf = RandomForestClassifier(random_state=42)

    X = df_filtered.drop(columns=['Attrition'], errors='ignore')

    for c in X.columns:
        if not pd.api.types.is_numeric_dtype(X[c]):
            X[c] = LabelEncoder().fit_transform(X[c].astype(str))

    y = df_filtered['Attrition']
    rf.fit(X, y)

    preds = rf.predict_proba(X)[:, 1]
    high_risk_pct = (np.sum(preds > 0.5) / total_employees) * 100

# =====================
# KPI TAMBAHAN
# =====================
avg_income_attr = df_filtered[df_filtered['Attrition'] == 1]['MonthlyIncome'].mean()
avg_income_non = df_filtered[df_filtered['Attrition'] == 0]['MonthlyIncome'].mean()

# =====================
# DISPLAY KPI
# =====================
col1, col2, col3 = st.columns(3)

col1.metric("Attrition Rate", f"{attrition_rate:.1f}%")
col2.metric("High Risk Employee", f"{high_risk_pct:.1f}%")
col3.metric("Income (Attr vs Stay)", f"${avg_income_attr:,.0f} / ${avg_income_non:,.0f}")

# =====================
# CHART 1: OVERTIME
# =====================
st.subheader("Overtime vs Attrition")

fig1, ax1 = plt.subplots()
sns.countplot(data=df_filtered, x='OverTime', hue='Attrition', ax=ax1)
st.pyplot(fig1)

# =====================
# CHART 2: INCOME
# =====================
st.subheader("Income Distribution")

fig2, ax2 = plt.subplots()
sns.histplot(data=df_filtered, x='MonthlyIncome', hue='Attrition', kde=True, ax=ax2)
st.pyplot(fig2)

# =====================
# CHART 3: WORK LIFE BALANCE
# =====================
if 'WorkLifeBalance' in df_filtered.columns:
    st.subheader("Work-Life Balance Impact")

    wlb = df_filtered.groupby(['WorkLifeBalance', 'Attrition']).size().unstack(fill_value=0)

    fig3, ax3 = plt.subplots()
    wlb.plot(kind='bar', stacked=True, ax=ax3)
    st.pyplot(fig3)

# =====================
# CHART 4: JOB LEVEL
# =====================
if 'JobLevel' in df_filtered.columns:
    st.subheader("Job Level vs Attrition")

    job = df_filtered.groupby(['JobLevel', 'Attrition']).size().unstack(fill_value=0)

    fig4, ax4 = plt.subplots()
    job.plot(kind='bar', stacked=True, ax=ax4)
    st.pyplot(fig4)

# =====================
# INSIGHT
# =====================
st.subheader("💡 Key Insights")

st.write("""
- Overtime memiliki pengaruh signifikan terhadap attrition
- Karyawan dengan income rendah lebih berisiko resign
- Work-life balance yang buruk meningkatkan attrition
- Karyawan entry-level memiliki turnover tertinggi
""")