```
=== Linux Fundamentals Part 3 - Resume Materi ===
[25 Apr 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TERMINAL TEXT EDITORS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sebelumnya  : simpan teks pakai echo + pipe (> dan >>) → tidak efisien
              untuk file multi-baris
Solusi      : gunakan terminal text editor → Nano atau VIM

NANO
──────────────────────────────────────
Buka/buat file : nano filename
Navigasi       : tombol panah atas/bawah, Enter untuk baris baru
Shortcut penting (^ = Ctrl) :
  ^G  = Get Help         ^O  = Simpan file
  ^X  = Keluar           ^W  = Cari teks
  ^K  = Cut (potong)     ^U  = Paste
  ^R  = Baca file lain   ^C  = Lihat posisi kursor
  ^\  = Replace          ^_  = Loncat ke baris
  M-U = Undo             M-E = Redo
  M-A = Mark Text        M-6 = Copy Text
Fitur    : search, copy-paste, jump to line, cek posisi baris
Analogi  : Notepad — simpel, langsung pakai, tanpa belajar dulu

VIM
──────────────────────────────────────
Level       : jauh lebih advanced dari Nano
Keunggulan  :
  - Customisable (shortcut bisa diubah sendiri)
  - Syntax Highlighting (populer untuk developer)
  - Berjalan di semua terminal (bahkan tanpa Nano)
  - Banyak cheatsheet & tutorial tersedia
Analogi  : cockpit pesawat tempur — butuh waktu belajar,
           tapi kalau sudah mahir sangat powerful

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 GENERAL UTILITIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WGET — Download file dari internet
──────────────────────────────────────
Format  : wget [URL]
Contoh  : wget https://assets.tryhackme.com/file.txt
Cara    : download via HTTP, seperti akses file lewat browser
Analogi : kurir yang pergi ke alamat tertentu dan ambilkan file untukmu

SCP — Secure Copy (transfer file antar mesin via SSH)
──────────────────────────────────────
Format  : scp [source] [destination]
Kirim file ke remote  :
  scp file.txt user@IP:/home/user/file.txt
Ambil file dari remote :
  scp user@IP:/home/user/file.txt namalocal.txt
Fitur   : autentikasi + enkripsi via SSH
Syarat  : tahu username & password mesin remote
Analogi : jasa pengiriman bersenjata — paket dikunci,
          jalur aman, hanya pemilik kunci yang bisa buka

PYTHON3 HTTP SERVER — Jadikan mesin sebagai web server
──────────────────────────────────────
Jalankan server  : python3 -m http.server
Default port     : 8000
Download dari server (mesin lain) :
  wget http://[IP]:8000/namafile
Catatan : buka terminal BARU untuk wget,
          terminal server harus tetap aktif
Kelemahan : tidak ada indexing → harus tahu nama & lokasi file persis
Alternatif lebih canggih : Updog
Analogi : buka lapak di depan rumah — siapa yang tahu
          alamat & nomor lapakmu bisa ambil barang yang dipajang

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PROCESSES 101
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi  : program yang sedang berjalan di mesin
PID       : Process ID — nomor unik tiap proses, urut sesuai proses dimulai
Dikelola oleh : kernel

MELIHAT PROSES
──────────────────────────────────────
ps          → tampilkan proses sesi user saat ini
              kolom : PID, TTY, TIME, CMD
ps aux      → tampilkan SEMUA proses termasuk milik user lain & sistem
              kolom : USER, PID, %CPU, %MEM, VSZ, RSS, TTY, STAT,
                      START, TIME, COMMAND
top         → tampilan real-time, refresh tiap 10 detik
              navigasi dengan tombol panah
Analogi ps  : foto snapshot kondisi sistem saat itu
Analogi top : CCTV live — terus update dan bisa dipantau real-time

MANAGING PROCESSES (KILL)
──────────────────────────────────────
Format  : kill [PID]
Contoh  : kill 1337
Sinyal  :
  SIGTERM  = matikan proses, izinkan cleanup dulu
  SIGKILL  = matikan paksa, tanpa cleanup apapun
  SIGSTOP  = pause/tunda proses

HOW PROCESSES START
──────────────────────────────────────
Namespace  : OS bagi sumber daya (CPU, RAM) ke proses lewat namespace
             proses dalam namespace sama bisa saling lihat
             → bagus untuk isolasi & keamanan
PID 0/1    : proses pertama saat boot = systemd (Ubuntu)
systemd    : induk semua proses, duduk antara OS dan user
             semua program jalan sebagai child process dari systemd
Analogi    : systemd = induk semang kos — pertama masuk,
             semua penghuni bergantung padanya

SYSTEMCTL — Kontrol service via systemd
──────────────────────────────────────
Format  : systemctl [option] [service]
Option  :
  start    = jalankan service sekarang
  stop     = hentikan service sekarang
  enable   = aktifkan otomatis jalan saat boot
  disable  = nonaktifkan dari boot otomatis
  status   = cek kondisi service
Contoh  : systemctl start apache2
          systemctl enable apache2
Analogi : remote control semua layanan Linux

BACKGROUND & FOREGROUND
──────────────────────────────────────
Foreground  : proses berjalan di terminal, output langsung tampil
Background  : proses berjalan di belakang, terminal tetap bebas

Cara background :
  [perintah] &    → langsung background, dapat PID
  Ctrl + Z        → pause & background proses yang sedang jalan

Cara foreground kembali :
  fg              → bawa proses background kembali ke foreground

Analogi foreground : ngobrol langsung — fokus penuh, tidak bisa lain
Analogi background : minta orang kerja di belakang layar —
                     kamu tetap bebas ngerjain hal lain

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 AUTOMATION — CRONTAB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cron    : proses yang jalan saat boot, kelola semua cron job
Crontab : file khusus berisi jadwal tugas otomatis

Format crontab (6 nilai) :
  MIN   = menit ke berapa (0-59)
  HOUR  = jam berapa (0-23)
  DOM   = tanggal berapa (1-31)
  MON   = bulan ke berapa (1-12)
  DOW   = hari apa (0-7, 0&7=Minggu)
  CMD   = perintah yang dijalankan

Contoh  : 0 */12 * * * cp -R /home/user/Documents /var/backups/
          → backup setiap 12 jam, berapapun hari/bulannya

Wildcard (*) = "terserah" untuk field tersebut
@reboot      = jalankan sekali saat sistem boot

Edit crontab  : crontab -e
Tools bantu   : Crontab Generator, Cron Guru (online)
Analogi       : alarm jadwal otomatis — set sekali, jalan sendiri selamanya

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PACKAGE MANAGEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Repository : tempat developer submit software → jika approved → publik
apt        : package manager Ubuntu/Debian, kelola install/update/remove
             keunggulan : setiap update sistem, semua repo ikut dicek

File penting :
  /etc/apt/sources.list       = daftar repositori utama
  /etc/apt/sources.list.d/    = folder untuk repo tambahan (1 file per repo)
  /etc/apt/trusted.gpg.d/     = folder GPG key terpercaya

GPG Key : kunci keamanan dari developer
          jika kunci tidak cocok → software ditolak sistem
Analogi  : stempel resmi — palsu/tidak cocok langsung ditolak

PERINTAH APT
──────────────────────────────────────
apt update                    = perbarui daftar package dari semua repo
apt install [nama]            = install software
apt remove [nama]             = hapus software
add-apt-repository [repo]     = tambah repo baru
add-apt-repository --remove ppa:PPA_Name/ppa = hapus repo

CARA TAMBAH REPO MANUAL (contoh Sublime Text)
──────────────────────────────────────
1. Download & simpan GPG key :
   wget -qO /etc/apt/trusted.gpg.d/nama.gpg [URL_KEY]

2. Buat file list di sources.list.d :
   touch /etc/apt/sources.list.d/nama.list

3. Isi file dengan alamat repo (pakai nano) :
   deb [URL_REPO] apt/stable/

4. Update apt agar kenali repo baru :
   apt update

5. Install software :
   apt install [nama-software]

Analogi apt  : tukang belanja pribadi yang tahu semua toko langganan,
               otomatis cek update setiap kali belanja

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LOGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Lokasi    : /var/log/
Fungsi    : catat semua aktivitas aplikasi & layanan di sistem
Rotating  : OS kelola log otomatis (arsip lama, buat yang baru)

Log penting :
  apache2/access.log  = catat setiap request ke web server
                        (IP, waktu, file diakses, status code)
  apache2/error.log   = catat semua error web server
  fail2ban.log        = pantau percobaan brute force
  ufw.log             = aktivitas firewall
  auth.log            = percobaan autentikasi user
  syslog              = aktivitas OS secara umum

Format access.log :
  [IP] - - [tanggal] "GET /file HTTP/1.1" [status] [size]

File .gz    : log lama yang sudah dikompresi
File .1/.2  : rotasi log (1 = kemarin, 2 = dua hari lalu, dst)
Warna hijau di ls = file world-readable (bisa dibaca semua user)

Kegunaan   : diagnosa masalah performa, selidiki aktivitas penyusup
Analogi    : buku diary sistem — setiap kejadian dicatat lengkap
             dengan waktu, siapa, dan ngapain

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PID          = Process ID, nomor unik setiap proses
systemd      = induk proses pertama saat boot di Ubuntu
Child Process= proses yang lahir dari/dikendalikan proses lain
Namespace    = isolasi sumber daya antar proses di OS
Foreground   = proses yang aktif & terlihat di terminal
Background   = proses berjalan di belakang tanpa blokir terminal
Rotating     = proses OS arsipkan log lama & buat log baru
GPG Key      = kunci enkripsi untuk verifikasi keaslian software
Repository   = server penyimpan kumpulan software yang bisa diinstall
Cron Job     = tugas terjadwal yang dijalankan otomatis oleh cron
World-readable = file yang bisa dibaca oleh semua user di sistem
```