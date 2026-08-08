```
=== Operating Systems Introduction - Resume Materi ===
[11 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU OPERATING SYSTEM (OS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Software INTI yang mengkoordinasikan semua yang terjadi
           di komputer — menghubungkan user, aplikasi, dan hardware
Posisi   : User → Applications → Operating System → Hardware
Fungsi   : Bertindak sebagai "manajer tak terlihat" yang menjaga
           seluruh mesin berjalan sebagai satu sistem terpadu
Analogi  : OS = menara kontrol bandara yang mengatur semua
           pesawat (aplikasi) di landasan pacu (hardware)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KENAPA OS ITU PERLU?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tanpa OS : Setiap aplikasi harus kontrol langsung CPU, memori,
           file, perangkat → konflik besar & sistem kacau
Dengan OS: OS jadi pengorganisir pusat → semua teratur, aman,
           dan bisa berjalan bersamaan tanpa tabrakan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SYSTEM PRIVILEGE LAYERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kernel Space → Area inti OS yang terkunci & sangat istimewa
               Akses PENUH ke CPU, RAM, storage, semua hardware
               Hanya kernel yang boleh beroperasi di sini
               Tidak bisa disentuh langsung oleh aplikasi biasa

User Space   → Tempat semua aplikasi standar berjalan
               Akses hardware DIBATASI untuk keamanan
               Kalau butuh hardware → harus kirim SYSTEM CALL
               ke kernel, lalu kernel yang eksekusi

System Call  → "Permintaan resmi" dari aplikasi ke kernel
               Contoh : buka file, putar suara, konek Wi-Fi

Analogi      : Kernel = menara kontrol (hanya petugas resmi)
               User space = maskapai di darat (hanya bisa
               radio/request ke menara, tidak boleh masuk tower)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 5 TUGAS UTAMA OS (WAJIB HAPAL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Process Management
   → Buat, jadwalkan, prioritaskan, hentikan program
   → OS atur berapa CPU time tiap proses dapat
   → Contoh : buka browser + musik + medsos = tidak freeze

2. Memory Management
   → Alokasikan RAM ke tiap proses
   → Lindungi memori satu app dari app lain
   → Kalau RAM habis → pakai Virtual Memory
   → Contoh : banyak app buka = OS jaga agar tidak crash

3. File System Management
   → Organisir file ke direktori
   → Tangani naming, path, permissions, metadata
     (nama, ukuran, tipe, timestamp)
   → Contoh : buat folder, simpan foto, set "read only"

4. User Management
   → Kelola banyak akun, autentikasi, dan permissions
   → Tentukan siapa bisa akses apa
   → Contoh : login password, file kamu tidak bisa dibuka
              akun user lain

5. Device Management
   → Load driver, sediakan hardware abstraction layer
   → Buat app bisa bilang "print ini" atau "putar suara"
   → Contoh : colok mouse/printer baru → langsung jalan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 OS SECURITY (KEAMANAN BAWAAN OS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OS sudah enforce keamanan SEBELUM antivirus/firewall apapun

Authentication    → Verifikasi identitas via password & biometrik
Permissions       → Kontrol apa yang boleh dibaca/ditulis/dieksekusi
Isolation         → Tiap proses di kotak perlindungan sendiri
System Protection → Lindungi file sistem kritis dari perubahan
                    tidak sah

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CARA INTERAKSI DENGAN OS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GUI (Graphical User Interface)
→ Visual : ikon, jendela, menu
→ Mudah dipakai, tidak perlu hafal perintah
→ Analogi : aplikasi navigasi — tinggal ketuk tujuan,
            rute muncul otomatis

CLI (Command-line Interface)
→ Berbasis teks, ketik perintah langsung
→ Lebih presisi, cepat, powerful untuk tugas lanjutan
→ Butuh hafal perintah & sintaks
→ Analogi : GPS manual — masukkan koordinat tepat,
            langsung ke tujuan, tapi harus tahu angkanya

Perbandingan : GUI = beberapa klik untuk buka folder
               CLI = 1 perintah langsung tampil isinya

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 5 TIPE OS (WAJIB HAPAL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Desktop      → PC harian, gaming, konten kreasi
               Ciri : GUI kaya, banyak app sekaligus, user-focused

Server       → Web hosting, database, cloud, back-end
               Ciri : Headless (no GUI), uptime max, multi-user,
                      remote access

Mobile       → Smartphone & tablet
               Ciri : Touch UI, hemat daya, always connected,
                      app sandboxing

Embedded     → Peralatan, mobil, IoT, smart TV, router
               Ciri : Jejak sangat kecil, hardware terbatas

Virtual/Cloud→ VM, container, cloud instance
               Ciri : Ringan, skalabel, deployment cepat

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 OS DI DUNIA NYATA (REAL WORLD)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DESKTOP
  Windows → Paling luas dipakai di PC
            Versi : Windows 10 (end-of-life), Windows 11
  macOS   → Apple, GUI halus, integrasi perangkat Apple
            Versi : Sonoma (14), Sequoia (15), Tahoe (26)
  Linux   → Keluarga OS open-source (distribusi)
            Versi : Ubuntu, Debian, Fedora

SERVER
  Windows → Jaringan besar, data center, korporat
            Versi : Server 2016, 2019, 2022, 2025
  Linux   → Mayoritas web server, andal & open-source
            Versi : Ubuntu Server, Debian, CentOS, Red Hat
  Unix    → Enterprise besar, finance, telco, pemerintah
            Versi : IBM AIX, Oracle Solaris

MOBILE
  Android → OS mobile terluas, ponsel/tablet/smart device
            Versi : Android 14-16, Manufacturer versions
  iOS     → Apple mobile, iPhone/iPad
            Versi : iOS 17, 18, 26

EMBEDDED & IoT
  Embedded Linux → OS khusus fungsi tertentu
                   Versi : OpenWrt, Ubuntu Core, Yocto Project
  Real-Time OS   → Butuh respons terjamin (kontrol pesawat)
                   Versi : FreeRTOS, VxWorks, QNX

VIRTUAL & CLOUD
  Cloud/VM          → Host website, app, streaming
                      Versi : Ubuntu LTS, Amazon Linux, Rocky Linux
  Container-optimized→ Alternatif ringan VM, paket app + dependensi
                      Versi : Alpine Linux, Bottlerocket AWS,
                              Flatcar Linux

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KENAPA BANYAK JENIS OS?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Laptop    → Perlu ramah pengguna + multitasking
Server    → Perlu stabilitas, keamanan, jalan non-stop
Mobile    → Perlu hemat daya + integrasi hardware
Embedded  → Perlu ringan untuk fungsi sangat spesifik

Tidak ada satu OS yang sempurna untuk semua situasi
→ Maka lahirlah ekosistem OS yang beragam

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kernel          = Bagian OS yang langsung kelola hardware &
                  sumber daya sistem
Kernel Space    = Area khusus tempat kernel berjalan,
                  akses penuh ke hardware
User Space      = Area tempat app biasa berjalan,
                  akses hardware dibatasi
System Call     = Permintaan dari app ke kernel untuk
                  lakukan sesuatu ke hardware
Virtual Memory  = Memori cadangan di storage saat RAM habis,
                  agar sistem tetap stabil
Driver          = Software penghubung OS dengan perangkat keras
GUI             = Antarmuka visual (klik, ikon, menu)
CLI             = Antarmuka teks (ketik perintah)
Distribution    = Varian/turunan dari OS Linux
                  (Ubuntu, Debian, Fedora = distribusi Linux)
Headless        = Server OS tanpa GUI sama sekali
Sandboxing      = Isolasi app agar tidak bisa ganggu sistem lain
Metadata        = Info tentang file (nama, ukuran, tipe, waktu)
Uptime          = Berapa lama sistem berjalan tanpa mati/restart
```