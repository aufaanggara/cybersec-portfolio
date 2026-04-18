```
=== Subdomain Enumeration - Resume Materi ===
[07 Mar 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU SUBDOMAIN ENUMERATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Proses menemukan subdomain valid dari sebuah domain utama
Tujuan   : Memperluas attack surface → temukan lebih banyak celah
Logika   : Subdomain terlupakan = tidak diupdate = lebih rentan
Contoh   : domain utama → acmeitsupport.thm
           subdomain    → admin.acmeitsupport.thm
                          mail.acmeitsupport.thm
                          dev.acmeitsupport.thm

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 3 METODE SUBDOMAIN ENUMERATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. OSINT      → Pasif, tidak menyentuh target langsung
2. Brute Force→ Aktif, mencoba ribuan kemungkinan
3. Virtual Host→ Aktif, manipulasi Host header HTTP

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 OSINT - SSL/TLS CERTIFICATES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Konsep   : Setiap sertifikat SSL/TLS yang dibuat CA dicatat
           di Certificate Transparency (CT) Logs → bisa diakses publik
Tujuan CT: Mencegah penggunaan sertifikat berbahaya/tidak sengaja
Tool     : https://crt.sh → database sertifikat historis & terkini
Cara     : Cari domain di crt.sh → lihat kolom "Matching Identities"
           → subdomain yang pernah punya sertifikat ketahuan semua

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 OSINT - SEARCH ENGINES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Konsep   : Google menyimpan triliunan link → bisa dimanfaatkan
Filter   : Gunakan operator "site:" untuk mempersempit hasil
Syntax   : site:*.domain.com -site:www.domain.com
Arti     : Tampilkan semua subdomain domain.com
           KECUALI www.domain.com
Contoh   : site:*.tryhackme.com -site:www.tryhackme.com

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 OSINT - SUBLIST3R
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Apa itu  : Tool otomatis yang menggabungkan banyak sumber OSINT sekaligus
Sumber   : Baidu, Yahoo, Google, Bing, Ask, Netcraft,
           VirusTotal, ThreatCrowd, SSL Certificates, PassiveDNS
Keunggulan: Satu perintah = semua sumber dicek otomatis
Output   : Daftar subdomain unik yang ditemukan dari semua sumber

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DNS BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Konsep   : Coba puluhan/ribuan/jutaan kemungkinan subdomain
           dari wordlist (daftar subdomain yang umum dipakai)
Tool     : dnsrecon
Cara     : Tool coba satu per satu → yang valid = ditemukan
Kelemahan: Lambat, bisa terdeteksi sebagai serangan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 VIRTUAL HOSTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Masalah  : Beberapa subdomain tidak ada di DNS publik
           (subdomain dev/admin dicatat di private DNS atau file hosts)
File hosts: Linux   → /etc/hosts
            Windows → c:\windows\system32\drivers\etc\hosts
Konsep   : Satu server bisa host banyak website → dibedakan via Host header
Teknik   : Ubah-ubah Host header → pantau respons → subdomain baru ketemu
Tool     : ffuf

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CARA PAKAI FFUF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Perintah 1 (tanpa filter):
ffuf -w wordlist.txt -H "Host: FUZZ.domain.com" -u http://IP

Perintah 2 (dengan filter):
ffuf -w wordlist.txt -H "Host: FUZZ.domain.com" -u http://IP -fs {size}

Switch penting:
  -w     = wordlist yang dipakai
  -H     = edit/tambah header HTTP
  FUZZ   = posisi yang dicoba satu per satu dari wordlist
  -u     = URL target
  -fs    = filter ukuran → abaikan response dengan ukuran tertentu

Alur benar:
  1. Jalankan perintah 1 dulu
  2. Lihat nilai Size yang paling sering muncul (misal: 2395)
  3. Jalankan perintah 2, ganti {size} dengan angka tersebut
  4. Yang tersisa = subdomain valid yang ditemukan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERBANDINGAN 3 METODE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Metode        Sifat    Kecepatan  Temukan subdomain
OSINT         Pasif    Cepat      Yang pernah terdaftar publik
Brute Force   Aktif    Lambat     Yang tidak dipublikasikan
Virtual Host  Aktif    Sedang     Yang tidak ada di DNS publik sama sekali

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Subdomain        = bagian di depan domain, misal admin.domain.com
Attack Surface   = semua titik/celah yang bisa diserang
CT Logs          = log publik berisi semua sertifikat SSL/TLS yang pernah dibuat
CA               = Certificate Authority, pihak yang menerbitkan sertifikat SSL
Wordlist         = daftar kata/nama subdomain umum untuk brute force
FUZZ             = keyword ffuf yang diganti satu per satu isi wordlist
Host Header      = bagian HTTP request yang memberitahu server website mana yang diminta
Virtual Host     = satu server yang melayani banyak domain/subdomain berbeda
-fs (filter size)= perintah ffuf untuk mengabaikan response berukuran tertentu
OSINT            = Open Source Intelligence, info dari sumber publik
```