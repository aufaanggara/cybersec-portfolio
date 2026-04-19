# [Archetype] — [SQL]

**Date:** 2025-04-19
**Platform:** HackTheBox
**Difficulty:** Very Easy
**Category:** OS 

---

## Target
Windows server dengan dua service utama yang terbuka: SMB lama (Port 139 Net BIOS) SMB modern (Port 445) dan Microsoft SQL server (Port 1433). Skenario kecerobohan menyimpan kredensial database di dalam file konfigurasi yang bisa diakses public melalui SMB share, lalu SQL server dikonfigurasi sedemikian rupa dengan fitur berbahaya yang memungkinkan eksekusi command windows langsung dari query SQL.

## Vulnerability
- SMB Missconfiguration - share backups bisa diakses tanpa autentikasi (anonymus/guest)
- Credentials in Config File - File prod.dtsConfig nyimpen username & password SQL server dalam plaintext dialam connection string
- xp_cmdshell abuse + powershell history - SQL server bisa dimanfaatkan untuk aktifin xp_cmdshell & jalanin command windows. Setelah masuk lalu cek powershell history dan terdapat kredensial administrator dalam plaintext

## Tools Used
- nmap - port scanning & service enumeration
- smbclient - SMB share enumeration & file download
- impacket-mssqlclient - koneksi ke microsoft sql server 
- python3 http.server - HTTP server untuk serve reverse shell script
- netcat (nc) - listener untuk nangkap reverse shell 
- powershell - reverse shell script di sisi target
- WinPEAS - windows privilege escalation enumeration
- impacket-psexec - remote login sebagai administrator 

## Exploitation Steps

### Step 1 — [Reconnaissance - Nmap scan]
Scan semua port untuk mengetahui port & service apa yang berjalan di target
```bash
# command yang kamu pakai
nmap -sV -sC target-ip
```
- sV - Deteksi versi service
- sC - Jalankan default scripts
- T4 - Speed scan

> ![nmap](image-2.png)

### Step 2 — [SMB Enumeration]
List semua share yang tersedia di target menggunakan anonymous login.
```bash
smbclient -N -L target-ip 
```

- -N - No password (anonymous)
- -L - List semua share

> ![smb enumeration](image-3.png)

Share backups adalah custom share (non-default) yang sering misconfigured dan bisa diakses tanpa password. Share default seperti ADMIN dan C otomatis di protect oleh windows dan hanya bisa diakses administrator.

### Step 3 — [SMB Share & Download File]
Masuk ke share backups dan download file yang ada.
```bash
smbclient -N \\\\ip-target\\sharename
```

- D - Directory : menggunakan cd
- AR - File (Achive, Read-only) : menggunakan get

> ![smb-share](image-5.png)

File .dtsConfig adalah file konfigurasi SSIS (SQL Server Integration Services) yang menyimpan connection string — termasuk username dan password dalam plaintext. Nama prod menandakan ini adalah konfigurasi production (sistem aktif, bukan test).

> ![cat prod](image-6.png)

### Step 4 — [Nama step, contoh: Post Exploitation / Getting the Flag]
Apa yang kamu dapetin setelah berhasil masuk.

---

## Proof
```
Flag: THM{xxxxxxxxxxxx}
```
> [Screenshot flag/bukti akses]

---

## Lessons Learned
- Hal baru yang kamu pelajari dari challenge ini
- Kesalahan yang kamu buat dan gimana kamu benerin
- Apa yang mau kamu explore lebih lanjut setelah ini