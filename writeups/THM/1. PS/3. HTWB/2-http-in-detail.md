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
📌 CONTENT-TYPE UMUM (MIME TYPES)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEXT:
text/html              → HTML document
text/plain             → Plain text
text/css               → CSS stylesheet
text/javascript        → JavaScript code
text/csv               → CSV file

APPLICATION:
application/json       → JSON data (API responses)
application/xml        → XML document
application/pdf        → PDF file
application/zip        → ZIP archive
application/x-www-form-urlencoded → Form data (default POST)
multipart/form-data    → Form dengan file upload

IMAGE:
image/jpeg             → JPEG image
image/png              → PNG image
image/gif              → GIF image
image/svg+xml          → SVG vector image
image/webp             → WebP image

VIDEO/AUDIO:
video/mp4              → MP4 video
audio/mpeg             → MP3 audio
audio/wav              → WAV audio

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTTP HEADER SECURITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Security Headers (Server → Client):

Strict-Transport-Security (HSTS):
  Fungsi : Paksa browser selalu pakai HTTPS
  Contoh : Strict-Transport-Security: max-age=31536000
  Benefit: Cegah downgrade attack ke HTTP

X-Frame-Options:
  Fungsi : Cegah clickjacking
  Contoh : X-Frame-Options: DENY
  Benefit: Website tidak bisa ditampilkan dalam iframe

X-Content-Type-Options:
  Fungsi : Cegah MIME sniffing
  Contoh : X-Content-Type-Options: nosniff
  Benefit: Browser harus ikuti Content-Type yang dideklarasi

Content-Security-Policy (CSP):
  Fungsi : Kontrol resource mana yang boleh dimuat
  Contoh : Content-Security-Policy: default-src 'self'
  Benefit: Cegah XSS attack

X-XSS-Protection:
  Fungsi : Aktifkan XSS filter browser (deprecated)
  Contoh : X-XSS-Protection: 1; mode=block
  Note   : Diganti dengan CSP yang lebih powerful

Referrer-Policy:
  Fungsi : Kontrol informasi referer yang dikirim
  Contoh : Referrer-Policy: no-referrer
  Benefit: Privacy protection

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTTP AUTHENTICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Basic Authentication:
  Format : Authorization: Basic base64(username:password)
  Contoh : Authorization: Basic YWRtaW46cGFzcw==
  Kelemahan: Password encoded (BUKAN encrypted)
             Mudah di-decode
             Harus pakai HTTPS!

Bearer Token:
  Format : Authorization: Bearer <token>
  Contoh : Authorization: Bearer eyJhbGc...
  Kegunaan: API authentication, OAuth 2.0
  Benefit : Token bisa di-revoke, ada expiry

Digest Authentication:
  Format : Authorization: Digest username="admin"...
  Benefit: Password di-hash, lebih aman dari Basic
  Jarang dipakai sekarang, diganti OAuth/JWT

API Key:
  Format : X-API-Key: abc123def456
          atau di query: /api/data?api_key=abc123
  Kegunaan: Simple API authentication
  Kelemahan: Tidak ada expiry otomatis

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CORS (Cross-Origin Resource Sharing)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Mekanisme izinkan/blokir request dari domain berbeda
Kenapa   : Browser block AJAX request ke domain lain (security)

Origin = protocol + domain + port
Contoh:
- https://example.com:443  → 1 origin
- http://example.com:80    → origin berbeda (protocol beda)
- https://api.example.com  → origin berbeda (subdomain beda)

Headers CORS:

Request (Preflight):
Origin: https://frontend.com
Access-Control-Request-Method: POST
Access-Control-Request-Headers: Content-Type

Response:
Access-Control-Allow-Origin: https://frontend.com
Access-Control-Allow-Methods: GET, POST, PUT
Access-Control-Allow-Headers: Content-Type
Access-Control-Allow-Credentials: true
Access-Control-Max-Age: 86400

Wildcard berbahaya:
Access-Control-Allow-Origin: *  ← JANGAN di production!
Kenapa: Semua domain bisa akses API Anda

