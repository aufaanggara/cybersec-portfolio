```
=== HTB Starting Point - Meow Machine ===
[29 Apr 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONSEP DASAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VM (Virtual Machine) = Komputer virtual yang berjalan di dalam komputer fisik
Terminal             = Tool untuk berinteraksi dengan OS via command line (shell)
Enumeration          = Proses identifikasi port, service, dan versi yang berjalan
                       di sistem target

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONEKSI VPN HTB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tujuan   : Masuk ke jaringan private HTB agar bisa akses mesin target
Tool     : OpenVPN
Perintah : sudo openvpn <file>.ovpn
Cek      : ping <target IP> → kalau reply = koneksi berhasil

Kenapa lag di mesin target?
→ Jalur : Kali → VPN HTB → Server HTB → Mesin target (panjang!)
→ Solusi: pilih server VPN yang lebih dekat (Switch VPN → Asia/Singapore)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NMAP - NETWORK SCANNER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi : Scan jaringan untuk temukan port terbuka & service yang berjalan

Sintaks dasar:
  nmap [switch] [target IP]

Switch penting:
  -sV        → Deteksi versi service di tiap port (Service Version Detection)
               Contoh hasil: 23/tcp open telnet Linux telnetd
  -p <port>  → Scan port spesifik saja (lebih cepat)
               Contoh: -p 23 (scan port 23 saja)
  -p <a,b,c> → Scan beberapa port: -p 22,23,80
  -p 1-1000  → Scan range port 1 sampai 1000
  -p-        → Scan SEMUA port (65535 port, paling lambat)

Contoh perintah:
  nmap -sV -p 23 10.129.1.131
  → Scan port 23 di IP target, sekaligus deteksi versi service-nya

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TELNET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Apa itu  : Protokol remote login via port 23
Bahaya   : Tidak terenkripsi → semua data terkirim dalam plaintext
           → Mudah disadap (sniffing)
           → Sering pakai default credentials

Perintah :
  telnet <IP target>
  Contoh  : telnet 10.129.1.131

Default credentials yang sering dicoba:
  root  / (kosong)
  admin / (kosong)
  admin / admin

Tanda berhasil masuk:
  root@NamaMesin:~#   ← kamu adalah root di dalam mesin target!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERINTAH LINUX DASAR (DIPAKAI DI LAB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ls          → Lihat isi direktori saat ini
cat <file>  → Baca isi file
cd <folder> → Masuk ke folder
cd ~        → Balik ke home directory (root = /root)
ping <IP>   → Cek koneksi ke target

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR SOLVE MEOW (REKAP)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Konek VPN      → sudo openvpn <file>.ovpn
2. Ping target    → ping 10.129.1.131  (cek koneksi)
3. Nmap scan      → nmap -sV 10.129.1.131  (temukan port 23/telnet)
4. Telnet masuk   → telnet 10.129.1.131
5. Login          → root : (password kosong)
6. Ambil flag     → ls → cat flag.txt
7. Submit flag    → paste ke kolom jawaban HTB

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Port             = "pintu" di sistem jaringan, tiap service punya port sendiri
                   Telnet = 23 | SSH = 22 | HTTP = 80 | HTTPS = 443
Service          = program/aplikasi yang berjalan dan mendengarkan di suatu port
Default Creds    = username & password bawaan yang belum diganti admin
Flag             = string unik bukti bahwa kamu berhasil kuasai mesin (format: hash)
Root             = user dengan akses tertinggi di Linux (setara Administrator)
Plaintext        = data yang tidak dienkripsi, bisa dibaca siapapun yang menyadap
```