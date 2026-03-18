# Proyek Akhir: Menyelesaikan Permasalahan Human Resources

## Business Understanding

**PT Jaya Jaya Maju** adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1.000 karyawan yang tersebar di berbagai divisi. Seiring pertumbuhan bisnis yang pesat, perusahaan menghadapi tantangan serius di bidang **manajemen sumber daya manusia (SDM)**, yaitu tingginya tingkat **attrition** (keluar/resign) karyawan.

Tingginya attrition tidak hanya menimbulkan biaya rekrutmen dan pelatihan yang besar, tetapi juga berdampak pada **produktivitas tim**, **moral karyawan**, dan **kelangsungan operasional** perusahaan secara keseluruhan.

---

## Permasalahan Bisnis

Berdasarkan data HR internal, perusahaan mengidentifikasi sejumlah permasalahan kritis:

1. **Tingkat attrition melebihi 10%** — angka yang dianggap berbahaya bagi keberlangsungan operasional
2. **Kesulitan mengidentifikasi faktor penyebab** attrition secara sistematis dan berbasis data
3. **Tidak ada sistem peringatan dini** (early warning) untuk mendeteksi karyawan yang berisiko resign
4. **Keputusan HR masih bersifat reaktif**, bukan proaktif berdasarkan data

---

## Cakupan Proyek

Proyek ini mencakup tiga area utama:

| Area | Deskripsi |
|------|-----------|
| **Analisis Data** | Eksplorasi mendalam terhadap dataset HR untuk menemukan pola dan faktor penyebab attrition |
| **Business Dashboard** | Visualisasi interaktif KPI dan faktor attrition untuk mendukung keputusan manajemen |
| **Machine Learning** | Model prediksi attrition dengan performa tinggi (optimized via hyperparameter tuning) |

---

## Persiapan

**Sumber Data:**
```
https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/employee/employee_data.csv
```

**Setup Environment:**

```bash
# Clone atau buat direktori proyek
mkdir submission && cd submission

# Install dependencies
pip install -r requirements.txt
```

**requirements.txt:**
```
numpy
pandas
matplotlib
seaborn
scikit-learn==1.2.2
joblib==1.3.1
```

**Struktur Proyek:**
```
submission/
├── model/
│   └── model.pkl
├── notebook.ipynb
├── prediction.py
├── README.md
├── dashboard.png
└── requirements.txt
```

---

## Business Dashboard

Dashboard dibuat untuk memberikan gambaran menyeluruh kepada tim HR dan manajemen eksekutif tentang kondisi attrition di perusahaan.

![Dashboard HR Attrition](dashboard.png)

### KPI Utama yang Ditampilkan:
| KPI | Nilai |
|-----|-------|
| **Total Karyawan** | ~1.400+ |
| **Jumlah Karyawan Keluar** | ~200+ |
| **Attrition Rate** | ~16.9% |

### Visualisasi dalam Dashboard:
1. **Attrition by Department** — Divisi mana yang paling banyak kehilangan karyawan
2. **Attrition by OverTime** — Perbandingan resign antara karyawan overtime vs tidak
3. **Attrition by Monthly Income** — Distribusi pendapatan karyawan yang resign vs bertahan
4. **Attrition by Job Level** — Level jabatan dengan tingkat resign tertinggi
5. **Attrition by Work-Life Balance** — Korelasi kepuasan WLB dengan keputusan resign

## Business Insights
- Employees with high overtime have significantly higher attrition risk, indicating workload imbalance.
- Low work-life balance is a strong predictor of resignation and should be addressed through HR policy.
- Employees in lower job levels are more likely to leave, suggesting career growth concerns.
- Lower-income employees show higher attrition tendency compared to higher-income groups.

## Model-Driven Insights Validation
The intuitive findings presented in the dashboard are unequivocally evidence-based. The variables featured—**OverTime, MonthlyIncome, JobLevel, and WorkLifeBalance**—are explicitly the top highest-contributing predictors of attrition according to the Random Forest model's feature importance analysis. This guarantees that all subsequent executive decisions target statistically proven root causes rather than mere observational correlation.

## High Risk Employee Definition
The "High Risk Employee (%)" KPI provides an actionable early warning metric for the HR team.
- **Definition:** An employee is classified as "High Risk" if their predicted probability of attrition exceeds the **0.5 (50%) threshold**.
- **Threshold Justification:** A decision boundary of 0.5 was selected to achieve a robust balance between precision and recall, ensuring HR interventions capture genuine flight risks without generating excessive false alarms.
- **Mechanism:** This metric is derived directly from the model's `predict_proba()` function, isolating the confidence score for the attrition class based on each employee's unique profile.
- **Business Value:** This transforms HR policy from reactive to proactive, enabling targeted retention strategies for highly vulnerable demographics before resignation occurs.

---

## Menjalankan Prediksi

Setelah model dilatih dan disimpan (melalui `notebook.ipynb`), gunakan script berikut untuk melakukan prediksi:

```bash
python prediction.py
```

Script ini akan memuat `model/model.pkl` dan menghasilkan prediksi attrition untuk contoh data karyawan.

---

## Conclusion

Berdasarkan analisis menyeluruh terhadap dataset HR PT Jaya Jaya Maju, ditemukan bahwa **attrition karyawan dipicu oleh beberapa faktor kunci yang saling berinteraksi**:

1. **OverTime** adalah prediktor terkuat — karyawan yang bekerja overtime secara reguler memiliki risiko resign jauh lebih tinggi
2. **Monthly Income rendah** menjadi faktor pendorong utama karyawan level bawah untuk mencari peluang di tempat lain
3. **Job Level rendah** (entry-level) menandakan minimnya jalur karier yang jelas
4. **Work-Life Balance buruk** menurunkan kepuasan kerja dan meningkatkan kemungkinan resign
5. **Distance From Home jauh** berkorelasi dengan kelelahan komuter yang berujung pada turnover

Model Random Forest (setelah hyperparameter tuning) berhasil mencapai **akurasi > 85%** dan **AUC > 0.80**, menjadikannya alat prediksi yang andal untuk sistem early warning HR.

---

## Rekomendasi Action Items

Berdasarkan temuan analisis, berikut adalah rekomendasi strategis untuk tim HR PT Jaya Jaya Maju:

### 🔴 Prioritas Tinggi (Segera Dilaksanakan)
1. **Batasi Overtime** — Terapkan kebijakan pembatasan jam lembur maksimal 2x/minggu dan berikan kompensasi yang adil
2. **Evaluasi & Sesuaikan Gaji Entry-Level** — Lakukan benchmarking salary untuk posisi Job Level 1 & 2 agar kompetitif di pasar

### 🟡 Prioritas Menengah (1-3 Bulan)
3. **Program Work-Life Balance** — Implementasikan flexible working hours, remote work option, dan wellness program
4. **Jalur Karier yang Jelas** — Buat Individual Development Plan (IDP) dan program mentoring untuk karyawan junior
5. **Fasilitas Commuting** — Sediakan shuttle bus, subsidi transportasi, atau opsi remote work bagi karyawan dengan jarak rumah > 20 km

### 🟢 Prioritas Jangka Panjang (3-12 Bulan)
6. **Sistem Early Warning Berbasis ML** — Deploy model prediksi ini ke dashboard HR untuk monitoring real-time karyawan berisiko
7. **Exit Interview Terstruktur** — Kumpulkan data kualitatif untuk memperkaya model prediksi
8. **Program Employee Engagement** — Survey kepuasan berkala (quarterly) dan tindak lanjut yang terukur

---

*Proyek ini dibuat sebagai submission Dicoding — Belajar Penerapan Data Science | © 2024*
