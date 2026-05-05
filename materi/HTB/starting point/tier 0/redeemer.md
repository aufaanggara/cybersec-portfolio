```
=== HTB Redeemer - Resume Materi ===
[02 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU REDIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tipe     : In-memory, NoSQL, Key-Value Store
Artinya  : Data disimpan di RAM → sangat cepat
Struktur : KEY → VALUE (contoh: "nama" → "Budi")
Port     : 6379 (default)
Masalah  : Sering tidak dikonfigurasi password → siapapun bisa konek langsung

Tipe data yang didukung :
  String      → teks/angka biasa
  List        → daftar berurutan
  Set         → kumpulan unik
  Hash        → field:value (mirip objek)
  Sorted Set  → data dengan skor/ranking

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TOOL UTAMA : redis-cli
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Install  : sudo apt install redis-tools
Fungsi   : Berinteraksi dengan Redis server dari terminal

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SWITCH redis-cli
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-h <IP>    → tentukan host/IP server target
             tanpa -h = konek ke localhost (127.0.0.1)
-p <PORT>  → tentukan port (default sudah 6379)

Contoh :
  redis-cli -h 10.129.8.170
  redis-cli -h 10.129.8.170 -p 6379

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 COMMAND PENTING DI DALAM redis-cli
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ping          → cek koneksi → harusnya balas PONG
info          → lihat semua info & statistik server
info server   → hanya tampil bagian server (versi, OS, port)
select <N>    → pindah ke database index N (0-15)
dbsize        → hitung jumlah keys di database aktif
keys *        → tampilkan semua keys (* = wildcard = semua)
get <key>     → ambil value dari key tertentu

Catatan select :
  Redis punya 16 database (index 0-15)
  Untuk pindah database → select 1, select 2, dst
  Tidak ada command "keluar" khusus → cukup select database lain

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 INFO PENTING DARI COMMAND info
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Server   → redis_version, OS, port
# Clients  → jumlah koneksi aktif
# Memory   → penggunaan RAM
# Keyspace → database mana yang ada isinya (PALING PENTING buat CTF)

Contoh Keyspace :
  db0:keys=4,expires=0,avg_ttl=0
  → artinya database 0 punya 4 keys

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR EKSPLOITASI REDIS (CTF)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Nmap scan → temukan port 6379 terbuka
   nmap -p- --min-rate 5000 10.129.8.170

2. Konek ke Redis
   redis-cli -h 10.129.8.170

3. Cek koneksi
   ping → harus balas PONG

4. Lihat info server
   info server → catat versi Redis

5. Lihat Keyspace
   info → scroll ke bagian # Keyspace
   → cari db mana yang ada isinya

6. Pilih database
   select 0

7. Hitung keys
   dbsize

8. Lihat semua keys
   keys *

9. Ambil value flag
   get flag

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SWITCH NMAP YANG DIPAKAI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-p-          → scan semua port (1-65535)
--min-rate   → set kecepatan minimum paket per detik
               contoh: --min-rate 5000
-T5          → timing template tercepat (alternatif --min-rate)
-sV          → deteksi versi service di tiap port

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
In-memory    = data hidup di RAM, bukan disk → cepat tapi hilang saat mati
Key-Value    = struktur data paling simpel, satu kunci → satu nilai
Wildcard (*)  = karakter pengganti "semua" → keys * = tampilkan semua keys
Keyspace     = informasi tentang database mana di Redis yang berisi data
Misconfigured= server tidak dipasang password → celah keamanan umum Redis
```