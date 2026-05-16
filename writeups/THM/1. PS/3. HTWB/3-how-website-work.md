```
=== How Websites Work - Resume Materi ===
[31 Jan 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONSEP DASAR WEB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cara Kerja : Browser membuat REQUEST → Internet → Web Server
             Server kirim RESPONSE (HTML, CSS, JS, images) → Browser render
Web Server : Komputer khusus yang menangani request dan kirim data balik
Komponen   : 
  • Front End (Client-Side) = Yang dilihat & interaksi user di browser
  • Back End (Server-Side)  = Server yang proses request & kirim response
Alur       : Request → DNS lookup → Server process → Response → Display

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTML (HyperText Markup Language)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi     : Bahasa untuk membangun STRUKTUR website
Struktur Dasar :
  <!DOCTYPE html>     → Deklarasi dokumen HTML5
  <html>              → Root element (semua elemen di dalamnya)
  <head>              → Info tentang halaman (title, meta, links)
  <body>              → Konten yang ditampilkan di browser
  <h1> sampai <h6>    → Heading (judul besar ke kecil)
  <p>                 → Paragraf

Tag Penting :
  <button>   → Tombol
  <img>      → Gambar
  <a>        → Link/hyperlink
  <form>     → Form input
  <input>    → Field input
  <div>      → Container/divider
  <span>     → Inline container

Attributes (Atribut) :
  class="..."    → Untuk styling CSS (bisa dipakai banyak elemen)
  id="..."       → Identifier UNIK (hanya 1 elemen, untuk JS & styling)
  src="..."      → Lokasi file (gambar, script)
  name="..."     → Nama elemen (untuk form)
  type="..."     → Tipe input (text, password, button)

Tips View Source : Klik kanan → "View Page Source" / "Show Page Source"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CSS (Cascading Style Sheets)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi     : Membuat website CANTIK & menarik (styling & layout)
Kegunaan   : Warna, font, ukuran, spacing, posisi, animasi, responsive design
Cara Pakai : 
  • Inline    : <p style="color: red;">
  • Internal  : <style> di dalam <head>
  • External  : <link rel="stylesheet" href="style.css">

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 JAVASCRIPT (JS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi     : Membuat website INTERAKTIF & dinamis
Tanpa JS   : Website = statis, tidak ada interaksi real-time
Dengan JS  : Website bisa update konten, animasi, validasi form, fetch data

Cara Tambah JS :
  1. Di dalam halaman :
     <script>
       // kode JS di sini
     </script>
  
  2. File eksternal :
     <script src="/location/of/javascript_file.js"></script>

Contoh Kode :
  • Ubah konten :
    document.getElementById("demo").innerHTML = "Hack the Planet";
  
  • Event handling :
    <button onclick='alert("Clicked!")'>Click Me!</button>

Events Penting :
  onclick    → Saat diklik
  onhover    → Saat mouse di atas elemen
  onload     → Saat halaman selesai load
  onchange   → Saat nilai input berubah
  onsubmit   → Saat form disubmit

Fungsi JS  :
  • getElementById()     → Cari elemen berdasarkan ID
  • querySelector()      → Cari elemen dengan CSS selector
  • addEventListener()   → Tambah event listener
  • fetch()              → Ambil data dari API

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SENSITIVE DATA EXPOSURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi   : Website tidak protect/hapus informasi sensitif di source code
Risiko     : Login credentials, hidden links, API keys terekspos
Lokasi     : Biasa ditemukan di HTML comments, JavaScript code
Cara Cek   : View Page Source → cari credentials/links tersembunyi

Contoh Vulnerable :
  <!-- TODO: remove test credentials admin:password123 -->

Dampak     : Attacker bisa login, akses backend, curi data
Pencegahan : 
  • Hapus semua test credentials sebelum production
  • Jangan simpan password/API key di frontend
  • Review source code sebelum deploy
  • Gunakan environment variables untuk data sensitif

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTML INJECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi   : Vulnerability saat unfiltered user input ditampilkan di halaman
Cara Kerja : User input HTML/JS → tidak disanitasi → browser eksekusi
Bahaya     : Attacker kontrol tampilan & fungsionalitas halaman (XSS)

Contoh Vulnerable Code :
  function sayHi() {
    const name = document.getElementById("name").value;
    document.getElementById("welcome-msg").innerHTML = "Welcome " + name;
  }
  // User bisa input: <h1>Hacked!</h1> atau <script>alert('XSS')</script>

Aturan Emas : "NEVER TRUST USER INPUT"

Cara Sanitasi Input :
  ✅ Opsi 1 - Gunakan textContent (PALING AMAN) :
     element.textContent = userInput;  // Auto-escape HTML tags
  
  ✅ Opsi 2 - Escape HTML Manual :
     function escapeHTML(text) {
       const div = document.createElement('div');
       div.textContent = text;
       return div.innerHTML;  // Ubah < jadi &lt; dan > jadi &gt;
     }
  
  ✅ Opsi 3 - Filter/Validasi Input :
     function sanitizeInput(input) {
       return input.replace(/[^a-zA-Z0-9 ]/g, '');  // Hapus karakter special
     }

Vulnerability Serupa :
  • SQL Injection       → Manipulasi database query
  • Command Injection   → Eksekusi command di server
  • XSS (Cross-Site Scripting) → Inject malicious script

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KOMPONEN TAMBAHAN WEB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. LOAD BALANCER
   Fungsi     : Distribusi traffic ke multiple servers
   Kegunaan   : High availability, failover otomatis
   Algoritma  :
     • Round-robin  → Kirim request ke server secara bergiliran
     • Weighted     → Kirim ke server yang paling tidak sibuk
   Health Check : Cek server secara berkala, stop traffic jika server down

2. CDN (Content Delivery Network)
   Fungsi     : Host file statis (JS, CSS, images, videos) di banyak server
   Kegunaan   : Kurangi traffic, percepat loading dari server terdekat
   Cara Kerja : User request file → CDN cari server terdekat → kirim dari sana

3. DATABASE
   Fungsi     : Simpan & ambil data user/aplikasi
   Jenis      : 
     • Relational  : MySQL, PostgreSQL, MSSQL
     • NoSQL       : MongoDB, Redis
     • File-based  : SQLite, plain text
   Kegunaan   : User accounts, posts, transactions, logs

4. WAF (Web Application Firewall)
   Fungsi     : Protect webserver dari hacking & DoS attacks
   Posisi     : Di antara user request dan web server
   Cara Kerja : 
     • Analisa request untuk attack patterns
     • Deteksi bot vs real browser
     • Rate limiting (batasi request per IP)
     • Block malicious request sebelum sampai server

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 WEB SERVER DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi    : Software yang listen koneksi & kirim web content via HTTP
Software    : Apache, Nginx, IIS, NodeJS

Root Directory (Default Location) :
  • Linux (Apache/Nginx) : /var/www/html
  • Windows (IIS)        : C:\inetpub\wwwroot

Cara Kerja Request :
  Request : http://example.com/picture.jpg
  Server kirim : /var/www/html/picture.jpg dari hard drive

Virtual Hosts :
  Fungsi     : 1 web server host MULTIPLE websites (beda domain)
  Cara Kerja : Cek hostname dari HTTP headers → match ke virtual host config
  Mapping    :
    one.com → /var/www/website_one
    two.com → /var/www/website_two
  No Limit   : Tidak ada batas jumlah website di 1 server

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 STATIC vs DYNAMIC CONTENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STATIC Content :
  Definisi   : Konten yang TIDAK PERNAH berubah
  Contoh     : Images, CSS, JavaScript files, HTML statis
  Cara Kerja : File disajikan LANGSUNG dari webserver tanpa perubahan

DYNAMIC Content :
  Definisi   : Konten yang BISA BERUBAH per request
  Contoh     : 
    • Blog homepage (update saat ada post baru)
    • Search results (beda per keyword)
    • User dashboard (beda per user)
  Cara Kerja : Diproses di BACKEND sebelum dikirim ke browser

Backend vs Frontend :
  • Backend  : Proses di server (tidak terlihat user), pakai programming language
  • Frontend : Yang ditampilkan di browser (HTML hasil proses backend)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 BACKEND LANGUAGES & SCRIPTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Bahasa Backend : PHP, Python, Ruby, NodeJS, Perl, Java, C#, Go

Kemampuan Backend :
  • Interact dengan database
  • Call external APIs/services
  • Process user input
  • Generate dynamic HTML
  • Handle authentication
  • Business logic processing

Contoh PHP :
  Request  : http://example.com/index.php?name=adam
  
  Kode PHP :
    <html><body>Hello <?php echo $_GET["name"]; ?></body></html>
  
  Output ke client :
    <html><body>Hello adam</body></html>

PENTING : User TIDAK LIHAT kode backend (hanya lihat hasil HTML)
          Ini buka security risks jika backend tidak aman!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR LENGKAP REQUEST WEBSITE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Request website in browser
   User ketik URL atau klik link
   
2. DNS Lookup (Find server IP address)
   DNS ubah domain name → IP address
   Contoh: google.com → 142.250.185.46
   
3. Connect to webserver via HTTP
   Browser kirim HTTP request ke server
   Server proses & kirim back: HTML, CSS, JS, images
   
4. Browser render & display
   Browser gunakan data untuk format & tampilkan website
   
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HTTP Protocol    = Set of commands untuk browser-server communication
DNS              = Domain Name System (ubah domain → IP address)
Request          = Permintaan dari browser ke server
Response         = Data yang dikirim server ke browser
Root Directory   = Folder utama tempat web files disimpan
Virtual Host     = Config untuk host multiple websites di 1 server
Static Content   = File yang tidak berubah (images, CSS, JS)
Dynamic Content  = Konten yang generated per request (blog, search)
Frontend         = Apa yang dilihat user di browser (client-side)
Backend          = Proses di server yang tidak terlihat user (server-side)
Sanitization     = Proses membersihkan user input dari kode berbahaya
XSS              = Cross-Site Scripting (inject malicious script)
innerHTML        = Property JS yang SET HTML (berbahaya jika tidak sanitasi)
textContent      = Property JS yang SET text (aman, auto-escape HTML)
Event            = Aksi yang trigger JavaScript (click, hover, submit)
Attribute        = Property tambahan di HTML tag (id, class, src)
Rate Limiting    = Batasi jumlah request per IP dalam waktu tertentu
Failover         = Backup otomatis saat server utama down
Health Check     = Periodic check apakah server masih running
CDN              = Content Delivery Network (distribute files globally)
Load Balancer    = Distribusi traffic ke multiple servers
WAF              = Web Application Firewall (protect dari attacks)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SECURITY BEST PRACTICES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ SELALU sanitasi user input sebelum display/proses
✅ Gunakan textContent (bukan innerHTML) untuk user input
✅ Hapus credentials & sensitive data dari source code
✅ Review page source sebelum production deploy
✅ Gunakan environment variables untuk API keys
✅ Implement rate limiting untuk prevent DoS
✅ Gunakan HTTPS (bukan HTTP) untuk encrypt data
✅ Validate & filter input di client DAN server side
✅ Implement WAF untuk protect dari common attacks
✅ Regular security audit & penetration testing

❌ JANGAN simpan password di frontend code
❌ JANGAN trust user input tanpa validasi
❌ JANGAN pakai innerHTML untuk user-generated content
❌ JANGAN expose API keys/credentials di source code
❌ JANGAN lupa hapus test credentials sebelum production
```