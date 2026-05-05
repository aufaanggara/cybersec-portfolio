```
=== HTTP in Detail - Resume Materi ===
[05 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU HTTP & HTTPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HTTP   : HyperText Transfer Protocol
         Protokol untuk komunikasi dengan web server
         Dikembangkan : Tim Berners-Lee (1989-1991)
         Fungsi : transmisi webpage data (HTML, images, videos, dll)

HTTPS  : HTTP Secure (versi aman dari HTTP)
         Data dienkripsi → mencegah orang lain baca data kita
         Fungsi : (1) enkripsi data, (2) verifikasi server asli (bukan palsu)
         Port   : HTTP = 80, HTTPS = 443

Analogi : HTTP = kirim surat terbuka (siapa saja bisa baca)
          HTTPS = kirim surat dalam amplop tersegel + materai (aman & terverifikasi)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KOMPONEN URL (Uniform Resource Locator)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Format lengkap:
scheme://user:password@host:port/path?query#fragment

Scheme   : Protokol yang digunakan (http, https, ftp)
User     : Username & password untuk autentikasi (opsional)
Host     : Domain name atau IP address server
Port     : Port koneksi (default: 80 untuk HTTP, 443 untuk HTTPS)
           Range valid: 1-65535
Path     : Lokasi file/resource di server
Query    : Parameter tambahan (?id=1&name=admin)
           Format: key=value, dipisah dengan &
Fragment : Referensi ke bagian spesifik halaman (#section1)
           Untuk jump langsung ke lokasi tertentu

Contoh:
https://user:pass@tryhackme.com:443/room?id=1#task3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTTP REQUEST - STRUKTUR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Format sederhana:
METHOD /path HTTP/version

Contoh lengkap:
GET / HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0 Firefox/87.0
Referer: https://google.com
[baris kosong] ← wajib untuk menandai akhir request

Line 1 : Method + Path + HTTP Version
Line 2+ : Headers (informasi tambahan)
Line terakhir : Baris kosong (penanda akhir)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTTP METHODS - WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GET    : Mengambil/membaca data dari server
         Contoh: buka halaman web, download gambar
         Paling sering digunakan untuk browsing biasa

POST   : Mengirim data ke server → MEMBUAT record baru
         Contoh: submit form registrasi, kirim komentar
         Data dikirim di body request (tidak terlihat di URL)

PUT    : Mengirim data ke server → UPDATE data yang sudah ada
         Contoh: edit profil, update artikel blog

DELETE : Menghapus data dari server
         Contoh: hapus akun, hapus postingan

Pemetaan CRUD:
GET    = Read (baca)
POST   = Create (buat baru)
PUT    = Update (ubah yang ada)
DELETE = Delete (hapus)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTTP STATUS CODES - KATEGORI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
100-199 : Information Response
          Request diterima sebagian, lanjutkan kirim
          Jarang digunakan sekarang

200-299 : Success ✓
          Request berhasil diproses

300-399 : Redirection ↪
          Client harus pindah ke URL lain

400-499 : Client Error ✗
          Ada kesalahan dari sisi client

500-599 : Server Error ⚠
          Ada masalah di sisi server

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 STATUS CODES YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SUCCESS:
200 OK       : Request berhasil sempurna
201 Created  : Resource baru berhasil dibuat (user baru, post baru)

REDIRECTION:
301 Moved Permanently : Halaman pindah permanen → update bookmark
302 Found            : Redirect sementara, bisa berubah lagi

CLIENT ERROR:
400 Bad Request     : Request salah/tidak lengkap
401 Not Authorised  : Belum login/autentikasi
403 Forbidden       : Tidak punya izin (meski sudah login)
404 Not Found       : Halaman tidak ditemukan
405 Method Not Allowed : Method salah (kirim GET, harusnya POST)

SERVER ERROR:
500 Internal Server Error : Server error, tidak tahu cara handle
503 Service Unavailable   : Server overload atau maintenance

Analogi 404:
> Seperti cari rumah nomor 404 di jalan yang hanya sampai nomor 300

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTTP HEADERS - REQUEST (Client → Server)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Host:
  Fungsi : Tentukan website mana yang diminta (1 server bisa host banyak site)
  Contoh : Host: tryhackme.com
  Penting: Tanpa ini, dapat website default server

User-Agent:
  Fungsi : Info browser & versi yang dipakai
  Contoh : User-Agent: Mozilla/5.0 Firefox/87.0
  Kenapa : Server bisa format halaman sesuai browser
           Beberapa fitur HTML/JS/CSS hanya ada di browser tertentu

Content-Length:
  Fungsi : Ukuran data yang dikirim (dalam bytes)
  Contoh : Content-Length: 348
  Kenapa : Server bisa validasi tidak ada data yang hilang

Accept-Encoding:
  Fungsi : Jenis kompresi yang didukung browser
  Contoh : Accept-Encoding: gzip, deflate, br
  Kenapa : Data bisa dikompres → lebih cepat dikirim via internet

Cookie:
  Fungsi : Kirim data yang disimpan sebelumnya ke server
  Contoh : Cookie: sessionid=abc123; username=john
  Kenapa : Server bisa "ingat" siapa kita (HTTP stateless)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTTP HEADERS - RESPONSE (Server → Client)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Set-Cookie:
  Fungsi : Perintah browser untuk simpan data ini
  Contoh : Set-Cookie: sessionid=xyz789; Path=/; Secure
  Kenapa : Data akan dikirim balik di request berikutnya

Cache-Control:
  Fungsi : Durasi simpan response di cache browser
  Contoh : Cache-Control: max-age=3600 (1 jam)
  Kenapa : Tidak perlu download ulang jika belum expired

Content-Type:
  Fungsi : Tipe data yang dikirim server
  Contoh : Content-Type: text/html; charset=UTF-8
           Content-Type: image/jpeg
           Content-Type: application/json
  Kenapa : Browser tahu cara render/proses data

Content-Encoding:
  Fungsi : Metode kompresi yang dipakai
  Contoh : Content-Encoding: gzip
  Kenapa : Browser tahu cara dekompresi data

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 COOKIES - CARA KERJA LENGKAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Potongan data kecil disimpan di komputer
Kenapa   : HTTP = stateless (tidak ingat request sebelumnya)
           Cookie = cara server "mengingat" kita

Alur kerja:
1. Client request halaman → GET /
2. Server kirim form login + Set-Cookie: (kosong)
3. Client isi form → POST /login dengan name=adam
4. Server set cookie → Set-Cookie: name=adam
5. Request selanjutnya → Client kirim Cookie: name=adam
6. Server baca cookie → tampilkan "Welcome back adam"

Kegunaan:
✓ Autentikasi (menyimpan session token)
✓ Personalisasi (bahasa, tema, preferensi)
✓ Tracking (analytics, iklan)
✓ Shopping cart (keranjang belanja)

Format cookie:
Cookie: key1=value1; key2=value2

Nilai cookie = biasanya TOKEN (kode rahasia)
BUKAN password dalam bentuk plaintext!

Lihat cookies:
Browser DevTools → Network tab → pilih request → tab Cookies

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PATH PARAMETER vs QUERY PARAMETER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PATH PARAMETER (RESTful URL):
Format   : /resource/id
Contoh   : /user/1, /blog/5, /product/123
Kegunaan : Identifikasi resource spesifik
Benefit  : Clean, SEO friendly, standar REST API
Struktur : Hierarki jelas (user → specific user)

QUERY PARAMETER (Query String):
Format   : /resource?key=value&key2=value2
Contoh   : /search?q=laptop&sort=price
           /users?role=admin&active=true
Kegunaan : Filtering, searching, optional parameters
Benefit  : Fleksibel untuk multiple filters

Kapan pakai:
Path → Identifikasi resource utama (/user/123)
Query → Filter, sort, search, optional data (?sort=name&limit=10)

Contoh kombinasi:
/products/smartphones?brand=samsung&price_max=5000000
         ↑ path param     ↑ query params

Analogi:
> Path = alamat rumah (Jl. Merdeka No. 5)
> Query = catatan tambahan (rumah pagar biru, ada pohon mangga)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTTP RESPONSE - STRUKTUR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Format:
HTTP/version StatusCode StatusMessage
Header1: value
Header2: value
[baris kosong]
[body/content]

Contoh:
HTTP/1.1 200 OK
Server: nginx/1.15.8
Date: Tue, 05 May 2026 10:52:47 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 252

<html>
<body>Welcome to TryHackMe</body>
</html>

Line 1 : HTTP version + Status Code + Message
Line 2+ : Response headers
Baris kosong : Pemisah header dengan body
Sisanya : Body (konten yang diminta)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Stateless       : HTTP tidak menyimpan riwayat request sebelumnya
                  Setiap request = berdiri sendiri
                  Solusi: pakai cookies/session

Protocol        : Aturan komunikasi antara client & server

Encryption      : Proses mengacak data agar tidak bisa dibaca pihak lain
                  HTTPS = HTTP + encryption

Request         : Permintaan dari client ke server

Response        : Jawaban dari server ke client

Header          : Metadata/info tambahan di request/response

Body            : Konten utama yang dikirim (form data, JSON, HTML, dll)

Session         : Periode waktu user aktif berinteraksi dengan aplikasi
                  Ditrack pakai session cookie

Token           : Kode unik sebagai bukti autentikasi
                  Lebih aman daripada simpan password di cookie

REST API        : Arsitektur web service menggunakan HTTP methods secara standar
                  GET=read, POST=create, PUT=update, DELETE=delete

Endpoint        : URL spesifik untuk akses resource tertentu
                  Contoh: /api/users, /api/products/123

MIME Type       : Format standar untuk Content-Type
                  Contoh: text/html, application/json, image/png

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERBEDAAN HTTP/1.0 vs HTTP/1.1 vs HTTP/2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HTTP/1.0 (1996):
- 1 request per connection → lambat
- Tidak ada Host header → sulit virtual hosting

HTTP/1.1 (1997): ← Paling umum saat ini
- Persistent connection (keep-alive)
- Host header wajib → 1 server bisa host banyak domain
- Chunked transfer encoding

HTTP/2 (2015):
- Multiplexing → banyak request paralel dalam 1 connection
- Binary protocol (bukan text)
- Server push
- Header compression
- JAUH lebih cepat dari HTTP/1.1

HTTP/3 (2022):
- Pakai QUIC (UDP) bukan TCP
- Lebih cepat & reliable untuk koneksi bermasalah

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TIPS UNTUK PENTEST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Selalu cek HTTP headers → bisa bocorkan info server/tech stack
✓ Perhatikan cookies → session token bisa dicuri (session hijacking)
✓ Test semua HTTP methods → kadang DELETE/PUT tidak diamankan
✓ Cek redirect chain → bisa ada open redirect vulnerability
✓ Analisa status codes → 403 vs 404 bisa bocorkan info
✓ Manipulasi query params → test for SQL injection, XSS
✓ Path traversal → coba /../../etc/passwd
✓ Pakai Burp Suite untuk intercept & modify HTTP traffic

Vulnerability umum terkait HTTP:
- Session Hijacking (curi cookie)
- CSRF (Cross-Site Request Forgery)
- HTTP Request Smuggling
- Open Redirect
- SSRF (Server-Side Request Forgery)
- Header Injection
- Cache Poisoning

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CHEAT SHEET PRAKTIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Lihat HTTP traffic:
Browser DevTools → Network tab
Burp Suite → Intercept ON
Wireshark → filter: http

Buat HTTP request manual:
curl -X GET https://example.com
curl -X POST -d "user=admin" https://example.com/login
curl -H "Cookie: session=abc123" https://example.com

Test dengan netcat:
nc example.com 80
GET / HTTP/1.1
Host: example.com
[tekan Enter 2x]

Common ports HTTP services:
80   → HTTP
443  → HTTPS
8080 → HTTP alternative
8443 → HTTPS alternative
3000 → Development server (Node.js)
5000 → Development server (Flask)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```