```
=== Computer Fundamentals - Resume Materi ===
[26 Mar 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MENGAPA PERLU PAHAM KOMPUTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Prinsip  : Tidak bisa mengamankan sesuatu yang tidak kamu pahami
Analogi  : Seperti menjaga kastil yang belum pernah kamu lihat
Tujuan   : Pahami dulu "kastilnya" → baru bisa pertahankan
Relevansi: Komponen komputer & proses boot = target serangan hacker

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KOMPONEN INTI KOMPUTER + ANALOGINYA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Motherboard  → Tulang & Sistem Saraf
               Fungsi : menghubungkan & menopang SEMUA komponen
               Isi    : CPU socket, RAM slots, expansion slots, port
               Fakta  : semua komponen lain terhubung MELALUI motherboard

CPU          → Otak
               Fungsi : memproses semua instruksi & kalkulasi
               Fitur  : multiple cores → proses instruksi secara paralel
               Koneksi: terhubung ke motherboard via CPU socket

RAM          → Memori Jangka Pendek
               Fungsi : simpan data sementara yang dibutuhkan CPU
               Sifat  : VOLATILE → data hilang saat daya mati
               Teknologi terbaru : DDR5 / DDR6

HDD / SSD    → Memori Jangka Panjang
               Fungsi : simpan data secara PERMANEN
               HDD    : teknologi lama, ada bagian bergerak, lambat, murah
               SSD    : tanpa bagian bergerak, pakai chip memori, LEBIH CEPAT
               Koneksi: via kabel SATA atau slot PCI Express

GPU          → Korteks Visual
               Fungsi : terima info dari OS/program → output visual ke monitor
               Koneksi: via slot PCI Express di motherboard

PSU          → Jantung & Paru-paru
               Fungsi : suplai daya ke SEMUA komponen
               Penting: jika komponen butuh daya > kapasitas PSU → sistem GAGAL
               Konektor: main motherboard connector, Molex connectors

Network Adapter → Pita Suara
               Fungsi : memungkinkan komputer komunikasi dengan sistem lain
               Varian : wireless (nirkabel) & wired (berkabel)
               Lokasi : bisa sudah tertanam di motherboard / expansion card
               Koneksi: via port PCI Express

Input/Output → Indra
               Input  : keyboard, mouse, mikrofon, scanner
               Output : monitor, printer, speaker
               Konektor umum : USB, HDMI, DisplayPort

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TABEL RINGKAS KOMPONEN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Komponen      | Analogi          | Fungsi Utama
--------------|------------------|---------------------------
Motherboard   | Tulang & Saraf   | Hubungkan semua komponen
CPU           | Otak             | Proses instruksi
RAM           | Memori Pendek    | Simpan data sementara
HDD/SSD       | Memori Panjang   | Simpan data permanen
GPU           | Korteks Visual   | Proses & tampilkan grafis
PSU           | Jantung          | Suplai daya
Network Adapter| Pita Suara      | Komunikasi jaringan
I/O Devices   | Indra            | Input & output data

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PROSES BOOTING (WAJIB HAPAL URUTAN)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Analogi : seperti manusia bangun tidur → cek kondisi → mulai beraktivitas

URUTAN :
  1. Press Power Button
     → Sinyal dikirim ke PSU → daya mengalir → sistem mulai menyala

  2. Firmware Starts (UEFI / BIOS)
     → SOFTWARE PERTAMA yang berjalan
     → Inisialisasi & koordinasi semua komponen
     → UEFI = versi modern | BIOS = versi lama (sudah digantikan UEFI)
     → Catatan : istilah BIOS masih sering disebut meski maksudnya UEFI

  3. POST (Power-On Self Test)
     → UEFI jalankan POST → cek semua hardware :
        ✔ Hadir/terpasang
        ✔ Dikonfigurasi benar
        ✔ Berfungsi normal
     → Jika ERROR → muncul bunyi BEEP atau alert

  4. Select Boot Device
     → UEFI ikuti DAFTAR PRIORITAS untuk cari perangkat boot
     → Biasanya SSD/HDD yang sudah terinstal OS

  5. Initiate Bootloader
     → Bootloader muat OS dari storage ke RAM
     → UEFI serahkan kendali ke OS
     → Boot sequence SELESAI → komputer siap dipakai

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 UEFI vs BIOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BIOS  → teknologi lama, fungsi sama seperti UEFI
UEFI  → pengganti BIOS, lebih modern
Fakta → istilah BIOS masih sering muncul, tapi UEFI yang sekarang dipakai
Tugas → inisialisasi komponen + jalankan POST + pilih boot device

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 VOLATILE vs NON-VOLATILE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Volatile     = data HILANG saat daya mati → contoh : RAM
Non-Volatile = data TETAP ada saat daya mati → contoh : HDD, SSD
Penting      : dalam forensik & cyber security, RAM bisa menyimpan
               data sensitif selama komputer hidup (passwords, keys, dll)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Booting       = proses menyalakan komputer hingga OS siap dipakai
Firmware      = software tingkat rendah yang berjalan pertama kali di hardware
UEFI          = Unified Extensible Firmware Interface (firmware modern)
BIOS          = Basic Input/Output System (firmware lama, digantikan UEFI)
POST          = Power-On Self Test (tes hardware saat komputer dinyalakan)
Bootloader    = program kecil yang muat OS ke RAM
Volatile      = data hilang saat daya mati (RAM)
Non-Volatile  = data tetap ada saat daya mati (HDD/SSD)
CPU Socket    = slot di motherboard tempat CPU dipasang
PCI Express   = jalur koneksi kecepatan tinggi di motherboard (GPU, NIC, SSD)
SATA          = konektor untuk HDD/SSD ke motherboard
DDR5/DDR6     = generasi terbaru teknologi RAM
Cores         = inti pemrosesan dalam CPU (lebih banyak = lebih paralel)
Expansion Card= komponen tambahan yang dipasang ke slot motherboard

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HUBUNGAN DENGAN CYBER SECURITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RAM          → bisa dieksploitasi → simpan data sensitif saat runtime
Boot Process → target hacker → bisa disisipi malware di level firmware
               (contoh : bootkits, rootkits yang berjalan sebelum OS)
UEFI/BIOS    → jika dikompromikan → sangat berbahaya, sulit dideteksi
Network Card → titik masuk serangan jaringan
Storage      → target pencurian data / ransomware
```