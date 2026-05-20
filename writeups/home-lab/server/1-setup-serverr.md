```
=== Web Server & Linux Server Admin - Resume Materi ===
[20 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONSEP DASAR SERVER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Server      = komputer/program yang melayani request dari client
Web Server  = server khusus yang melayani request HTTP dari browser
VM sebagai  = bisa dijadikan server lokal untuk belajar, konsep &
server        perintahnya identik dengan server fisik atau VPS
VPS         = Virtual Private Server, server virtual yang disewa
              di cloud, selalu online tanpa perlu hardware sendiri

Perbedaan jalur server :
  Self-hosted → server fisik sendiri, full kontrol, butuh IP statis
  VPS/Cloud   → sewa server di cloud, praktis, bayar bulanan
  VM lokal    → untuk belajar, tidak perlu selalu online

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NGINX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi  : Software web server, melayani request browser
Cara kerja: Browser kirim request → Nginx terima → kirim file
            HTML/CSS/JS balik ke browser
Analogi   : Seperti resepsionis — tamu (browser) datang minta
            sesuatu, resepsionis (Nginx) yang ambilkan dan antarkan
vs Apache : Fungsi sama, Nginx lebih ringan & cepat untuk
            traffic tinggi, lebih populer saat ini

Install   : sudo apt install nginx -y
Start     : sudo systemctl start nginx
Stop      : sudo systemctl stop nginx
Restart   : sudo systemctl restart nginx  ← matikan lalu nyalakan
Reload    : sudo systemctl reload nginx   ← terapkan config baru
                                            tanpa matikan server
Status    : sudo systemctl status nginx
Test cfg  : sudo nginx -t  ← SELALU lakukan ini sebelum reload

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 STRUKTUR FOLDER NGINX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
/etc/nginx/                → markas besar konfigurasi Nginx
/etc/nginx/nginx.conf      → file konfigurasi utama/global
/etc/nginx/sites-available/→ semua config website yang tersedia
                             (belum tentu aktif)
/etc/nginx/sites-enabled/  → config website yang aktif dijalankan
                             (biasanya symlink ke sites-available)
/etc/nginx/conf.d/         → konfigurasi tambahan
/etc/nginx/mime.types      → daftar jenis file yang Nginx kenali
/var/www/html/             → folder default tempat file website
                             disimpan (HTML, CSS, JS, gambar)
/var/log/nginx/access.log  → log semua request yang masuk
/var/log/nginx/error.log   → log semua error yang terjadi

Alur tambah perubahan config :
  1. Edit file di /etc/nginx/sites-available/
  2. sudo nginx -t          → test syntax
  3. sudo systemctl reload nginx → terapkan perubahan

Alur tambah file website baru (HTML/CSS/JS) :
  → Cukup taruh file di /var/www/html/
  → Tidak perlu edit config, Nginx otomatis layani

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONFIGURASI NGINX (sites-available/default)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Struktur blok aktif :

  server {
      listen 80 default_server;   → dengarkan port 80 (HTTP)
      listen [::]:80 default_server; → sama untuk IPv6
      root /var/www/html;         → folder file website
      index index.html index.htm; → file yang dicari pertama
      server_name _;              → layani semua domain/IP
      location / {
          try_files $uri $uri/ =404; → cari file, kalau tidak
      }                              ada tampilkan 404
      error_page 404 /404.html;  → halaman custom untuk error 404
  }

Catatan penting :
  → Baris diawali # = komentar, diabaikan Nginx
  → Yang tidak ada # = aktif dan dieksekusi
  → Port 80 = HTTP standar
  → Port 443 = HTTPS (butuh SSL certificate)
  → server_name _ = tangkap semua request apapun domainnya

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FIREWALL - UFW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
UFW = Uncomplicated Firewall, tool kelola lalu lintas jaringan
      di Ubuntu. Tanpa firewall semua port terbuka.

WAJIB : tambahkan rule SEBELUM enable, terutama SSH
        kalau SSH tidak diizinkan dulu, koneksi langsung terputus

Perintah UFW :
  sudo ufw status          → cek status firewall
  sudo ufw status verbose  → cek status + detail semua rule
  sudo ufw status numbered → tampilkan rule beserta nomornya
  sudo ufw enable          → aktifkan firewall
  sudo ufw disable         → nonaktifkan firewall
  sudo ufw allow ssh       → izinkan port 22 (SSH)
  sudo ufw allow http      → izinkan port 80 (HTTP)
  sudo ufw allow https     → izinkan port 443 (HTTPS)
  sudo ufw allow 3000      → izinkan port spesifik
  sudo ufw deny 80         → blokir port
  sudo ufw delete allow 80 → hapus rule tertentu

Status rule :
  ALLOW IN  = koneksi masuk diizinkan
  DENY IN   = koneksi masuk diblokir
  (v6)      = rule berlaku untuk IPv6

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MEMBACA LOG NGINX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dua file log utama :
  access.log → semua request yang masuk ke server
  error.log  → semua error yang terjadi di server

Format satu baris access.log :
  192.168.56.1 - - [20/May/2026:05:24:10] "GET /about.html HTTP/1.1" 200 238 "http://..." "Mozilla/5.0..."

  192.168.56.1        = IP pengakses
  [20/May/2026:...]   = waktu request
  GET                 = method HTTP (GET=baca, POST=kirim data)
  /about.html         = halaman yang diakses
  HTTP/1.1            = versi protokol
  200                 = HTTP response code
  238                 = ukuran response dalam bytes
  "http://..."        = halaman asal sebelum klik (referer)
  "Mozilla/5.0..."    = browser & OS pengakses (user agent)

HTTP Response Code yang wajib hapal :
  200 = OK, sukses
  304 = Not Modified, browser pakai cache
  400 = Bad Request
  403 = Forbidden, tidak punya izin akses
  404 = Not Found, halaman tidak ada
  500 = Internal Server Error

Perintah log :
  sudo cat /var/log/nginx/access.log    → lihat semua log
  sudo cat /var/log/nginx/error.log     → lihat log error
  sudo tail -f /var/log/nginx/access.log → monitor realtime
                                           Ctrl+C untuk berhenti

Tingkat severity error.log (ringan ke berat) :
  notice → info biasa, tidak ada masalah
  warn   → peringatan
  error  → error yang perlu diperhatikan
  crit   → error kritis
  alert  → butuh tindakan segera
  emerg  → sistem tidak bisa digunakan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NETWORK ADAPTER VIRTUALBOX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NAT           → VM bisa akses internet keluar, tapi tidak bisa
                diakses dari luar VM. IP biasanya 10.0.2.x
Host-only     → VM bisa diakses dari laptop host dan VM lain,
                tidak bisa akses internet langsung.
                IP biasanya 192.168.56.x
Internal      → Hanya bisa komunikasi antar VM, laptop host
Network         tidak bisa akses
Bridged       → VM dapat IP dari router seperti perangkat nyata,
                bisa diakses dari jaringan luar

Kombinasi ideal untuk lab :
  Adapter 1 = NAT        → untuk download package & update
  Adapter 2 = Host-only  → untuk akses dari Kali & Windows

Interface di Linux :
  lo      = loopback, 127.0.0.1, komunikasi VM dengan dirinya sendiri
  enp0s3  = biasanya NAT (IP 10.0.2.x)
  enp0s8  = biasanya Host-only (IP 192.168.56.x)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DNS & RESOLV.CONF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DNS             = sistem yang ubah nama domain jadi IP address
                  Tanpa DNS, sistem tidak bisa resolve nama domain
/etc/resolv.conf= file konfigurasi DNS di Linux
                  isinya : nameserver [IP DNS server]
8.8.8.8         = DNS publik Google, selalu online dan cepat
8.8.4.4         = DNS publik Google cadangan
1.1.1.1         = DNS publik Cloudflare

Fix DNS cepat :
  echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf

Gejala DNS bermasalah :
  → ping IP langsung berhasil (ping 8.8.8.8 = OK)
  → ping domain gagal (ping google.com = FAIL)
  → apt install gagal dengan "Temporary failure resolving"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERINTAH LINUX SERVER YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
sudo [perintah]     → jalankan sebagai root, sementara
sudo su / sudo -i   → masuk sesi root permanen (hindari)
ip addr show        → lihat semua interface & IP address
ping [IP/domain]    → test koneksi ke target
ssh user@IP         → remote masuk ke server lewat SSH
cat [file]          → tampilkan isi file
nano [file]         → buka file di text editor terminal
sudo rm [file]      → hapus file
ls [folder]         → lihat isi folder
cd [folder]         → pindah ke folder
apt update          → update daftar package
apt upgrade         → upgrade semua package
apt install [nama]  → install package baru

Shortcut nano :
  Ctrl+O → save file
  Ctrl+X → keluar
  Ctrl+K → cut satu baris
  Ctrl+Shift+6 → mulai select/mark blok
  Ctrl+C → lihat posisi kursor (baris & kolom)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Daemon        = program yang berjalan di background di Linux
                contoh : nginx, ssh, ufw semua berjalan sebagai daemon
Symlink       = shortcut/link yang menunjuk ke file lain
                sites-enabled isinya symlink ke sites-available
Port          = pintu masuk ke server, setiap layanan punya port sendiri
                22=SSH, 80=HTTP, 443=HTTPS, 3306=MySQL, 3000=Node.js
Root/var/www  = konvensi standar Linux untuk menyimpan file website
Permission    = hak akses file di Linux (read/write/execute)
Referer       = halaman asal sebelum pengakses klik link ke halaman ini
User Agent    = identitas browser & OS yang dikirim saat request HTTP
Reload        = terapkan config baru tanpa matikan server
Restart       = matikan lalu nyalakan ulang server
IPv4          = format IP biasa, contoh 192.168.56.101
IPv6          = format IP baru, contoh fe80::1, lebih panjang
```

