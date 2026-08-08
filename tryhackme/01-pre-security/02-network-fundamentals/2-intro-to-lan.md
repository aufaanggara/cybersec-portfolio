```
=== Networking Fundamentals - Resume Materi ===
[25 Mar 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TOPOLOGI JARINGAN (LAN TOPOLOGY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Desain/tampilan fisik atau logis dari sebuah jaringan
Fungsi   : Menentukan bagaimana perangkat saling terhubung
           dan bagaimana data mengalir antar perangkat

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TIGA JENIS TOPOLOGI LAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STAR TOPOLOGY
  Cara kerja : Semua perangkat terhubung ke switch/hub pusat
               Data selalu melewati switch sebelum ke tujuan
  Keunggulan : Paling andal & scalable, mudah tambah perangkat
               Jika 1 kabel putus → hanya 1 perangkat terdampak
  Kelemahan  : Biaya tinggi (banyak kabel + switch)
               Switch = single point of failure
               Makin besar → makin susah maintenance
  Paling     : UMUM DIGUNAKAN saat ini

BUS TOPOLOGY
  Cara kerja : Semua perangkat terhubung ke 1 kabel backbone
               Data bergerak 2 arah (kiri & kanan) di backbone
               Ujung kabel dipasang terminator
  Keunggulan : Murah & mudah dipasang
  Kelemahan  : Mudah bottleneck jika banyak data sekaligus
               Troubleshooting sulit (semua data jalur sama)
               Backbone putus = seluruh jaringan mati
               Single point of failure di backbone

RING TOPOLOGY
  Cara kerja : Perangkat membentuk lingkaran, tiap perangkat
               terhubung ke 2 tetangga (kiri & kanan)
               Data bergerak 1 arah (seperti estafet)
               Perangkat forward data hanya jika tidak ada
               data miliknya sendiri yang perlu dikirim
  Keunggulan : Hemat kabel, minim bottleneck
               Troubleshooting mudah (data 1 arah)
  Kelemahan  : 1 kabel putus / 1 perangkat mati = jaringan mati
               Tidak efisien (data bisa lewat banyak hop)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERBANDINGAN TOPOLOGI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
              STAR      BUS       RING
Biaya       : Tinggi    Rendah    Sedang
Skalabel    : ✓✓✓       ✗         ✗✗
Troubleshoot: Sedang    Sulit     Mudah
Keandalan   : Tinggi    Rendah    Rendah
Cara rusak  : Switch    Overload  Putus 1
              dirusak   backbone  titik

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SWITCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Perangkat jaringan untuk menghubungkan banyak
           perangkat dalam satu jaringan (LAN)
Port     : Slot fisik tempat mencolok kabel ethernet
           Ukuran umum : 4, 8, 16, 24, 32, 64 port
Layer    : OSI Layer 2 (Data Link)
Cara     : Menyimpan MAC Address Table → tahu perangkat
kerja      mana di port mana → kirim data langsung ke
           tujuan (bukan broadcast ke semua)

Fungsi Switch vs Hub :
  Switch : Kirim data LANGSUNG ke tujuan (unicast)
           Punya MAC Address Table → lebih pintar
           Lebih aman & efisien
  Hub    : Kirim data ke SEMUA port (broadcast)
           Tidak punya memori → lebih bodoh
           Boros bandwidth & kurang aman

Switch + Router bisa saling dihubungkan untuk
meningkatkan REDUNDANSI (jika 1 jalur mati, pakai jalur lain)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ROUTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Perangkat yang menghubungkan ANTAR jaringan
           dan meneruskan data di antara jaringan tersebut
Layer    : OSI Layer 3 (Network Layer)
Cara     : Menggunakan ROUTING → membuat jalur antar
kerja      jaringan agar data bisa sampai ke tujuan
           Menggunakan IP address & Routing Table

Perbedaan Switch vs Router :
  Switch : Hubungkan perangkat DALAM 1 jaringan (LAN)
  Router : Hubungkan ANTAR jaringan berbeda (LAN ke Internet)

Alur data : Internet → Router → Switch → Perangkat

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LAN (LOCAL AREA NETWORK)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Jaringan yang menghubungkan perangkat dalam
           area terbatas (rumah, kantor, sekolah)
Fungsi   : Berbagi file antar perangkat
           Berbagi printer (1 printer banyak komputer)
           Main game multiplayer lokal
           Berbagi koneksi internet
           Keamanan data internal
Analogi  : "Jalan tol privat" untuk perangkat agar bisa
           saling berkomunikasi cepat & aman

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SUBNETTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Memecah jaringan besar menjadi jaringan-jaringan
           lebih kecil di dalam jaringan itu sendiri
Analogi  : Memotong kue → tiap departemen dapat potongannya

Mengapa perlu :
  → Jaringan besar (kantor, bisnis) butuh pemisahan
  → Contoh : Accounting, Finance, HR → subnet berbeda

3 Cara Subnet Menggunakan IP :

  Network Address  = identifikasi JARINGAN itu sendiri
    Contoh : 192.168.1.0
    Analogi: Nama jalan

  Host Address     = identifikasi PERANGKAT di subnet
    Contoh : 192.168.1.100
    Analogi: Nomor rumah
    Range  : .1 sampai .254 (254 host tersedia)

  Default Gateway  = perangkat yang bisa kirim data
    Contoh : 192.168.1.254        ke jaringan LAIN
    Analogi: Pintu keluar kompleks
    Biasanya: .1 atau .254

Subnet Mask : Angka 4 oktet (32 bit) yang menentukan
              berapa host yang bisa masuk jaringan
  Contoh umum : 255.255.255.0 = max 254 perangkat

Manfaat Subnetting :
  Efficiency   = data tidak banjiri seluruh jaringan
  Security     = subnet berbeda tidak bisa akses bebas
  Full Control = admin bisa atur akses dengan presisi

Contoh nyata : Kafe
  Subnet 1 → Kasir + karyawan (data sensitif)
  Subnet 2 → WiFi pengunjung (hotspot publik)
  Keduanya tetap bisa akses internet tapi TERPISAH

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ARP (ADDRESS RESOLUTION PROTOCOL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Protokol yang mengaitkan IP address (logis)
           dengan MAC address (fisik) di jaringan
Fungsi   : Agar perangkat bisa tahu MAC address tujuan
           sebelum mengirim data

Dua Identitas Perangkat :
  MAC Address = Identitas FISIK
    → Dibakar ke hardware saat dibuat di pabrik
    → Permanen & unik di seluruh dunia
    → Tidak berubah meskipun pindah jaringan
    → Contoh : 01:00:AB:78:99:33
    → Analogi: NIK di KTP

  IP Address  = Identitas LOGIS
    → Diberikan secara software/konfigurasi
    → Bisa berubah tergantung jaringan
    → Contoh : 192.168.1.10
    → Analogi: Alamat rumah (bisa pindah)

Cara Kerja ARP (2 pesan) :

  ARP Request → Perangkat broadcast ke SEMUA
    DST MAC : FF:FF:FF:FF:FF:FF (broadcast universal)
    MSG     : "Siapa yang punya IP 192.168.1.10?"
    Analogi : Teriak di kelas "Siapa namanya Budi?"

  ARP Reply   → Hanya perangkat yang punya IP itu jawab
    DST MAC : MAC address penanya (bukan broadcast)
    MSG     : "Saya! MAC saya 18:AC:33:12:88:29"
    Analogi : Si Budi angkat tangan "Saya Budi!"

ARP Cache : Tempat penyimpanan hasil ARP
    → Agar tidak perlu tanya ulang setiap saat
    → Bersifat SEMENTARA (akan expired)
    → Format : IP 192.168.1.10 = MAC 18:AC:33:12:88:29

FF:FF:FF:FF:FF:FF = MAC broadcast → semua perangkat
                    di jaringan WAJIB membaca pesan ini

Ancaman : ARP Spoofing/Poisoning
    → Penyerang kirim ARP reply PALSU
    → MAC penyerang dikaitkan dengan IP korban
    → Lalu lintas dialihkan ke penyerang
    → Teknik : Man-in-the-Middle (MitM)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DHCP (DYNAMIC HOST CONFIGURATION PROTOCOL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Protokol yang memberikan IP address secara
           OTOMATIS ke perangkat yang terhubung jaringan
Kepanjangan :
  Dynamic       = Dinamis/berubah-ubah
  Host          = Perangkat
  Configuration = Konfigurasi
  Protocol      = Aturan/protokol

2 Cara Assign IP :
  Manual  = diketik langsung ke perangkat (statis)
  Otomatis= pakai DHCP server (dinamis) ← paling umum

Proses DHCP → Hapal singkatan DORA :

  D → DISCOVER
      Dari    : Perangkat baru
      Ke      : Semua jaringan (broadcast)
      Isi     : "Ada DHCP server? Saya butuh IP!"
      IP src  : 0.0.0.0 (belum punya IP)
      IP dst  : 255.255.255.255 (broadcast)

  O → OFFER
      Dari    : DHCP Server
      Ke      : Perangkat
      Isi     : "Ada! Pakai IP 192.168.1.10"
      Sumber  : Diambil dari DHCP Pool (daftar IP tersedia)

  R → REQUEST
      Dari    : Perangkat
      Ke      : DHCP Server
      Isi     : "Oke, saya mau pakai IP 192.168.1.10"
      Catatan : Masih broadcast agar DHCP server lain tahu

  A → ACK (Acknowledgement)
      Dari    : DHCP Server
      Ke      : Perangkat
      Isi     : "Confirmed! Berlaku selama 24 jam"
      Hasil   : Perangkat resmi bisa pakai IP tersebut

Lease Time : Waktu sewa IP address dari DHCP server
    → IP tidak diberikan permanen, hanya dipinjamkan
    → Setelah habis → perangkat minta IP lagi (DORA ulang)
    → Inilah mengapa IP address bersifat "dinamis"

DHCP Pool  : Daftar IP address yang dikelola DHCP server
    → DHCP pilih IP yang belum dipakai dari pool ini

Contoh nyata : Konek HP ke WiFi rumah → HP langsung
    dapat IP otomatis → itu DHCP bekerja!
    Router rumah biasanya = DHCP server sekaligus

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Topology        = Desain/tampilan jaringan
Backbone        = Kabel utama di bus topology
Terminator      = Penutup ujung kabel backbone
Broadcast       = Kirim ke SEMUA perangkat sekaligus
Unicast         = Kirim ke SATU tujuan spesifik
MAC Address     = Identitas fisik perangkat (hardware)
IP Address      = Identitas logis perangkat (software)
Subnet Mask     = Angka penentu ukuran jaringan
Default Gateway = Pintu keluar menuju jaringan lain
ARP Cache       = Tabel penyimpanan pasangan IP-MAC
DHCP Pool       = Daftar IP tersedia di DHCP server
Lease Time      = Durasi peminjaman IP dari DHCP
Redundansi      = Jalur cadangan agar jaringan tidak mati
Single Point    = Satu titik yang jika rusak =
of Failure        seluruh jaringan mati
Routing         = Proses menentukan jalur data antar jaringan
NIC             = Network Interface Card (kartu jaringan)
Oktet           = Satu bagian IP address (4 bagian total)
Host            = Perangkat yang terhubung di jaringan
Subnet          = Bagian/potongan dari jaringan yang lebih besar
MitM            = Man-in-the-Middle (serangan penyadapan)
```