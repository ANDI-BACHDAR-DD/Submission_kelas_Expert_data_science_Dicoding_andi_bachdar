# Script Narasi Video Presentasi (Target: 5 Menit)
**Proyek: Analisis dan Prediksi Attrition Karyawan PT Jaya Jaya Maju**

---

## 🎬 Bagian 1: Pembukaan & Latar Belakang (0:00 - 1:00)

**(Visual: Menampilkan slide judul dan kemudian beralih ke struktur dataset di notebook/slide pengantar)**

**[Narator]**
"Halo semuanya. Saya [ANDI BACHDAR DD], dan pada kesempatan kali ini saya akan mempresentasikan hasil proyek *Human Resources Analytics* untuk PT Jaya Jaya Maju. 

Saat ini, PT Jaya Jaya Maju sedang menghadapi tantangan serius. Meskipun bisnis terus berkembang, tingkat attrition atau persentase karyawan yang keluar *resign* dari perusahaan berada di angka yang cukup tinggi, yaitu sekitar 16,9% berdasarkan data yang kita miliki. Tingkat turnover yang tinggi ini tentu berdampak buruk pada efisiensi operasional dan biaya rekrutmen.

Tujuan dari proyek ini adalah menemukan akar permasalahan *mengapa* karyawan memilih keluar, serta membangun sistem prediksi dini dengan Machine Learning untuk mencegah attrition di masa depan."

---

## 🎬 Bagian 2: Penjelasan Dashboard & Insight (1:00 - 3:00)

**(Visual: Menampilkan layar penuh `dashboard.png` dan menunjuk ke bagian-bagian spesifik yang sedang dibahas)**

**[Narator]**
"Untuk memudahkan tim HR dan Manajemen memonitor situasi, saya telah merancang sebuah Business Dashboard interaktif. Mari kita lihat insight bisnis utama yang kita temukan:

*(Tunjuk angka KPI di atas)*
"Dari total lebih dari 1.400 karyawan, kita sudah kehilangan lebih dari 200 talenta atau sekitar 16,9% attrition rate. Ini adalah angka merah yang harus segera diturunkan ke bawah 10%."

*(Tunjuk grafik "Attrition by OverTime")*
"Insight pertama dan yang paling kritis adalah **Overtime** atau kerja lembur. Dari grafik ini, terlihat jelas bahwa karyawan yang sering bekerja lembur memiliki attrition rate **3 kali lebih tinggi** dibandingkan mereka yang jam kerjanya normal. Ini adalah indikasi kuat adanya beban kerja yang tidak seimbang (*burnout*)."

*(Tunjuk grafik Boxplot Income & Job Level)*
"Insight kedua adalah dari segi kompensasi dan jenjang karier. Dapat kita lihat di grafik ini, mayoritas karyawan yang *resign* adalah mereka yang berada di Job Level 1 (Entry level) dan memiliki pendapatan per bulan (Monthly Income) yang rendah, yakni berada di kisaran kuartil bawah. Artinya, kompensasi finansial yang kurang kompetitif menjadi pendorong kuat karyawan untuk mencari peluang di perusahaan lain."

*(Tunjuk grafik Work-Life Balance)*
"Selain itu, faktor *Work-Life Balance* juga sangat berpengaruh. Karyawan yang melaporkan skor WLB 'Buruk' atau skor 1, jauh lebih rentan untuk keluar."

"Kesimpulan dari analisis data ini adalah: **Kombinasi antara beban kerja yang di luar batas (overtime) dan sistem kompensasi yang kurang memadai di level bawah adalah akar dari tingginya attrition di PT Jaya Jaya Maju.**"

---

## 🎬 Bagian 3: Machine Learning & Prediksi (3:00 - 4:00)

**(Visual: Menampilkan cuplikan `notebook.ipynb` pada bagian evaluasi model: ROC Curve & Feature Importance, lalu beralih ke script `prediction.py`)**

**[Narator]**
"Untuk mengubah analisis ini menjadi *tindakan proaktif*, saya telah membangun dan mentuning dua model Machine Learning: *Logistic Regression* dan *Random Forest*.

Setelah melalui proses *hyperparameter tuning*, kita mendapatkan performa model yang sangat baik dengan akurasi di atas 85% dan AUC Score mendekati 0.85. 

Dari *Feature Importance* model, kita kembali memvalidasi bahwa atribut seperti OverTime, MonthlyIncome, dan TotalWorkingYears adalah fitur yang paling dominan dalam membedakan mana karyawan yang akan bertahan dan mana yang akan resign.

Bukan hanya itu, saya juga telah menyiapkan skrip `prediction.py`. Skrip ini memungkinkan tim HR untuk memasukkan data profil seorang karyawan, dan sistem secara otomatis akan mengeluarkan prediksi apakah karyawan tersebut berisiko resign, lengkap dengan nilai probabilitasnya. Sistem peringatan dini (*early warning system*) ini sangat vital bagi HR agar bisa melakukan intervensi sebelum surat *resign* diajukan."

---

## 🎬 Bagian 4: Rekomendasi Actionable & Penutup (4:00 - 5:00)

**(Visual: Slide rekomendasi akhir / Action Items yang jelas berserta Business Impact-nya)**

**[Narator]**
"Berdasarkan insight data dan model yang telah kita bangun, ada tiga rekomendasi strategis (*Action Items*) yang saya ajukan untuk Manajemen PT Jaya Jaya Maju:

1. **Evaluasi dan Batasi Overtime Segera:** Kita harus membatasi jam lembur maksimal. Jika beban kerja memang terlalu tinggi, perusahaan harus memprioritaskan rekrutmen tambahan daripada membebankan overtime terus-menerus ke karyawan yang sama.
2. **Review Struktur Kompensasi Entry-Level:** Tingkatkan *baseline salary* atau sediakan insentif khusus untuk Job Level 1 agar mereka tidak merasa 'underpaid' dan punya alasan untuk bertahan lebih lama.
3. **Menerapkan Sistem Prediksi:** HR perlu mengintegrasikan model Machine Learning yang telah dibuat ke dalam sistem evaluasi semesteran. Karyawan-karyawan yang diprediksi berisiko tinggi (*high risk of attrition*) harus segera dipanggil untuk sesi *1-on-1* dan diberikan program retensi yang tepat.

Dengan implementasi rekomendasi berbasis data ini, saya yakin PT Jaya Jaya Maju dapat menekan angka attrition secara signifikan, menghemat miliaran rupiah dari biaya rekrutmen berulang, dan membangun budaya kerja yang jauh lebih produktif.

Terima kasih atas perhatiannya. Saya [Nama Anda], pamit undur diri." 

*(Fade out / Selesai)*
