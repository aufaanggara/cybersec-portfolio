```
=== Web Server Lanjutan — Virtual Host, Reverse Proxy, SSL - Resume Materi ===
[20 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 VIRTUAL HOST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi  : Konfigurasi yang memungkinkan satu server Nginx melayani
            banyak domain/subdomain berbeda sekaligus
Cara kerja: Nginx baca header "Host" dari request browser, cocokkan
            dengan server_name di konfigurasi, lalu arahkan ke
            folder atau aplikasi yang sesuai

Konvensi file konfigurasi :
  → Satu domain = satu file di sites-available
  → Subdomain dari domain yang sama = masuk file yang sama
  → Domain berbeda = file konfigurasi baru yang terpisah
  Contoh : aufaserver.local dan blog.aufaserver.local → satu file
           proyekbaru.local → file baru terpisah

Struktur blok virtual host :
  server {
      listen 80;
      server_name namadomain.local;   → domain yang dilayani blok ini
      root /var/www/namadomain;       → folder file website
      index index.html;
      location / {
          try_files $uri $uri/ =404;
      }
  }

Cara aktifkan virtual host :
  1. Buat file config di /etc/nginx/sites-available/namadomain
  2. Buat symlink ke sites-enabled :
     sudo ln -s /etc/nginx/sites-available/nama /etc/nginx/sites-enabled/
  3. sudo nginx -t
  4. sudo systemctl reload nginx

Symlink = shortcut yang menunjuk ke file asli di lokasi lain
  → Buka symlink = buka file aslinya
  → Edit file asli = symlink otomatis reflect perubahan
  → Hapus symlink = disable virtual host tanpa hapus file asli
  Perintah buat symlink : ln -s [file_asli] [lokasi_symlink]

Relevansi cybersecurity :
  → Attacker pakai virtual host enumeration untuk temukan
    subdomain tersembunyi yang tidak dipublikasikan
  → Tool yang dipakai : gobuster mode vhost, ffuf
  → Subdomain internal (dev, staging, admin) sering kurang
    dijaga keamanannya dibanding production

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 REVERSE PROXY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi  : Nginx bertindak sebagai perantara antara client dan
            aplikasi backend yang berjalan di port lain
Cara kerja: Client request ke port 80/443 → Nginx terima →
            teruskan ke aplikasi backend (misal port 8000) →
            terima response → kirim balik ke client
Manfaat   : Aplikasi backend tidak perlu expose port langsung
            ke luar, semua lalu lintas lewat Nginx

Analogi   : Nginx = resepsionis kantor. Tamu datang ke lobby
            (port 80), resepsionis antarkan ke ruangan yang
            tepat di dalam (port 8000). Tamu tidak perlu tahu
            ruangan mana yang dituju.

Struktur blok reverse proxy :
  server {
      listen 80;
      server_name api.namadomain.local;

      location / {
          proxy_pass http://localhost:8000;         → teruskan ke port ini
          proxy_set_header Host $host;              → kirim nama domain asli
          proxy_set_header X-Real-IP $remote_addr; → kirim IP pengakses asli
      }
  }

Perbedaan dengan virtual host biasa :
  → Virtual host biasa : ada root dan file HTML yang disajikan
  → Reverse proxy      : tidak ada root, tidak ada file HTML
                         Nginx hanya meneruskan request ke backend

Directive reverse proxy :
  proxy_pass              → URL tujuan forward request
  proxy_set_header Host   → pastikan backend tahu nama domain yang diakses
  proxy_set_header X-Real-IP → pastikan backend tahu IP client asli,
                               bukan IP Nginx

Relevansi cybersecurity :
  → Misconfiguration reverse proxy adalah celah umum di CTF
    dan real world
  → SSRF (Server Side Request Forgery) sering memanfaatkan
    proxy_pass yang salah konfigurasi
  → Path traversal via reverse proxy juga umum ditemukan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SSL/HTTPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi  : Protokol enkripsi yang mengamankan koneksi antara
            browser dan server sehingga tidak bisa disadap
Port      : HTTPS berjalan di port 443, HTTP di port 80

Dua jenis sertifikat :
  Let's Encrypt   → sertifikat gratis dari CA resmi, diverifikasi
                    pihak ketiga, browser langsung percaya
                    Syarat : domain harus terdaftar di internet
  Self-signed     → sertifikat buatan sendiri, tidak ada CA yang
                    memverifikasi, browser kasih peringatan
                    Cocok untuk : lab lokal, development, internal

CA (Certificate Authority) = lembaga resmi yang memverifikasi
  identitas pemilik domain dan mengeluarkan sertifikat SSL
  Contoh : Let's Encrypt, DigiCert, Comodo
  Analogi : CA seperti pemerintah yang keluarkan KTP resmi,
            self-signed seperti kartu nama buatan sendiri

Buat self-signed certificate :
  sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/nama.key \
    -out /etc/ssl/certs/nama.crt

Switch openssl :
  req -x509      → buat sertifikat format X.509 (standar SSL)
  -nodes         → private key tidak dienkripsi dengan password
  -days 365      → masa berlaku sertifikat dalam hari
  -newkey rsa:2048→ buat private key baru, RSA 2048 bit
  -keyout        → lokasi simpan private key
  -out           → lokasi simpan file sertifikat

Lokasi standar file SSL di Linux :
  /etc/ssl/private/   → private key (hanya bisa dibaca root)
  /etc/ssl/certs/     → file sertifikat
  /etc/ssl/openssl.cnf→ konfigurasi default OpenSSL

Pasang SSL di konfigurasi Nginx :
  server {
      listen 80;
      server_name namadomain.local;
      return 301 https://$host$request_uri;  → redirect HTTP ke HTTPS
  }

  server {
      listen 443 ssl;                        → WAJIB ada kata "ssl"
      server_name namadomain.local;

      ssl_certificate /etc/ssl/certs/nama.crt;
      ssl_certificate_key /etc/ssl/private/nama.key;
      ssl_protocols TLSv1.2 TLSv1.3;        → gunakan TLS versi aman
      ssl_ciphers HIGH:!aNULL:!MD5;          → tolak cipher lemah

      root /var/www/html;
      index index.html;
      location / {
          try_files $uri $uri/ =404;
      }
  }

Directive SSL penting :
  listen 443 ssl        → dengarkan port 443 dengan SSL aktif
  ssl_certificate       → lokasi file sertifikat .crt
  ssl_certificate_key   → lokasi private key .key
  ssl_protocols         → versi TLS yang diizinkan
                          TLSv1.0 dan TLSv1.1 sudah deprecated/tidak aman
  ssl_ciphers           → algoritma enkripsi yang diizinkan
                          HIGH = kuat, !aNULL = tolak tanpa auth,
                          !MD5 = tolak MD5 yang sudah lemah
  return 301            → redirect permanen HTTP → HTTPS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HOSTS FILE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi  : File teks di sistem operasi yang memetakan nama domain
            ke IP address secara manual, tanpa perlu DNS server
Lokasi    :
  Windows : C:\Windows\System32\drivers\etc\hosts
  Linux   : /etc/hosts (ini yang kita edit di VM)
  macOS   : /etc/hosts

Cara edit di Windows : buka Notepad as Administrator
Format isi :
  192.168.56.101    aufaserver.local
  192.168.56.101    blog.aufaserver.local
  192.168.56.101    api.aufaserver.local

Cara kerja : browser cek hosts file dulu sebelum tanya ke DNS
             kalau ketemu → langsung pakai IP dari hosts file
             kalau tidak ketemu → baru tanya ke DNS server

Keterbatasan : entry hosts file hanya berlaku di perangkat itu
               sendiri. HP, laptop lain, tidak bisa resolve
               domain yang sama kecuali mereka juga edit
               hosts file masing-masing

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERINTAH TAMBAHAN YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ln -s [asli] [tujuan]  → buat symbolic link (symlink)
sudo ss -tlnp          → lihat semua port yang sedang listen
  -t = TCP
  -l = listening
  -n = tampilkan angka bukan nama
  -p = tampilkan nama proses
sudo ss -tlnp | grep nginx → filter hanya port milik Nginx

mkdir -p [path]        → buat folder beserta parent folder
                         kalau belum ada

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 STRUKTUR DOMAIN DI LAB INI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
aufaserver.local         → website utama, HTTPS, /var/www/html
blog.aufaserver.local    → website blog, HTTP, /var/www/blog
api.aufaserver.local     → reverse proxy ke FastAPI port 8000

Semua domain di-resolve via hosts file Windows karena .local
tidak terdaftar di DNS internet

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Virtual Host       = konfigurasi satu server untuk layani banyak domain
Reverse Proxy      = Nginx sebagai perantara ke aplikasi backend
SSL/TLS            = protokol enkripsi untuk koneksi aman
                     SSL sudah deprecated, TLS penggantinya,
                     tapi istilah "SSL" masih umum dipakai
HTTPS              = HTTP + enkripsi TLS/SSL di port 443
Certificate        = file berisi identitas server dan public key
Private Key        = kunci rahasia untuk dekripsi, jangan pernah dibagikan
Self-signed cert   = sertifikat tanpa verifikasi CA, browser kasih warning
CA                 = Certificate Authority, lembaga penerbit sertifikat resmi
Symlink            = shortcut yang menunjuk ke file asli di lokasi lain
Hosts file         = file lokal yang petakan domain ke IP tanpa DNS
301 Redirect       = redirect permanen, browser dan search engine ikuti
TLS 1.2 / 1.3      = versi TLS yang aman dan direkomendasikan saat ini
ERR_SSL_PROTOCOL   = error browser karena SSL tidak dikonfigurasi benar
                     penyebab umum : listen 443 tanpa kata "ssl"
```

