# [Archetype] — [SQL]

**Date:** 2025-04-19
**Platform:** HackTheBox
**Difficulty:** Very Easy
**Category:** OS 

---

## Target
Windows server dengan dua service utama yang terbuka: SMB lama (Port 139 Net BIOS)SMB modern (Port 445) dan Microsoft SQL server (Port 1433). Skenario kecerobohan menyimpan kredensial database di dalam file konfigurasi yang bisa diakses public melalui SMB share, lalu SQL server dikonfigurasi sedemikian rupa dengan fitur berbahaya yang memungkinkan eksekusi command windows langsung dari query SQL.

## Vulnerability
- SMB Missconfiguration - share backups bisa diakses tanpa autentikasi (anonymus/guest)
- Credentials in Config File
- xp_cmdshell abuse + powershell history

## Tools Used
- smbclient
- Tool 2 (contoh: Burp Suite)
- WinPeas

## Exploitation Steps

### Step 1 — [Nama step, contoh: Reconnaissance]
Jelaskan apa yang kamu lakuin dan kenapa.
```bash
# command yang kamu pakai
nmap -sV -sC target-ip
```
> [Taruh screenshot di sini kalau ada]

### Step 2 — [Nama step, contoh: Finding the Vulnerability]
Jelaskan apa yang kamu temuin.
```
[output atau payload yang relevan]
```

### Step 3 — [Nama step, contoh: Exploitation]
Jelaskan cara eksploitnya.
```bash
# command eksploit
```

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