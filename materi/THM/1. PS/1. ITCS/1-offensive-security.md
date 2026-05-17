=== Offensive Security Introduction - Resume Materi ===
[17 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 OFFENSIVE vs DEFENSIVE SECURITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Offensive Security → PROAKTIF: berpikir & bertindak seperti penyerang
                     Tujuan: temukan & eksploitasi kelemahan SEBELUM hacker jahat
                     Analogi: ujian ketahanan dengan menyerang sendiri
                     Metode: penetration testing, red teaming, vulnerability assessment

Defensive Security → REAKTIF: lindungi sistem dari serangan
                     Tujuan: deteksi, cegah, respon terhadap ancaman
                     Analogi: benteng pertahanan & sistem alarm
                     Metode: monitoring, firewall, IDS/IPS, incident response

Perbedaan Utama:
• Offensive = CARI celah dengan menyerang (simulate attacker)
• Defensive = TUTUP celah & tangkal serangan (protect & detect)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONSEP HACKING ETIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi: Hacking yang dilakukan secara LEGAL dalam lingkungan AMAN
Syarat Mutlak:
  ✓ Ada izin resmi dari pemilik sistem
  ✓ Dilakukan di environment yang terkontrol (lab/sandbox)
  ✓ Mengikuti Rules of Engagement (ROE)

Tujuan:
• Latihan skill offensive tanpa melanggar hukum
• Pahami cara kerja serangan cyber
• Berlatih seperti skenario nyata tapi AMAN

Platform Latihan:
• TryHackMe → guided learning, step-by-step labs
• Hack The Box → CTF challenges, realistic machines
• VulnHub → vulnerable VMs untuk practice

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 WEB APPLICATION SECURITY BASICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kelemahan Umum Web Apps:

1. Hidden Pages / Directory Traversal
   Masalah: Halaman admin/sensitive bisa diakses tanpa autentikasi
   Contoh: /admin, /backup, /config, /bank-transfer
   Dampak: Akses tidak sah ke fungsi privileged

2. Broken Access Control
   Masalah: User biasa bisa akses fungsi admin
   Contoh: Manipulasi URL untuk akses admin panel
   Dampak: Privilege abuse, data manipulation

3. Insecure Direct Object Reference (IDOR)
   Masalah: Parameter bisa diubah untuk akses data orang lain
   Contoh: ?account=8881 → ubah jadi ?account=8882
   Dampak: Data breach, unauthorized access

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TOOLS DASAR OFFENSIVE SECURITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dirb / Dirbuster
  Fungsi: Brute force directory & file discovery di web server
  Cara Kerja: Coba ribuan kemungkinan nama direktori dari wordlist
  Syntax: dirb http://target.thm
  Output: Daftar URL yang ditemukan (kode HTTP 200 = found)
  
  Kapan Pakai:
  • Content discovery / enumeration
  • Cari halaman tersembunyi yang tidak ter-link
  • Mapping struktur direktori website

Gobuster
  Fungsi: Sama seperti Dirb tapi lebih cepat (multithreading)
  Syntax: gobuster dir -u http://target.thm -w wordlist.txt
  
Burp Suite
  Fungsi: Intercept & modify HTTP request/response
  Gunakan untuk: manipulasi request, fuzzing, vulnerability scanning

Nmap
  Fungsi: Port scanning & service enumeration
  Contoh: nmap -sV target.thm → deteksi service & versi

Metasploit
  Fungsi: Framework eksploitasi dengan database exploit
  Gunakan untuk: automate exploitation process

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TAHAPAN SERANGAN WEB (SIMPLIFIED)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Reconnaissance (Pengintaian)
   → Kumpulkan info tentang target
   → Identifikasi teknologi yang dipakai (CMS, framework, server)
   → TIDAK ada interaksi langsung dengan sistem

2. Enumeration (Enumerasi)
   → SCAN sistem untuk temukan attack surface
   → Tools: Dirb, Nmap, Nikto
   → Output: daftar direktori, port terbuka, service running

3. Exploitation (Eksploitasi)
   → Manfaatkan kelemahan untuk gain access
   → Contoh: akses /admin tanpa autentikasi
   → Contoh: manipulasi parameter untuk ubah data

4. Post-Exploitation
   → Maintain access atau pivot ke sistem lain
   → Extract data sensitif
   → Cover tracks (hapus log)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LAB PRACTICE: FAKEBANK SCENARIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Skenario: Aplikasi banking dengan kelemahan keamanan

Step 1: Directory Enumeration
  Command: dirb http://fakebank.thm
  Goal: Temukan hidden pages
  Expected Output: 2 URLs ditemukan (termasuk /bank-transfer)

Step 2: Access Hidden Admin Page
  URL: http://fakebank.thm/bank-transfer
  Finding: Admin panel TIDAK memerlukan autentikasi
  Vulnerability: Broken Access Control

Step 3: Exploit the Weakness
  Action: Deposit money ke account 8881
  Method: Gunakan admin panel untuk manipulasi saldo
  Result: Saldo berubah → proof of exploitation
  Flag: "BANK-HACKED" (pop-up hijau setelah berhasil)

Step 4: Documentation
  Catat: Vulnerability type, steps to reproduce, impact
  Report: Broken Access Control → unauthorized fund manipulation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 INDIKATOR HTTP RESPONSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kode Status yang Penting Dikenali:

200 OK           → Halaman ditemukan & berhasil diakses (TARGET UTAMA)
301 Moved        → Redirect permanent
302 Found        → Redirect temporary
401 Unauthorized → Butuh autentikasi (halaman ada tapi protected)
403 Forbidden    → Halaman ada tapi akses ditolak
404 Not Found    → Halaman tidak ada
500 Server Error → Error di server (bisa jadi celah)

Saat Dirb Scanning:
• Fokus pada response 200 → halaman aktif yang bisa diakses
• Response 403 → ada file/folder tapi diblokir (investigasi lebih lanjut)
• Response 301/302 → ikuti redirect untuk lihat endpoint sebenarnya

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 BEST PRACTICES OFFENSIVE SECURITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ SELALU dapat izin tertulis sebelum test
✓ Kerja di environment TERISOLASI (lab/VM)
✓ Dokumentasikan SEMUA langkah yang dilakukan
✓ Pahami scope & batasan testing
✓ Jangan test sistem production tanpa approval
✓ Gunakan VPN saat connect ke platform lab (TryHackMe/HTB)
✓ Backup data sebelum exploit (lab bisa crash)

✗ JANGAN exploit sistem tanpa izin (= ILEGAL)
✗ JANGAN bagikan exploit untuk sistem nyata
✗ JANGAN gunakan skill untuk keuntungan pribadi ilegal
✗ JANGAN lewati tahap enumeration (bisa miss important info)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Offensive Security = pendekatan proaktif cari celah dengan simulate attack
Defensive Security = pendekatan reaktif lindungi sistem dari ancaman
Ethical Hacking    = hacking legal dengan izin untuk tujuan keamanan
Content Discovery  = proses menemukan file/direktori tersembunyi di web
Directory Brute Force = coba banyak kemungkinan nama direktori sampai ketemu
Hidden Pages       = halaman web yang tidak ter-link tapi masih accessible
Broken Access Control = kelemahan di mana user bisa akses fungsi yang seharusnya restricted
Admin Panel        = interface management biasanya hanya untuk administrator
Enumeration        = fase scanning untuk identifikasi detail sistem target
HTTP Status Code   = kode respons server (200=OK, 404=Not Found, dll)
Attack Surface     = semua titik masuk yang bisa diserang di sistem
Wordlist           = daftar kata untuk brute force (directory names, passwords)
Session            = koneksi aktif antara user dan aplikasi web
Proof of Concept   = bukti bahwa vulnerability bisa dieksploitasi
Flag               = string/tanda bukti berhasil selesaikan challenge (CTF)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 COMMAND REFERENCE CEPAT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Directory brute force
dirb http://target.thm
gobuster dir -u http://target.thm -w /usr/share/wordlists/dirb/common.txt

# Port scanning
nmap -sV target.thm
nmap -p- target.thm  # scan semua port

# Web enumeration
nikto -h http://target.thm
whatweb http://target.thm

# Manual testing
curl http://target.thm/admin  # test akses URL
wget http://target.thm/backup.zip  # download file