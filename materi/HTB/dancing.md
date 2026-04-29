```
=== HTB Starting Point - Dancing (SMB) ===
[29 Apr 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU SMB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kepanjangan : Server Message Block
Fungsi      : Protokol berbagi file, folder, & printer antar komputer
              dalam satu jaringan
OS          : Aslinya milik Windows, tapi Linux bisa pakai via Samba
Port        : 445 (SMB over TCP) — nama service: microsoft-ds
              139 (SMB lama via NetBIOS) — nama service: netbios-ssn
Analogi     : SMB = sistem rak penitipan barang di kantor,
              siapapun yang punya kunci bisa ambil barang di rak tertentu

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONSEP SMB SHARES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Share    = folder yang dibagikan lewat jaringan via SMB
Share $  = share tersembunyi milik sistem (butuh admin)
           Contoh : ADMIN$, C$, IPC$
Share non-$ = share biasa, bisa jadi publik tanpa password
           Contoh : WorkShares ← celah di mesin Dancing!

Jenis share default Windows:
  ADMIN$   → Remote admin folder, butuh password
  C$       → Drive C:\, butuh password
  IPC$     → Inter-Process Communication, bukan folder biasa
  WorkShares → Buatan admin, TIDAK diproteksi = CELAH!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TOOL — NMAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi : Scanner jaringan — temukan port terbuka & service yang jalan

Syntax dasar:
  nmap [switch] [IP target]

Switch penting:
  -sV   → Deteksi versi service di tiap port
          Contoh output: "microsoft-ds 3.1.1"
  -sC   → Jalankan default scripts otomatis (cek vuln umum, ambil info)
          Outputnya muncul di bagian "Host script results"
  -p    → Scan port spesifik saja
          Contoh: nmap -p 445 10.129.7.35

Contoh perintah:
  nmap -sV -sC 10.129.7.35

Output penting yang harus dibaca:
  PORT      STATE  SERVICE       VERSION
  135/tcp   open   msrpc         Microsoft Windows RPC
  139/tcp   open   netbios-ssn   Microsoft Windows netbios-ssn
  445/tcp   open   microsoft-ds  ← TARGET SMB
  5985/tcp  open   http          Microsoft HTTPAPI 2.0

Bagian -sC (Host script results):
  smb2-security-mode → info keamanan SMB
  smb2-time          → waktu server
  "Message signing enabled but not required" → SMB bisa diakses tanpa signing!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TOOL — SMBCLIENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi : Client untuk mengakses SMB share dari Linux
         smb = protokolnya, client = posisi kita sebagai tamu

Syntax:
  smbclient [switch] [target]

Switch penting:
  -L   → List (tampilkan semua share yang ada di server)
  -N   → No password (anonymous login, tanpa password)

Perintah list share:
  smbclient -L 10.129.7.35 -N

Perintah masuk ke share:
  smbclient \\\\10.129.7.35\\WorkShares -N

Kenapa 4 backslash?
  Linux baca \\ = satu \ saja
  Jadi tulis \\\\ agar SMB terima \\
  Format SMB asli : \\IP\ShareName
  Di Linux harus  : \\\\IP\\ShareName

Error yang aman diabaikan:
  "Unable to connect with SMB1" → normal, kita pakai SMB2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERINTAH DALAM SMB SHELL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Setelah masuk, prompt jadi: smb: \>

  ls          → lihat isi folder (D = Directory, A = file)
  cd [folder] → masuk ke folder
  cd ..       → kembali ke folder sebelumnya
  get [file]  → download file ke mesin kita
  exit        → keluar dari SMB shell

Setelah get, baca file di terminal biasa:
  cat flag.txt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PING — TIPS LINUX VS WINDOWS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Linux   : ping jalan selamanya → harus pakai -c [angka] untuk berhenti
Windows : ping berhenti sendiri setelah 4x (default)

Contoh:
  ping 10.129.7.35        → jalan terus sampai Ctrl+C
  ping -c 4 10.129.7.35   → berhenti setelah 4 kali

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR ATTACK MESIN DANCING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. ping -c 4 10.129.7.35
   → Pastikan target hidup & VPN konek

2. nmap -sV -sC 10.129.7.35
   → Temukan port 445 (SMB) terbuka

3. smbclient -L 10.129.7.35 -N
   → List share → temukan WorkShares (tanpa $)

4. smbclient \\\\10.129.7.35\\WorkShares -N
   → Masuk ke share tanpa password

5. ls → cd James.P → ls
   → Temukan flag.txt

6. get flag.txt → exit → cat flag.txt
   → Baca flag!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CELAH KEAMANAN YANG DITEMUKAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Misconfiguration : SMB share (WorkShares) bisa diakses tanpa password
Dampak           : Siapapun di jaringan bisa baca/ambil file sensitif
File bocor       : flag.txt & worknotes.txt (catatan internal admin!)
Pelajaran        : Selalu proteksi SMB share dengan password &
                   jangan simpan file sensitif di share publik

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SMB              = Server Message Block, protokol berbagi file Windows
Share            = folder yang dibagikan via SMB
Anonymous login  = masuk tanpa username/password
Misconfiguration = pengaturan yang salah → jadi celah keamanan
Enumeration      = identifikasi detail sistem (port, service, share, user)
microsoft-ds     = nama service SMB di port 445 (ds = Directory Services)
```