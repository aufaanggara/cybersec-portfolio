```
=== Lab Cyber — Reconnaissance & Hardening - Resume Materi ===
[20 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR FASE 2 LAB CYBER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Posisi    : Pindah dari sisi admin (fase 1) ke sisi attacker
Target    : Ubuntu Server VM (192.168.56.101) yang sudah dibangun di fase 1
Attacker  : Kali Linux VM (192.168.56.102)
Jaringan  : Keduanya di Host-only adapter 192.168.56.x

Alur yang dilakukan :
  1. Verifikasi koneksi Kali → Ubuntu (ping)
  2. Reconnaissance dengan nmap
  3. Vulnerability scanning dengan nikto
  4. Analisis temuan — bedakan real vs false positive
  5. Hardening — tutup semua celah yang ditemukan
  6. Verifikasi hasil hardening

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NETWORK ADAPTER — SYARAT KOMUNIKASI ANTAR VM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Syarat    : Kedua VM harus pakai adapter yang SAMA dan SATU jaringan
            Kalau beda (satu Host-only, satu Internal) = tidak bisa komunikasi

Host-only : VM bisa komunikasi sesama VM DAN dengan laptop host
            IP range : 192.168.56.x
            Cocok untuk : lab cyber, akses dari browser Windows juga bisa

Internal  : Hanya sesama VM, laptop host tidak bisa akses
            Cocok untuk : isolasi total dari host

Restart network setelah ganti adapter (tanpa matiin VM) :
  sudo systemctl restart NetworkManager

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NMAP — NETWORK SCANNER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi  : Tool reconnaissance untuk scan jaringan, port, dan service
Fungsi    : Lihat port apa yang terbuka, service apa yang jalan,
            versi software, dan OS target

Perintah & switch :
  nmap [target]          → scan dasar, deteksi port terbuka
  nmap -sV [target]      → service version detection
                           deteksi versi software di tiap port
  nmap -sC [target]      → jalankan default scripts untuk info lebih detail
                           (ssh-hostkey, http-title, dll)
  nmap -T4 [target]      → timing template, T4 = cepat
                           T1=paling lambat, T5=paling cepat
  nmap -sV -sC -T4 [IP]  → kombinasi lengkap, paling sering dipakai

Format output nmap :
  PORT      STATE    SERVICE   VERSION
  22/tcp    open     ssh       OpenSSH 9.6p1 Ubuntu
  80/tcp    open     http      nginx 1.24.0 (Ubuntu)
  8000/tcp  closed   http-alt

  open   = port terbuka, service aktif dan bisa diakses
  closed = port tertutup tapi terdeteksi ada (UFW blokir tapi nmap masih lihat)
  filtered = port difilter, tidak bisa ditentukan open/closed

Info yang bocor dari nmap sebelum hardening :
  → Versi software (nginx 1.24.0)
  → OS (Ubuntu)
  → SSH fingerprint/hostkey
  → Title halaman web (Server Aufa)
  → Server header (nginx/1.24.0)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NIKTO — WEB VULNERABILITY SCANNER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi  : Tool scanner kerentanan khusus web server
Fungsi    : Cek misconfiguration, missing security headers,
            file sensitif yang tidak sengaja terbuka, dan celah umum
            Melakukan 8000+ request otomatis ke target

Perintah & switch :
  nikto -h [target]              → scan dasar
  nikto -h http://[IP]           → scan dengan protokol eksplisit
  nikto -h [IP] -p [port]        → scan port spesifik
  nikto -h [IP] -o hasil.txt     → simpan output ke file

Temuan nikto di lab ini (sebelum hardening) :
  1. Server: nginx/1.24.0 (Ubuntu)   → versi terbaca, bisa dicari CVE
  2. X-Frame-Options tidak ada       → rentan clickjacking
  3. X-Content-Type-Options tidak ada→ rentan MIME sniffing
  4. wp-config.php terdeteksi        → FALSE POSITIVE, file tidak ada

Penting : tidak semua temuan nikto valid — harus diverifikasi manual
          Kemampuan bedakan false positive dari real finding = skill penting

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CURL — HTTP REQUEST DARI TERMINAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi  : Tool untuk kirim HTTP request langsung dari terminal

Perintah & switch :
  curl [URL]       → GET request, tampilkan isi HTML response
  curl -I [URL]    → tampilkan HANYA headers response, tidak tampilkan HTML
                     dipakai untuk verifikasi security headers

Contoh output curl -I setelah hardening :
  Server: nginx                        ← versi sudah disembunyikan
  X-Frame-Options: SAMEORIGIN          ← proteksi clickjacking aktif
  X-Content-Type-Options: nosniff      ← proteksi MIME sniffing aktif

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SECURITY HEADERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi  : Header HTTP tambahan yang dikirim server untuk
            memberitahu browser cara menangani konten secara aman

X-Frame-Options       → mencegah halaman dimuat dalam iframe
  SAMEORIGIN          = boleh iframe hanya dari domain yang sama
  DENY                = tidak boleh iframe dari manapun
  Serangan yang dicegah : Clickjacking

X-Content-Type-Options→ mencegah browser tebak-tebak tipe file
  nosniff             = browser harus percaya header Content-Type dari server
  Serangan yang dicegah : MIME type confusion / script injection via file upload

server_tokens         → directive Nginx untuk sembunyikan versi
  off                 = hanya tampilkan "nginx" tanpa versi dan OS
  Manfaat             : attacker tidak tahu versi spesifik untuk cari CVE

Cara tambahkan di nginx.conf (dalam blok http {}) :
  server_tokens off;
  add_header X-Frame-Options "SAMEORIGIN";
  add_header X-Content-Type-Options "nosniff";

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SERANGAN YANG DIPELAJARI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Clickjacking :
  Cara kerja : attacker embed halaman target dalam iframe transparan
               di atas halaman jebakan → korban klik tombol palsu
               tapi sebenarnya klik tombol di halaman asli di bawahnya
  Contoh     : tombol "Klik dapat hadiah" menutupi tombol "Transfer Dana"
  Pencegahan : X-Frame-Options header

MIME Sniffing Attack :
  Cara kerja : attacker upload file gambar yang berisi script JS
               browser tanpa nosniff bisa salah baca sebagai JS
               dan langsung eksekusi script berbahaya itu
  Pencegahan : X-Content-Type-Options: nosniff

Server Version Disclosure :
  Cara kerja : server header mengumumkan versi software dan OS
               attacker cari CVE spesifik untuk versi tersebut
               lalu eksploitasi kerentanan yang sudah terdokumentasi
  Contoh     : nginx/1.24.0 (Ubuntu) → cari exploit nginx 1.24.0
  Pencegahan : server_tokens off di nginx.conf

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONSEP PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
False Positive  = temuan scanner yang ternyata tidak valid setelah
                  diverifikasi manual. Scanner bekerja otomatis dan
                  tidak selalu akurat — harus selalu dikonfirmasi

Hardening       = proses memperkuat server dengan menutup celah,
                  meminimalkan informasi yang bocor, dan tambah
                  proteksi ekstra. Dilakukan SETELAH vulnerability
                  assessment

Server Header   = informasi yang dikirim server ke browser/client
                  di setiap response HTTP. Bisa berisi versi software,
                  OS, dan teknologi yang dipakai — sumber info bagi attacker

CVE             = Common Vulnerabilities and Exposures, database
                  kerentanan software yang sudah terdokumentasi publik
                  Attacker pakai ini untuk cari exploit berdasarkan
                  versi software target

Reconnaissance  = tahap pengumpulan informasi tentang target sebelum
                  menyerang. Semakin banyak info = semakin mudah
                  menemukan celah yang bisa dieksploitasi

Iframe          = tag HTML yang menampilkan halaman website lain
                  di dalam halaman kamu, seperti layar dalam layar

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERBANDINGAN SEBELUM DAN SESUDAH HARDENING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    SEBELUM              SESUDAH
Server header     : nginx/1.24.0 (Ubuntu)  nginx
X-Frame-Options   : tidak ada              SAMEORIGIN
X-Content-Type    : tidak ada              nosniff
Nikto findings    : 3 item                 2 item (false positive)
Info bocor        : versi + OS             tidak ada
```

