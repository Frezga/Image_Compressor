# Image Compression with SVD

Proyek ini adalah aplikasi web **kompresi gambar  berbasis  website** menggunakan algoritma **SVD**, dibangun dengan Python & Flask sebagai backend  dan  framework Vue sebagai frontend.

---

## Kontributor
- **Muhamad Afif Aji Putra (L0124134)**
- **Muhammad Akbar Kurniawan (L0124136)**
- **Muhammad Ayman (L0124137)**

##  Fitur Utama

- **Upload Gambar** Pengguna dapat mengunggah gambar untuk dikompresi.
- **Atur Tingkatan Kompresi** Pengguna dapat mengatur tingkatan kompresi gambar.
- **Preview Gambar** Pengguna dapat melihat perbandingan tampilan gambar sebelum dan sesudah kompresi.
- **Antarmuka Web Interaktif:** Tampilan responsif dan mudah digunakan.

---

##  Algoritma: Singular Value Decomposition (SVD)

- **Konversi ke Matriks:** Gambar diubah menjadi matriks numerik (grayscale atau RGB).
- **Dekomposisi SVD:** Matriks gambar dipecah menjadi tiga matriks utama (U, Σ, V^T) menggunakan algoritma SVD.
- **Reduksi Rank:** Hanya sebagian nilai singular terbesar yang dipilih untuk merekonstruksi gambar, sehingga ukuran file menjadi lebih kecil.
- **Rekonstruksi Gambar:** Matriks hasil reduksi digabungkan kembali menjadi gambar yang telah dikompresi.

---

##  Framework & Library

- **Flask:** Backend web server.
- **FastAPI** Framework  untuk membangun REST API backend.
- **Uvicorn** ASGI server untuk menjalankan aplikasi FastAPI.
- **NumPy:** Perhitungan numerik dan PCA.
- **OpenCV:** Manipulasi dan pembacaan gambar.
- **Vue** Framework website.
- **Uvicorn** ASGI server untuk menjalankan aplikasi FastAPI.
---

## 📁 Struktur Direktori

```
Image_Compressor/
├── backend/
│   ├── main.py            # File utama backend FastAPI
│   ├── app/
│   │   └── processing.py  # Proses kompresi gambar
│   ├── uploads/           # Tempat upload gambar asli
│   ├── compressed/        # Hasil gambar yang sudah dikompresi
│   └── requirements.txt   # Daftar dependensi backend
├── src/
│   ├── views/             # Halaman-halaman utama frontend (Vue)
│   ├── components/        # Komponen frontend (Vue)
│   └── assets/            # Gambar/logo untuk frontend
└── README.md              # Dokumentasi proyek
```

---

##  Cara Menjalankan

1. **Siapkan environment:**
   ```bash
   pip install -r requirements.txt
   npm install
   .\venv\Scripts\activate
   ```

2. **Jalankan server backend (terminal pertama)**
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

3. **Jalankan website (terminal kedua)**
   ```bash
   npm run dev
   ```

4. **Buka website di browser:**
   ```
   http://localhost:5173/Image_Compressor/
   ```

---

## 📸 Cara Kerja Singkat

1. **Upload gambar** melalui halaman utama.
2. **Pilih tingkatan kompresi gambar** geser slider untuk memilih tingkatan kompresi gambar.
3. **Sistem memproses gambar** sistem akan melakukan kompresi gambar yang telah diupload.
4. **Hasil kompresi** (ukuran gambar, persentase perbedaan gambar, waktu kompresi gambar) ditampilkan di halaman hasil.


---

## ❓ FAQ & Catatan

- **Format gambar:** JPG/PNG.
- **Download:** Hasil kompresi gambar dengan resolusi penuh dapat dilihat  dengan menekan tombol "download" dan pengguna dapat menyimpannya ke local storage
- **Upload:** Gambar yang diupload disimpan di folder `uploads/`.
- **Compressed:** Hasil gambar yang telah dikompresi disimpan di folder `compressed/`


---

## 👨‍💻 Kontribusi

Silakan fork dan pull request jika ingin berkontribusi atau mengembangkan fitur lebih lanjut.

---

## Lisensi

Proyek ini dibuat untuk memenuhi tugas project mata kuliah Aljabar Linear

## PROGRAM STUDI INFORMATIKA
## FAKULTAS TEKNOLOGI INFORMASI DAN SAINS DATA
## UNIVERSITAS SEBELAS MARET
