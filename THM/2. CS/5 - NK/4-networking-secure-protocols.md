```
=== Networking Secure Protocols - Resume Materi ===
[03 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MASALAH PROTOKOL TANPA KEAMANAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Masalah  : HTTP, SMTP, POP3, IMAP, TELNET → kirim data dalam CLEARTEXT
Akibat   : Siapapun yang capture paket bisa baca password, email, kredensial
Mode     : Penyerang pakai "promiscuous mode" di network card → tangkap semua paket
3 Hal    : Protokol lama TIDAK melindungi →
           Confidentiality = isi data bisa dibaca siapapun
           Integrity       = isi data bisa diubah di tengah jalan
           Authenticity    = tidak bisa verifikasi server asli atau palsu

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TIGA PENDEKATAN KEAMANAN JARINGAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. TLS   → Tambahkan enkripsi ke protokol yang sudah ada
2. SSH   → Ganti TELNET dengan protokol remote access yang aman
3. VPN   → Buat jaringan privat virtual di atas internet publik

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SSL & TLS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SSL      : Secure Sockets Layer → dibuat Netscape, SSL 2.0 rilis 1995
TLS      : Transport Layer Security → dibuat IETF, rilis 1999
           TLS 1.3 rilis 2018 → versi terbaru & paling aman
Posisi   : Beroperasi di TRANSPORT LAYER model OSI
Fungsi   : Lindungi Confidentiality + Integrity komunikasi
Fakta    : SSL sudah pensiun, tapi orang masih sebut "SSL Certificate"
           padahal aslinya pakai TLS

Sertifikat TLS :
  CSR  = Certificate Signing Request → dibuat admin server
  CA   = Certificate Authority → verifikasi CSR & terbitkan sertifikat digital
  Self-signed = sertifikat ditandatangani sendiri → TIDAK bisa buktikan keaslian
  Let's Encrypt = CA gratis untuk dapat sertifikat TLS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CIPHER & CIPHER SUITE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cipher       : Algoritma matematika untuk enkripsi & dekripsi data
Cipher Suite : Kombinasi beberapa algoritma sekaligus
Contoh       : TLS_AES_256_GCM_SHA384
               → TLS          = protokol
               → AES_256_GCM  = cipher enkripsi data
               → SHA384        = algoritma hashing integritas

Negosiasi Cipher :
  Client Hello → kirim daftar cipher suite yang didukung
  Server Hello → pilih satu cipher suite dari daftar klien
  → Setelah sepakat, semua komunikasi pakai cipher itu

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTTPS (HTTP OVER TLS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HTTP  : port 80  → cleartext, siapapun bisa baca
HTTPS : port 443 → terenkripsi TLS

Urutan koneksi HTTPS :
  1. TCP Three-Way Handshake (SYN, SYN-ACK, ACK)
  2. TLS Negotiation (Client Hello, Server Hello, Change Cipher Spec, Finished)
  3. Sesi TLS terbentuk
  4. Komunikasi HTTP terenkripsi
  5. Pemutusan koneksi

Paket HTTPS di Wireshark → terlihat "Application Data" = gibberish
Untuk dekripsi → butuh private key atau ssl-key.log

Cara dekripsi di Wireshark :
  1. Klik kanan paket TLSv1.3
  2. Protocol Preferences
  3. Transport Layer Security
  4. Open TLS preferences → Browse ke ssl-key.log
  5. OK → traffic terdekripsi

Cara buat ssl-key.log :
  chromium --ssl-key-log-file=~/ssl-key.log
  SSLKEYLOGFILE=~/ssl-key.log firefox

Kesimpulan : TLS tidak ubah TCP/IP di bawah maupun HTTP di atas
             → hanya membungkus HTTP dengan enkripsi

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TABEL PORT CLEARTEXT vs SECURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Protokol   Port Cleartext    Protokol Secure   Port Secure
HTTP       80                HTTPS             443
SMTP       25                SMTPS             465 / 587
POP3       110               POP3S             995
IMAP       143               IMAPS             993
FTP        21                FTPS              990
TELNET     23                SSH               22

Catatan SMTPS :
  Port 465 = lama, masih banyak dipakai
  Port 587 = resmi, pakai STARTTLS (mulai plaintext → upgrade ke TLS)

STARTTLS vs langsung TLS :
  Port 443/993/995/990 → langsung TLS dari awal
  Port 587 → mulai plaintext dulu, upgrade ke TLS di tengah

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SSH (SECURE SHELL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dibuat   : Tatu Ylönen, SSH-1 rilis 1995 (sama tahun dengan SSL 2.0)
SSH-2    : 1996
OpenSSH  : 1999, open-source, yang paling banyak dipakai sekarang
Port     : 22 (TELNET port 23)

Keunggulan OpenSSH :
  Secure Authentication → support password, public key, 2FA
  Confidentiality       → enkripsi end-to-end, proteksi MITM
  Integrity             → kriptografi lindungi integritas traffic
  Tunneling             → buat "terowongan" aman → mirip VPN
  X11 Forwarding        → jalankan aplikasi GUI remote lewat SSH

Perintah SSH :
  ssh username@hostname        → login dengan username berbeda
  ssh hostname                 → login dengan username yang sama
  ssh 192.168.1.1 -X           → login + aktifkan X11 Forwarding (GUI)
    -X = enable X11 Forwarding untuk tampilkan GUI dari remote

Tool untuk konek ke protokol TLS secara manual :
  Telnet   → HANYA bisa ke cleartext (port 80, 25, 110, 143)
  OpenSSL  → bisa ke protokol + TLS

  openssl s_client -connect ip:port
  openssl s_client -connect ip:443          → HTTPS
  openssl s_client -connect ip:993          → IMAPS
  openssl s_client -connect ip:995          → POP3S
  openssl s_client -connect ip:465          → SMTPS
  openssl s_client -connect ip:587 -starttls smtp  → SMTPS STARTTLS
  openssl s_client -connect ip:143 -starttls imap  → IMAP STARTTLS
  openssl s_client -connect ip:110 -starttls pop3  → POP3 STARTTLS
    -starttls = mulai plaintext dulu lalu upgrade ke TLS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SFTP vs FTPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SFTP  : SSH File Transfer Protocol
        → Bagian dari SSH protocol suite
        → Pakai port 22 (sama dengan SSH)
        → Setup mudah = aktifkan opsi di OpenSSH server
        Perintah :
          sftp username@hostname  → konek ke SFTP server
          get filename            → download file dari server
          put filename            → upload file ke server

FTPS  : File Transfer Protocol Secure
        → FTP + TLS (seperti HTTPS = HTTP + TLS)
        → Pakai port 990
        → Butuh sertifikat TLS
        → Bisa sulit melewati firewall ketat karena pakai koneksi
          terpisah untuk kontrol dan transfer data

Perbedaan utama :
  SFTP  → anak SSH, numpang port 22, tidak butuh sertifikat TLS
  FTPS  → anak FTP, pakai TLS, port 990, butuh sertifikat TLS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 VPN (VIRTUAL PRIVATE NETWORK)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
V = Virtual  → tidak perlu kabel fisik antar lokasi
P = Private  → traffic terlindungi dari pengungkapan & pengubahan
N = Network  → membentuk jaringan sendiri di atas internet publik

Syarat minimal : koneksi internet + VPN server + VPN client

Cara kerja :
  VPN client → enkripsi traffic → kirim lewat VPN tunnel → VPN server
  Server tujuan hanya lihat IP VPN server, bukan IP asli kita

Dua skenario VPN :
  Site-to-Site  = hubungkan seluruh jaringan kantor cabang ke pusat
  Remote Access = satu perangkat individual konek ke VPN server

Kegunaan :
  1. Hubungkan kantor cabang ke kantor pusat
  2. Bypass pembatasan geografis (IP terlihat dari lokasi VPN server)
  3. Sembunyikan traffic dari ISP → ISP hanya lihat traffic terenkripsi

Peringatan :
  Tidak semua VPN rutekan semua traffic → cek DNS leak test
  Beberapa VPN bocorkan IP asli
  Beberapa negara → VPN ILEGAL → cek hukum lokal sebelum pakai

Tool VPN open source : OpenVPN
  sudo openvpn file.ovpn  → konek ke VPN server pakai file config

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 URL ENCODING — WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
%20 = spasi
%40 = @
%7B = {
%7D = }
%3A = :
%2F = /
Tool decode : urldecoder.org

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cleartext        = data dikirim tanpa enkripsi, bisa dibaca siapapun
Promiscuous Mode = mode network card untuk tangkap semua paket di jaringan
TLS Handshake    = proses negosiasi TLS antara klien dan server
VPN Tunnel       = jalur terenkripsi yang dibuat VPN di atas internet
STARTTLS         = metode upgrade koneksi dari plaintext ke TLS di tengah jalan
X11 Forwarding   = fitur SSH untuk tampilkan GUI aplikasi remote ke lokal
CSR              = Certificate Signing Request
CA               = Certificate Authority (penerbit sertifikat digital)
Self-signed Cert = sertifikat ditandatangani sendiri, tidak ada pihak ketiga
DNS Leak         = kebocoran DNS yang ungkap IP asli meski pakai VPN
Cipher Suite     = paket algoritma enkripsi + hashing yang dipakai TLS
ssl-key.log      = file berisi session key TLS untuk dekripsi traffic di Wireshark
```