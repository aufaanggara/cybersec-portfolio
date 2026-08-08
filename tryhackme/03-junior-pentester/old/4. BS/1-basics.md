```
=== Burp Suite Basics - Resume Materi ===
[19 Apr 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU BURP SUITE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Framework berbasis Java untuk web application penetration testing
Fungsi   : Menangkap, melihat, memodifikasi traffic HTTP/HTTPS antara
           browser dan web server
Status   : Standar industri untuk security assessment web & mobile app + API
Inti     : Burp Proxy — komponen paling fundamental di seluruh framework

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TIGA EDISI BURP SUITE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Community   → GRATIS, non-komersial, fitur terbatas
              Tools utama: Proxy, Repeater, Intruder (rate limited),
              Decoder, Comparer, Sequencer + BApp Store

Professional→ BERBAYAR (lisensi), unrestricted version
              Tambahan: automated vulnerability scanner, fuzzer/brute-forcer
              tanpa rate limit, saving projects, built-in API,
              unlimited extensions, Burp Collaborator

Enterprise  → BERBAYAR (lisensi), untuk continuous scanning
              Berjalan di SERVER, scan otomatis & berkala seperti Nessus
              Bukan untuk manual attack, tapi monitoring 24 jam

FOKUS MODUL INI → Community Edition

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FITUR UTAMA COMMUNITY EDITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Proxy      → Aspek paling terkenal. Intercept & modifikasi
             request/response antara browser dan server

Repeater   → Tangkap, modifikasi, kirim ulang request berkali-kali
             Berguna untuk: SQLi payload crafting, uji endpoint

Intruder   → Spray request ke banyak endpoint sekaligus
             Digunakan untuk: brute-force & fuzzing
             (rate limited di Community)

Decoder    → Transformasi data: decode/encode payload
             Format: URL, Base64, HTML, Hex, dll

Comparer   → Bandingkan 2 data di level kata atau byte
             Shortcut keyboard = sangat mempercepat proses

Sequencer  → Uji keacakan token (session cookie, random data)
             Jika randomness lemah = celah serangan besar

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 EKSTENSI & BAPP STORE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Extender   → Modul untuk load ekstensi ke framework
BApp Store → Marketplace ekstensi pihak ketiga (seperti App Store-nya Burp)
Bahasa     → Java, Python (Jython), Ruby (JRuby)
Contoh     → Logger++ : extend logging bawaan Burp
Catatan    → Beberapa ekstensi butuh lisensi Professional

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DASHBOARD — 4 KUADRAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Tasks          → Definisikan background tasks
                    Default: "Live Passive Crawl" (catat semua halaman dikunjungi)

2. Event Log      → Catat semua aksi Burp (proxy nyala, koneksi, dll)

3. Issue Activity → KHUSUS Professional
                    Tampilkan kerentanan dari automated scanner
                    Diurutkan berdasarkan severity & certainty

4. Advisory       → Detail kerentanan + referensi + saran remediasi
                    Bisa diekspor jadi laporan
                    (Tidak tampil di Community)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NAVIGASI BURP SUITE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Module Selection → Baris atas: pilih modul (Proxy, Target, dll)
Sub-tabs         → Baris kedua: opsi spesifik modul yang dipilih
Detach Tabs      → Window → Detach [nama tab] → buka di jendela terpisah

KEYBOARD SHORTCUTS:
Ctrl + Shift + D → Dashboard
Ctrl + Shift + T → Target tab
Ctrl + Shift + P → Proxy tab
Ctrl + Shift + I → Intruder tab
Ctrl + Shift + R → Repeater tab

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SETTINGS — DUA JENIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Global Settings  → Berlaku untuk seluruh instalasi Burp
(User Settings)    Tersimpan permanen, aktif setiap Burp dibuka

Project Settings → Hanya berlaku selama sesi berjalan
                   HILANG saat Burp ditutup (Community tidak support save project)

Cara akses : Klik tombol Settings di navigation bar atas
Menu kiri  : Search / Type filter (User|Project) / Categories

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 BURP PROXY — CARA KERJA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Alur     : Browser → Burp Proxy (127.0.0.1:8080) → Internet
Fungsi   : Intercept, view, modify request/response

Intercepting  → Request ditahan sebelum ke server
                Muncul di tab Proxy untuk: Forward/Drop/Edit/kirim ke modul lain
                Tombol "Intercept is on" = aktif menahan request

Taking Control→ Kendali penuh atas semua web traffic

Capture & Log → Burp SELALU catat semua request meski intercept OFF
                Berguna untuk analisis retrospektif

WebSocket     → Burp juga tangkap & catat komunikasi WebSocket

HTTP History  → Lihat semua request yang sudah lewat (sub-tab)
WS History    → Lihat semua WebSocket communication (sub-tab)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PROXY SETTINGS — FITUR NOTABLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Response Interception → Default: proxy TIDAK intercept response server
                        Aktifkan via checkbox + atur rules di Proxy settings
                        Rule contoh: "Request Was intercepted" = intercept response-nya

Match and Replace     → Gunakan regex untuk modifikasi request masuk/keluar
                        Contoh: ganti user agent, manipulasi cookies secara otomatis

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SETUP PROXY — FOXYPROXY (FIREFOX)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Install ekstensi FoxyProxy Basic di Firefox
2. Klik ikon FoxyProxy → Options → Add
3. Isi:  Title : Burp (bebas)
         IP    : 127.0.0.1
         Port  : 8080
4. Save
5. Klik ikon FoxyProxy → pilih konfigurasi Burp
6. Pastikan Burp Suite sedang berjalan
7. Aktifkan Intercept di tab Proxy Burp
8. Buka website → browser hang = intercept berhasil!

INGAT:
→ Browser hang saat intercept ON = NORMAL & BERHASIL
→ Jangan lupa matikan intercept kalau tidak dipakai
→ Klik kanan request di Burp = Forward/Drop/Send to tools/dll

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 BURP BROWSER (BUILT-IN)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Apa      : Browser Chromium bawaan yang sudah pre-configured ke proxy
Cara     : Tab Proxy → klik tombol "Open browser"
Kelebihan: Tidak perlu setup FoxyProxy, langsung terhubung ke Burp

Masalah Linux (root/AttackBox):
→ Error karena tidak bisa buat sandbox environment
→ Solusi 1 (Smart)  : buat user baru dengan low-privilege account
→ Solusi 2 (Easy)   : Settings → Tools → Burp's browser →
                       centang "Allow Burp's browser to run without a sandbox"
                       ⚠️ Disabled by default karena alasan keamanan!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TARGET TAB — 3 SUB-TAB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Site Map        → Peta seluruh struktur website target (tree structure)
                  Auto-generate hanya dengan browsing biasa
                  Professional: bisa automated crawling
                  Community   : bagus untuk enumeration awal & mapping API
                  Endpoint tersembunyi = muncul di sini meski tidak ada link-nya!

Issue Definitions→ Daftar lengkap semua jenis kerentanan web + deskripsi + referensi
                   Berguna untuk: referensi laporan & deskripsi kerentanan manual

Scope Settings  → Kontrol target scope: include/exclude domain atau IP
                  Mencegah Burp tangkap traffic yang tidak relevan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SCOPING & TARGETING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cara set scope : Tab Target → klik kanan target → "Add To Scope"
                 Burp tanya: stop logging out-of-scope? → pilih YES

Cek scope      : Target → sub-tab Scope

PENTING: Scope TIDAK otomatis stop intercept traffic luar scope!
Solusi  : Proxy settings → Request Interception Rules →
          aktifkan "And URL Is in target scope"
          → Proxy benar-benar abaikan traffic di luar scope

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PROXYING HTTPS — CA CERTIFICATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Masalah  : Browser tidak percaya sertifikat Burp (PortSwigger CA)
           → Error "Potential Security Issue" saat buka HTTPS site

Solusi   : Install CA Certificate PortSwigger ke Firefox

Langkah  :
1. Burp aktif → buka http://burp/cert → download cacert.der
2. Firefox → ketik about:preferences di URL bar → cari "certificates"
3. Klik View Certificates → Import → pilih cacert.der
4. Centang "Trust this CA to identify websites" → OK

Hasil    : Firefox percaya sertifikat Burp → HTTPS site bisa diakses normal

Catatan HSTS: Website dengan HSTS Preload List (misal: vercel.app)
              tidak bisa di-bypass meski CA sudah diinstall
              → Solusi: matikan FoxyProxy untuk website tersebut

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CONTOH SERANGAN NYATA — XSS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
XSS = Cross-Site Scripting
      Menyuntikkan script (biasanya Javascript) ke halaman web
      agar dieksekusi oleh browser

Reflected XSS = hanya memengaruhi orang yang membuat request

Skenario:
Target   : Form support dengan client-side email filter
Masalah  : Filter blokir karakter khusus di browser langsung

Bypass dengan Burp:
1. Intercept ON, masukkan data legitimate (email valid + query)
2. Submit form → request tertangkap Burp
3. Di raw request, ganti field email dengan payload:
   <script>alert("Succ3ssful XSS")</script>
4. (Opsional) Select payload → Ctrl+U = URL encode di Burp
5. Klik Forward → alert box muncul di browser = XSS BERHASIL!

Kenapa bisa bypass?
→ Filter hanya ada di client-side (browser)
→ Dengan Burp, kita bypass browser dan langsung edit raw request
→ Server tidak punya filter → script tereksekusi

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 BURP vs WIRESHARK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Wireshark → Level jaringan (TCP/IP, UDP, DNS, dll)
            Tangkap SEMUA paket dari semua protokol
            Sifat: PASIF — hanya lihat & catat, tidak bisa ubah

Burp Suite → Level HTTP/HTTPS khusus
             Intercept, modify, replay request/response
             Sifat: AKTIF — bisa tahan, ubah, kirim ulang data

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Proxy            = Perantara antara browser dan server
Intercept        = Menahan request sebelum sampai ke server
Forward          = Teruskan request yang ditahan ke tujuannya
Drop             = Buang/batalkan request yang ditahan
Scope            = Batasan target yang dipantau Burp
Endpoint         = Path/alamat spesifik di sebuah website (/about, /api/user)
CA Certificate   = Sertifikat otoritas untuk validasi koneksi HTTPS
TLS/HTTPS        = Protokol komunikasi terenkripsi
HSTS             = HTTP Strict Transport Security (paksa HTTPS)
Client-side      = Filter/validasi yang berjalan di browser
Server-side      = Filter/validasi yang berjalan di server
URL Encoding     = Mengubah karakter khusus jadi format aman (%3C = <)
Payload          = Data/kode yang dikirim dalam serangan
Rate Limited     = Dibatasi kecepatannya (Intruder di Community)
Fuzzing          = Kirim banyak input acak untuk cari kerentanan
Crawling         = Jelajahi semua link website secara otomatis
Sandbox          = Lingkungan terisolasi untuk jalankan program berbahaya
```