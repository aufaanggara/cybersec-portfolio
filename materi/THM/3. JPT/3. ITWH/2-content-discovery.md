```
=== Content Discovery - Resume Materi ===
[07 Mar 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU CONTENT DISCOVERY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Menemukan konten tersembunyi di website yang tidak
           ditampilkan secara publik & tidak selalu untuk publik
Konten   : File, video, gambar, backup, fitur website,
           panel admin, halaman staff, config files, dll
3 Cara   : Manual → Automated → OSINT

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MANUAL DISCOVERY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
robots.txt
  → Memberitahu mesin pencari halaman mana yang DILARANG diindeks
  → Justru berisi daftar halaman yang paling menarik untuk pentester
  → Akses : http://TARGET_IP/robots.txt

sitemap.xml
  → Kebalikan robots.txt → daftar halaman yang INGIN diindeks
  → Bisa mengandung halaman lama yang masih aktif di balik layar
  → Akses : http://TARGET_IP/sitemap.xml

Favicon
  → Ikon kecil di tab/address bar browser
  → Jika developer tidak ganti favicon bawaan framework → bocorkan
    framework yang dipakai
  → Cocokkan hash MD5 favicon dengan database OWASP :
    https://wiki.owasp.org/index.php/OWASP_favicon_database
  → Command : curl URL/favicon.ico | md5sum

HTTP Headers
  → Berisi info software webserver & bahasa pemrograman yang dipakai
  → Contoh : nginx/1.18.0, PHP/7.4.3
  → Command : curl http://TARGET_IP -v
  → Flag -v = verbose mode (tampilkan semua detail header)

Framework Stack
  → Setelah tahu framework (dari favicon/source code/komentar/copyright)
  → Cari website resmi framework tersebut
  → Dari dokumentasinya bisa ditemukan path admin portal, dll
  → Cek source code halaman untuk komentar tersembunyi

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 OSINT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Google Dorking
  → Manfaatkan fitur pencarian canggih Google
  → Filter yang wajib hapal :
    site:domain.com     = hasil hanya dari domain tersebut
    inurl:admin         = URL mengandung kata tertentu
    filetype:pdf        = ekstensi file tertentu
    intitle:admin       = judul halaman mengandung kata tertentu
  → Bisa dikombinasikan : site:target.com inurl:admin
  → Info lebih : https://en.wikipedia.org/wiki/Google_hacking

Wappalyzer
  → Tool online & ekstensi browser
  → Identifikasi teknologi website : framework, CMS,
    payment processor, versi software, dll
  → Link : https://www.wappalyzer.com/

Wayback Machine
  → Arsip historis website sejak akhir 90-an
  → Temukan halaman lama yang masih aktif di website saat ini
  → Link : https://archive.org/web/

GitHub
  → Git = version control system (lacak perubahan file proyek)
  → GitHub = Git yang di-hosting di internet
  → Cari nama perusahaan/website target di GitHub
  → Bisa temukan : source code, password, konten tersembunyi

S3 Buckets
  → Layanan penyimpanan cloud milik Amazon AWS
  → Format URL : http(s)://{name}.s3.amazonaws.com
  → Jika misconfigured → file publik/writable yang harusnya privat
  → Cara temukan : source code, GitHub, atau brute force nama :
    {name}-assets, {name}-www, {name}-public, {name}-private

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 AUTOMATED DISCOVERY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi   : Gunakan tools untuk kirim ratusan ribu request otomatis
             mengecek apakah file/direktori ada di website target
Wordlist   : File teks berisi daftar kata umum yang dicoba satu per satu
             Sumber terbaik : https://github.com/danielmiessler/SecLists
             Install di Kali : sudo apt install seclists -y

Tools :
  ffuf     → Paling CEPAT, sangat fleksibel (bisa fuzzing parameter dll)
  dirb     → Paling TUA & sederhana, paling lambat, cocok pemula
  gobuster → Seimbang kecepatan & fitur, bisa scan subdomain juga

Command :
  ffuf :
  ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
       -u http://TARGET_IP/FUZZ

  dirb :
  dirb http://TARGET_IP/
       /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt

  gobuster :
  gobuster dir --url http://TARGET_IP/
           -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Brute Force    = coba semua kemungkinan satu per satu sampai ketemu
Wordlist       = file teks berisi daftar kata untuk brute force
Favicon        = ikon kecil di tab browser untuk branding website
Framework      = kerangka kerja yang dipakai untuk membangun website
Crawling       = proses mesin pencari menjelajahi isi website
Verbose mode   = mode tampilkan detail lengkap output (-v di curl)
MD5 Hash       = nilai unik hasil enkripsi file, dipakai identifikasi
FUZZ           = placeholder di ffuf yang diganti kata dari wordlist
Repository     = tempat penyimpanan kode/file di Git/GitHub
Misconfigured  = salah konfigurasi → buka celah keamanan
```

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SWITCH & FUNGSI - ffuf, dirb, gobuster
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

