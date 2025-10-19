# 🏥 Chatbot Kesehatan - Versi Pemula

Chatbot kesehatan sederhana berbasis AI yang dibuat dengan Python dan Streamlit. **GRATIS** dan **TANPA API KEY**!

![Version](https://img.shields.io/badge/version-1.0-blue) ![Python](https://img.shields.io/badge/Python-3.8+-green) ![Streamlit](https://img.shields.io/badge/Streamlit-1.31-red)

## 📸 Screenshot

### 1. Halaman Utama

![Homepage](screenshots/homepage.png)

### 2. Chat Interface

![Chat](screenshots/chat.png)

### 3. Profil Pengguna

![Profile](screenshots/profile.png)

## 🎯 Fitur

✅ **Tanpa API Key** - Tidak perlu daftar atau bayar apapun  
✅ **Database Pengetahuan** - Informasi kesehatan yang sudah tersimpan  
✅ **Profil Pengguna** - Simpan nama, usia, dan tujuan kesehatan  
✅ **Respons Cepat** - Langsung menjawab tanpa loading  
✅ **UI Menarik** - Desain modern dengan gradient warna  
✅ **Mudah Digunakan** - Cocok untuk pemula

## 💡 Topik yang Bisa Ditanyakan

- 🥗 Sarapan sehat
- 💪 Olahraga untuk pemula
- 💧 Kebutuhan air minum
- 😴 Tips tidur berkualitas
- 🧘 Mengatasi stress
- 🍎 Diet sehat
- 💊 Vitamin penting
- 🏋️ Program workout

## 🚀 Cara Install & Jalankan

### Langkah 1: Download Python

1. Buka [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.8 atau lebih baru
3. **PENTING**: Centang "Add Python to PATH" saat install

### Langkah 2: Download Project

```bash
# Download ZIP dari GitHub atau clone:
git clone https://github.com/username/chatbot-kesehatan.git
cd chatbot-kesehatan
```

### Langkah 3: Install Library

```bash
# Install Streamlit (hanya ini yang dibutuhkan!)
pip install streamlit
```

### Langkah 4: Jalankan

```bash
streamlit run chatbot.py
```

Aplikasi akan terbuka di browser: `http://localhost:8501`

## 📝 Struktur File

```
chatbot-kesehatan/
│
├── chatbot.py          # File utama (HANYA 1 FILE!)
├── requirements.txt    # Library yang dibutuhkan
├── README.md          # Dokumentasi ini
└── screenshots/       # Folder screenshot
    ├── homepage.png
    ├── chat.png
    └── profile.png
```

## 💻 Cara Pakai

### 1. **Isi Profil** (di sidebar kiri)

- Masukkan nama Anda
- Atur usia dengan slider
- Pilih tujuan kesehatan

### 2. **Mulai Chat**

Ketik pertanyaan di kotak chat, contoh:

```
"Apa saran sarapan sehat?"
"Gimana cara olahraga untuk pemula?"
"Berapa gelas air yang harus diminum per hari?"
"Tips mengatasi stress dong"
```

### 3. **Lihat Statistik**

- Total pesan yang dikirim
- Jumlah tujuan kesehatan aktif
- Nama pengguna

### 4. **Hapus Chat**

Klik tombol "🗑️ Hapus Riwayat Chat" di sidebar

## 🎨 Kelebihan Versi Ini

| Fitur        | Versi Ini      | Versi Lain     |
| ------------ | -------------- | -------------- |
| API Key      | ❌ Tidak Perlu | ✅ Butuh       |
| Biaya        | 💚 GRATIS      | 💰 Bayar       |
| Setup        | ⚡ 5 Menit     | ⏰ 30+ Menit   |
| File         | 📄 1 File      | 📚 Banyak File |
| Kompleksitas | 🟢 Mudah       | 🔴 Susah       |

## ❓ FAQ (Pertanyaan Umum)

**Q: Apa bedanya dengan ChatGPT?**  
A: ChatGPT pakai API berbayar. Ini gratis dan offline (tanpa internet juga bisa jalan).

**Q: Apakah jawabannya akurat?**  
A: Ya, tapi tetap konsultasi ke dokter untuk masalah serius.

**Q: Bisa ditambah topik lain?**  
A: Bisa! Tambahkan di `knowledge_base` di file `chatbot.py`.

**Q: Kenapa tidak pakai AI beneran?**  
A: Ini versi pemula. Kalau mau pakai AI (GPT), lihat versi advanced.

**Q: Bisa dipakai untuk ujian/tugas?**  
A: Bisa! Ini project yang lengkap untuk final project.

## 🔧 Troubleshooting

### Error: "streamlit not found"

```bash
# Install ulang streamlit
pip install --upgrade streamlit
```

### Error: "python not found"

```bash
# Coba pakai python3 atau py
python3 -m pip install streamlit
py -m pip install streamlit
```

### Aplikasi tidak muncul

```bash
# Cek apakah ada error di terminal
# Atau coba port lain:
streamlit run chatbot.py --server.port 8502
```

### Tombol tidak berfungsi

```bash
# Refresh browser (Ctrl + R)
# Atau restart aplikasi (Ctrl + C, lalu jalankan lagi)
```

## 📚 Cara Upload ke GitHub

### 1. Buat Repository Baru

- Login ke [github.com](https://github.com)
- Klik tombol **+** → **New repository**
- Nama: `chatbot-kesehatan`
- Pilih **Public**
- Klik **Create repository**

### 2. Upload File

```bash
# Di folder project:
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/USERNAME/chatbot-kesehatan.git
git branch -M main
git push -u origin main
```

Ganti `USERNAME` dengan username GitHub Anda.

## 🎓 Untuk Final Project

Yang perlu dikumpulkan:

1. ✅ **URL GitHub**: `https://github.com/USERNAME/chatbot-kesehatan`
2. ✅ **Screenshot UI**: Ambil 3-4 screenshot (homepage, chat, profile)
3. ✅ **README lengkap**: Sudah ada di file ini

## 📈 Cara Upgrade ke Versi Advanced

Jika nanti mau pakai AI sungguhan (GPT):

1. Daftar di [openai.com](https://platform.openai.com/)
2. Dapatkan API Key
3. Install library tambahan: `pip install openai`
4. Ganti fungsi `get_bot_response()` dengan API call

## 🤝 Kontribusi

Silakan fork dan submit pull request! Semua kontribusi diterima.

## 📄 License

MIT License - Bebas digunakan untuk belajar dan project.

## 👨‍💻 Author

**Nama Anda**

- GitHub: [@username](https://github.com/username)
- Email: your.email@example.com

## ⭐ Support

Jika project ini membantu, kasih ⭐ di GitHub ya!

---

**Made with ❤️ and ☕ untuk pembelajaran AI**
