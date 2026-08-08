```
=== Virtualization - Resume Materi ===
[26 Mar 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU VIRTUALISASI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Teknologi yang memungkinkan SATU komputer fisik
           menjalankan BANYAK komputer virtual secara bersamaan
Masalah  : Dulu → "One Server = One Application" → SANGAT BOROS
Solusi   : Virtualisasi → banyak aplikasi berbagi 1 server fisik
Analogi  : Gedung apartemen — 1 gedung, banyak penghuni, berbagi
           listrik & air, tapi tiap unit punya privasi sendiri

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MASALAH ERA SEBELUM VIRTUALISASI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
High Cost        → Beli banyak server fisik = mahal (hardware +
                   listrik + cooling + maintenance + data center)
Low Utilization  → Server hanya dipakai 5–20% kapasitasnya
                   → CPU, RAM, storage TERBUANG SIA-SIA
Slow Deployment  → Setup server fisik baru = berhari-hari/minggu
Hard to Scale    → Butuh lebih banyak resource? Beli server lagi!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KOMPONEN UTAMA VIRTUALISASI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Physical Server  → Gedung (hardware nyata)
Hypervisor       → Manajer gedung (software pengatur VM)
Virtual Machine  → Apartemen (komputer virtual)
Container        → Ruangan dalam apartemen (isolasi per-app)
Tenant/OS/App    → Penghuni (sistem operasi / aplikasi)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HYPERVISOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Software inti virtualisasi → menciptakan & mengelola VM
Fungsi   : → Bagi komputer fisik jadi banyak VM
           → Beri tiap VM bagian CPU, RAM, storage sendiri
           → Jaga isolasi & keamanan antar VM
           → Kelola lifecycle VM (start/stop/pause/clone/delete)

TYPE 1 (Bare-Metal)
  Berjalan : Langsung di atas hardware fisik (tanpa OS host)
  Sifat    : Cepat, efisien, stabil
  Cocok    : Server profesional, data center, production
  Contoh   : VMware ESXi, Microsoft Hyper-V

TYPE 2 (Hosted)
  Berjalan : Di dalam OS yang sudah ada
  Sifat    : Mudah install, fleksibel
  Cocok    : Belajar, testing, home lab, setup kecil
  Contoh   : VirtualBox, VMware Workstation

TABEL USE CASE:
  Test Malicious Files  → Type 2
  Production Server     → Type 1
  Database Server       → Type 1
  Software Testing      → Type 2
  Kali Linux            → Type 2
  Data Center           → Type 1

⚠️  Saat uji malicious files → pastikan guest TERISOLASI dari host
    agar malware tidak menyebar ke mesin utama!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 VIRTUAL MACHINE (VM)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Komputer virtual yang dibuat oleh hypervisor
Sifat    : Berperilaku seperti mesin fisik sungguhan
Isi      : → CPU virtual, RAM, storage, network sendiri
           → Bisa jalankan OS apapun (Windows, Linux, dll)
           → Sepenuhnya TERISOLASI dari VM lain
           → Kalau 1 VM crash → VM lain tetap jalan
Tools    : Oracle VirtualBox, VMware Workstation (Type 2)

Contoh penggunaan :
  → Butuh Kali Linux tapi tidak mau beli laptop baru?
    Install hypervisor → jalankan Kali Linux VM
  → Mau uji file mencurigakan?
    Buat VM terisolasi → uji di sana → PC utama aman

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CONTAINER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Lingkungan RINGAN & terisolasi untuk 1 aplikasi
           + semua dependensinya (libraries, tools, versions)
Bedanya  : VM = bawa OS sendiri PENUH
           Container = PINJAM kernel OS host (lebih ringan)
Kernel   : Bagian OS yang komunikasi dengan hardware &
           kelola resource (memori, program berjalan)

Karakteristik Container :
  → Paket aplikasi + dependensi dalam 1 unit
  → Berbagi kernel OS host → start HAMPIR INSTAN
  → Terisolasi satu sama lain → 1 rusak ≠ merusak lainnya
  → Bisa jalan KONSISTEN di mesin mana pun
  → Ideal untuk : development, testing, scalable deployment

⚠️  BATASAN : Tidak bisa run Windows container di Linux host
              karena harus match tipe kernel OS host

Docker   : Platform open-source paling populer untuk deploy
           container → simplify build, deploy, run aplikasi

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERBANDINGAN VM vs CONTAINER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                VM              Container
OS sendiri    : Ya (penuh)      Tidak (pakai kernel host)
Isolasi       : Maksimal        Sedang
Boot speed    : Menit           Detik (hampir instan)
Resource      : Berat           Ringan
Cocok untuk   : Full isolation  Scalable, fast deployment
Analogi       : Apartemen penuh Ruangan dalam apartemen

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 STRUKTUR LAYER VIRTUALISASI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Physical Server
  └── Hypervisor
        ├── Virtual Machine A
        └── Virtual Machine B
              ├── Container A
              └── Container B

Ingat : Container berjalan DI DALAM VM,
        VM berjalan DI ATAS Hypervisor,
        Hypervisor berjalan DI ATAS Physical Server

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MANAGING VM (VIRTUALIZATION MANAGER)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3 Section utama di dashboard :
  Summary  → Tampilan umum kondisi lingkungan virtual
  VMs      → Detail tiap VM + aksi yang bisa dijalankan
  Hosts    → Usage & performa tiap server fisik

Status VM yang perlu dihapal :
  Running      → VM berjalan normal ✅
  Stopped      → VM tidak berjalan ⚪
  Error        → VM bermasalah, perlu direstart ❌

Aksi pada VM :
  ▶ Play Button   → Start VM
  ⬛ Stop Button  → Stop VM
  🔵 Blue Button  → Restart / Rerun VM
  🗑 Delete       → Hapus VM

Membuat VM baru → isi form :
  Name / Nama VM
  CPU Cores
  Memory (GB)
  Disk Size (GB)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MONITORING HOST (SERVER FISIK)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Yang dipantau : CPU Usage, Memory Usage, Storage Usage, Jumlah VM

Status warna bar :
  Hijau  → Normal, aman
  Merah  → KRITIS, hampir penuh → perlu dilaporkan!

Kondisi yang perlu diperhatikan :
  CPU/Memory/Storage mendekati 100% → BAHAYA, bisa crash
  Status Disconnected               → Server tidak berjalan
  Capacity masih rendah             → Aman tambah VM baru

Contoh analisis :
  HV-PROD-01 : CPU 45%, Mem 68%, Storage 72% → AMAN, bisa tambah VM
  HV-PROD-02 : CPU 98%, Mem 90%, Storage 95% → ⚠️ KRITIS, lapor!
  HV-BACKUP-01: CPU 0%, Disconnected         → Server mati

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MANFAAT VIRTUALISASI (HAPAL INI!)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cost Savings          → Hemat biaya hardware, listrik, ruang
Better Resource Usage → Sumber daya fisik dimanfaatkan maksimal
Safe Testing          → Uji malware/exploit tanpa risiko mesin asli
Faster Deployment     → VM/container bisa dibuat dalam menit
Flexibility           → Jalankan OS apapun di satu mesin
Portability           → VM/container bisa dipindah antar host
Scalability           → Mudah tambah/kurangi resource sesuai kebutuhan
Centralized Mgmt      → Kelola semua VM dari satu dashboard

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Virtualization   = 1 fisik → banyak virtual
Hypervisor       = software manajer VM
Virtual Machine  = komputer virtual lengkap dengan OS sendiri
Container        = isolasi ringan untuk 1 app, pakai kernel host
Container Image  = template/resep pre-packed untuk buat container
Kernel           = inti OS yang komunikasi langsung ke hardware
Docker           = platform open-source untuk deploy container
Host             = server fisik yang menjalankan hypervisor
Guest            = VM yang berjalan di atas hypervisor
Snapshot         = foto kondisi VM di titik waktu tertentu
Network Port     = titik masuk bernomor untuk komunikasi antar app
Bare-Metal       = langsung di hardware, tanpa OS perantara
Scalability      = kemampuan sistem tumbuh sesuai kebutuhan
Isolation        = tiap VM/container tidak bisa ganggu yang lain
```