# Ubuntu Server Home Lab — Virtual Host, Reverse Proxy & SSL/HTTPS

**Date:** 2026-05-20
**Platform:** Home Lab (VirtualBox)
**Difficulty:** Beginner
**Category:** Web / Network

---

## Target

Ubuntu Server VM yang sudah disetup di Fase 1 dan 2.
- IP: 192.168.56.101
- OS: Ubuntu Server 24.04 LTS
- Web Server: Nginx 1.24.0
- Backend: FastAPI (uvicorn) di port 8000

---

## Tujuan

Mengkonfigurasi web server Nginx dengan fitur lanjutan:
1. Virtual Host — satu server melayani banyak domain
2. Reverse Proxy — Nginx sebagai perantara ke aplikasi backend
3. SSL/HTTPS — enkripsi koneksi dengan self-signed certificate

---

## Tools Used

- Nginx — web server dan reverse proxy
- OpenSSL — generate self-signed SSL certificate
- uvicorn — ASGI server untuk menjalankan FastAPI
- curl — verifikasi konfigurasi dari terminal

---

## Steps

### Step 1 — Setup Virtual Host

Buat folder untuk website kedua:

```bash
sudo mkdir -p /var/www/blog
```

Buat halaman index untuk website blog:

```bash
sudo nano /var/www/blog/index.html
```

