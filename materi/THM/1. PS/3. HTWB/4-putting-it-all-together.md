```
=== How Websites Work - Resume Materi ===
[31 Jan 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONSEP DASAR WEB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cara Kerja : Browser buat REQUEST → Internet → Web Server
             Server kirim RESPONSE (HTML, CSS, JS, images) → Browser render
Web Server : Komputer khusus yang handle request & kirim data balik
Komponen   : 
  • Front End (Client-Side) = Yang dilihat & interaksi user di browser
  • Back End (Server-Side)  = Server yang proses request & kirim response
Alur Utama : Request → DNS lookup → Server process → Response → Display
Kecepatan  : Semua proses terjadi dalam hitungan DETIK

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DNS (Domain Name System)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi     : Ubah domain name → IP address
Contoh     : google.com → 142.250.185.46
Analogi    : Seperti buku telepon internet
Proses     : Browser tidak tahu IP server → tanya DNS → dapat IP → connect
Penting    : Tanpa DNS, kita harus hapal IP address semua website

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTTP PROTOCOL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi   : Set of commands untuk browser-server communication
Fungsi     : Atur cara request & response dikirim antara client-server
HTTPS      : HTTP + Security (data dienkripsi)
Port       : HTTP = port 80, HTTPS = port 443

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTML (HyperText Markup Language)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi     : Bahasa untuk bangun STRUKTUR website
Analogi    : HTML = kerangka bangunan

Struktur Dasar :
  <!DOCTYPE html>     → Deklarasi dokumen HTML5
  <html>              → Root element (semua di dalamnya)
  <head>              → Info halaman (title, meta, CSS/JS links)
  <body>              → Konten yang ditampilkan browser
  
Tag Heading :
  <h1> ... <h6>       → Heading (h1=terbesar, h6=terkecil)

Tag Konten :
  <p>                 → Paragraf
  <a href="">         → Link/hyperlink
  <img src="">        → Gambar
  <button>            → Tombol
  <div>               → Container/divider
  <span>              → Inline container
  <form>              → Form input
  <input>             → Field input
  <ul>, <ol>, <li>    → Unordered/Ordered list & list item

Attributes (Atribut) :
  class="..."    → Untuk styling CSS (bisa banyak elemen)
  id="..."       → Identifier UNIK (cuma 1 elemen, untuk JS & CSS)
  src="..."      → Lokasi file (gambar, script, dll)
  href="..."     → URL tujuan (untuk link)
  name="..."     → Nama elemen (untuk form)
  type="..."     → Tipe input (text, password, email, button)
  value="..."    → Nilai default input

View Source : Klik kanan → "View Page Source" / "Show Page Source"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CSS (Cascading Style Sheets)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi     : Buat website CANTIK & menarik (styling & layout)
Analogi    : CSS = cat & dekorasi bangunan
Kegunaan   : Warna, font, ukuran, spacing, posisi, animasi, responsive

Cara Pakai :
  1. Inline    : <p style="color: red;">Text</p>
  2. Internal  : <style> di dalam <head>
  3. External  : <link rel="stylesheet" href="style.css">

Contoh :
  p { color: blue; font-size: 16px; }
  .classname { background: yellow; }
  #idname { margin: 10px; }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 JAVASCRIPT (JS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi     : Buat website INTERAKTIF & dinamis
Analogi    : JS = sistem listrik & otomasi bangunan
Tanpa JS   : Website = statis, tidak ada interaksi real-time
Dengan JS  : Website bisa update konten, animasi, validasi, fetch data

Cara Tambah :
  1. Inline    : <script>kode JS</script>
  2. External  : <script src="file.js"></script>

Method Penting :
  getElementById("id")           → Cari elemen by ID
  querySelector("selector")      → Cari elemen by CSS selector
  addEventListener("event", fn)  → Tambah event listener
  innerHTML                      → Get/set HTML content (BAHAYA!)
  textContent                    → Get/set text content (AMAN)
  fetch(url)                     → Ambil data dari API

Events Umum :
  onclick     → Saat diklik
  onhover     → Saat mouse di atas
  onload      → Saat halaman selesai load
  onchange    → Saat nilai input berubah
  onsubmit    → Saat form disubmit
  onkeypress  → Saat keyboard ditekan

Contoh Kode :
  // Ubah konten
  document.getElementById("demo").innerHTML = "New Text";
  
  // Event handling
  <button onclick="alert('Clicked!')">Click</button>
  
  // Fungsi
  function sayHi(name) {
    alert("Hello " + name);
  }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TIGA PILAR WEB (WAJIB HAPAL!)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HTML = STRUKTUR (kerangka bangunan)
CSS  = STYLING (cat & dekorasi)
JS   = INTERAKTIVITY (sistem otomasi)

Ketiga-tiganya SELALU bekerja BERSAMA dalam website modern!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SENSITIVE DATA EXPOSURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi   : Website tidak protect/hapus info sensitif di source code
Risiko     : Login credentials, hidden links, API keys terekspos
Lokasi     : HTML comments, JavaScript code, hidden inputs
Cara Cek   : View Page Source → cari credentials/secrets

Contoh Vulnerable :
  <!-- TODO: remove test credentials admin:password123 -->
  <input type="hidden" value="API_KEY_12345">
  // var apiKey = "secret123";

Dampak :
  • Attacker bisa login ke sistem
  • Akses backend components
  • Curi data sensitif
  • Lateral movement ke sistem lain

Pencegahan :
  ✅ Hapus SEMUA test credentials sebelum production
  ✅ JANGAN simpan password/API key di frontend
  ✅ Review source code sebelum deploy
  ✅ Pakai environment variables untuk secrets
  ✅ Implement proper access control
  ✅ Regular security audit

ATURAN EMAS : "NEVER STORE SECRETS IN FRONTEND CODE"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTML INJECTION & XSS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi   : Vulnerability saat UNFILTERED user input ditampilkan
Penyebab   : Tidak ada input sanitization/validation
Dampak     : Attacker kontrol tampilan & fungsionalitas halaman

Cara Kerja Attack :
  1. User input data ke form
  2. Data tidak disanitasi
  3. Data ditampilkan di halaman via innerHTML
  4. Browser eksekusi HTML/JS yang diinject attacker

Contoh Vulnerable Code :
  function sayHi() {
    const name = document.getElementById("name").value;
    // BAHAYA: Langsung pakai innerHTML tanpa sanitasi
    document.getElementById("msg").innerHTML = "Welcome " + name;
  }

Contoh Attack :
  Input: <h1>Hacked!</h1>
  Input: <script>alert('XSS')</script>
  Input: <img src=x onerror="alert('XSS')">

ATURAN EMAS : "NEVER TRUST USER INPUT"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 INPUT SANITIZATION (WAJIB!)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Metode 1 - textContent (PALING AMAN & MUDAH) :
  ✅ function sayHi() {
       const name = document.getElementById("name").value;
       document.getElementById("msg").textContent = "Welcome " + name;
     }
  → textContent auto-escape HTML tags

Metode 2 - Escape HTML Manual :
  ✅ function escapeHTML(text) {
       const div = document.createElement('div');
       div.textContent = text;
       return div.innerHTML;
     }
     
     function sayHi() {
       const name = document.getElementById("name").value;
       const safe = escapeHTML(name);
       document.getElementById("msg").innerHTML = "Welcome " + safe;
     }
  → Ubah < jadi &lt; dan > jadi &gt;

Metode 3 - Filter/Validasi Input :
  ✅ function sanitize(input) {
       // Hanya izinkan huruf, angka, spasi
       return input.replace(/[^a-zA-Z0-9 ]/g, '');
     }
     
     function sayHi() {
       const name = sanitize(document.getElementById("name").value);
       document.getElementById("msg").innerHTML = "Welcome " + name;
     }

Metode 4 - Whitelist Allowed Tags (Advanced) :
  ✅ Pakai library seperti DOMPurify
     const clean = DOMPurify.sanitize(dirty);

BEST PRACTICE :
  • Sanitasi di CLIENT-SIDE DAN SERVER-SIDE
  • Pakai textContent untuk plain text
  • Pakai innerHTML HANYA untuk trusted content
  • Validate & filter semua input
  • Implement Content Security Policy (CSP)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KOMPONEN TAMBAHAN WEB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. LOAD BALANCER (Penyeimbang Beban)
   Fungsi     : Distribusi traffic ke multiple servers
   Kegunaan   : 
     • High availability (ketersediaan tinggi)
     • Failover otomatis jika server down
     • Handle traffic tinggi
   
   Algoritma :
     Round-robin → Kirim ke server secara bergiliran
     Weighted    → Kirim ke server paling tidak sibuk
     Least Conn  → Kirim ke server dengan koneksi paling sedikit
     IP Hash     → Request dari IP sama → server sama
   
   Health Check : Cek server berkala, stop traffic jika down
   Diagram      : Client → Load Balancer → Server 1/2/3

2. CDN (Content Delivery Network)
   Fungsi     : Host file STATIS di ribuan server worldwide
   File       : JavaScript, CSS, Images, Videos
   Cara Kerja : User request file → CDN kirim dari server TERDEKAT
   Keuntungan : 
     • Loading lebih CEPAT
     • Kurangi load server utama
     • Better user experience
     • DDoS protection
   
   Contoh CDN : Cloudflare, Akamai, AWS CloudFront, Fastly

3. DATABASE
   Fungsi     : Simpan & ambil data user/aplikasi
   
   Jenis Database :
     Relational (SQL) :
       • MySQL        → Open source, populer
       • PostgreSQL   → Advanced features
       • MSSQL        → Microsoft SQL Server
       • MariaDB      → Fork dari MySQL
     
     NoSQL :
       • MongoDB      → Document-based
       • Redis        → Key-value, in-memory
       • Cassandra    → Distributed
       • DynamoDB     → AWS managed
     
     File-based :
       • SQLite       → Embedded database
       • Plain text   → Simple storage
   
   Kegunaan : User accounts, posts, comments, transactions, logs

4. WAF (Web Application Firewall)
   Fungsi     : PROTECT webserver dari attacks
   Posisi     : Di antara user dan web server
   
   Proteksi Dari :
     • SQL Injection
     • XSS (Cross-Site Scripting)
     • CSRF (Cross-Site Request Forgery)
     • DDoS attacks
     • Bot traffic
     • Brute force attacks
   
   Cara Kerja :
     • Analisa request untuk attack patterns
     • Deteksi bot vs real browser
     • Rate limiting (batasi request per IP)
     • Block malicious request SEBELUM sampai server
   
   Rate Limiting : Max X request per detik dari 1 IP
   Contoh WAF    : Cloudflare WAF, AWS WAF, ModSecurity
   Diagram       : Client → WAF (firewall) → Web Server

Kesimpulan Komponen :
  Load Balancer → CEPAT & HANDAL
  CDN           → CEPAT & EFISIEN
  Database      → SIMPAN DATA
  WAF           → AMAN & TERLINDUNGI

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 WEB SERVER DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi    : SOFTWARE yang listen koneksi & kirim web content via HTTP

Software Populer :
  • Apache    → Open source, paling populer, Linux/Windows
  • Nginx     → High performance, reverse proxy, load balancing
  • IIS       → Internet Information Services (Windows only)
  • NodeJS    → JavaScript runtime, modern web apps
  • LiteSpeed → High performance, caching
  • Caddy     → Auto HTTPS, modern config

Root Directory (Lokasi Default File) :
  Linux  (Apache/Nginx) : /var/www/html
  Windows (IIS)         : C:\inetpub\wwwroot

Cara Kerja Request :
  Request user : http://example.com/picture.jpg
  Server kirim : /var/www/html/picture.jpg dari hard drive

Virtual Hosts :
  Fungsi     : 1 server host BANYAK website (beda domain)
  Cara Kerja : 
    1. Server cek HOSTNAME dari HTTP headers
    2. Match dengan virtual host config
    3. Jika match → serve website yang benar
    4. Jika tidak → serve default website
  
  Contoh Mapping :
    one.com → /var/www/website_one
    two.com → /var/www/website_two
  
  Limit : TIDAK ADA batas jumlah website per server

Config File :
  Apache : /etc/apache2/sites-available/
  Nginx  : /etc/nginx/sites-available/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 STATIC vs DYNAMIC CONTENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STATIC Content (Konten Statis) :
  Definisi   : Konten yang TIDAK PERNAH berubah
  Contoh     : Images, CSS, JavaScript files, HTML statis, PDFs
  Cara Kerja : File disajikan LANGSUNG dari server tanpa perubahan
  Kecepatan  : CEPAT (tidak perlu processing)
  Caching    : Mudah di-cache (CDN friendly)

DYNAMIC Content (Konten Dinamis) :
  Definisi   : Konten yang BISA BERUBAH per request
  Contoh     : 
    • Blog homepage (update saat ada post baru)
    • Search results (beda per keyword)
    • User dashboard (beda per user)
    • Shopping cart (beda per session)
    • Real-time data (stock prices, weather)
  
  Cara Kerja : Diproses di BACKEND sebelum dikirim
  Kecepatan  : Lebih lambat (butuh processing)
  Personalisasi : Bisa disesuaikan per user

Backend vs Frontend :
  Backend  : Proses di SERVER (tidak terlihat user)
           : Pakai programming/scripting languages
           : User TIDAK bisa lihat kode backend
  
  Frontend : Ditampilkan di BROWSER
           : HTML hasil dari proses backend
           : User bisa lihat via View Source

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 BACKEND LANGUAGES & SCRIPTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Backend Languages Populer :
  • PHP        → Web scripting, WordPress, Laravel
  • Python     → Django, Flask, FastAPI
  • JavaScript → NodeJS, Express, NestJS
  • Ruby       → Ruby on Rails
  • Java       → Spring Boot, Jakarta EE
  • C#         → ASP.NET, .NET Core
  • Go         → High performance, concurrency
  • Perl       → Legacy systems
  • Rust       → Performance & safety

Kemampuan Backend :
  ✅ Interact dengan database (CRUD operations)
  ✅ Call external APIs/services
  ✅ Process & validate user input
  ✅ Generate dynamic HTML
  ✅ Handle authentication & authorization
  ✅ Business logic processing
  ✅ File uploads & processing
  ✅ Email sending
  ✅ Payment processing
  ✅ Session management

Contoh PHP Sederhana :
  Request : http://example.com/index.php?name=adam
  
  File PHP :
    <html><body>
      Hello <?php echo $_GET["name"]; ?>
    </body></html>
  
  Output ke Browser :
    <html><body>Hello adam</body></html>

PENTING : 
  • User TIDAK LIHAT kode backend (cuma hasil HTML)
  • Kode backend jalan di SERVER
  • Security risk jika backend tidak aman!
  • Backend = tempat logika bisnis & data sensitif

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR LENGKAP REQUEST WEBSITE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 1 : REQUEST WEBSITE
  User    : Ketik URL atau klik link
  Browser : Siapkan HTTP request

Step 2 : DNS LOOKUP
  Browser : Tanya DNS server "IP address google.com apa?"
  DNS     : "IP-nya 142.250.185.46"
  Browser : Save IP address untuk connect

Step 3 : CONNECT TO SERVER
  Browser : Connect ke IP via HTTP/HTTPS protocol
  Browser : Kirim HTTP request (GET, POST, dll)
  Request berisi :
    • URL yang diminta
    • Headers (User-Agent, Cookies, dll)
    • Body (untuk POST request)

Step 4 : SERVER PROCESS
  Server  : Terima request
  Server  : Proses (jalankan backend code jika dynamic)
  Server  : Siapkan response (HTML, CSS, JS, images)

Step 5 : SERVER RESPONSE
  Server  : Kirim HTTP response
  Response berisi :
    • Status code (200, 404, 500, dll)
    • Headers (Content-Type, Cookies, dll)
    • Body (HTML, JSON, file, dll)

Step 6 : BROWSER RENDER
  Browser : Terima response
  Browser : Parse HTML
  Browser : Download CSS, JS, images yang referenced
  Browser : Execute JavaScript
  Browser : Render halaman ke layar

TOTAL WAKTU : Biasanya < 1 detik untuk website yang optimal!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTTP STATUS CODES (WAJIB HAPAL!)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2xx = SUCCESS
  200 OK              → Request berhasil
  201 Created         → Resource baru dibuat
  204 No Content      → Berhasil tapi tidak ada content

3xx = REDIRECTION
  301 Moved Permanently → URL pindah permanen
  302 Found            → Redirect sementara
  304 Not Modified     → Pakai cached version

4xx = CLIENT ERROR
  400 Bad Request     → Request salah format
  401 Unauthorized    → Perlu authentication
  403 Forbidden       → Tidak ada permission
  404 Not Found       → Halaman tidak ditemukan
  405 Method Not Allowed → Method tidak support

5xx = SERVER ERROR
  500 Internal Server Error → Error di server
  502 Bad Gateway     → Proxy/gateway error
  503 Service Unavailable → Server overload/maintenance
  504 Gateway Timeout → Proxy timeout

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTTP METHODS (WAJIB HAPAL!)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GET     → Ambil data (read-only, tidak ubah data)
POST    → Kirim data (create, bisa ubah data)
PUT     → Update data (replace entire resource)
PATCH   → Update sebagian data
DELETE  → Hapus data
HEAD    → Sama seperti GET tapi tanpa body
OPTIONS → Cek method yang di-support

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HTTP Protocol    = Set commands untuk browser-server communication
DNS              = Domain Name System (domain → IP address)
Request          = Permintaan dari browser ke server
Response         = Data yang dikirim server ke browser
Root Directory   = Folder utama tempat web files disimpan
Virtual Host     = Config untuk host multiple websites di 1 server
Static Content   = File yang tidak berubah
Dynamic Content  = Konten generated per request
Frontend         = Client-side (dilihat di browser)
Backend          = Server-side (proses di server)
Sanitization     = Bersihkan input dari kode berbahaya
XSS              = Cross-Site Scripting (inject malicious script)
innerHTML        = Set HTML (BAHAYA jika user input!)
textContent      = Set text (AMAN, auto-escape)
Event            = Trigger JavaScript (click, hover, submit)
Attribute        = Property di HTML tag (id, class, src)
Rate Limiting    = Batasi request per IP per waktu
Failover         = Backup otomatis saat server down
Health Check     = Cek berkala apakah server running
CDN              = Content Delivery Network (distribute files globally)
Load Balancer    = Distribusi traffic ke multiple servers
WAF              = Web Application Firewall (protect dari attacks)
API              = Application Programming Interface
CRUD             = Create, Read, Update, Delete
Session          = Data temporary per user
Cookie           = Data disimpan di browser
Cache            = Simpan sementara untuk akses cepat
SSL/TLS          = Enkripsi untuk HTTPS
Port             = Endpoint untuk komunikasi (HTTP=80, HTTPS=443)
Reverse Proxy    = Server perantara antara client-server
Vulnerability    = Kerentanan keamanan
Exploit          = Manfaatkan vulnerability untuk attack
Payload          = Data/code yang dikirim dalam attack

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SECURITY BEST PRACTICES (WAJIB!)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ SELALU sanitasi user input sebelum display/proses
✅ Gunakan textContent (bukan innerHTML) untuk user input
✅ Hapus credentials & secrets dari source code
✅ Review page source sebelum production
✅ Gunakan environment variables untuk API keys
✅ Implement rate limiting untuk prevent DoS
✅ Gunakan HTTPS (bukan HTTP) untuk encrypt data
✅ Validate & filter input di CLIENT DAN SERVER
✅ Implement WAF untuk protect dari attacks
✅ Regular security audit & penetration testing
✅ Keep software/dependencies updated
✅ Use strong authentication & authorization
✅ Implement proper error handling
✅ Log security events
✅ Backup data regularly

❌ JANGAN simpan password di frontend
❌ JANGAN trust user input tanpa validasi
❌ JANGAN pakai innerHTML untuk user content
❌ JANGAN expose API keys/credentials
❌ JANGAN lupa hapus test credentials
❌ JANGAN disable security features
❌ JANGAN ignore security warnings
❌ JANGAN use default passwords
❌ JANGAN expose detailed error messages
❌ JANGAN skip input validation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 COMMON WEB VULNERABILITIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Sensitive Data Exposure
   → Credentials/secrets di source code

2. HTML Injection / XSS
   → Unfiltered input ditampilkan di halaman

3. SQL Injection
   → Manipulasi database query

4. CSRF (Cross-Site Request Forgery)
   → Force user action tanpa sepengetahuan

5. Authentication Bypass
   → Lewati mekanisme login

6. Broken Access Control
   → Akses resource tanpa authorization

7. Security Misconfiguration
   → Default config, unnecessary features

8. Insecure Deserialization
   → Execute arbitrary code via serialized object

9. Using Components with Known Vulnerabilities
   → Library/framework versi lama yang vulnerable

10. Insufficient Logging & Monitoring
    → Tidak detect/respond terhadap attacks

Referensi : OWASP Top 10

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TOOLS UNTUK WEB SECURITY TESTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Browser DevTools : Inspect element, network, console
Burp Suite       : Web vulnerability scanner & proxy
OWASP ZAP        : Open source web app scanner
Nikto            : Web server scanner
SQLMap           : SQL injection testing
XSSer            : XSS detection & exploitation
Nmap             : Network & port scanning
Wireshark        : Network traffic analyzer
Postman          : API testing
curl/wget        : Command-line HTTP clients
```