# Ubuntu Server Home Lab — Reconnaissance & Web Server Hardening

**Date:** 2026-05-20
**Platform:** Home Lab (VirtualBox)
**Difficulty:** Beginner
**Category:** Web / Network

---

## Target

Ubuntu Server VM yang sudah disetup di Fase 1 dengan Nginx web server.
- IP: 192.168.56.101
- OS: Ubuntu Server 24.04 LTS
- Service: Nginx 1.24.0, OpenSSH 9.6p1
- Attacker: Kali Linux VM (192.168.56.102)

---

## Vulnerability

Tiga misconfiguration ditemukan di web server:

1. **Server Version Disclosure** — Nginx secara default mengumumkan versi software dan OS di setiap response header, memudahkan attacker mencari CVE spesifik untuk versi tersebut.
2. **Missing X-Frame-Options Header** — Tidak ada proteksi terhadap serangan clickjacking, halaman bisa di-embed di iframe website manapun.
3. **Missing X-Content-Type-Options Header** — Browser bisa salah interpretasi tipe file yang dikirim server, berpotensi dieksploitasi untuk menjalankan script berbahaya.

---

## Tools Used

- nmap — network scanner, reconnaissance port dan service
- nikto — web vulnerability scanner
- curl — HTTP request dari terminal untuk verifikasi headers

---

## Steps

### Step 1 — Verifikasi Koneksi Attacker ke Target

Sebelum mulai reconnaissance, pastikan Kali bisa reach Ubuntu Server. Kedua VM harus berada di jaringan Host-only yang sama (192.168.56.x).

```bash
ping 192.168.56.101
```

Output:
```
64 bytes from 192.168.56.101: icmp_seq=1 ttl=64 time=2.87 ms
64 bytes from 192.168.56.101: icmp_seq=2 ttl=64 time=2.74 ms
4 packets transmitted, 4 received, 0% packet loss
```

