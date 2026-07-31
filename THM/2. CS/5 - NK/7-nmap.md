```
=== Nmap - Resume Materi ===
[13 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU NMAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Network scanner open-source, pertama rilis tahun 1997
Fungsi   : 1. Temukan host yang aktif di jaringan
           2. Temukan layanan/service yang berjalan di host tersebut
Kenapa   : Manual (ping/arp-scan/telnet) terlalu lambat & terbatas
Syarat   : Jalankan dengan sudo/root untuk fitur penuh
           → Tanpa sudo : fitur terbatas, default ke connect scan (-sT)
           → Dengan sudo : akses penuh, default ke SYN scan (-sS)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CARA TENTUKAN TARGET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IP Range    : 192.168.0.1-10     → scan IP .1 sampai .10
IP Subnet   : 192.168.0.1/24    → scan seluruh subnet (setara .0-255)
Hostname    : example.thm       → scan lewat nama host
List Scan   : -sL               → cuma daftarkan target, TIDAK scan
              Contoh : nmap -sL 192.168.0.1/24 → tampilkan 256 target

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HOST DISCOVERY (SIAPA YANG ONLINE?)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Switch   : -sn (ping scan)
Fungsi   : Temukan host aktif TANPA scan port/service
Cara     : Nmap kirim berbagai probe → tunggu respons

Jaringan LOKAL (Ethernet/WiFi langsung terhubung)
→ Nmap kirim ARP request
→ Jika dibalas → "Host is up"
→ Bonus : bisa lihat MAC address → tahu vendor kartu jaringan

Jaringan REMOTE (ada router di antara kita & target)
→ TIDAK bisa pakai ARP (ARP tidak melewati router)
→ Nmap kirim kombinasi :
   • 2x ICMP echo (ping)
   • 2x ICMP timestamp
   • 2x TCP SYN ke port 443
   • 2x TCP ACK ke port 80
→ Jika tidak ada yang dibalas = host dianggap DOWN
→ Catatan : tanpa MAC address karena beda jaringan

Fakta penting : TCP memiliki 65.535 port, UDP juga 65.535 port

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PORT SCANNING (SIAPA YANG LISTENING?)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Network Service = proses yang mendengarkan koneksi di port TCP/UDP
Contoh layanan  : Web server (port 80/443), DNS (port 53), SSH (port 22)

── TCP CONNECT SCAN ──────────────────
Switch  : -sT
Cara    : Selesaikan THREE-WAY HANDSHAKE penuh (SYN → SYN-ACK → ACK)
          Jika berhasil → Nmap langsung putus koneksi (RST-ACK)
Port terbuka  : SYN → SYN-ACK → ACK → RST-ACK (4 paket)
Port tertutup : SYN → RST-ACK (2 paket, langsung ditolak)
Kelebihan     : Bisa dipakai user biasa (tanpa sudo)
Kekurangan    : Meninggalkan log di target (koneksi tercatat)

── TCP SYN SCAN (STEALTH) ────────────
Switch  : -sS
Cara    : Hanya langkah PERTAMA handshake → kirim SYN saja
          Jika target balas SYN-ACK → port TERBUKA
          Nmap balas RST (putus paksa, TIDAK selesaikan handshake)
Port terbuka  : SYN → SYN-ACK → RST (3 paket, tidak selesai)
Port tertutup : SYN → RST-ACK (sama seperti connect scan)
Kelebihan     : Lebih sedikit log (koneksi tidak pernah terbentuk)
Kekurangan    : Butuh sudo/root (perlu buat raw packet)
Default       : Otomatis dipilih jika jalankan Nmap dengan sudo

── UDP SCAN ──────────────────────────
Switch  : -sU
Kapan   : DNS, DHCP, NTP, SNMP, VoIP pakai UDP
Cara    : Kirim paket UDP ke setiap port
          Port tertutup → target balas ICMP "Port unreachable"
          Port terbuka  → tidak ada respons (UDP tidak perlu konfirmasi)
Catatan : UDP lebih sederhana dari TCP, cocok untuk real-time

── BATASI PORT TARGET ────────────────
Default Nmap : scan 1.000 port paling umum
-F           : Fast mode → scan 100 port paling umum
-p[range]    : Tentukan rentang sendiri
               Contoh : -p10-1024 (scan port 10 sampai 1024)
                        -p-25     (scan port 1 sampai 25)
                        -p-       (scan SEMUA port = -p1-65535)
-p1-1023     : Scan well-known ports saja

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 VERSION & OS DETECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-O    : OS Detection
        → Nmap tebak OS target dari berbagai indikator
        → Tidak 100% akurat tapi sangat mendekati
        → Output : "Running: Linux 4.X|5.X"

-sV   : Service & Version Detection
        → Tambah kolom VERSION di output
        → Tahu versi spesifik layanan yang berjalan
        → Contoh : OpenSSH 8.9p1 Ubuntu 3ubuntu0.10
        → Berguna : cari tahu apakah versi punya vulnerability

-A    : All-in-one (OS detection + version detection + traceroute + lainnya)
        → Gabungan -O dan -sV plus fitur tambahan lain

-Pn   : Force Scan (paksa scan meski host tampak down)
        → Nmap tidak skip host yang tidak balas ICMP
        → Berguna jika firewall blokir ping tapi host sebenarnya aktif

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TIMING (SEBERAPA CEPAT SCAN?)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kenapa penting : Scan terlalu cepat → trigger IDS/IPS → ketahuan

Template Timing (-T0 sampai -T5) :
┌─────────────────┬──────────────────┬───────────────┐
│ Template        │ Nama             │ Kecepatan     │
├─────────────────┼──────────────────┼───────────────┤
│ -T0             │ paranoid         │ 9.8 jam       │
│ -T1             │ sneaky           │ 27.53 menit   │
│ -T2             │ polite           │ 40.56 detik   │
│ -T3             │ normal (default) │ 0.15 detik    │
│ -T4             │ aggressive       │ 0.13 detik    │
│ -T5             │ insane           │ secepat mungkin│
└─────────────────┴──────────────────┴───────────────┘
Cara pakai : -T0 atau -T paranoid (nama/angka sama saja)

Parallelism (berapa probe aktif bersamaan) :
--min-parallelism <n>  : minimal n probe aktif sekaligus
--max-parallelism <n>  : maksimal n probe aktif sekaligus
→ Default : Nmap atur otomatis
→ Jaringan buruk  : Nmap turunkan ke 1
→ Jaringan bagus  : Nmap bisa ratusan probe sekaligus

Rate (kecepatan kirim paket) :
--min-rate <n>  : minimal n paket per detik
--max-rate <n>  : maksimal n paket per detik
→ Berlaku untuk SELURUH scan, bukan per host

--host-timeout  : batas waktu tunggu per host
→ Berguna untuk host atau koneksi yang lambat

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 OUTPUT & VERBOSITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Verbosity (info real-time saat scan berjalan) :
-v    : verbose level 1 → info tahap-tahap scan
-vv   : verbose level 2 → lebih detail
-v4   : verbose level 4 → sangat detail
→ Bisa tekan "v" saat scan sedang berjalan untuk naikkan level

Debugging (jika verbosity tidak cukup) :
-d    : debugging level 1
-d9   : debugging level maksimal → ribuan baris info
→ Pakai hanya saat troubleshoot masalah spesifik

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SAVE HASIL SCAN (FORMAT OUTPUT)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-oN <filename>  : Normal output → enak dibaca manusia (.nmap)
-oX <filename>  : XML output → bisa dibaca program/tool lain (.xml)
-oG <filename>  : Grepable output → mudah dicari pakai grep/awk (.gnmap)
-oA <basename>  : Simpan SEMUA format sekaligus
                  → Otomatis buat 3 file : .nmap + .xml + .gnmap
                  Contoh : nmap -sS 192.168.1.1 -oA hasil
                  → hasil.nmap, hasil.xml, hasil.gnmap

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TABEL CHEAT SHEET SEMUA SWITCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
UMUM
  -sL          → List targets (tidak scan)

HOST DISCOVERY
  -sn          → Ping scan, host discovery only

PORT SCANNING
  -sT          → TCP connect scan (full handshake) — default tanpa sudo
  -sS          → TCP SYN/stealth scan — default dengan sudo
  -sU          → UDP scan
  -F           → Fast mode (100 port)
  -p[range]    → Tentukan range port, -p- = semua port
  -Pn          → Paksa scan host yang tampak down

SERVICE DETECTION
  -O           → OS detection
  -sV          → Service version detection
  -A           → OS + version + traceroute + lainnya

TIMING
  -T<0-5>                          → Template timing
  --min/max-parallelism <n>        → Jumlah probe paralel
  --min/max-rate <n>               → Kecepatan paket/detik
  --host-timeout                   → Batas waktu per host

OUTPUT REAL-TIME
  -v / -vv / -v4    → Verbosity level
  -d / -d9          → Debugging level

SIMPAN HASIL
  -oN <file>   → Normal
  -oX <file>   → XML
  -oG <file>   → Grepable
  -oA <nama>   → Semua format sekaligus

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Host Discovery  = proses cari tahu host mana yang aktif di jaringan
Port Scanning   = proses cari tahu port mana yang terbuka di host
Service         = layanan/program yang listen di port tertentu
Three-Way Handshake = proses koneksi TCP : SYN → SYN-ACK → ACK
Raw Packet      = paket jaringan yang dibuat manual (butuh root)
ARP             = protokol untuk cari tahu MAC address di LAN
ICMP            = protokol untuk pesan error & diagnostik (ping)
IDS/IPS         = sistem deteksi/pencegahan intrusi
Well-known ports= port 1-1023, dipakai layanan umum/standar
Latency         = waktu tunda respons dari host target
Grepable output = format teks yang mudah difilter dengan grep
```