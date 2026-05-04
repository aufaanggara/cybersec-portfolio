```
=== HTB Starting Point — Crocodile ===
[04 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR ATTACK CROCODILE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Nmap Scan       → temukan port & service yang terbuka
2. FTP Anonymous   → masuk tanpa password, download credentials
3. Nmap Full Scan  → temukan web server (port 80) + versi Apache
4. Gobuster        → temukan halaman tersembunyi (login.php)
5. Web Login       → pakai credentials dari FTP → dapat FLAG

Vulnerability utama : Anonymous FTP + credential exposure + no login protection

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NMAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi : Network scanner — temukan host, port terbuka, service, versi

Syntax dasar :
  nmap [switch] [target IP]

Switch penting :
  -sC        → jalankan default scripts (deteksi celah umum otomatis)
  -sV        → deteksi versi service yang berjalan
  -v         → verbose (tampilkan proses scanning secara live)
  -p [port]  → scan port tertentu saja (contoh: -p 21)
  -p-        → scan semua 65535 port
  -A         → aggressive scan (OS detect + version + scripts + traceroute)

Contoh pakai :
  nmap -sC -sV -v 10.129.1.15
  nmap -sC -sV -p 21 10.129.1.15

Output penting yang dibaca :
  PORT   STATE  SERVICE  VERSION
  21/tcp open   ftp      vsftpd 3.0.3
  → state "open" = port aktif & bisa diakses
  → ftp-anon: Anonymous FTP login allowed ← celah!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTTP STATUS CODES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
200 → OK            : halaman ADA dan bisa diakses langsung ← target utama
301 → Redirect Perm : ada tapi diarahkan ke URL lain (folder biasanya)
302 → Redirect Temp : redirect sementara, biasanya butuh login dulu
401 → Unauthorized  : ada tapi butuh autentikasi HTTP
403 → Forbidden     : ada tapi akses dilarang → menarik, kadang bisa bypass!
404 → Not Found     : tidak ada (gobuster pakai ini sebagai penanda negatif)
500 → Server Error  : server error, kadang bisa dieksploitasi

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FTP (File Transfer Protocol)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Port    : 21
Fungsi  : Transfer file antara client dan server

Anonymous Login :
  → Misconfiguration berbahaya — siapa saja bisa masuk tanpa password
  → Normal hanya untuk public repository (driver, patch publik)
  → Berbahaya kalau ada file sensitif di dalamnya

Cara masuk :
  ftp [IP target]
  Name     : anonymous
  Password : (enter kosong)

Command di dalam FTP :
  ls        → lihat isi direktori
  get [file] → download file ke lokal
  put [file] → upload file ke server
  bye        → keluar dari FTP

Deteksi via Nmap :
  Script ftp-anon otomatis mencoba anonymous login
  Kalau allowed → langsung terdeteksi + tampilkan isi direktori

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 GOBUSTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi : Web fuzzing / directory & file enumeration
         Menebak nama file & folder tersembunyi di web server
         menggunakan wordlist

BUKAN brute force login! Brute force login = Hydra / Burp Intruder

Mode :
  dir   → directory & file enumeration ← paling sering dipakai
  dns   → subdomain enumeration
  vhost → virtual host enumeration
  fuzz  → fuzzing parameter/header/body
  s3    → AWS bucket enumeration

Syntax :
  gobuster dir -u [URL] -w [wordlist] [switch tambahan]

Switch penting (mode dir) :
  -u [URL]       → target URL
  -w [wordlist]  → path ke wordlist
  -x [ekstensi]  → filter tipe file (contoh: -x php,html,txt)
  -t [angka]     → jumlah threads (default 10, lebih besar = lebih cepat)
  -o [file]      → simpan output ke file
  --status-codes → filter status code tertentu

Contoh pakai :
  gobuster dir -u http://10.129.1.15 -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x php

Wordlist umum di Kali :
  /usr/share/wordlists/dirb/common.txt            → kecil, cepat
  /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt → medium
  /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt → besar

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Anonymous FTP      = akses FTP tanpa credentials → misconfiguration berbahaya
Directory Enum     = proses mencari file/folder tersembunyi di web server
Web Fuzzing        = teknik menebak-nebak path/parameter di web
Wordlist           = file berisi daftar kata untuk digunakan sebagai tebakan
Credential Exposure= credentials tersimpan di tempat yang bisa diakses publik
Misconfiguration   = kesalahan konfigurasi server → sumber celah umum
```