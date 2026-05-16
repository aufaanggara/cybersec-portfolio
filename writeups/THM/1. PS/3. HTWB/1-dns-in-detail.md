```
=== DNS (Domain Name System) - Resume Materi ===
[05 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU DNS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Sistem yang menerjemahkan nama domain menjadi IP address
Fungsi   : Memudahkan manusia mengakses internet tanpa hafal angka IP
Analogi  : Seperti buku telepon internet — tryhackme.com → 104.26.10.229
Kenapa   : Lebih mudah ingat "google.com" daripada "142.250.185.46"
Cara     : Domain name → DNS lookup → IP address → koneksi tercapai

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HIERARKI DOMAIN (STRUKTUR POHON)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Root Domain (.)
   ↓
TLD (Top-Level Domain)
   ↓
Second-Level Domain
   ↓
Subdomain

Contoh Lengkap: jupiter.servers.tryhackme.com
  jupiter  = subdomain level 3
  servers  = subdomain level 2
  tryhackme= second-level domain
  .com     = TLD
  .        = root (tidak terlihat)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TLD (TOP-LEVEL DOMAIN)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
gTLD (Generic)
  .com = komersial/bisnis
  .org = organisasi
  .edu = pendidikan
  .gov = pemerintah
  .mil = militer
  .net = network/ISP
  Baru : .online, .club, .website, .biz, dll (2000+ TLD)

ccTLD (Country Code)
  .id   = Indonesia
  .uk   = United Kingdom
  .ca   = Canada
  .au   = Australia
  .jp   = Japan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SECOND-LEVEL DOMAIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Nama domain yang kita daftarkan/beli
Contoh   : tryhackme, google, facebook, microsoft
Batasan  :
  - Maksimal 63 karakter
  - Hanya a-z, 0-9, dan tanda hubung (-)
  - TIDAK boleh diawali/diakhiri dengan tanda hubung
  - TIDAK boleh ada tanda hubung berturut-turut

Format: [nama-domain].[TLD]
  ✓ tryhackme.com
  ✓ google.co.uk
  ✗ -invalid.com (diawali -)
  ✗ test--.com (-- berturut-turut)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SUBDOMAIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Posisi   : Di KIRI second-level domain, dipisah titik (.)
Contoh   : admin.tryhackme.com
           ↑ subdomain
Aturan   : Sama seperti second-level (maks 63 karakter, a-z 0-9 -)
Multi    : Bisa berlapis → jupiter.servers.tryhackme.com
Batasan  : Total panjang domain maksimal 253 karakter
           Jumlah subdomain = UNLIMITED
Kegunaan : Memisahkan service (mail.domain.com, shop.domain.com, blog.domain.com)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 JENIS DNS RECORD (WAJIB HAPAL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A Record
  Fungsi : Domain → IPv4 address
  Contoh : tryhackme.com → 104.26.10.229
  Paling : Umum digunakan

AAAA Record
  Fungsi : Domain → IPv6 address
  Contoh : tryhackme.com → 2606:4700:20::681a:be5
  Untuk  : IPv6 (format IP baru yang lebih panjang)

CNAME Record
  Fungsi : Domain → Domain lain (alias)
  Contoh : store.tryhackme.com → shops.shopify.com
  Proses : DNS query CNAME dulu → dapat domain baru → query lagi ke domain baru
  Gunanya: Redirect subdomain ke layanan pihak ketiga

MX Record
  Fungsi : Domain → Mail server address
  Contoh : tryhackme.com → alt1.aspmx.l.google.com
  Prioritas: Ada angka priority (lebih kecil = lebih prioritas)
  Backup : Server prioritas 10 dicoba dulu, kalau down baru coba prioritas 20
  Untuk  : Routing email ke server yang benar

TXT Record
  Fungsi : Simpan data teks bebas
  Kegunaan:
    - Verifikasi kepemilikan domain
    - Daftar server authorized untuk kirim email (anti-spam)
    - Konfigurasi SPF, DKIM, DMARC
    - Menyimpan flag/data untuk verifikasi
  Contoh : THM{7012BBA60997F35A9516C2E16D2944FF}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PROSES DNS REQUEST (5 LANGKAH)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Local Cache (Komputer)
   → Cek cache lokal komputer
   → Kalau ada, langsung pakai (SELESAI)
   → Kalau tidak ada, lanjut ke step 2

2. Recursive DNS Server (ISP)
   → Biasanya dari ISP (Telkom, Indihome, dll)
   → Atau bisa pilih sendiri (8.8.8.8 Google, 1.1.1.1 Cloudflare)
   → Cek cache server ini
   → Kalau ada (untuk site populer: Google, FB, Twitter), kirim balik (SELESAI)
   → Kalau tidak ada, lanjut ke step 3

3. Root DNS Server
   → Backbone of the internet
   → Redirect ke TLD server yang benar
   → Contoh: request .com → arahkan ke TLD server .com
   → Tidak kasih jawaban final, hanya petunjuk

4. TLD Server
   → Punya data nameserver authoritative untuk domain
   → Contoh: tryhackme.com → nameserver di kip.ns.cloudflare.com
   → Biasanya ada 2+ nameserver untuk redundancy
   → Lanjut ke step 5

5. Authoritative DNS Server
   → Server yang SIMPAN DNS records asli
   → Tempat update DNS records dilakukan
   → Kasih jawaban FINAL (A, AAAA, MX, TXT, dll)
   → Hasil dikirim balik ke Recursive → di-cache → kirim ke komputer
   → Ada nilai TTL untuk tentukan berapa lama di-cache

Waktu Total: Hitungan MILIDETIK (sangat cepat!)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING DNS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TTL (Time To Live)
  = Nilai dalam DETIK, tentukan berapa lama DNS record boleh di-cache
  = Setelah TTL habis, harus query ulang
  = Hemat bandwidth & waktu

Cache
  = Penyimpanan sementara hasil DNS query
  = Ada di komputer & di Recursive DNS Server
  = Untuk site populer (Google, FB) selalu ada di cache

Recursive DNS Server
  = Server yang melakukan pencarian penuh untuk kita
  = Dari ISP atau pilih sendiri
  = Punya cache sendiri

Authoritative DNS Server
  = Server yang punya DNS records asli
  = Tempat update dilakukan
  = Memberikan jawaban final

Nameserver
  = Nama lain untuk Authoritative DNS Server
  = Contoh: kip.ns.cloudflare.com, uma.ns.cloudflare.com

Root Server
  = Server paling atas di hierarki DNS
  = Ada 13 grup root server di seluruh dunia
  = Dikelola berbagai organisasi (ICANN, dll)

Resolver
  = Software di komputer yang melakukan DNS query
  = Bagian dari OS (Windows, Linux, macOS)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TOOLS DNS QUERY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
nslookup
  Command : nslookup domain.com
  Fungsi  : Query DNS records dari command line
  OS      : Windows, Linux, macOS
  Hasil   : Tampilkan IP address & DNS server yang menjawab

dig (Domain Information Groper)
  Command : dig domain.com
  Fungsi  : DNS lookup lebih detail dari nslookup
  OS      : Linux, macOS (install manual di Windows)
  Hasil   : Info lengkap termasuk TTL, record type, dll

host
  Command : host domain.com
  Fungsi  : DNS lookup sederhana
  OS      : Linux, macOS
  Hasil   : IP address & mail server

Online Tools
  - DNS Checker
  - MX Toolbox
  - What's My DNS
  - DNS Watch

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LAB PRAKTIK (Hasil Task 5)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Command  : nslookup website.thm

Query 1  : CNAME shop.website.thm
Hasil    : shops.myshopify.com
Artinya  : Subdomain shop pakai layanan Shopify

Query 2  : TXT website.thm
Hasil    : THM{7012BBA60997F35A9516C2E16D2944FF}
Artinya  : Flag tersimpan di TXT record (untuk verifikasi)

Query 3  : MX record priority
Hasil    : 30
Artinya  : Mail server dengan priority 30 (angka kecil = prioritas tinggi)

Query 4  : A record www.website.thm
Hasil    : 10.10.10.10
Artinya  : IPv4 address untuk www subdomain

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONSEP PENTING UNTUK PENTEST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DNS Enumeration
  = Teknik untuk kumpulkan info tentang target dari DNS
  = Cari subdomain, mail server, nameserver
  = Tools: dnsrecon, fierce, sublist3r

DNS Zone Transfer
  = Teknik ambil semua DNS records sekaligus
  = Kalau misconfigured, bisa dapat semua subdomain
  = Command: dig axfr @nameserver domain.com

Reverse DNS Lookup
  = IP address → domain name (kebalikan dari A record)
  = Gunakan PTR record
  = Untuk verifikasi atau investigasi

DNS Tunneling
  = Teknik kirim data lewat DNS query (bypass firewall)
  = Bisa untuk exfiltration data
  = Deteksi: monitor DNS query yang tidak normal

DNS Cache Poisoning
  = Serangan masukkan data palsu ke DNS cache
  = User ke facebook.com → redirect ke situs phishing
  = Proteksi: DNSSEC

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FAKTA MENARIK DNS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- DNS diciptakan tahun 1983 oleh Paul Mockapetris
- Sebelum DNS, pakai file HOSTS.TXT yang di-update manual
- Ada 13 root server (tapi replika ratusan di seluruh dunia)
- DNS query biasanya pakai UDP port 53
- DNS zone transfer pakai TCP port 53
- Google Public DNS (8.8.8.8) handle 400+ miliar query/hari
- Cloudflare DNS (1.1.1.1) diklaim tercepat di dunia
- Tanpa DNS, internet seperti yang kita kenal tidak akan berfungsi

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CHEAT SHEET SINGKAT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A      = Domain → IPv4
AAAA   = Domain → IPv6
CNAME  = Domain → Domain lain
MX     = Domain → Mail server (ada priority)
TXT    = Data teks bebas (verifikasi, SPF, dll)
NS     = Nameserver untuk domain
PTR    = IP → Domain (reverse lookup)
SOA    = Start of Authority (info zone DNS)

Recursive = Server yang cari jawaban untuk kita
Authoritative = Server yang punya jawaban asli
TTL = Waktu cache dalam detik
Root Server = Server paling atas (.)
TLD = Top-Level Domain (.com, .id, dll)
```