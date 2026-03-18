import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from matplotlib.patches import Rectangle
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import warnings
import matplotlib

warnings.filterwarnings('ignore')

# =====================
# 1. LOAD DATASET
# =====================
df = pd.read_csv('employee_data.csv')

# Clean Attrition column
if 'Attrition' in df.columns:
    if df['Attrition'].dtype == 'object':
        df['Attrition'] = df['Attrition'].apply(lambda x: 1 if str(x).lower() == 'yes' else 0)
    else:
        df['Attrition'] = df['Attrition'].fillna(0).astype(int)

# =====================
# CLEANING TAMBAHAN (WORK-LIFE BALANCE)
# =====================
if 'WorkLifeBalance' in df.columns:
    df['WorkLifeBalance'] = df['WorkLifeBalance'].map({
        1: "Poor",
        2: "Fair",
        3: "Good",
        4: "Excellent"
    })

# =====================
# CLEANING TAMBAHAN (JOB LEVEL) — PERBAIKAN UTAMA
# =====================
if 'JobLevel' in df.columns:
    df['JobLevel'] = df['JobLevel'].map({
        1: "Entry",
        2: "Junior",
        3: "Mid",
        4: "Senior",
        5: "Executive"
    })

total_employees = len(df)
attrition_rate = (df['Attrition'].sum() / total_employees) * 100

# =====================
# 2. HIGH RISK EMPLOYEE
# =====================
high_risk_pct = 0

try:
    model = joblib.load("model/model.pkl")

    X = df.drop(columns=['Attrition', 'EmployeeCount', 'EmployeeId', 'StandardHours', 'Over18'], errors='ignore')

    for c in X.columns:
        if not pd.api.types.is_numeric_dtype(X[c]):
            X[c] = LabelEncoder().fit_transform(X[c].astype(str))

    if hasattr(model, 'predict_proba'):
        preds = model.predict_proba(X)[:, 1]
    else:
        preds = model.predict(X)

    high_risk_pct = (np.sum(preds > 0.5) / total_employees) * 100

except Exception as e:
    print("Fallback: training Random Forest...", e)

    X = df.drop(columns=['Attrition', 'EmployeeCount', 'EmployeeId', 'StandardHours', 'Over18'], errors='ignore')

    for c in X.columns:
        if not pd.api.types.is_numeric_dtype(X[c]):
            X[c] = LabelEncoder().fit_transform(X[c].astype(str))

    y = df['Attrition']

    rf = RandomForestClassifier(random_state=42)
    rf.fit(X, y)

    preds = rf.predict_proba(X)[:, 1]
    high_risk_pct = (np.sum(preds > 0.5) / total_employees) * 100

# =====================
# 3. KPI CALCULATION
# =====================
avg_income_attrition = df[df['Attrition'] == 1]['MonthlyIncome'].mean()
avg_income_non_attrition = df[df['Attrition'] == 0]['MonthlyIncome'].mean()

# =====================
# 4. PLOTTING SETTINGS
# =====================
plt.style.use('dark_background')

fig = plt.figure(figsize=(20, 11), facecolor='#121212')
grid = plt.GridSpec(4, 4, wspace=0.3, hspace=0.6)

# =====================
# HEADER
# =====================
fig.text(0.5, 0.94, 'EXECUTIVE HR ANALYTICS DASHBOARD', fontsize=28, fontweight='bold', color='#FFFFFF', ha='center')
fig.text(0.5, 0.90, 'Strategic Overview of Employee Attrition Drivers & Risk Assessment', fontsize=14, color='#A0A0A0', ha='center')

# =====================
# KPI CARD FUNCTION
# =====================
def create_kpi_card(fig, rect, title, value, subtitle="", highlight_color="#3498DB"):
    ax = fig.add_axes(rect)
    ax.axis('off')

    box = Rectangle((0,0), 1, 1, facecolor='#1A1A24', edgecolor='#2A2A3D', linewidth=1.5, transform=ax.transAxes)
    ax.add_patch(box)

    ax.text(0.5, 0.72, title.upper(), fontsize=11, color='#808080', ha='center', fontweight='bold')
    ax.text(0.5, 0.45, value, fontsize=36, color=highlight_color, ha='center', fontweight='bold')

    if subtitle:
        ax.text(0.5, 0.18, subtitle, fontsize=10, color='#606060', ha='center')

