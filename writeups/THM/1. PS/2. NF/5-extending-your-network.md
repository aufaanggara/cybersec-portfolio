```
=== Networking Fundamentals - Resume Materi ===
[25 Mar 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PORT FORWARDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Komponen penting untuk menghubungkan aplikasi/service ke Internet
Tanpa PF : Server hanya bisa diakses perangkat di jaringan lokal saja (intranet)
Dengan PF: Server bisa diakses dari luar jaringan lewat IP publik
Letak    : Dikonfigurasi di ROUTER jaringan

Contoh Alur:
  Server  192.168.1.10 : Port 80
     ↓
  Router  82.62.51.70  : Port 80  ← IP Publik
     ↓
  Internet
     ↓
  Pengguna luar berhasil akses

Perbedaan PF vs Firewall:
  Port Forwarding → MEMBUKA port tertentu agar bisa diakses
  Firewall        → MENENTUKAN apakah traffic boleh lewat port tsb
  (Firewall tetap bisa blokir meski port sudah dibuka oleh PF)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FIREWALL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Perangkat dalam jaringan yang menentukan traffic
           mana yang boleh masuk & keluar
Analogi  : Border security / keamanan perbatasan jaringan
Fungsi   : Admin bisa PERMIT atau DENY traffic berdasarkan:
  → Dari mana traffic berasal?       (source network)
  → Ke mana traffic menuju?          (destination network)
  → Port berapa yang digunakan?      (misal: port 80 saja)
  → Protokol apa yang dipakai?       (UDP, TCP, atau keduanya)

Cara kerja : Firewall melakukan PACKET INSPECTION untuk
             menentukan jawaban dari faktor-faktor di atas

Bentuk Firewall:
  Hardware  → Dedicated device, untuk jaringan besar/bisnis,
              mampu tangani data sangat banyak
  Software  → Aplikasi seperti Snort
  Router    → Residential router di rumah (built-in firewall)

KATEGORI FIREWALL:
┌─────────────┬─────────────────────────────────────────────────┐
│  Stateful   │ Periksa SELURUH koneksi, bukan per paket        │
│             │ Keputusan bersifat DINAMIS                      │
│             │ Konsumsi resource TINGGI                        │
│             │ Jika koneksi dari host buruk → blokir           │
│             │ SELURUH perangkat host tersebut                 │
│             │ Contoh: izinkan bagian pertama TCP handshake,   │
│             │ lalu blokir jika handshake gagal                │
├─────────────┼─────────────────────────────────────────────────┤
│  Stateless  │ Periksa PAKET INDIVIDUAL satu per satu          │
│             │ Pakai aturan STATIS (static rules)              │
│             │ Konsumsi resource RENDAH                        │
│             │ Paket buruk ≠ langsung blokir seluruh perangkat │
│             │ Lebih "bodoh" — hanya efektif jika traffic      │
│             │ persis cocok aturan, jika tidak = useless       │
│             │ Unggul : hadapi DDoS / traffic massal           │
└─────────────┴─────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 VPN (Virtual Private Network)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Teknologi yang memungkinkan perangkat di jaringan
           BERBEDA berkomunikasi secara AMAN melalui Internet
Cara     : Membuat jalur khusus (TUNNEL) antar perangkat
Hasil    : Perangkat dalam tunnel → membentuk jaringan privat sendiri

Contoh 3 Jaringan VPN:
  Network #1 → Office #1
  Network #2 → Office #2
  Network #3 → Jaringan privat VPN (gabungan device dari N#1 & N#2)
  → Device di Network #3 tetap bagian dari N#1 & N#2,
    tapi HANYA bisa berkomunikasi privat sesama anggota VPN

MANFAAT VPN:
  1. Koneksi Geografis Berbeda
     → Bisnis multi-kantor bisa akses server/infrastruktur
       dari kantor manapun

  2. Privasi
     → Enkripsi data → hanya bisa dipahami pengirim & penerima
     → Data tidak rentan sniffing (penyadapan)
     → Berguna di WiFi publik yang tidak ada enkripsi

  3. Anonimitas
     → Jurnalis & aktivis pakai VPN di negara sensor ketat
     → Tanpa VPN: traffic bisa dilihat ISP & perantara lain
     → ⚠️ Catatan: level anonimitas tergantung apakah VPN
       provider itu sendiri menghormati privasi atau tidak
       VPN yang log semua data = sama saja tidak pakai VPN

TEKNOLOGI VPN:
┌────────┬───────────────────────────────────────────────────┐
│  PPP   │ Autentikasi + enkripsi data                       │
│        │ Pakai private key & public certificate (mirip SSH)│
│        │ Key & cert harus COCOK untuk bisa connect         │
│        │ ⚠️ NON-ROUTABLE → tidak bisa keluar jaringan     │
│        │    sendiri, butuh PPTP                            │
├────────┼───────────────────────────────────────────────────┤
│  PPTP  │ Kepanjangan: Point-to-Point Tunneling Protocol    │
│        │ Fungsi: bawa data PPP keluar dari jaringan        │
│        │ ✅ Mudah setup, didukung banyak perangkat         │
│        │ ⚠️ Enkripsi LEMAH dibanding alternatif lain       │
├────────┼───────────────────────────────────────────────────┤
│ IPSec  │ Kepanjangan: Internet Protocol Security           │
│        │ Enkripsi pakai framework IP yang sudah ada        │
│        │ ❌ Sulit dikonfigurasi                            │
│        │ ✅ Enkripsi KUAT, didukung banyak perangkat       │
└────────┴───────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LAN NETWORKING DEVICES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[ ROUTER ]
Fungsi   : Menghubungkan JARINGAN BERBEDA & meneruskan data antar jaringan
Layer    : Layer 3 OSI (Network Layer)
Cara     : Menggunakan proses ROUTING → buat jalur optimal antar jaringan
Interface: Punya UI (website/konsol) untuk konfigurasi
           → port forwarding, firewalling, dll
Dedicated: Router ≠ Switch → fungsinya berbeda, tidak tumpang tindih

Faktor Pemilihan Jalur Routing:
  → Jalur paling PENDEK?
  → Jalur paling ANDAL (reliable)?
  → Medium paling CEPAT? (copper vs fibre)

[ SWITCH ]
Fungsi   : Menghubungkan BANYAK PERANGKAT dalam satu jaringan lokal
Kapasitas: 3 hingga 63 perangkat via kabel Ethernet
Layer    : Bisa Layer 2 ATAU Layer 3 (tidak bisa keduanya sekaligus)
           Layer 2 Switch → TIDAK BISA operasi di Layer 3

  ┌──────────────┬──────────────────────────────────────────┐
  │ Layer 2      │ Kirim FRAMES ke perangkat                │
  │ Switch       │ Basis pengiriman : MAC ADDRESS           │
  │              │ Paket IP dikapsulasi dalam frames        │
  │              │ Fungsi : semata-mata kirim frame         │
  │              │ ke perangkat yang tepat, tidak lebih     │
  ├──────────────┼──────────────────────────────────────────┤
  │ Layer 3      │ Kirim FRAMES (seperti L2) +              │
  │ Switch       │ ROUTING PAKET via protokol IP            │
  │              │ Lebih canggih → bisa lakukan             │
  │              │ sebagian fungsi router                   │
  │              │ Punya BEBERAPA IP address                │
  │              │ Contoh: 192.168.1.1 & 192.168.2.1        │
  └──────────────┴──────────────────────────────────────────┘

[ VLAN ]
Kepanjangan : Virtual Local Area Network
Definisi    : Teknologi untuk memisahkan perangkat dalam satu
              jaringan secara VIRTUAL (meski pakai switch fisik sama)
Tujuan      : Keamanan — aturan menentukan siapa bisa
              berkomunikasi dengan siapa
Letak config: Di Switch (Layer 2 atau Layer 3)

Contoh VLAN:
  Switch yang sama → dibagi 2 VLAN:
  VLAN 1 (192.168.1.1) → Sales Department
  VLAN 2 (192.168.2.1) → Accounting Department
  → Keduanya bisa akses Internet
  → Keduanya TIDAK BISA saling berkomunikasi
    meski terhubung ke switch yang sama

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERBANDINGAN ROUTER vs SWITCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Router       → Hubungkan ANTAR jaringan berbeda → Layer 3
  Switch L2    → Hubungkan perangkat DALAM satu jaringan → Layer 2
  Switch L3    → Hubungkan perangkat + bisa routing → Layer 2 & 3
  VLAN         → Pisahkan perangkat virtual dalam switch → Layer 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Routing          = Proses data berjalan & mencari jalur antar jaringan
Tunnel           = Jalur privat terenkripsi yang dibuat VPN
Packet Inspection= Cara firewall memeriksa isi & asal-tujuan paket
Sniffing         = Penyadapan data yang lewat di jaringan
Intranet         = Jaringan internal, hanya bisa diakses lokal
Frame            = Unit data di Layer 2, berisi paket IP di dalamnya
MAC Address      = Identitas unik perangkat (dipakai switch L2)
IP Address       = Alamat logis perangkat (dipakai router & switch L3)
Non-routable     = Tidak bisa keluar/masuk jaringan secara mandiri
DDoS             = Distributed Denial-of-Service → banjiri traffic
ISP              = Internet Service Provider (provider internet)
Segregasi        = Pemisahan jaringan/perangkat berdasarkan aturan
```