Pentest tip:
✓ Cek apakah CORS terlalu permissive
✓ Test dengan Origin berbeda
✓ Cek apakah credentials diizinkan + wildcard origin

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CACHING MECHANISM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cache-Control directives:

no-store
  → Jangan simpan cache SAMA SEKALI
  Untuk: data sensitif, banking

no-cache
  → Boleh simpan tapi harus validasi dulu sebelum pakai
  Untuk: data yang sering berubah

public
  → Boleh di-cache di shared cache (CDN, proxy)
  Untuk: static assets (CSS, JS, images)

private
  → Hanya boleh di-cache di browser user
  Untuk: data personal user

max-age=3600
  → Cache valid selama 3600 detik (1 jam)
  Setelah itu harus request ulang

must-revalidate
  → Setelah expired, WAJIB revalidasi ke server

Contoh kombinasi:
Cache-Control: public, max-age=31536000, immutable
→ File statis yang tidak akan pernah berubah (versioned assets)

Cache-Control: private, no-cache, no-store, must-revalidate
→ Data sangat sensitif (banking, medical)

Cache-Control: public, max-age=3600, must-revalidate
→ News article (cache 1 jam)

ETag & Last-Modified:
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
Last-Modified: Tue, 05 May 2026 10:52:47 GMT
→ Untuk conditional request (304 Not Modified)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTTP/2 PUSH & MULTIPLEXING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Server Push:
  Server kirim resource SEBELUM diminta client
  Contoh: Request HTML → server push CSS & JS sekalian
  Benefit: Lebih cepat, mengurangi round-trip

Multiplexing:
  Multiple request/response paralel dalam 1 TCP connection
  HTTP/1.1: 1 request → tunggu response → request lagi
  HTTP/2  : kirim 10 request sekaligus → terima parallel

Stream Prioritization:
  Resource penting (CSS) dapat prioritas lebih tinggi
  Resource tidak kritis (analytics) prioritas rendah

Header Compression:
  HPACK algorithm → kompres header
  Benefit: Header sering berulang, kompresi hemat bandwidth

Binary Protocol:
  HTTP/1.1: text-based
  HTTP/2  : binary-based → lebih efisien parsing

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SESSION vs TOKEN AUTHENTICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SESSION-BASED (Cookie):
1. User login → server buat session ID
2. Session ID disimpan di cookie
3. Server simpan session data di memory/database
4. Setiap request → server lookup session ID

Pros:
✓ Session bisa di-revoke instant dari server
✓ Data session tidak perlu dikirim tiap request
✓ Built-in di banyak framework

Cons:
✗ Tidak scalable (butuh shared session storage)
✗ Tidak cocok untuk microservices
✗ CSRF vulnerability (butuh CSRF token)

TOKEN-BASED (JWT):
1. User login → server generate JWT token
2. Token disimpan di localStorage/sessionStorage
3. Setiap request → kirim token di Authorization header
4. Server verify signature token (stateless)

Pros:
✓ Stateless → sangat scalable
✓ Cocok untuk API & microservices
✓ Cross-domain friendly
✓ Mobile-friendly

Cons:
✗ Tidak bisa revoke sebelum expiry (kecuali pakai blacklist)
✗ Token size lebih besar dari session ID
✗ XSS vulnerability jika simpan di localStorage

JWT Structure:
header.payload.signature

Contoh:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJ1c2VyIjoiYWRtaW4iLCJleHAiOjE2MjAw...
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 COMPRESSION ALGORITHMS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
gzip:
  Paling umum digunakan
  Kompresi ratio: baik
  Speed: cepat
  Support: hampir semua browser

deflate:
  Jarang digunakan
  Predecessor dari gzip
  Support: legacy browser

br (Brotli):
  Modern algorithm dari Google
  Kompresi ratio: TERBAIK (15-25% lebih kecil dari gzip)
  Speed: lebih lambat saat compress, cepat saat decompress
  Support: browser modern only
  Cocok: static assets

compress:
  Deprecated
  Jangan digunakan

