## === Networking Fundamentals - Lab Notes ===
### [27 Feb 2026]

---

```
╔══════════════════════════════════════════════════════════╗
║           NETWORKING FUNDAMENTALS — SESI 1               ║
║                    27 Feb 2026                           ║
╚══════════════════════════════════════════════════════════╝
```

---

📌 **APA ITU JARINGAN (NETWORK)?**
```
Definisi : Kumpulan perangkat yang saling terhubung
Contoh   : Transportasi kota, jaringan listrik, sistem pos
Di komput: Bisa dari 2 device hingga miliaran device
Isi      : Laptop, HP, kamera CCTV, lampu lalu lintas, dll
Penting  : Dasar dari semua konsep cybersecurity
```

---

📌 **APA ITU INTERNET?**
```
Definisi  : Satu jaringan RAKSASA = banyak jaringan kecil digabung
Sejarah   :
  - 1960s → ARPANET (proyek militer AS, jaringan pertama)
  - 1989  → Tim Berners-Lee ciptakan WWW (World Wide Web)
  - WWW   = yang bikin internet jadi tempat simpan & bagi info

2 Tipe Jaringan:
  Private Network → jaringan lokal (rumah/kantor)
  Public Network  → Internet (menghubungkan semua jaringan)
```

---

📌 **IP ADDRESS**
```
Definisi : Label angka untuk identifikasi perangkat di jaringan
Format   : 4 oktet, masing-masing 0–255
Contoh   : 192 . 168 . 1 . 1
           [ok1] [ok2] [ok3] [ok4]

2 Jenis IP:
  Private → dalam jaringan lokal    contoh: 192.168.1.77
  Public  → identitas di Internet   contoh: 86.157.52.21

Catatan penting:
  - 2 device beda bisa punya IP private beda tapi PUBLIC SAMA
  - Public IP diberikan oleh ISP (Internet Service Provider)
  - IP tidak bisa aktif 2x dalam jaringan yang sama
```

---

📌 **IPv4 vs IPv6**
```
IPv4 → format lama  → 2^32  = ±4,29 MILIAR alamat  → HAMPIR HABIS
IPv6 → format baru  → 2^128 = 340 TRILIUN+ alamat  → solusi

Contoh IPv4 : 86.157.52.21
Contoh IPv6 : 2a00:22c4:a531:c500:425f:cce6:c36b:f64d

Kenapa pindah ke IPv6? → miliaran device baru terus terhubung
```

---

📌 **MAC ADDRESS**
```
Definisi  : Alamat fisik permanen di chip jaringan (motherboard)
Format    : 12 karakter heksadesimal, dipisah titik dua
Contoh    : a4 : c3 : f0 : 85 : ac : 2d
            [vendor/pabrik ]   [nomor unik device]

6 karakter PERTAMA → kode perusahaan pembuat (Intel, dll)
6 karakter TERAKHIR → nomor unik perangkat

Bedanya dengan IP:
  IP Address  = bisa berubah (seperti nama)
  MAC Address = permanen (seperti sidik jari)
```

---

📌 **MAC SPOOFING ⚠️**
```
Definisi : Memalsukan MAC Address untuk berpura jadi device lain
Bahaya   : Bisa bobol firewall yang hanya cek MAC Address
Contoh   : Firewall izinkan MAC admin → kita palsukan → lolos

Tempat pakai MAC control:
  → WiFi hotel, kafe, bandara (bayar per device)
  → Guest WiFi publik

Skenario spoofing:
  Alice (bayar WiFi) → MAC: AA:BB:CC:11:22:33 → diizinkan ✅
  Bob (belum bayar)  → MAC: XX:XX:XX:XX:XX:XX → diblokir ❌
  Bob spoof MAC Alice → router kira itu Alice  → lolos ✅
```

---

📌 **PING & ICMP**
```
Definisi : Tool dasar untuk cek koneksi antar perangkat
Protokol : ICMP (Internet Control Message Protocol)
Cara kerja:
  1. Kirim ICMP echo REQUEST ke target
  2. Terima ICMP echo REPLY dari target
  3. Hitung waktu tempuh (latency)

Syntax  : ping [IP / URL]
Contoh  : ping 192.168.1.254
          ping 8.8.8.8 (DNS Google)
          ping google.com

Baca output ping:
  time=2.18 ms        → latensi SATU paket (makin kecil makin bagus)
  0% packet loss      → tidak ada paket hilang = koneksi sehat
  time 5008ms         → TOTAL WAKTU SESI ping (bukan latensi!)
  rtt min/avg/max     → statistik waktu min, rata-rata, maksimal

Kegunaan:
  ✅ Cek device online/offline
  ✅ Ukur kecepatan koneksi (latensi)
  ✅ Deteksi packet loss
  ✅ Diagnosa awal masalah jaringan
```

---

📌 **KONSEP KUNCI YANG WAJIB DIHAPAL**
```
Network     = perangkat yang saling terhubung
Internet    = jaringan dari banyak jaringan (public network)
IP Address  = identitas device di jaringan (bisa berubah)
MAC Address = identitas fisik permanen di hardware
Private IP  = dalam jaringan lokal
Public IP   = di Internet, dikasih ISP
IPv4        = format IP lama, hampir habis (4,29 miliar)
IPv6        = format IP baru, 340 triliun+
Ping        = tool cek koneksi pakai ICMP
Latency     = waktu bolak-balik paket (ms)
Spoofing    = memalsukan identitas (MAC/IP)
ISP         = penyedia layanan Internet
WWW         = World Wide Web, diciptakan Tim Berners-Lee 1989
ARPANET     = cikal bakal Internet, tahun 1960an
```

---

📌 **ANALOGI BIAR MUDAH DIINGAT**
```
IP Address  → seperti ALAMAT RUMAH (bisa pindah/berubah)
MAC Address → seperti NOMOR KTP/NIK (permanen, dari lahir)
Internet    → seperti JARINGAN JALAN TOL antar kota
Private Net → seperti JALAN KAMPUNG dalam komplek
Ping        → seperti nanya "Halo ada?" dan tunggu jawaban
Spoofing    → seperti pakai KTP palsu buat masuk gedung
```