# Ubuntu Server Home Lab — Web Server Setup dengan Nginx

**Date:** 2026-05-20
**Platform:** Home Lab (VirtualBox)
**Difficulty:** Beginner
**Category:** Web / Linux Server Admin

---

## Target

Ubuntu Server VM yang berjalan di VirtualBox di atas laptop utama (Windows, 16GB RAM). VM dikonfigurasi sebagai web server menggunakan Nginx, sebagai fondasi sebelum masuk ke fase lab cybersecurity.

**Spesifikasi VM:**
- OS: Ubuntu Server 24.04 LTS
- RAM: 4096 MB
- CPU: 2 core
- Storage: 25 GB
- Hostname: aufaserver

---

## Tujuan

Membangun web server lokal yang bisa diakses dari host Windows dan nantinya dari VM Kali Linux, sebagai target latihan cybersecurity sekaligus media belajar sysadmin.

---

## Tools Used

- VirtualBox — hypervisor untuk menjalankan VM
- Ubuntu Server — OS server
- Nginx — web server
- UFW — firewall
- nano — text editor terminal
- SSH — remote access ke VM
- Browser (Chrome) — verifikasi hasil

---

## Setup Steps

### Step 1 — Konfigurasi Network Adapter VM

Sebelum mulai, pastikan VM punya dua adapter jaringan:

