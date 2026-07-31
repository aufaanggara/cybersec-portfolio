```
=== SSRF (Server-Side Request Forgery) - Resume Materi ===
[18 Mar 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU SSRF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Vulnerability yang memungkinkan attacker memaksa
           webserver membuat HTTP request ke resource pilihan attacker
Cara     : Memanipulasi parameter URL yang digunakan server
           untuk fetch data dari server lain
Analogi  : Menyuruh kurir (server) mengambil sesuatu dari
           tempat yang tidak boleh kamu datangi sendiri

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERBEDAAN SSRF vs IDOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IDOR  → Kamu SENDIRI yang akses data orang lain langsung
        Manipulasi : ID/parameter objek (id=1 → id=2)
        Target     : Data user lain di aplikasi yang sama

SSRF  → SERVER yang melakukan request atas perintahmu
        Manipulasi : URL tujuan yang di-fetch server
        Target     : Resource internal/eksternal yang tidak
                     bisa diakses attacker secara langsung

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DUA JENIS SSRF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Regular SSRF → Data dikembalikan ke layar attacker
               Attacker BISA lihat hasilnya langsung

Blind SSRF   → SSRF terjadi tapi tidak ada output
               Attacker TIDAK BISA lihat hasilnya
               Butuh tools external untuk konfirmasi

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DAMPAK SSRF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Access to unauthorised areas
   → Akses area/halaman terlarang
2. Access to customer/organisational data
   → Baca data pelanggan atau data internal
3. Ability to scale to internal networks
   → Pivot masuk ke jaringan internal
4. Reveal authentication tokens/credentials
   → Curi API key, password, token auth

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 4 TEMPAT MENEMUKAN SSRF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Full URL di address bar          ← PALING MUDAH
   Contoh : ?url=http://api.website.thm/store
   Cara   : Langsung ganti nilai URL di parameter

2. Hidden field di form HTML        ← PERLU DEVTOOLS
   Contoh : <input type="hidden" value="http://server/store">
   Cara   : Inspect Element → edit value → submit form

3. Partial URL / hostname only      ← TRIAL & ERROR
   Contoh : ?server=api
   Cara   : Tebak format sistem + pakai trik &x=

4. Path URL saja                    ← TRIAL & ERROR
   Contoh : ?dst=/forms/contact
   Cara   : Directory traversal dengan ../

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TEKNIK EKSPLOITASI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Full URL Control
  → Ganti seluruh URL parameter dengan target
  → Contoh : ?url=http://internal-server/secret

Directory Traversal
  → Gunakan ../ untuk naik folder
  → Contoh : ?url=/../user
  → ../ = keluar dari folder saat ini

Subdomain + Parameter Poisoning (&x=)
  → Pakai saat hanya bisa kontrol hostname
  → Tambah &x= di akhir payload
  → Sisa URL otomatis jadi nilai parameter x
    (tidak berguna/diabaikan server)
  → Kenapa & jadi ? :
    & tidak boleh ada sebelum ? dalam URL
    sistem auto-koreksi & menjadi ?
  → Contoh :
    Input  : ?server=target.com/api/user&x=
    Hasil  : http://target.com/api/user?x=[sampah]

Open Redirect ke Server Hacker
  → Arahkan server ke domain milik hacker
  → Server membawa header + API key saat request
  → Hacker tangkap header tersebut di servernya

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERTAHANAN & CARA BYPASSNYA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DENY LIST
  Cara kerja : Semua request OK kecuali yang di daftar
  Contoh blokir : localhost, 127.0.0.1, 169.254.169.254
  Bypass dengan alternatif localhost :
    → 0
    → 0.0.0.0
    → 0000
    → 127.1
    → 127.*.*.*
    → 2130706433  (desimal dari 127.0.0.1)
    → 017700000001 (oktal dari 127.0.0.1)
    → 127.0.0.1.nip.io (DNS resolve ke 127.0.0.1)
  Bypass IP cloud 169.254.169.254 :
    → Daftarkan subdomain dengan DNS record
      yang mengarah ke IP tersebut

ALLOW LIST
  Cara kerja : Semua request DITOLAK kecuali yang di daftar
  Contoh aturan : URL harus diawali https://website.thm
  Bypass :
    → Buat subdomain yang namanya mengandung
      string yang diizinkan
    → Contoh : https://website.thm.attacker-domain.thm
    → Filter melihat awalan benar → izinkan

OPEN REDIRECT
  Bukan pertahanan, tapi dimanfaatkan untuk bypass
  Cara kerja : Endpoint yang redirect pengunjung
               ke URL lain otomatis
  Contoh     : /link?url=https://tryhackme.com
  Dimanfaatkan : Pakai endpoint redirect ini sebagai
                 "pintu masuk" yang sudah di-whitelist
                 untuk redirect ke domain hacker

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TOOLS UNTUK BLIND SSRF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
requestbin.com        → Catat semua HTTP request masuk
HTTP server sendiri   → Server pribadi untuk logging
Burp Suite Collaborator → Tool profesional deteksi blind SSRF

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CARA IDENTIFIKASI URL RENTAN SSRF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tanda-tanda URL rentan :
  → Ada parameter berisi URL/domain/hostname
  → Ada parameter srv=, server=, url=, dst=
  → Ada parameter port= (indikasi server konek ke host lain)
  → Ada path file yang di-fetch server

Contoh rentan :
  ?fetch-file.php?fname=file.pdf&srv=storage.cloud.thm&port=8001
  ↑ ada srv= (hostname) dan port= → sangat mencurigakan

Contoh TIDAK rentan :
  ?categoryId=5325   → hanya angka ID (lebih ke IDOR)
  ?itemId=213&price=100 → angka biasa, bukan URL/host

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HIDDEN FIELD — BEDAKAN MANA BAHAYA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BERBAHAYA (potensi SSRF) :
  <input type="hidden" name="server" value="http://api.site.com">
  → Nilainya URL → bisa diganti ke server lain

TIDAK BERBAHAYA (proteksi keamanan) :
  <input type="hidden" name="logintoken" value="abc123xyz">
  <input type="hidden" name="state" value="hKFo2SA3...">
  <input type="hidden" name="lt" value="B12EA43B...">
  → Ini CSRF Token / OAuth State Token
  → Acak, sekali pakai, expire, server yang validasi
  → Justru ini PERTAHANAN, bukan celah

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SSRF          = Server-Side Request Forgery
CSRF Token    = Token anti-pemalsuan request (proteksi)
OAuth State   = Token binding sesi OAuth (proteksi)
nip.io        = Layanan DNS yang resolve subdomain ke IP
Base64        = Format enkode data (hasil fetch SSRF)
Deny List     = Daftar hitam — blokir yang terdaftar
Allow List    = Daftar putih — izinkan yang terdaftar saja
Open Redirect = Endpoint yang redirect ke URL lain otomatis
Directory Traversal = Teknik naik folder pakai ../
Parameter Poisoning = Racuni parameter dengan &x= trick
Content Discovery   = Proses jelajah endpoint tersembunyi
Metadata Server     = 169.254.169.254 — berisi info server cloud
```