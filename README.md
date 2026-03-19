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
# 1. Buat virtual environment
python3 -m venv venv

# 2. Aktifkan virtual environment
# Mac/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

**requirements.txt:**
```
numpy
pandas
matplotlib
seaborn
scikit-learn>=1.4.0
joblib
streamlit>=1.28.0
altair>=5.0.0
pillow>=10.0.0
```

**Struktur Proyek:**
```
submission/
├── model/
│   └── model.pkl
├── app.py
├── notebook.ipynb
├── prediction.py
├── employee_data.csv
├── README.md
└── requirements.txt
```

---

## Business Dashboard

Dashboard interaktif dibuat menggunakan Streamlit untuk memberikan gambaran menyeluruh kepada tim HR dan manajemen eksekutif tentang kondisi attrition di perusahaan.

🔗 **Link Dashboard:** [https://3xhevdnjbhbg7xziwsxvg9.streamlit.app](https://3xhevdnjbhbg7xziwsxvg9.streamlit.app)

> **Cara upload gambar dashboard ke README:**
> Buka file README.md di GitHub → klik Edit (ikon pensil) → drag & drop gambar dashboard ke text editor → GitHub akan otomatis generate URL gambar → gunakan URL tersebut di bawah ini.

<!-- Ganti URL_GAMBAR_DARI_GITHUB dengan URL yang didapat setelah drag & drop gambar di GitHub editor -->
![Dashboard HR Attrition](URL_GAMBAR_DARI_GITHUB)

### KPI Utama yang Ditampilkan:
| KPI | Keterangan |
|-----|-----------|
| **Attrition Rate** | Persentase karyawan yang keluar |
| **High Risk Employee** | % karyawan dengan probabilitas resign > 50% |
| **Avg Income** | Perbandingan rata-rata gaji karyawan resign vs bertahan |

### Fitur Filter Dashboard:
- **Filter Department** — Multiselect, bisa pilih satu/lebih/semua departemen
- **Filter Gender** — Multiselect, bisa pilih satu/lebih/semua gender

### Visualisasi dalam Dashboard:
1. **Overtime vs Attrition** — Perbandingan resign antara karyawan overtime vs tidak
2. **Distribusi Pendapatan** — Distribusi income karyawan resign vs bertahan
3. **Work-Life Balance vs Attrition** — Korelasi WLB dengan keputusan resign
4. **Job Level vs Attrition** — Level jabatan dengan tingkat resign tertinggi

---

## Insight Bisnis

- Karyawan dengan lembur tinggi memiliki risiko attrition yang jauh lebih besar, mengindikasikan adanya ketidakseimbangan beban kerja.
- Work-life balance yang rendah merupakan prediktor kuat terhadap pengunduran diri dan perlu segera ditangani melalui kebijakan HR.
- Karyawan pada level jabatan yang lebih rendah cenderung lebih sering keluar, mengindikasikan adanya kekhawatiran terkait pengembangan karir.
- Karyawan berpenghasilan rendah menunjukkan kecenderungan attrition yang lebih tinggi dibandingkan kelompok berpenghasilan lebih tinggi.

## Validasi Insight Berbasis Model

Temuan-temuan yang disajikan dalam dashboard ini sepenuhnya berbasis bukti empiris. Variabel-variabel yang ditampilkan — **OverTime, MonthlyIncome, JobLevel, dan WorkLifeBalance** — secara eksplisit merupakan prediktor dengan kontribusi tertinggi terhadap attrition berdasarkan analisis *feature importance* model Random Forest.

## Definisi Karyawan Berisiko Tinggi

- **Definisi:** Seorang karyawan dikategorikan sebagai "Berisiko Tinggi" apabila probabilitas prediksi attrition-nya melebihi ambang batas **0,5 (50%)**.
- **Justifikasi Threshold:** Batas keputusan 0,5 dipilih untuk mencapai keseimbangan optimal antara precision dan recall.
- **Mekanisme:** Metrik ini diturunkan langsung dari fungsi `predict_proba()` model.
- **Nilai Bisnis:** Mentransformasi kebijakan HR dari reaktif menjadi proaktif.

---

## Menjalankan Prediksi

```bash
python prediction.py
```

---

## Conclusion

Berdasarkan analisis menyeluruh terhadap dataset HR PT Jaya Jaya Maju:

1. **OverTime** adalah prediktor terkuat attrition
2. **Monthly Income rendah** mendorong karyawan level bawah untuk keluar
3. **Job Level rendah** menandakan minimnya jalur karier yang jelas
4. **Work-Life Balance buruk** menurunkan kepuasan kerja
5. **Distance From Home jauh** berkorelasi dengan kelelahan komuter

Model Logistic Regression dipilih sebagai model terbaik karena menunjukkan performa yang lebih stabil dibanding Random Forest.

---

## Rekomendasi Action Items

### 🔴 Prioritas Tinggi
1. **Batasi Overtime** — Terapkan kebijakan pembatasan jam lembur maksimal 2x/minggu
2. **Evaluasi & Sesuaikan Gaji Entry-Level** — Lakukan benchmarking salary untuk Job Level 1 & 2

### 🟡 Prioritas Menengah (1-3 Bulan)
3. **Program Work-Life Balance** — Flexible working hours dan wellness program
4. **Jalur Karier yang Jelas** — Individual Development Plan (IDP) untuk karyawan junior
5. **Fasilitas Commuting** — Subsidi transportasi bagi karyawan dengan jarak > 20 km

### 🟢 Prioritas Jangka Panjang (3-12 Bulan)
6. **Sistem Early Warning Berbasis ML** — Deploy model prediksi ke dashboard HR
7. **Exit Interview Terstruktur** — Kumpulkan data kualitatif untuk memperkaya model
8. **Program Employee Engagement** — Survey kepuasan berkala (quarterly)

---

## Link Proyek

- 🔗 **GitHub:** [https://github.com/ANDI-BACHDAR-DD/Submission_kelas_Expert_data_science_Dicoding_andi_bachdar](https://github.com/ANDI-BACHDAR-DD/Submission_kelas_Expert_data_science_Dicoding_andi_bachdar.git)
- 🌐 **Streamlit Dashboard:** [https://3xhevdnjbhbg7xziwsxvg9.streamlit.app](https://3xhevdnjbhbg7xziwsxvg9.streamlit.app)

---

*Proyek ini dibuat sebagai submission Dicoding — Belajar Penerapan Data Science | © 2026 Andi Bachdar*