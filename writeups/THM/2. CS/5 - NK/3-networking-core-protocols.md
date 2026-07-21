```
=== Networking Core Protocols - Resume Materi ===
[03 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DNS (Domain Name System)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Menerjemahkan nama domain → alamat IP
Layer    : Application Layer (Layer 7 OSI)
Port     : UDP 53 (default) | TCP 53 (fallback)
Tool CLI : nslookup <domain>

JENIS RECORD DNS :
  A Record    → hostname → IPv4 (contoh: example.com → 172.17.2.172)
  AAAA Record → hostname → IPv6 (quad-A, bukan battery/AAA/auth)
  CNAME       → domain → domain lain (alias/nama panggilan)
                contoh: www.example.com → example.com
  MX Record   → menentukan mail server untuk domain tersebut

CARA KERJA :
  Buka browser example.com → browser query DNS untuk A Record
  Kirim email ke x@example.com → mail server query DNS untuk MX Record

ANALISIS PAKET (nslookup www.example.com hasilkan 4 paket) :
  Paket 1 → Query A Record (IPv4) keluar
  Paket 2 → Response A Record masuk
  Paket 3 → Query AAAA Record (IPv6) keluar
  Paket 4 → Response AAAA Record masuk

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 WHOIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Database info siapa yang daftarkan domain/IP
Baca     : "who is" (BUKAN akronim)
Tool CLI : whois <domain>
Isi Record : nama, telp, email, alamat, tgl buat, tgl expired

PRIVACY PROTECTION :
  Tanpa proteksi → info asli pemilik domain tampil publik
  Dengan proteksi → nama perusahaan proxy yang tampil
                    contoh: Domains By Proxy, LLC (GoDaddy)

INFO YANG BISA DILIHAT :
  Registrar, WHOIS Server, Creation Date,
  Expiration Date, Updated Date, Status domain,
  Registrant / Admin / Tech contact

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HTTP & HTTPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HTTP  = Hypertext Transfer Protocol → port TCP 80
HTTPS = HTTP + Secure (enkripsi) → port TCP 443
Port lain yang mungkin : 8080 (HTTP alt), 8443 (HTTPS alt)
Transport : TCP

HTTP METHODS :
  GET    → ambil data dari server (HTML, gambar, dll)
  POST   → kirim data baru ke server (form, upload file)
  PUT    → buat resource baru / update & timpa yang lama
  DELETE → hapus file atau resource di server

HTTP HEADERS (yang penting dikenali) :
  Request (dari browser) :
    GET / HTTP/1.1
    Host          → domain/IP tujuan
    User-Agent    → identitas browser & OS
    Accept        → jenis konten yang bisa diterima
    Accept-Encoding → format kompresi yang didukung
    Accept-Language → preferensi bahasa

  Response (dari server) :
    200 OK        → request berhasil
    Server        → software & OS server (misal: nginx/1.18.0 Ubuntu)
    Content-Type  → jenis konten yang dikirim
    Last-Modified → kapan halaman terakhir diubah
    ETag          → sidik jari unik versi halaman (untuk caching)

AKSES MANUAL VIA TELNET :
  telnet <IP> 80
  GET /namafile.html HTTP/1.1
  Host: anything
  [Enter 2x]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FTP (File Transfer Protocol)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Transfer file antar komputer (lebih efisien dari HTTP)
Port     : TCP 21 (kontrol) | port terpisah untuk transfer data
Transport: TCP

COMMAND FTP (yang diketik user) :
  ls           → lihat isi direktori
  get <file>   → download file dari server
  put <file>   → upload file ke server
  type ascii   → ganti mode ke ASCII (opsional, untuk file teks)
  quit         → keluar

COMMAND PROTOKOL ASLI (di balik layar) :
  USER → kirim username
  PASS → kirim password
  LIST → daftar file (saat user ketik ls)
  RETR → download file (saat user ketik get)
  STOR → upload file (saat user ketik put)
  QUIT → tutup koneksi

KONEKSI :
  ftp <IP>
  login: anonymous (jika server mengizinkan tanpa password)

CATATAN :
  Type ascii TIDAK wajib untuk file .txt
  Binary mode (default) bisa transfer semua jenis file
  Data listing & file dikirim via KONEKSI TERPISAH

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SMTP (Simple Mail Transfer Protocol)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : KIRIM email (mail client → server, server → server)
Port     : TCP 25
Transport: TCP

COMMAND SMTP :
  HELO/EHLO    → sapa server, mulai sesi SMTP
  MAIL FROM    → alamat email pengirim
  RCPT TO      → alamat email penerima (harus pakai <> dan @ yang valid)
  DATA         → mulai tulis isi email
  .            → titik di baris sendiri = akhir pesan
  QUIT         → tutup koneksi

ALUR KIRIM EMAIL VIA TELNET :
  telnet <IP> 25
  HELO <nama>
  MAIL FROM: <pengirim@domain>
  RCPT TO: <penerima@domain>
  DATA
  From: ...
  To: ...
  Subject: ...
  [baris kosong]
  isi pesan
  .
  QUIT

PENTING :
  RCPT TO harus domain yang dikelola server tersebut
  Gmail/domain eksternal → 550 relay not permitted
  Format salah (tanpa @) → 501 recipient address must contain a domain
  User tidak exist → 550 Unroutable address
  Berhasil → 250 Accepted

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 POP3 (Post Office Protocol v3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : AMBIL email dari server → download ke perangkat lokal
Port     : TCP 110 (plaintext) | TCP 995 (SSL/TLS = POP3S)
Transport: TCP
Sifat    : Email didownload → DIHAPUS dari server
           Hanya cocok untuk 1 perangkat

COMMAND POP3 :
  USER <username> → identifikasi user
  PASS <password> → masukkan password
  STAT            → jumlah pesan & total ukuran
  LIST            → daftar semua pesan & ukurannya
  RETR <nomor>    → ambil pesan nomor tertentu
  DELE <nomor>    → tandai pesan untuk dihapus
  QUIT            → keluar & terapkan perubahan

KONEKSI PLAINTEXT :
  telnet <IP> 110

KONEKSI SSL/TLS (jika server tolak plaintext) :
  openssl s_client -connect <IP>:995 -quiet

FLAG OPENSSL :
  s_client          → mode SSL client (seperti telnet tapi terenkripsi)
  -connect <IP:PORT>→ tentukan server & port tujuan
  -quiet            → sembunyikan output SSL, biarkan data mengalir bersih
                      (penting! tanpa ini RETR bisa gagal/renegotiation error)
  -legacy_renegotiation → izinkan renegotiasi SSL versi lama (jika perlu)

BAHAYA PLAINTEXT :
  Password & isi email bisa dibaca langsung via Wireshark/packet capture
  Rentan MITM attack (Man-in-the-Middle)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 IMAP (Internet Message Access Protocol)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : SINKRONISASI email di banyak perangkat
Port     : TCP 143 (plaintext) | TCP 993 (SSL/TLS = IMAPS)
Transport: TCP
Sifat    : Email TETAP di server, tersinkron ke semua perangkat
           Storage server lebih besar dari POP3

COMMAND IMAP (pakai TAG huruf di depan) :
  A LOGIN <user> <pass> → autentikasi
  B SELECT <mailbox>    → pilih folder (contoh: inbox)
  C FETCH <nomor> body[]→ ambil pesan lengkap (header + body)
  D LOGOUT              → keluar

KENAPA PAKAI TAG (A B C D) :
  IMAP bisa handle banyak command bersamaan
  Tag mencocokkan setiap command dengan responnya

INFO DARI SELECT inbox :
  FLAGS          → status yang tersedia (\Seen \Answered \Draft dll)
  EXISTS         → jumlah total pesan di mailbox
  RECENT         → pesan baru sejak sesi terakhir
  UNSEEN         → nomor pesan pertama yang belum dibaca
  UIDVALIDITY    → validasi UID pesan masih berlaku
  UIDNEXT        → UID yang akan diberikan untuk pesan berikutnya

KONEKSI :
  telnet <IP> 143

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TABEL PORT SEMUA PROTOKOL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  TELNET → TCP  → port 23
  DNS    → UDP/TCP → port 53
  HTTP   → TCP  → port 80
  HTTPS  → TCP  → port 443
  FTP    → TCP  → port 21
  SMTP   → TCP  → port 25
  POP3   → TCP  → port 110  (SSL: 995)
  IMAP   → TCP  → port 143  (SSL: 993)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERBANDINGAN POP3 vs IMAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  POP3 → download & hapus dari server
         1 perangkat saja
         storage server kecil
         tidak sinkron

  IMAP → tetap di server, sinkron semua perangkat
         multi-perangkat
         storage server lebih besar
         bisa tandai sudah dibaca/belum di semua device

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Plaintext        = data dikirim tanpa enkripsi, bisa dibaca siapapun
SSL/TLS          = lapisan enkripsi untuk proteksi data saat transfer
MITM Attack      = Man-in-the-Middle, hacker menyadap koneksi di tengah jalan
Relay            = meneruskan email ke domain lain (diblokir server by default)
Non-authoritative= jawaban DNS dari cache, bukan dari server pemilik domain asli
Open Relay       = SMTP server yang mau relay email ke domain manapun (berbahaya)
EOF              = End Of File, sinyal akhir data
Renegotiation    = proses "refresh" parameter enkripsi SSL di tengah koneksi
Passive Mode     = mode FTP di mana client yang buka koneksi data ke server
Tag (IMAP)       = huruf penanda di depan command untuk cocokkan dengan response
Registrant       = pemilik/pendaftar domain
Registrar        = perusahaan tempat domain didaftarkan (contoh: GoDaddy)
```