- **Adapter 1 (NAT)** — supaya VM bisa akses internet untuk download package
- **Adapter 2 (Host-only)** — supaya VM bisa diakses dari Windows host dan VM Kali

Cek IP yang aktif setelah VM nyala:

```bash
ip addr show
```

Output yang relevan:
- `enp0s3` dengan IP `10.0.2.x` → ini adapter NAT
- `enp0s8` dengan IP `192.168.56.101` → ini adapter Host-only, IP inilah yang dipakai untuk akses web server

---

### Step 2 — Fix DNS dan Update Sistem

Test koneksi internet:

```bash
ping 8.8.8.8
```

Kalau ping IP berhasil tapi apt gagal resolve domain, berarti DNS bermasalah. Fix dengan:

```bash
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
```

Lalu update sistem:

```bash
sudo apt update && sudo apt upgrade -y
```

---

### Step 3 — Install Nginx

```bash
sudo apt install nginx -y
```

Cek status setelah install:

```bash
sudo systemctl status nginx
```

Nginx otomatis langsung jalan setelah install dan otomatis enable sehingga nyala lagi setiap VM restart.

---

### Step 4 — Buat Halaman Web

Nginx secara default melayani file dari `/var/www/html/`. Buat halaman utama:

```bash
sudo nano /var/www/html/index.html
```