Koneksi berhasil, lanjut ke scanning.

---

### Step 2 — Reconnaissance dengan Nmap

Scan port dan deteksi service yang berjalan di target.

```bash
nmap -sV -sC -T4 192.168.56.101
```

Output:
```
PORT      STATE   SERVICE  VERSION
22/tcp    open    ssh      OpenSSH 9.6p1 Ubuntu 3ubuntu13.16
80/tcp    open    http     nginx 1.24.0 (Ubuntu)
| http-title: Server Aufa
| http-server-header: nginx/1.24.0 (Ubuntu)
8000/tcp  closed  http-alt

MAC Address: 08:00:27:32:4C:05 (Oracle VirtualBox)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Informasi yang berhasil dikumpulkan dari perspektif attacker:
- Web server: Nginx versi 1.24.0
- OS: Ubuntu Linux
- SSH: OpenSSH 9.6p1
- Title halaman: "Server Aufa"
- Port 8000 tertutup tapi terdeteksi — ada service lain yang pernah jalan

---

### Step 3 — Vulnerability Scanning dengan Nikto

Scan lebih dalam untuk temukan misconfiguration dan celah umum di web server.

```bash
nikto -h http://192.168.56.101
```

Output temuan utama:
```
+ Server: nginx/1.24.0 (Ubuntu)
+ /: The anti-clickjacking X-Frame-Options header is not present.
+ /: The X-Content-Type-Options header is not set.
+ /#wp-config.php#: file found. This file contains the credentials.
+ 8102 requests: 0 error(s) and 3 item(s) reported
```

---

### Step 4 — Analisis dan Verifikasi Temuan

Verifikasi temuan nikto secara manual sebelum hardening.

**Verifikasi wp-config.php** — cek apakah file benar-benar ada di server:

```bash
find /var/www/html -name "*.php*"
```

Output: kosong, tidak ada hasil.

Kesimpulan: temuan wp-config.php adalah **false positive**. Nikto scan ribuan path secara otomatis dan tidak selalu akurat — verifikasi manual wajib dilakukan.

**Verifikasi headers via curl:**

```bash
curl -I http://192.168.56.101
```

Output sebelum hardening:
```
HTTP/1.1 200 OK
Server: nginx/1.24.0 (Ubuntu)
Content-Type: text/html
```

Konfirmasi: versi Nginx dan OS terbaca jelas, security headers tidak ada.

---

### Step 5 — Hardening: Tutup Semua Celah

Edit file konfigurasi utama Nginx:

```bash
sudo nano /etc/nginx/nginx.conf
```

Tambahkan tiga baris berikut di dalam blok `http {}`:

```nginx
server_tokens off;
add_header X-Frame-Options "SAMEORIGIN";
add_header X-Content-Type-Options "nosniff";
```

Test konfigurasi sebelum diterapkan:

```bash
sudo nginx -t
```

Output:
```
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

Reload Nginx untuk terapkan perubahan:

```bash
sudo systemctl reload nginx
```

---

### Step 6 — Verifikasi Hasil Hardening

Cek headers setelah hardening:

```bash
curl -I http://192.168.56.101
```

Output setelah hardening:
```
HTTP/1.1 200 OK
Server: nginx
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
```

Jalankan nikto ulang untuk konfirmasi:

```bash
nikto -h http://192.168.56.101
```

Hasil: temuan turun dari 3 item menjadi 2 item, dan server header sudah tidak menampilkan versi maupun OS.

---

## Hasil Perbandingan Sebelum dan Sesudah Hardening

| | Sebelum | Sesudah |
|---|---|---|
| Server header | nginx/1.24.0 (Ubuntu) | nginx |
| X-Frame-Options | tidak ada | SAMEORIGIN |
| X-Content-Type-Options | tidak ada | nosniff |
| Nikto findings | 3 item | 2 item (false positive) |

---

## Lessons Learned

- Reconnaissance dengan nmap bisa mengungkap banyak informasi dari server yang tidak dikonfigurasi dengan benar — versi software, OS, dan service yang berjalan semuanya terbaca jelas
- Scanner otomatis seperti nikto tidak selalu akurat — verifikasi manual setiap temuan adalah keharusan sebelum menyimpulkan ada celah
- Security headers adalah lapisan proteksi yang mudah ditambahkan tapi sering diabaikan — tiga baris konfigurasi di nginx.conf sudah menutup beberapa vektor serangan
- Memahami server dari sisi admin (fase 1) membuat analisis dari sisi attacker (fase 2) jauh lebih bermakna — kamu tahu apa yang dicari karena kamu yang membangunnya
- `server_tokens off` adalah konfigurasi minimal yang wajib ada di setiap web server production

---

## Next Step

Fase 3 (opsional): Virtual host, reverse proxy, dan SSL/HTTPS untuk melengkapi konfigurasi web server. Lanjut juga ke Metasploitable untuk latihan eksploitasi yang lebih dalam.