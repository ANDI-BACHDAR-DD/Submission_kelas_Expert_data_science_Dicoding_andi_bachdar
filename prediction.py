"""
===============================================================================
PREDICTION SCRIPT - HR EMPLOYEE ATTRITION
===============================================================================
Deskripsi:
    Script ini digunakan untuk memprediksi apakah seorang karyawan akan
    melakukan attrition (resign/keluar) atau tidak, berdasarkan model
    Machine Learning yang telah dilatih dan disimpan dalam file model.pkl.

Cara Penggunaan:
    1. Pastikan model sudah dilatih terlebih dahulu dengan menjalankan notebook.ipynb
    2. Pastikan file model/model.pkl sudah ada
    3. Jalankan script ini:
       python prediction.py

Output:
    - Prediksi: 0 = Tidak Attrition (Bertahan), 1 = Attrition (Resign)
    - Probabilitas attrition
    - Interpretasi hasil

Author  : Andi Bahdar
Dataset : HR Employee Attrition - PT Jaya Jaya Maju
===============================================================================
"""

import os
import joblib
import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────────────────────────────────────
# 1. LOAD MODEL
# ─────────────────────────────────────────────────────────────────────────────

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "model.pkl")

def load_model(path: str):
    """Load model dari file .pkl menggunakan joblib."""
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"\n[ERROR] Model tidak ditemukan di: {path}\n"
            "Jalankan notebook.ipynb terlebih dahulu untuk melatih dan menyimpan model."
        )
    model = joblib.load(path)
    print(f"✅ Model berhasil dimuat dari: {path}")
    print(f"   Tipe model : {type(model).__name__}\n")
    return model


# ─────────────────────────────────────────────────────────────────────────────
# 2. DATA KARYAWAN (CONTOH INPUT)
# ─────────────────────────────────────────────────────────────────────────────

# Contoh data karyawan yang akan diprediksi.
# Sesuaikan nilai-nilai di bawah ini untuk memprediksi karyawan lain.
sample_employees = [
    {
        # Karyawan berisiko tinggi resign (overtime, gaji rendah, WLB buruk)
        "Age": 28,
        "BusinessTravel": 2,          # 2 = Travel_Frequently
        "DailyRate": 400,
        "Department": 2,              # 2 = Sales
        "DistanceFromHome": 25,
        "Education": 3,
        "EducationField": 4,          # 4 = Marketing
        "EnvironmentSatisfaction": 1, # 1 = Low
        "Gender": 1,                  # 1 = Male
        "HourlyRate": 45,
        "JobInvolvement": 2,
        "JobLevel": 1,
        "JobRole": 8,                 # 8 = Sales Representative
        "JobSatisfaction": 1,         # 1 = Low
        "MaritalStatus": 1,           # 1 = Single
        "MonthlyIncome": 2500,
        "MonthlyRate": 5000,
        "NumCompaniesWorked": 4,
        "OverTime": 1,                # 1 = Yes (Overtime)
        "PercentSalaryHike": 11,
        "PerformanceRating": 3,
        "RelationshipSatisfaction": 2,
        "StockOptionLevel": 0,
        "TotalWorkingYears": 4,
        "TrainingTimesLastYear": 1,
        "WorkLifeBalance": 1,         # 1 = Bad
        "YearsAtCompany": 2,
        "YearsInCurrentRole": 1,
        "YearsSinceLastPromotion": 1,
        "YearsWithCurrManager": 1,
    },
    {
        # Karyawan berisiko rendah (senior, gaji baik, WLB bagus, tidak overtime)
        "Age": 42,
        "BusinessTravel": 1,          # 1 = Travel_Rarely
        "DailyRate": 900,
        "Department": 0,              # 0 = Human Resources
        "DistanceFromHome": 5,
        "Education": 4,
        "EducationField": 2,          # 2 = Life Sciences
        "EnvironmentSatisfaction": 4, # 4 = Very High
        "Gender": 0,                  # 0 = Female
        "HourlyRate": 80,
        "JobInvolvement": 4,
        "JobLevel": 4,
        "JobRole": 0,                 # 0 = Healthcare Representative
        "JobSatisfaction": 4,         # 4 = Very High
        "MaritalStatus": 2,           # 2 = Married
        "MonthlyIncome": 9500,
        "MonthlyRate": 18000,
        "NumCompaniesWorked": 1,
        "OverTime": 0,                # 0 = No
        "PercentSalaryHike": 20,
        "PerformanceRating": 4,
        "RelationshipSatisfaction": 4,
        "StockOptionLevel": 3,
        "TotalWorkingYears": 18,
        "TrainingTimesLastYear": 4,
        "WorkLifeBalance": 4,         # 4 = Best
        "YearsAtCompany": 12,
        "YearsInCurrentRole": 7,
        "YearsSinceLastPromotion": 2,
        "YearsWithCurrManager": 6,
    },
]