Struktur file website yang dibuat:

```
/var/www/html/
├── index.html      — halaman utama
├── about.html      — halaman tentang
├── contact.html    — halaman kontak
└── 404.html        — halaman error custom
```

Setiap halaman dilengkapi navbar untuk navigasi antar halaman.

Akses dari browser Windows di `http://192.168.56.101` — tidak perlu restart atau reload Nginx setiap tambah file HTML baru.

---

### Step 5 — Konfigurasi Error Page Custom

Edit file konfigurasi Nginx:

```bash
sudo nano /etc/nginx/sites-available/default
```

Tambahkan baris berikut di dalam blok `server {}`, setelah blok `location / {}`:

```nginx
error_page 404 /404.html;
```

Test konfigurasi sebelum reload:

```bash
sudo nginx -t
```

Jika output `syntax is ok` dan `test is successful`, lanjut reload:

```bash
sudo systemctl reload nginx
```

Sekarang setiap URL yang tidak ada akan otomatis redirect ke halaman 404 custom.

---

### Step 6 — Setup Firewall UFW

Tambahkan rule terlebih dahulu SEBELUM enable firewall:

```bash
sudo ufw allow ssh
sudo ufw allow http
```

Baru aktifkan firewall:

```bash
sudo ufw enable
```

Verifikasi rule yang aktif:

```bash
sudo ufw status verbose
```

Port yang terbuka:
- Port 22 (SSH) — remote access
- Port 80 (HTTP) — web server Nginx
- Port 8000 — aplikasi Python yang masih aktif dipakai

Semua port lain tertutup secara default.

---

### Step 7 — Membaca Log Akses

Lihat semua log akses:

```bash
sudo cat /var/log/nginx/access.log
```

Monitor log secara realtime:

```bash
sudo tail -f /var/log/nginx/access.log
```

Format satu baris log:

```
192.168.56.1 - - [20/May/2026:05:24:10 +0000] "GET /about.html HTTP/1.1" 200 238 "-" "Mozilla/5.0..."
```

Kolom dari kiri ke kanan: IP pengakses — timestamp — method dan path — HTTP response code — ukuran response — referer — user agent.

Lihat log error:

```bash
sudo cat /var/log/nginx/error.log
```

---

## Hasil

Web server berhasil berjalan dan dapat diakses dari browser Windows di `http://192.168.56.101`. Website memiliki tiga halaman yang saling terhubung via navbar, halaman 404 custom, firewall aktif dengan rule minimal, dan log akses bisa dipantau secara realtime.

---

## Struktur Konfigurasi Nginx Aktif

```nginx
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
    }

    error_page 404 /404.html;
}
```

---

## Lessons Learned

- Network adapter di VirtualBox harus dikombinasikan — NAT untuk internet, Host-only untuk akses lokal antar VM
- DNS dan koneksi internet adalah dua hal berbeda — internet bisa jalan tapi DNS bisa gagal secara terpisah
- Perubahan file konfigurasi Nginx harus selalu ditest dulu dengan `nginx -t` sebelum reload
- File HTML baru tidak perlu didaftarkan ke konfigurasi — cukup taruh di `/var/www/html/` dan Nginx langsung layani
- UFW harus ditambahkan rule SSH sebelum diaktifkan, agar tidak terkunci dari server sendiri
- `reload` lebih aman dari `restart` untuk menerapkan perubahan config karena server tidak dimatikan
- Log akses Nginx menyimpan semua aktivitas termasuk IP pengakses, halaman yang dibuka, dan browser yang dipakai — ini akan sangat berguna di fase lab cybersecurity

---

## Next Step

Fase 2 — Lab Cybersecurity: scan web server ini dari Kali Linux menggunakan nmap, analisis hasil scan dari perspektif attacker, dan lanjut ke eksploitasi serta hardening.