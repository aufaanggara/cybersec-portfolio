# 📚 RESUME ROOM: Introduction to Digital Forensics
**Tanggal:** 27 Juni 2026

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📌 1. KONSEP DASAR

- **Forensics**: penerapan metode & prosedur untuk menyelidiki dan menyelesaikan kejahatan.
- **Digital Forensics**: cabang forensik yang menyelidiki **cyber crime**.
- **Cyber Crime**: segala aktivitas kriminal yang dilakukan pada/menggunakan perangkat digital.
- Tujuan: menemukan & menganalisis bukti digital secara sah untuk keperluan hukum (legal proceedings).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📌 2. EMPAT FASE DIGITAL FORENSICS (Standar NIST)

**NIST (National Institute of Standards and Technology)** mendefinisikan 4 fase proses digital forensics:

1. **Collection** (Pengumpulan)
   - Identifikasi semua perangkat sumber data (PC, laptop, kamera digital, USB, dll).
   - Data asli **tidak boleh tampered** (dimanipulasi).
   - Harus disertai dokumentasi rinci barang yang dikumpulkan.

2. **Examination** (Pemeriksaan)
   - Menyaring (filter) data besar → ekstrak data yang relevan saja.
   - Contoh: dari banyak media file, ambil hanya yang sesuai tanggal/waktu/user tertentu.

3. **Analysis** (Analisis)
   - Fase paling kritis.
   - Korelasikan data dengan bukti lain → tarik kesimpulan.
   - Tujuan: susun kronologi aktivitas relevan dengan kasus.

4. **Reporting** (Pelaporan)
   - Laporan rinci: metodologi + temuan + rekomendasi.
   - Disampaikan ke law enforcement & executive management.
   - Wajib ada **executive summary** (untuk pihak non-teknis).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📌 3. JENIS-JENIS DIGITAL FORENSICS

Computer Forensics = payung/induk besar, dengan cabang:

- **Computer Forensics**: investigasi komputer (jenis paling umum).
- **Mobile Forensics**: ekstraksi call records, text messages, GPS location, dll dari perangkat seluler.
- **Network Forensics**: investigasi seluruh jaringan, mayoritas bukti dari **network traffic logs**.
- **Database Forensics**: investigasi intrusi ke database → modifikasi/eksfiltrasi data.
- **Cloud Forensics**: investigasi data di infrastruktur cloud — sulit karena bukti minim.
- **Email Forensics**: investigasi email untuk deteksi phishing/fraudulent campaign.
- **Memory Forensics**: investigasi data di RAM (volatile).
- **Malware Forensics**: investigasi malware.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📌 4. PRINSIP PENTING AKUISISI BUKTI

- **Proper Authorization**: wajib ada izin (search warrant) dari otoritas berwenang sebelum mengumpulkan bukti. Tanpa ini → bukti **inadmissible** (tidak sah) di pengadilan.

- **Chain of Custody**: dokumen formal pencatatan bukti, berisi:
  - Deskripsi bukti (nama, jenis)
  - Nama individu yang mengumpulkan
  - Tanggal & waktu pengumpulan
  - Lokasi penyimpanan bukti
  - Waktu akses & siapa yang mengakses
  - Fungsi: membuktikan **integrity** & **reliability** bukti di pengadilan.

- **Write Blocker**: alat (hardware) yang dipasang antara hard drive tersangka & workstation forensik, mencegah perubahan data (timestamp, dll) selama proses akuisisi → menjaga **original state** bukti.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📌 5. WINDOWS FORENSICS — JENIS IMAGE

- **Disk Image**: copy bit-by-bit seluruh storage (HDD/SSD). Bersifat **non-volatile** (data tetap ada walau restart). Isi: file media, dokumen, browsing history, dll.
- **Memory Image**: copy isi RAM. Bersifat **volatile** (hilang saat power off/restart). Isi: open files, running processes, network connections. **Harus diambil PERTAMA** sebelum disk image, karena cepat hilang.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📌 6. TOOLS WINDOWS FORENSICS

