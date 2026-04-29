```
=== HTB Starting Point - Resume Materi ===
[29 Apr 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR UMUM CTF HTB STARTING POINT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Konek VPN    → sudo openvpn [file.ovpn]
2. Cek koneksi  → ping [target IP]
3. Scan port    → nmap [target IP]
4. Eksploitasi  → sesuai port/service yang terbuka
5. Ambil flag   → baca isi flag.txt → submit ke HTB

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NMAP - NETWORK SCANNER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Scan port & service yang berjalan di target
Perintah : nmap [IP]              → scan dasar
           nmap -sV [IP]          → + deteksi versi service
           nmap -sV -p 21 [IP]    → scan port spesifik saja

Switch :
  -sV   = service version detection (tau versi software)
  -p    = tentukan port yang mau discan
  -A    = aggressive scan (OS, versi, script, traceroute)
  -sC   = jalankan default scripts

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MEOW - TELNET (Port 23)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Protokol : Telnet → remote access langsung ke shell server
Celah    : Login tanpa password (misconfigured)
Eksploit :
  telnet [IP]          → konek ke target
  login: root          → coba login sebagai root
  (langsung enter)     → kadang tanpa password

Hasil    : Dapat SHELL PENUH di dalam server
           → bisa langsung cat flag.txt tanpa perlu keluar
Analogi  : Seperti masuk langsung ke dalam rumah,
           bisa pegang semua barang di sana

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FAWN - FTP (Port 21)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Protokol : FTP (File Transfer Protocol) → transfer file antar host
Celah    : Anonymous login (siapa saja bisa masuk tanpa akun)
Eksploit :
  ftp [IP]             → konek ke server FTP
  Name: anonymous      → username anonymous
  Password: (enter)    → kosongkan password

Perintah di dalam FTP :
  ls                   → lihat daftar file di server
  get [namafile]       → download file ke Kali
  exit                 → keluar dari FTP

Setelah exit, baca file di Kali :
  cat flag.txt

Switch :
  get   = download 1 file dari server ke lokal
  mget  = download banyak file sekaligus
  put   = upload file dari lokal ke server
  ls    = list file di server

Hasil    : TIDAK dapat shell, hanya bisa ambil file
Analogi  : Seperti loker titipan — bisa lihat & ambil barang,
           tapi tidak bisa buka/baca di tempat, harus dibawa pulang dulu

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERBANDINGAN TELNET vs FTP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
              TELNET (Meow)        FTP (Fawn)
Port        : 23                   21
Akses       : Shell penuh          Transfer file saja
Cat file    : Langsung di server   Harus get dulu → exit → cat
Analogi     : Masuk ke dalam rumah Ambil barang dari depan pintu
Celah umum  : Login tanpa password Anonymous login

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FILE TERSIMPAN DIMANA SETELAH GET?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
File hasil get tersimpan di folder aktif saat ftp dijalankan
Cek posisi    : pwd
Cari file     : find / -name flag.txt 2>/dev/null
Tips          : Sebelum ftp, cd ke Desktop dulu biar rapi
                → cd ~/Desktop → ftp [IP]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Anonymous Login  = login FTP tanpa akun (username: anonymous)
Misconfigured    = server yang salah setting → jadi celah keamanan
Shell            = akses command line langsung ke sistem target
Flag             = string unik sebagai bukti berhasil eksploitasi
OpenVPN          = tool untuk konek ke jaringan HTB secara aman
VPN              = Virtual Private Network, terowongan aman ke lab HTB
```