# =====================
# KPI CARDS
# =====================
create_kpi_card(fig, [0.15, 0.75, 0.22, 0.11],
                'Corporate Attrition Rate',
                f'{attrition_rate:.1f}%',
                f'Total Resignations: {df["Attrition"].sum()}',
                '#E74C3C')

create_kpi_card(fig, [0.39, 0.75, 0.22, 0.11],
                'High Risk Employees (Next 6 Mo)',
                f'{high_risk_pct:.1f}%',
                'Predicted Probability > 50%',
                '#F39C12')

create_kpi_card(fig, [0.63, 0.75, 0.22, 0.11],
                'Avg Income (Resign vs Retain)',
                f'${avg_income_attrition:,.0f} / ${avg_income_non_attrition:,.0f}',
                'Attrition group earns significantly less',
                '#2ECC71')

# =====================
# COLORS
# =====================
colors = ["#2ECC71", "#E74C3C"]

# =====================
# 1. OVERTIME
# =====================
ax1 = fig.add_subplot(grid[1:3, 0:2])
ax1.set_facecolor('#1A1A24')

sns.countplot(data=df, x='OverTime', hue='Attrition', palette=colors, ax=ax1)

ax1.set_title("High Overtime Demands Are Strongly Associated with Resignation", color='#FFFFFF', loc='left')
ax1.set_ylabel("Headcount")
ax1.set_xlabel("Overtime Status")
ax1.legend(["Retained", "Resigned"], frameon=False)

# =====================
# 2. INCOME
# =====================
ax2 = fig.add_subplot(grid[1:3, 2:4])
ax2.set_facecolor('#1A1A24')

sns.histplot(data=df, x='MonthlyIncome', hue='Attrition',
             palette=colors, kde=True, alpha=0.2, ax=ax2)

ax2.set_title("Lower-Income Segments Show Higher Risk", color='#FFFFFF', loc='left')

# =====================
# 3. WORK LIFE BALANCE
# =====================
ax3 = fig.add_subplot(grid[3, 0:2])
ax3.set_facecolor('#1A1A24')

# Tentukan urutan kategori yang logis
wlb_order = ["Poor", "Fair", "Good", "Excellent"]
wlb_data = df.groupby(['WorkLifeBalance', 'Attrition']).size().unstack(fill_value=0)
wlb_data = wlb_data.reindex([o for o in wlb_order if o in wlb_data.index])

x = np.arange(len(wlb_data))

ax3.bar(x, wlb_data[0], color=colors[0], label='Retained')
ax3.bar(x, wlb_data[1], bottom=wlb_data[0], color=colors[1], label='Resigned')

ax3.set_xticks(x)
ax3.set_xticklabels(wlb_data.index, fontsize=10)
ax3.set_title("Poor Work-Life Balance Drives Attrition", color='#FFFFFF', loc='left')
ax3.legend(["Retained", "Resigned"], frameon=False, loc='upper right')

# =====================
# 4. JOB LEVEL — PERBAIKAN LABEL
# =====================
ax4 = fig.add_subplot(grid[3, 2:4])
ax4.set_facecolor('#1A1A24')

# Urutan level jabatan yang logis
jl_order = ["Entry", "Junior", "Mid", "Senior", "Executive"]
job_data = df.groupby(['JobLevel', 'Attrition']).size().unstack(fill_value=0)
job_data = job_data.reindex([o for o in jl_order if o in job_data.index])

x = np.arange(len(job_data))

ax4.bar(x, job_data[0], color=colors[0], label='Retained')
ax4.bar(x, job_data[1], bottom=job_data[0], color=colors[1], label='Resigned')

ax4.set_xticks(x)
ax4.set_xticklabels(job_data.index, fontsize=10)  # Label deskriptif, bukan angka
ax4.set_title("Entry-Level Roles Have Highest Turnover", color='#FFFFFF', loc='left')
ax4.legend(["Retained", "Resigned"], frameon=False, loc='upper right')

# =====================
# STYLE
# =====================
for ax in [ax1, ax2, ax3, ax4]:
    ax.grid(color='#2A2A3D', linestyle='--', linewidth=0.5)
    for spine in ax.spines.values():
        spine.set_color('#2A2A3D')
    ax.tick_params(colors='#A0A0A0')

# =====================
# FOOTER
# =====================
fig.text(0.02, 0.02,
         'Data Source: HR Dataset | Random Forest Model Applied | Threshold = 0.5',
         fontsize=10, color='#606060')

# =====================
# SAVE
# =====================
plt.savefig('dashboard.png', dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())

plt.show()
print("Dashboard successfully saved as dashboard.png")