# === Offensive Security Intro - Resume Materi ===
[27 Mar 2026]

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU OFFENSIVE SECURITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Menguji sistem secara PROAKTIF dari sudut pandang penyerang
           dengan tujuan menemukan kelemahan SEBELUM hacker jahat melakukannya
Cara     : Bertanya → Apa yang terekspos? Apa yang bisa diakses?
           Asumsi apa yang dibuat sistem ini?
Syarat   : Harus ada IZIN (permission) — ini aturan paling kritis
Analogi  : Seperti mencoba membobol rumahmu sendiri untuk tau di mana
           celah yang perlu diperbaiki

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HACKING = PENETRATION TESTING (BUKAN KRIMINAL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Di modul ini "hacking" = penetration testing yaitu :
  ✅ Ethical   → dilakukan secara etis
  ✅ Legal     → diizinkan secara hukum
  ✅ Structured→ terstruktur & metodis
Hacker di sini = orang yang pakai skill ini secara POSITIF
                 untuk meningkatkan keamanan sistem

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CORE OFFENSIVE SECURITY TERMS — WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Red Teaming    = Serangan terstruktur & diotorisasi yang mensimulasikan
                 musuh nyata → uji efektivitas pertahanan dalam scope
                 yang ditentukan

Penetration    = Penilaian keamanan terstruktur oleh tester yang
Test             diotorisasi → identifikasi & eksploitasi vulnerability
                 dalam scope → pahami risiko dunia nyata

Vulnerability  = Kelemahan/cacat pada sistem, aplikasi, atau konfigurasi
                 yang bisa disalahgunakan penyerang

Exploit        = Teknik/metode untuk memanfaatkan vulnerability
                 → tujuan : akses data/fungsi yang dibatasi

Scope          = Batasan apa yang BOLEH diuji dalam engagement
                 → sistem mana, aplikasi mana, tindakan apa yang
                   diizinkan & mana yang off-limits

Enumeration    = Mengumpulkan detail sistem, pengguna, layanan
                 → untuk menemukan titik lemah

Credentials    = Detail login (username + password) yang membuka akses

Authentication = Langkah verifikasi identitas saat login

Dictionary     = Serangan menggunakan wordlist yang sudah ditentukan
Attack           sebelumnya untuk menebak password/username

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ATURAN EMAS : PERMISSION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Semua istilah berbagi 1 aturan kritis → PERMISSION (izin)
Ethical hacking = pengujian sistem secara TERKONTROL & LEGAL
Ethical hacker  = diizinkan eksplisit untuk uji sistem dalam scope
Di dunia nyata  : organisasi sewa pentest/red team untuk simulasi
                  serangan ke sistem mereka sendiri
Tujuan          : BUKAN rusak — tapi uji kekuatan kontrol keamanan,
                  ungkap gap, bantu tingkatkan security posture

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MINDSET HACKER — THINK LIKE A HACKER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Hacker melihat melampaui "apakah ini bekerja?" →
tanya "bagaimana ini bisa DISALAHGUNAKAN?"

4 Poin kunci yang wajib diingat :

  Ask questions     → Jangan asumsikan fitur bekerja normal
                      Tanya : "What if it doesn't?"

  Test the          → Coba tindakan & input yang TIDAK dipikirkan
  unexpected          developer

  Chain small       → Cacat kecil bisa dihubungkan → dampak besar
  weaknesses          (efek domino)

  Think like an     → "Bagaimana pelaku jahat mendekati target ini?"
  adversary

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONSEP CHAINING WEAKNESSES (EFEK DOMINO)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1 kelemahan saja → tidak kritis
Tapi kelemahan A + kelemahan B → KONSEKUENSI SERIUS

Analogi domino :
  → 1 domino jatuh sendiri = tidak berbahaya
  → Banyak domino berderet = 1 jatuh → semua jatuh

Contoh di modul :
  Domino 1 = menemukan halaman login tersembunyi (/admin)
  Domino 2 = password lemah (abc123, qwerty, dll)
  Hasil    = MASUK ke sistem → akses sensitif terbuka

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA YANG BISA DIAKSES SETELAH MASUK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sensitive       = Fitur esensial (modif data, konten terbatas,
functionality     proses khusus) → seharusnya hanya untuk user resmi

User data       = Nama, email, detail akun pengguna
                  → bisa dicuri, disalahgunakan, atau dijual

Administrative  = Fitur hak-istimewa tinggi → kelola user,
features          ubah setting, KONTROL PENUH aplikasi

Further attack  = Akses terautentikasi → ekspos kerentanan lain
opportunities     → penyerang bisa pivot lebih dalam

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TOOLS YANG DIPAKAI DI MODUL INI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GOBUSTER — Directory/File Enumeration Tool
  Fungsi : Otomatis scan halaman/direktori tersembunyi di web server
  Mode   : dir → mode enumerasi direktori & file
  Command:
    gobuster dir --url http://www.onlineshop.thm/ \
    -w /usr/share/wordlists/dirbuster/directory-list.txt

  Switch & Fungsinya :
    gobuster       → tool utama untuk penemuan konten web
    dir            → aktifkan mode directory & file enumeration
    --url [target] → set target website yang akan di-scan
    -w [file]      → tentukan wordlist untuk tebak nama dir/file

─────────────────────────────────────
HYDRA — Password Cracking / Dictionary Attack Tool
  Fungsi : Otomatis uji ratusan/ribuan password ke form login target
  Teknik : Dictionary attack → pakai wordlist yang sudah ada
  Command:
    hydra -l admin -P passlist.txt www.onlineshop.thm \
    http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect" -V

  Switch & Fungsinya :
    hydra            → tool utama untuk dictionary attack
    -l admin         → set username yang dipakai (admin)
    -P passlist.txt  → set file wordlist password yang akan dicoba
    www.onlineshop.thm → set target website
    http-post-form   → indikasikan ini adalah HTTP POST request form
    "/login:..."     → tentukan cara login request dikirim &
                       cara Hydra tahu login GAGAL (F=incorrect)
    -V               → verbose → tampilkan setiap username &
                       password yang sedang dicoba

  Tips    : Password valid → ada di baris KEDUA DARI AKHIR output

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR PRAKTIK DI MODUL INI (STUDI KASUS MIKE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Skenario : Mike mau launch website toko online → minta assessment
           apakah ada halaman sensitif yang tidak sengaja publik

Step 1 → MANUAL ENUMERATION
         Coba URL berikut satu per satu di browser :
           http://www.onlineshop.thm/sitemap
           http://www.onlineshop.thm/mail
           http://www.onlineshop.thm/register
           http://www.onlineshop.thm/login   ← ADA! (halaman tersembunyi)
           http://www.onlineshop.thm/admin
         Jika halaman tidak ada → Error 404

Step 2 → AUTOMATED ENUMERATION dengan Gobuster
         → Scan otomatis seluruh kemungkinan direktori
         → Lebih cepat dari manual jika daftar panjang

Step 3 → MANUAL PASSWORD TESTING
         Username : admin
         Coba password : abc123 / 123456 / password / qwerty / 654321

Step 4 → AUTOMATED ATTACK dengan Hydra
         → Hydra coba semua password dalam wordlist otomatis
         → Jauh lebih cepat dari manual

Step 5 → BERHASIL MASUK → dapat FLAG → assessment selesai

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KARIER DI OFFENSIVE SECURITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Penetration       = Jelajahi vulnerability secara aman dalam
Tester /            scope yang ditentukan
Ethical Hacker

Vulnerability     = Identifikasi & validasi kelemahan yang belum
Researcher          ditemukan dalam software & hardware

Red Team          = Simulasikan musuh dunia nyata → uji kemampuan
Operator            deteksi, respons & pertahanan organisasi

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 JALUR BELAJAR SELANJUTNYA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Become a Defender  → pelajari teknik DEFENSIF (blue team)
Cyber Security 101 → fondasi lebih luas
Jr Penetration     → spesialisasi offensive lebih dalam
Tester
SOC Level 1        → jalur karier Security Operations Center
```