Request header:
Accept-Encoding: gzip, deflate, br

Response header:
Content-Encoding: br

Tip untuk pentest:
✓ Cek apakah compression diaktifkan (performance issue)
✓ Test BREACH attack (jika HTTPS + compression + secret di response)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 REDIRECT TYPES & SECURITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Redirect Status Codes:

301 Moved Permanently:
  Search engine update index
  Browser cache redirect
  Use case: domain migration

302 Found (Temporary):
  Search engine tidak update index
  Browser tidak cache
  Use case: maintenance redirect

303 See Other:
  Setelah POST, redirect ke GET
  Use case: form submission

307 Temporary Redirect:
  Seperti 302 tapi preserve HTTP method
  POST tetap POST setelah redirect

308 Permanent Redirect:
  Seperti 301 tapi preserve HTTP method

Open Redirect Vulnerability:
URL: /redirect?url=https://evil.com
→ User dikira redirect internal, ternyata ke situs phishing

Cara test:
1. Cari parameter redirect/return/callback/next
2. Isi dengan URL eksternal
3. Cek apakah aplikasi validasi domain

Secure redirect:
✓ Whitelist domain yang diizinkan
✓ Validasi URL dimulai dengan /
✓ Gunakan indirect reference (ID bukan URL langsung)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 RATE LIMITING & THROTTLING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Response Headers:

X-RateLimit-Limit: 100
  → Maksimal request per window

X-RateLimit-Remaining: 45
  → Sisa quota request

X-RateLimit-Reset: 1620000000
  → Timestamp reset quota (Unix timestamp)

Retry-After: 60
  → Tunggu 60 detik sebelum retry

Status code saat limit exceeded:
429 Too Many Requests

Strategi rate limiting:

Fixed Window:
  100 request per jam
  Reset setiap jam tepat (misalnya jam 13:00, 14:00)

Sliding Window:
  100 request per 60 menit terakhir
  Lebih smooth, tidak ada spike saat reset

Token Bucket:
  Bucket diisi token dengan rate tetap
  Request consume token
  Flexible untuk burst traffic

Leaky Bucket:
  Request masuk queue
  Diproses dengan rate konstan
  Smooth traffic

Pentest tip:
✓ Cek apakah ada rate limiting (brute force protection)
✓ Test bypass: rotate IP, user-agent, cookies
✓ Cek apakah limit per IP atau per user
✓ Perhatikan header X-RateLimit untuk planning attack

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTTP METHOD TAMPERING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HTTP Verb Tampering:

Skenario:
DELETE /api/user/123 → 403 Forbidden (tidak punya akses)

Bypass attempt:
1. Ganti ke POST dengan header:
   X-HTTP-Method-Override: DELETE
   atau
   X-Method-Override: DELETE

2. Gunakan _method parameter:
   POST /api/user/123?_method=DELETE

3. Try alternative methods:
   PATCH, PUT, HEAD, OPTIONS, TRACE

Real case:
GET /admin → 403 Forbidden
POST /admin → 200 OK (bypass!)

HEAD method:
  Seperti GET tapi tidak return body
  Berguna untuk cek resource exists tanpa download
  Bisa bypass security check yang hanya cek body

OPTIONS method:
  Tanya server method apa yang diizinkan
  Response: Allow: GET, POST, PUT, DELETE
  Info disclosure: tahu method available

TRACE method:
  Echo back request yang diterima server
  Vulnerability: HTTP TRACE XSS
  Seharusnya disabled!

Pentest checklist:
✓ Test semua HTTP methods (bukan hanya GET/POST)
✓ Cek method override headers
✓ Cari endpoint yang tidak validasi method properly
✓ Test TRACE untuk XSS
✓ Gunakan OPTIONS untuk recon

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CHUNKED TRANSFER ENCODING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kenapa chunked encoding:
- Server tidak tahu Content-Length di awal
- Streaming response (live data)
- Server-Sent Events (SSE)

Header:
Transfer-Encoding: chunked