# ─────────────────────────────────────────────────────────────────────────────
# 3. FUNGSI PREDIKSI
# ─────────────────────────────────────────────────────────────────────────────

def predict_attrition(model, employee_data: dict) -> dict:
    """
    Melakukan prediksi attrition untuk satu karyawan.

    Parameters
    ----------
    model : sklearn estimator
        Model yang sudah dilatih.
    employee_data : dict
        Data karyawan dalam bentuk dictionary.

    Returns
    -------
    dict
        Dictionary berisi prediksi, probabilitas, dan interpretasi.
    """
    df_input = pd.DataFrame([employee_data])

    prediction = model.predict(df_input)[0]

    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(df_input)[0]
        prob_attrition = round(proba[1] * 100, 2)
    else:
        prob_attrition = None

    if prediction == 1:
        label = "⚠️  ATTRITION (Berisiko Resign)"
        action = "Segera lakukan intervensi HR: evaluasi beban kerja, kompensasi, dan kepuasan karyawan."
    else:
        label = "✅  TIDAK ATTRITION (Kemungkinan Bertahan)"
        action = "Pertahankan kondisi kerja saat ini. Lakukan monitoring rutin setiap 6 bulan."

    return {
        "prediction": int(prediction),
        "label": label,
        "probability_attrition": f"{prob_attrition}%" if prob_attrition is not None else "N/A",
        "recommendation": action,
    }


def print_result(idx: int, data: dict, result: dict) -> None:
    """Menampilkan hasil prediksi secara terformat."""
    separator = "─" * 60
    print(separator)
    print(f"  KARYAWAN #{idx + 1}")
    print(separator)
    print(f"  Usia            : {data['Age']} tahun")
    print(f"  Job Level       : {data['JobLevel']}")
    print(f"  Monthly Income  : ${data['MonthlyIncome']:,}")
    print(f"  OverTime        : {'Ya' if data['OverTime'] == 1 else 'Tidak'}")
    print(f"  Work-Life Bal.  : {data['WorkLifeBalance']} / 4")
    print(f"  Job Satisfaction: {data['JobSatisfaction']} / 4")
    print()
    print(f"  🎯 Hasil Prediksi : {result['label']}")
    print(f"  📊 Probabilitas   : {result['probability_attrition']}")
    print(f"  💡 Rekomendasi    : {result['recommendation']}")
    print(separator)
    print()


# ─────────────────────────────────────────────────────────────────────────────
# 4. MAIN EXECUTION
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("\n" + "=" * 60)
    print("  HR ATTRITION PREDICTION SYSTEM")
    print("  PT Jaya Jaya Maju — Model v1.0")
    print("=" * 60 + "\n")

    # Load model
    model = load_model(MODEL_PATH)

    # Prediksi untuk setiap contoh karyawan
    print("📋 Hasil Prediksi Attrition Karyawan:\n")
    for idx, employee in enumerate(sample_employees):
        result = predict_attrition(model, employee)
        print_result(idx, employee, result)

    print("=" * 60)
    print("  Prediksi selesai. Total karyawan dianalisis:", len(sample_employees))
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