Buat file konfigurasi virtual host — satu file untuk satu domain beserta semua subdomainnya:

```bash
sudo nano /etc/nginx/sites-available/aufaserver.local
```

Isi konfigurasi dengan dua blok server untuk dua subdomain:

```nginx
server {
    listen 80;
    server_name aufaserver.local;

    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}

server {
    listen 80;
    server_name blog.aufaserver.local;

    root /var/www/blog;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

Aktifkan virtual host dengan membuat symlink ke sites-enabled:

```bash
sudo ln -s /etc/nginx/sites-available/aufaserver.local /etc/nginx/sites-enabled/
```

Test dan reload:

```bash
sudo nginx -t && sudo systemctl reload nginx
```

Tambahkan entry di hosts file Windows (`C:\Windows\System32\drivers\etc\hosts`) dengan Notepad as Administrator:

```
192.168.56.101    aufaserver.local
192.168.56.101    blog.aufaserver.local
```

Hasil: `aufaserver.local` dan `blog.aufaserver.local` masing-masing menampilkan halaman berbeda dari server yang sama.

---

### Step 2 — Setup Reverse Proxy

Jalankan aplikasi FastAPI di background:

```bash
cd ~/server && uvicorn main:app --host 0.0.0.0 --port 8000
```

Tambahkan blok server baru di file konfigurasi yang sama:

```bash
sudo nano /etc/nginx/sites-available/aufaserver.local
```

Tambahkan blok reverse proxy:

```nginx
server {
    listen 80;
    server_name api.aufaserver.local;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Test dan reload:

```bash
sudo nginx -t && sudo systemctl reload nginx
```

Tambahkan entry baru di hosts file Windows:

```
192.168.56.101    api.aufaserver.local
```

Hasil: mengakses `http://api.aufaserver.local` di browser menampilkan response JSON dari FastAPI tanpa perlu ketik port 8000:

```json
{"status": "server running", "workers": 3}
```

---

### Step 3 — Setup SSL/HTTPS

Generate self-signed certificate:

```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/ssl/private/aufaserver.key \
  -out /etc/ssl/certs/aufaserver.crt
```

Isi pertanyaan yang muncul, pastikan Common Name diisi `aufaserver.local`.

Verifikasi file berhasil dibuat:

```bash
ls /etc/ssl/private/aufaserver.key && ls /etc/ssl/certs/aufaserver.crt
```

Buka UFW untuk port 443:

```bash
sudo ufw allow https
```

Update konfigurasi blok server `aufaserver.local` untuk pakai HTTPS:

```nginx
server {
    listen 80;
    server_name aufaserver.local;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name aufaserver.local;

    ssl_certificate /etc/ssl/certs/aufaserver.crt;
    ssl_certificate_key /etc/ssl/private/aufaserver.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

Test dan reload:

```bash
sudo nginx -t && sudo systemctl reload nginx
```

Verifikasi Nginx listen di port 443:

```bash
sudo ss -tlnp | grep nginx
```

Output:
```
LISTEN   0   511   0.0.0.0:80    0.0.0.0:*   users:(("nginx"...))
LISTEN   0   511   0.0.0.0:443   0.0.0.0:*   users:(("nginx"...))
```

Hasil: mengakses `https://aufaserver.local` menampilkan peringatan self-signed certificate dari browser. Setelah klik Advanced → Proceed, halaman berhasil muncul dengan koneksi terenkripsi. HTTP otomatis redirect ke HTTPS via kode 301.

---

## Struktur Akhir Konfigurasi

```
/etc/nginx/sites-available/aufaserver.local
  → server aufaserver.local      port 80  → redirect ke HTTPS
  → server aufaserver.local      port 443 → /var/www/html (HTTPS)
  → server blog.aufaserver.local port 80  → /var/www/blog
  → server api.aufaserver.local  port 80  → proxy ke localhost:8000

/etc/ssl/certs/aufaserver.crt    → sertifikat SSL
/etc/ssl/private/aufaserver.key  → private key SSL
/var/www/html/                   → file website utama
/var/www/blog/                   → file website blog
```

---

## Kesalahan yang Ditemukan dan Diperbaiki

Saat setup SSL pertama kali terjadi `ERR_SSL_PROTOCOL_ERROR` karena dua kesalahan:

1. `listen 443;` tanpa kata `ssl` — Nginx tidak tahu koneksi ini SSL
2. Typo `aufaservel.local` di `server_name` — domain tidak cocok

Pelajaran: selalu cek ulang konfigurasi setelah ditulis, terutama bagian `listen` dan `server_name`.

---

## Lessons Learned

- Satu file konfigurasi Nginx bisa menampung banyak blok server — konvensi satu file per domain memudahkan pengelolaan jangka panjang
- Symlink di sites-enabled memungkinkan enable/disable website tanpa menghapus file konfigurasi aslinya
- Reverse proxy tidak butuh folder atau file HTML — Nginx hanya meneruskan request ke aplikasi backend
- Self-signed certificate cukup untuk lab lokal, tapi di production butuh sertifikat dari CA resmi seperti Let's Encrypt
- Kata `ssl` di `listen 443 ssl` adalah wajib — tanpanya Nginx tidak mengaktifkan enkripsi meski port 443 terbuka
- Hosts file adalah DNS lokal yang hanya berlaku di perangkat itu sendiri — perangkat lain tidak bisa resolve domain yang sama tanpa edit hosts file mereka sendiri
- Virtual host enumeration (gobuster vhost, ffuf) adalah teknik attacker untuk temukan subdomain tersembunyi — subdomain internal yang kurang dijaga sering jadi titik masuk

---

## Next Step

Lanjut ke eksploitasi lebih dalam menggunakan Metasploitable 2 sebagai target, dan eksplorasi teknik virtual host enumeration dari sisi attacker menggunakan gobuster di Kali Linux.