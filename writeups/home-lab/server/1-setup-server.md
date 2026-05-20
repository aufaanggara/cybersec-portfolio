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