╔══════════════════════════════════════╗
║              F F U F                 ║
╚══════════════════════════════════════╝
Switch    Fungsi
───────   ──────────────────────────────────────────
-w        Wordlist yang dipakai (path ke file .txt)
-u        URL target (FUZZ = placeholder kata dari wordlist)
-H        Tambahkan custom header
-X        HTTP method yang dipakai (GET, POST, dll)
-d        Data untuk POST request
-t        Jumlah thread/koneksi bersamaan (default: 40)
-p        Delay antar request (detik)
-mc       Filter berdasarkan HTTP status code
          (default: 200,301,302,307,401,403)
-fc       Sembunyikan hasil dengan status code tertentu
-fs       Sembunyikan hasil berdasarkan ukuran response
-fw       Sembunyikan hasil berdasarkan jumlah kata
-ac       Auto-kalibrasi filter otomatis
-v        Verbose → tampilkan full URL hasil temuan
-o        Simpan output ke file
-of       Format output (json, csv, dll)
-r        Ikuti redirect otomatis
-recursion     Scan rekursif ke dalam direktori yang ditemukan
-recursion-depth  Kedalaman maksimal rekursi

Contoh penggunaan :
  Basic :
  ffuf -w /usr/share/wordlists/SecLists/Discovery/
       Web-Content/common.txt -u http://10.48.136.239/FUZZ

  Filter hanya status 200 :
  ffuf -w common.txt -u http://10.48.136.239/FUZZ -mc 200

  Rekursif 2 level :
  ffuf -w common.txt -u http://10.48.136.239/FUZZ
       -recursion -recursion-depth 2

╔══════════════════════════════════════╗
║              D I R B                 ║
╚══════════════════════════════════════╝
Switch    Fungsi
───────   ──────────────────────────────────────────
(none)    Tanpa switch → pakai wordlist default bawaan dirb
-a        Set custom User-Agent
-b        Gunakan path tanpa slash di akhir URL
-c        Set cookie untuk request
-e        Cari ekstensi file tertentu (misal: -e php,html)
-f        Fine tuning → tampilkan semua response
-i        Abaikan HTTP error
-l        Print lokasi header saat ada redirect
-N        Abaikan response dengan kode status tertentu
-o        Simpan output ke file
-p        Gunakan proxy (format: host:port)
-P        Autentikasi proxy (username:password)
-r        Jangan scan secara rekursif
-R        Kedalaman rekursi maksimal
-S        Mode silent → tidak tampilkan hasil yang tidak ditemukan
-t        Jumlah thread koneksi bersamaan
-u        Username untuk autentikasi HTTP
-v        Verbose → tampilkan semua response termasuk NOT_FOUND
-w        Lanjutkan scan meski ada peringatan
-x        Cari file dengan ekstensi tertentu
-X        Ekstensi yang diabaikan
-z        Tambahkan delay antar request (ms)

Contoh penggunaan :
  Basic :
  dirb http://10.48.136.239/
       /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt

  Cari file PHP :
  dirb http://10.48.136.239/ common.txt -e php

  Tidak rekursif :
  dirb http://10.48.136.239/ common.txt -r

  Simpan output :
  dirb http://10.48.136.239/ common.txt -o hasil.txt

╔══════════════════════════════════════╗
║          G O B U S T E R            ║
╚══════════════════════════════════════╝

Mode yang tersedia :
  dir   = brute force direktori & file
  dns   = brute force subdomain
  vhost = brute force virtual host

── MODE dir (yang kita pakai) ──────────
Switch         Fungsi
───────────    ──────────────────────────────────────
--url / -u     URL target
-w             Wordlist yang dipakai
-t             Jumlah thread (default: 10)
-o             Simpan output ke file
-x             Ekstensi file yang dicari (misal: -x php,html,txt)
-s             Status code yang dianggap sukses
               (default: 200,204,301,302,307,401,403)
-b             Blacklist/sembunyikan status code tertentu
-k             Abaikan error SSL certificate
-r             Ikuti redirect
-e             Print URL lengkap di hasil
-q             Mode quiet → minimalis output
-v             Verbose → tampilkan semua request
--delay        Delay antar request
--timeout      Timeout per request
--proxy        Gunakan proxy
-U             Username untuk HTTP auth
-P             Password untuk HTTP auth
-c             Cookie untuk request
-H             Custom header
--wildcard     Paksa lanjut meski wildcard response terdeteksi

Contoh penggunaan :
  Basic :
  gobuster dir --url http://10.48.136.239/
           -w /usr/share/wordlists/SecLists/Discovery/
              Web-Content/common.txt

  Cari file PHP & HTML :
  gobuster dir --url http://10.48.136.239/
           -w common.txt -x php,html

  Scan subdomain :
  gobuster dns -d target.com -w common.txt

  Simpan output :
  gobuster dir --url http://10.48.136.239/
           -w common.txt -o hasil.txt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERBANDINGAN CEPAT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
              ffuf      dirb      gobuster
Kecepatan  :  ★★★★★    ★★☆☆☆    ★★★★☆
Kemudahan  :  ★★★☆☆    ★★★★★    ★★★★☆
Fitur      :  ★★★★★    ★★☆☆☆    ★★★★☆
Subdomain  :  ✗         ✗         ✓
Rekursif   :  ✓         ✓         ✗
```