Format:
[size in hex]\r\n
[data]\r\n
[size in hex]\r\n
[data]\r\n
0\r\n
\r\n

Contoh:
4\r\n
Wiki\r\n
5\r\n
pedia\r\n
0\r\n
\r\n

Result: "Wikipedia"

HTTP Request Smuggling:
Vulnerability saat proxy & backend berbeda parsing chunked
Content-Length: 49
Transfer-Encoding: chunked

→ Proxy pakai Content-Length, Backend pakai Transfer-Encoding
→ Request bisa "diselundupkan" (smuggling)

Attack vector:
CL.TE: Proxy pakai CL, Backend pakai TE
TE.CL: Proxy pakai TE, Backend pakai CL
TE.TE: Keduanya pakai TE, tapi parsing berbeda

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SAME-ORIGIN POLICY (SOP)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Browser security policy
           Script di satu origin tidak bisa akses data di origin lain

Origin = scheme + host + port

Contoh:
https://example.com:443  ← Origin A
https://example.com:8443 ← Origin B (port beda)
http://example.com:443   ← Origin C (scheme beda)
https://api.example.com  ← Origin D (host beda)

Yang di-block SOP:
✗ XMLHttpRequest / Fetch API ke origin lain
✗ Read cookies dari origin lain
✗ Access DOM dari iframe origin lain
✗ Read localStorage/sessionStorage origin lain

Yang TIDAK di-block:
✓ Embed images: <img src="https://other.com/pic.jpg">
✓ Embed scripts: <script src="https://cdn.com/lib.js"></script>
✓ Embed CSS: <link href="https://other.com/style.css">
✓ Form submission: <form action="https://other.com">
✓ Redirect: window.location = "https://other.com"

Bypass SOP (legitimate):
- CORS headers
- JSONP (deprecated)
- PostMessage API
- document.domain (same-site)

Vulnerability:
- CORS misconfiguration
- Postmessage XSS
- JSONP hijacking

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 WEBSOCKET vs HTTP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HTTP:
- Request-Response model
- Stateless
- Half-duplex (satu arah per waktu)
- Overhead besar (header tiap request)

WebSocket:
- Full-duplex (dua arah simultan)
- Persistent connection
- Low overhead setelah handshake
- Real-time communication

WebSocket Handshake (HTTP Upgrade):

Client:
GET /chat HTTP/1.1
Host: example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Sec-WebSocket-Version: 13

Server:
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=

Setelah handshake → persistent connection

Use case:
- Chat application
- Live notifications
- Real-time gaming
- Stock ticker
- Collaborative editing

Security concern:
✓ WebSocket tidak respect SOP
✓ Harus implement CORS-like origin check
✓ Vulnerable to CSRF jika tidak ada token validation
✓ Man-in-the-middle jika tidak pakai WSS (WebSocket Secure)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 RANGKUMAN AKHIR - MIND MAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HTTP REQUEST:
├── Request Line: METHOD /path HTTP/version
├── Headers: Host, User-Agent, Cookie, Content-Type, dll
├── Blank Line (wajib)
└── Body (opsional, untuk POST/PUT)

HTTP RESPONSE:
├── Status Line: HTTP/version CODE Message
├── Headers: Set-Cookie, Content-Type, Cache-Control, dll
├── Blank Line (wajib)
└── Body (HTML, JSON, Image, dll)

SECURITY CHECKLIST:
├── HTTPS (encryption)
├── Security Headers (CSP, HSTS, X-Frame-Options)
├── CORS properly configured
├── Rate limiting
├── Session management (secure cookies)
├── Input validation
├── Method validation (tidak hanya GET/POST)
└── Proper authentication & authorization

TESTING TOOLS:
├── Browser DevTools
├── Burp Suite
├── curl / httpie
├── Postman
└── Wireshark

COMMON VULNERABILITIES:
├── CSRF
├── XSS
├── Session Hijacking
├── Open Redirect
├── SSRF
├── HTTP Request Smuggling
├── Header Injection
├── CORS Misconfiguration
├── Method Tampering
└── Cache Poisoning

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```