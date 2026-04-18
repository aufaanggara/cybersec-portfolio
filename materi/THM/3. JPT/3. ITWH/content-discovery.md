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