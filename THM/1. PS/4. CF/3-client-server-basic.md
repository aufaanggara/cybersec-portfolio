```
=== Networking Fundamentals - Resume Materi ===
[26 Mar 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SEJARAH SINGKAT JARINGAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Awalnya  : Komputer bekerja MANDIRI (standalone)
           → simpan file sendiri, jalankan program sendiri
           → tidak berkomunikasi dengan komputer lain

Berkembang: Organisasi mulai menghubungkan sistem satu sama lain
Tujuan   : 1. Information Exchange  = tukar data antar komputer
           2. Resource Sharing      = pakai sumber daya komputer lain

Cikal bakal internet (jaringan awal) :
  ARPANET  → milik Dept. Pertahanan Amerika
  CYCLADES → jaringan riset dari Prancis
  NPL      → National Physical Laboratory, Inggris
  NSFNET   → milik National Science Foundation Amerika

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MODEL CLIENT - SERVER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Client   : Pihak yang MEMINTA layanan/data
           Contoh : browser di komputermu
Server   : Pihak yang MELAYANI/memberikan data
           Contoh : server website yang kamu kunjungi

Aturan   : CLIENT selalu yang pertama memulai request
Analogi  : Alice (client) minta pizza → Bob bawa ke Luigi's (server)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 REQUEST & RESPONSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Request  : Permintaan yang dikirim client ke server
Response : Jawaban yang dikirim server ke client

PENTING  : Jika request tidak diformat benar ATAU
           resource tidak tersedia → dapat ERROR response
           Contoh error : "No pepperoni pizza available"

Dalam komputer : Browser (client) request halaman web
                 → Server kirim halaman web kembali ke client

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PROTOCOL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Aturan/standar komunikasi agar dua sistem bisa
           saling bertukar data
Analogi  : Bahasa yang dipakai saat memesan pizza

Protocol mendefinisikan :
  → Perintah apa yang dipahami client & server (contoh: GET)
  → Bagaimana request disusun (urutan: perintah dulu, lalu data)
  → Sintaks/bahasa yang digunakan
  → Respons untuk request yang benar
  → Respons untuk request yang salah/error

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : "Pintu" numerik untuk mengidentifikasi layanan
           SPESIFIK yang berjalan di sebuah sistem
Fungsi   : Client harus konek ke port yang BENAR
           untuk mengakses layanan yang diinginkan

Analogi  : Luigi's punya 3 pintu berbeda →
           Pintu A = Takeaway
           Pintu B = Restoran (dine in)
           Pintu C = Delivery

Penting  : Satu server bisa jalankan BANYAK layanan sekaligus
           masing-masing layanan diidentifikasi oleh port berbeda

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DNS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Singkatan: Domain Name Service
Fungsi   : Menerjemahkan nama domain → alamat IP server
Analogi  : GPS yang ubah nama tempat → koordinat lokasi

Cara kerja :
  Kamu ketik  → "google.com"
  DNS resolve → 142.250.x.x (IP address)

IP Address : Alamat unik setiap sistem di jaringan
             Ibarat alamat rumah (jalan, nomor, kota, negara)
             tapi untuk komputer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTTP / HTTPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kepanjangan : Hypertext Transfer Protocol (Secure)
Sifat       : STATELESS → setiap request diproses independen,
              server tidak ingat request sebelumnya

Tapi website modern pakai mekanisme tambahan :
  → Session identifier (disimpan di cookie/token)
  → Dikirim di setiap request agar server "ingat" kamu
  → Tanpa ini, kamu harus login ulang di setiap request

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 9 HTTP METHODS (WAJIB HAPAL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GET      → Ambil/retrieve resource dari server       ← PALING UMUM
POST     → Kirim data baru ke server
PUT      → Update/replace resource di server
DELETE   → Hapus resource di server
PATCH    → Update sebagian resource di server
HEAD     → Sama seperti GET tapi hanya ambil header
OPTIONS  → Tanya method apa saja yang didukung server
CONNECT  → Buat tunnel ke server
TRACE    → Loop-back test untuk debugging

Dalam HTTP, command disebut METHOD (bukan command)
Spesifikasi resmi HTTP disebut RFC (Request for Comments)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 METHOD GET - DETAIL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Retrieve (ambil) resource dari web server
Contoh   : GET https://tryhackme.com/index.php

Alur HTTP Communication :
  1. CLIENT → kirim HTTP REQUEST (GET /index.html)
  2. Lewat INTERNET
  3. SERVER → kirim HTTP RESPONSE (200 OK + konten)
  4. Browser tampilkan halaman

Kamu tidak perlu tulis request manual →
browser otomatis bangun request di balik layar

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FIELD PENTING DALAM GET REQUEST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scheme   → Protokol yang dipakai        : HTTP / HTTPS
Host     → Nama host yang diminta       : httpdemo.local:8080
Filename → File yang diminta dari host  : "/" = index.html
Address  → IP address server            : 127.0.0.1
Status   → Hasil request berhasil/tidak : 200 OK = berhasil

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTTP STATUS CODES (PENTING)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
200  → OK          = Request BERHASIL
404  → Not Found   = Resource TIDAK DITEMUKAN

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 RESPONSE = 2 BAGIAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Response Header → Metadata tentang respons
                  (info tambahan, bukan konten utama)
                  Contoh isi : Content-Type, Content-Length,
                               Date, Server, Last-Modified

Response Body   → Konten yang diminta
                  Contoh : kode HTML halaman website

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CARA INSPECT GET REQUEST (DEV TOOLS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Buka     : F12 atau klik kanan → Inspect
Tab      : Network
Cara     : Reload halaman → lihat semua request muncul
Klik     : Entry pertama → lihat detail di panel kanan

Tab yang tersedia di detail :
  Headers  → info request & response header
  Cookies  → cookie yang dikirim/diterima
  Request  → isi request yang dikirim
  Response → isi response body (HTML, dll)
  Timings  → waktu yang dibutuhkan tiap proses

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Stateless       = server tidak ingat request sebelumnya
Session         = sesi login yang disimpan via cookie/token
IP Address      = alamat unik komputer di jaringan
DNS             = sistem penerjemah domain → IP
Port            = nomor identifikasi layanan di server
Protocol        = aturan komunikasi antar sistem
HTTP Method     = perintah dalam protokol HTTP (GET, POST, dll)
Status Code     = kode angka hasil dari sebuah request
Response Header = metadata dari respons server
Response Body   = konten/isi dari respons server
RFC             = Request for Comments (dokumen spesifikasi resmi)
Developer Tools = tool bawaan browser untuk inspeksi web traffic
```