
# 🧠 Analisis Sentimen Review Produk Skintific Cushion

Proyek ini merupakan aplikasi analisis sentimen berbasis Machine Learning yang dibangun menggunakan Python dan Streamlit. Tujuannya adalah untuk memahami persepsi pelanggan terhadap produk **Skintific Cushion** melalui ulasan yang ditulis di platform e-commerce.

---

## 🚀 Fitur Utama

1. **Tabel Data Review (Setelah Preprocessing)**
   - Menampilkan review asli, hasil preprocessing (pembersihan teks), dan hasil klasifikasi sentimen (Positif, Negatif, Netral).
2. **Distribusi Sentimen**
   - Visualisasi dalam bentuk pie chart atau bar chart untuk menunjukkan proporsi masing-masing sentimen.
3. **Wordcloud Positif & Negatif**
   - Visualisasi kata-kata yang sering muncul di review positif dan negatif.
4. **Evaluasi Model Machine Learning**
   - Menampilkan metrik performa model seperti Akurasi, Precision, Recall, dan F1-score.
5. **Kesimpulan dan Insight**
   - Rangkuman insight dari hasil analisis, seperti keunggulan dan kekurangan produk berdasarkan persepsi pengguna.

---

## 🛠️ Teknologi yang Digunakan

- Python
- Streamlit
- Pandas
- scikit-learn
- NLTK
- WordCloud
- Matplotlib & Seaborn

---

## 📸 Galeri Output (Tambahkan Screenshot-mu di Sini)

### 1. Tabel Data Review (Preprocessing & Sentimen)
![Preview Tabel Review](<Tabel Data Review.png>)

### 2. Distribusi Sentimen
![Pie Chart Sentimen](<Distribusi Sentimen.png>)

### 3. Wordcloud Positif & Negatif
![Wordcloud Positif & Negatif](<Wordcloud Review Positif & Negatif.png>)

### 4. Wordcloud Negatif
![Akurasi Model Machine Learning](<Akurasi Model Machine Learning.png>)

### 5. Kesimpulan dan Insight
![Kesimpulan dan Insight](<Kesimpulan dan Insight.png>)

---

## 📂 Struktur File

```
📁 Project Folder
├── cleaned_cushion_skintific.csv     # Dataset ulasan
├── streamlit_sentimen_skintific.py   # Aplikasi Streamlit utama
├── README.md                         # Dokumentasi ini
└── /screenshots                      # Folder untuk menyimpan screenshot
```

---

## 📈 Cara Menjalankan Aplikasi

1. Pastikan sudah install semua dependensi:
   ```bash
   pip install streamlit pandas scikit-learn nltk wordcloud seaborn matplotlib
   ```
2. Jalankan aplikasi Streamlit:
   ```bash
   streamlit run streamlit_sentimen_skintific.py
   ```

---

## 🧠 Insight dari Proyek

- Mayoritas review terhadap Skintific Cushion bersifat **positif**.
- **Kelebihan** yang sering disebutkan: coverage bagus, ringan di kulit, glowing finish.
- **Kekurangan** yang paling sering muncul: cakey, tidak cocok untuk kulit berminyak.
- Rekomendasi untuk brand: formula dapat ditingkatkan agar lebih cocok untuk kulit kombinasi hingga berminyak.

---

## 📚 Potensi Pengembangan

- Upload file ulasan sendiri
- Perbandingan beberapa model ML (Naive Bayes, SVM, LogReg)
- Ekspor hasil ke CSV/Excel
- Dashboard analitik lebih interaktif

---

## 🏁 Penutup

Proyek ini cocok digunakan untuk:
- Skripsi/Tugas Akhir (tema: NLP, ML, Analisis Sentimen, Streamlit)
- Portofolio Data Science
- Studi pasar & feedback produk e-commerce

---

> Dibuat dengan ❤️ oleh [Nama Kamu]