| Tool | Fungsi |
|---|---|
| **FTK Imager** | Akuisisi disk image (GUI), juga bisa analisis disk image |
| **Autopsy** | Platform open-source untuk analisis disk image: keyword search, deleted file recovery, file metadata, extension mismatch detection |
| **DumpIt** | Akuisisi memory image via command-line, berbagai format |
| **Volatility** | Analisis memory image, pakai plugin per-artifact, support Windows/Linux/macOS/Android |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📌 7. ANALISIS METADATA — COMMAND & TOOLS

### `pdfinfo` — baca metadata file PDF

```
pdfinfo <namafile>.pdf
```
- Tidak ada switch khusus dipakai di room ini — command dasar langsung menampilkan semua metadata.
- Output penting: **Title**, **Subject**, **Author**, **Creator**, **Producer**, **CreationDate**, **ModDate**, Pages, File size, PDF version, dll.
- Install jika belum ada (Kali/Debian):
```
sudo apt install poppler-utils
```

### `exiftool` — baca/tulis metadata EXIF pada gambar

```
exiftool <namafile>.jpg
```
- Tidak ada switch khusus dipakai — command dasar menampilkan semua EXIF metadata.
- Output penting: **Make** (merk kamera), **Camera Model Name**, **Lens ID**, **Date/Time Original**, **GPS Latitude**, **GPS Longitude**, **GPS Position**, Focal Length, Aperture, ISO, dll.
- Install jika belum ada (Kali/Debian):
```
sudo apt install libimage-exiftool-perl
```

**EXIF (Exchangeable Image File Format)**: standar penyimpanan metadata pada file gambar — bisa berisi info kamera, waktu, GPS, dll.

### Konversi format koordinat GPS untuk dicari di Maps
- Format mentah exiftool: `51 deg 30' 51.90" N`
- Format yang diterima Google/Bing Maps: ganti `deg` → simbol derajat `°`, hapus spasi ekstra → `51°30'51.9"N 0°5'38.73"W`

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📌 8. STUDI KASUS DALAM ROOM

1. **Kasus perampokan bank**: bukti ditemukan di laptop/hard drive/ponsel tersangka berupa peta bank digital, dokumen rute masuk-keluar, dokumen kontrol keamanan fisik, foto/video perampokan sebelumnya, chat & call record ilegal.

2. **Kasus "penculikan kucing Gado" (ransom letter)**: dokumen permintaan tebusan (Word→PDF) dan foto terlampir dianalisis metadatanya untuk mengungkap identitas pelaku:
   - `pdfinfo` pada PDF → mengungkap **Author** dokumen.
   - `exiftool` pada foto → mengungkap **Camera Model** & **GPS Position** lokasi foto diambil, lalu dicocokkan ke Google/Bing Maps → menemukan **nama jalan** lokasi.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📌 9. GLOSSARY (WAJIB HAPAL)

- **Digital Forensics**: cabang forensik untuk investigasi cyber crime.
- **Cyber Crime**: kejahatan yang dilakukan pada/menggunakan perangkat digital.
- **NIST**: badan standar AS yang mendefinisikan 4 fase digital forensics.
- **Collection / Examination / Analysis / Reporting**: 4 fase proses digital forensics.
- **Chain of Custody**: dokumen pelacakan riwayat bukti (siapa, kapan, di mana).
- **Search Warrant**: surat izin sah untuk mengumpulkan bukti.
- **Write Blocker**: alat pencegah perubahan data saat akuisisi bukti.
- **Disk Image**: copy bit-by-bit storage, non-volatile.
- **Memory Image**: copy RAM, volatile, harus diambil pertama.
- **Volatile Data**: data yang hilang saat sistem mati/restart.
- **Non-Volatile Data**: data yang tetap ada meski sistem mati/restart.
- **EXIF**: standar metadata pada file gambar.
- **FTK Imager, Autopsy, DumpIt, Volatility**: tools utama Windows forensics.
- **pdfinfo**: command baca metadata PDF.
- **exiftool**: command baca/tulis metadata EXIF gambar.
- **Inadmissible**: bukti tidak sah/tidak bisa diterima di pengadilan (karena prosedur salah).
- **Integrity & Reliability**: keaslian & keandalan bukti yang harus dijaga sepanjang proses forensik.