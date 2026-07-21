=== Searching Skills — Resume Materi ===
[05 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 EVALUASI INFORMASI (4 FILTER UTAMA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Source              = Siapa penulisnya? Apakah punya otoritas di bidang itu?
                      Menulis blog ≠ otomatis jadi ahli
Evidence & Reason   = Apakah klaimnya didukung bukti & logika solid?
Objectivity & Bias  = Apakah objektif? Atau ada agenda tersembunyi?
                      (promosi produk / menyerang rival)
Corroboration       = Apakah beberapa sumber independen sepakat?
                      Satu sumber saja tidak cukup

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 GOOGLE SEARCH OPERATORS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"exact phrase"    = Cari frasa persis
                    Contoh : "passive reconnaissance"

site:             = Batasi pencarian ke domain tertentu
                    Contoh : site:tryhackme.com success stories

-                 = Hilangkan kata dari hasil pencarian
                    Contoh : pyramids -tourism

filetype:         = Cari file spesifik (pdf, doc, xls, ppt)
                    Contoh : filetype:ppt cyber security

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SPECIALIZED SEARCH ENGINES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Shodan    = Mesin pencari untuk PERANGKAT yang terhubung internet
            Cari : server, router, webcam, IoT, industrial control system
            Contoh query : apache 2.4.1

Censys    = Mirip Shodan TAPI fokus ke HOST, website, sertifikat, aset internet
            Kegunaan : enumerasi domain, audit port terbuka, temukan rogue asset

VirusTotal= Scan file/URL pakai 67+ antivirus engine sekaligus
            Bisa input : file langsung / URL / hash file
            Ada komunitas untuk diskusi hasil scan yang meragukan

HIBP      = Have I Been Pwned — cek apakah email pernah bocor di data breach
            Penting : banyak orang pakai password sama di banyak platform
                      → 1 platform bocor = semua platform berisiko

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CVE & EXPLOIT DATABASE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CVE       = Common Vulnerabilities and Exposures
            → Kamus standar kerentanan perangkat lunak & hardware
            → Format ID : CVE-TAHUN-NOMOR (contoh : CVE-2014-0160)
            → Dikelola oleh MITRE Corporation
            → Referensi lain : National Vulnerability Database (NVD)

Exploit DB= Database kode eksploit dari berbagai penulis
            → Beberapa exploit sudah diverifikasi (marked as verified)
            → HANYA boleh dipakai jika sudah ada izin resmi

GitHub    = Platform development yang juga berisi PoC & exploit code
            → Bisa cari CVE tertentu → temukan tools pengujiannya

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DOKUMENTASI TEKNIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Man Page  = Manual bawaan Linux untuk setiap perintah
            → Akses : man [perintah]   contoh : man ip / man cat
            → Juga ada untuk : system calls, library functions, config files
            → Bisa dicari di browser : ketik "man ip" di Google
            → Keluar dari man page : tekan q

Windows   = Microsoft punya portal dokumentasi resmi di Microsoft Learn
            → Contoh : cari "ipconfig" → dapat penjelasan lengkap resmi

Prinsip   = Selalu utamakan dokumentasi RESMI
            → Paling up-to-date & paling lengkap
            → Contoh dokumen resmi : Snort, Apache HTTP, PHP, Node.js

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERINTAH JARINGAN PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
netstat        = Perintah lama — masih aktif di Windows
ss             = Pengganti netstat di Linux (socket statistics)

ss -p          = Tampilkan proses yang terkait tiap socket (Linux)
netstat -b     = Tampilkan executable tiap koneksi aktif (Windows)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SOCIAL MEDIA UNTUK OSINT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LinkedIn  = Latar belakang PROFESIONAL & teknis seseorang
            → Riwayat kerja, skill, sertifikasi, tools yang dipakai

Facebook  = Informasi PERSONAL & kehidupan pribadi
            → Nama sekolah, kampung halaman, keluarga, momen masa kecil
            → Bahaya : bisa jadi jawaban secret question akun orang lain

Twitter   = Update real-time, tren teknis, diskusi komunitas siber

Tips aman = Gunakan email sementara saat eksplorasi platform baru
            → Jangan pakai akun utama → hindari kontak menghubungimu

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Snake Oil    = Metode/produk kriptografi yang palsu atau penipuan
PoC          = Proof of Concept — kode bukti bahwa eksploit benar-benar jalan
Hash         = Sidik jari unik sebuah file (dipakai di VirusTotal)
Data Breach  = Insiden kebocoran data yang tidak disengaja ke publik
Rogue Asset  = Perangkat/sistem dalam jaringan yang tidak diotorisasi
IoT          = Internet of Things — perangkat sehari-hari yang terhubung internet
HIBP         = Have I Been Pwned — layanan cek kebocoran email
NVD          = National Vulnerability Database — referensi CVE resmi pemerintah AS
Oversharing  = Berbagi informasi berlebihan di media sosial yang bisa dieksploitasi