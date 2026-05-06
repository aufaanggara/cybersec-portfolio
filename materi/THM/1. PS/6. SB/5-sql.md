```
=== Database & SQL - Resume Materi ===

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU DATA & DATABASE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Data     : Fakta/informasi mentah (nama, harga, waktu, dll)
Database : Sistem penyimpanan data secara TERSTRUKTUR
           → Ibarat buku catatan digital yang tidak pernah habis halaman
           → Bisa mencari, menghitung, mengurutkan data dengan SANGAT CEPAT
Masalah  : File biasa (buku/spreadsheet) → lambat & membingungkan saat data banyak
Solusi   : Database → terstruktur, mudah dicari, mudah dikelola
Fakta    : Bahkan ribuan data → database tetap jawab dalam hitungan detik

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 STRUKTUR DATABASE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Di dalam database, informasi disimpan dalam TABEL

TABEL   : Menyerupai spreadsheet → data diorganisir rapi ke baris & kolom
KOLOM   : Judul di bagian atas tabel → mendeskripsikan JENIS informasi
          Contoh : id, drink, price, time
BARIS   : Membentang melintasi tabel → berisi SATU set informasi lengkap
          Contoh : 1 baris = 1 pesanan kafe

Analogi Kafe :
  Kolom → nomor pesanan, minuman, harga, waktu
  Baris → SATU pesanan kafe (1 transaksi)
  Satu kolom = satu jenis info (misal: hanya harga)
  Satu baris = semua info tentang satu pesanan

Aturan tabel :
  → Kafe jual 10 minuman = tabel punya 10 baris
  → Pelanggan baru pesan = 1 baris DITAMBAH
  → Pesanan dihapus = hanya baris itu yang HILANG, sisanya tetap

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU SQL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SQL     : Structured Query Language
Fungsi  : Bahasa untuk BERKOMUNIKASI dengan database
          → Menyimpan, mengambil, mengubah, menghapus data
Query   : Pertanyaan/perintah yang dikirim ke database
          → Query TIDAK mengubah data, hanya MENAMPILKAN informasi
Intinya : SQL = cara kita "bertanya" ke database tanpa baca satu per satu

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 4 PERINTAH SQL INTI (WAJIB HAPAL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SELECT   → Pilih kolom apa yang ingin ditampilkan
FROM     → Pilih dari tabel mana data diambil
WHERE    → Filter baris berdasarkan kondisi tertentu
ORDER BY → Urutkan hasil (default: ascending / terendah ke tertinggi)
           Tambah DESC → descending (tertinggi ke terendah)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 QUERY SQL & CONTOHNYA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
① Tampilkan SEMUA kolom dari tabel Orders :
   SELECT * FROM Orders;
   → * = semua kolom

② Tampilkan kolom TERTENTU saja :
   SELECT drink, price FROM Orders;
   → Hanya tampil kolom drink dan price

③ Filter berdasarkan kondisi :
   SELECT * FROM Orders WHERE drink = 'Coffee';
   → Hanya tampil baris yang drinknya Coffee

④ Urutkan hasil (ascending) :
   SELECT * FROM Orders ORDER BY price;
   → Harga terendah → tertinggi

⑤ Urutkan hasil (descending) :
   SELECT * FROM Orders ORDER BY price DESC;
   → Harga tertinggi → terendah

⑥ Gabungkan filter + pengurutan :
   SELECT * FROM Orders WHERE drink = 'Coffee' ORDER BY price DESC;
   → Hanya Coffee, diurutkan harga tertinggi dulu

⑦ Cek nama minuman yang tersedia di Menu :
   SELECT * FROM Menu;

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TABEL LATIHAN (CAFÉ SQL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Orders : id | drink | price | time
Menu   : drink | price

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Database   : Sistem penyimpanan data terstruktur di komputer
Tabel      : Kumpulan data sejenis dalam format baris & kolom
Kolom      : Kategori/jenis data (vertikal)
Baris      : Satu entri/rekaman data lengkap (horizontal)
SQL        : Bahasa untuk berinteraksi dengan database
Query      : Perintah SQL untuk mengambil informasi
SELECT *   : Ambil semua kolom
WHERE      : Syarat/kondisi untuk memfilter data
ORDER BY   : Perintah pengurutan data
DESC       : Descending = dari besar ke kecil / Z ke A
ASC        : Ascending = dari kecil ke besar (DEFAULT, tidak perlu ditulis)
```

## Rangkuman Task 1 — Pengantar: Mengapa Database Ada?

---

Materi ini dibuka dengan pertanyaan sederhana tapi sangat relevan: *"Bagaimana sebuah kafe bisa melacak setiap pesanan dan tetap bisa menjawab pertanyaan tentang pesanan tersebut dengan cepat di kemudian hari?"* Pertanyaan ini bukan sekadar pembuka — ini adalah inti dari mengapa database diciptakan.

Komputer bisa memproses informasi selama menyala, tapi saat dimatikan, data yang hanya ada di memori (RAM) akan hilang sepenuhnya. Pertanyaannya kemudian: di mana data disimpan secara permanen dan bagaimana cara mengaksesnya kembali dengan efisien?

Ketika bisnis masih kecil, menyimpan data di buku catatan atau file biasa masih bisa ditoleransi. Tapi saat bisnis berkembang, cara itu menjadi lambat dan membingungkan — pemilik harus membaca halaman demi halaman hanya untuk menjawab pertanyaan seperti *"Berapa banyak kopi yang terjual hari ini?"*. Di sinilah **database** hadir sebagai solusi: menyimpan informasi secara **terstruktur** sehingga mudah dicari, difilter, dan dikelola.

---

### Tujuan Pembelajaran (Learning Objectives)

Setelah menyelesaikan course ini, ada lima hal yang harus dikuasai:

- Memahami apa itu data dan mengapa data penting — data adalah fakta mentah seperti nama, harga, dan waktu yang ketika diorganisir menjadi bermakna dan berguna.
- Menjelaskan apa itu database dan alasan penggunaannya — database adalah sistem penyimpanan data terstruktur yang memungkinkan pencarian dan pengelolaan data secara efisien.
- Memahami apa itu SQL dan kegunaannya — SQL adalah bahasa khusus yang digunakan untuk berkomunikasi dengan database, mulai dari menyimpan hingga mengambil data.
- Mengidentifikasi tabel, baris, dan kolom — tiga komponen struktural utama dalam database yang wajib dipahami sebelum bisa menulis query apapun.
- Menulis query SQL sederhana untuk mengambil informasi dari database.

---

### Prasyarat Pembelajaran (Learning Prerequisites)

Sebelum masuk ke materi ini, ada tiga fondasi yang harus sudah dipahami:

- **Inside a Computer System** — cara kerja komponen dalam komputer seperti prosesor, memori, dan penyimpanan, karena database erat kaitannya dengan bagaimana data disimpan secara fisik.
- **Client-Server Basics** — konsep hubungan antara klien (pengguna yang meminta data) dan server (yang menyimpan dan melayani data), karena database hampir selalu beroperasi dalam model ini.
- **Data Representation** — bagaimana data direpresentasikan dalam komputer dalam bentuk biner, teks, angka, dan sebagainya, karena database menyimpan berbagai tipe data tersebut.

---

## Rangkuman Task 2 — Memahami Tabel, Baris, dan Kolom

---

### Analogi Kafe: Masalah Nyata yang Dipecahkan Database

Untuk memahami mengapa database dibutuhkan, materi ini menggunakan cerita kafe kecil sebagai analogi. Awalnya, pemilik kafe mencatat setiap pesanan di buku catatan kertas. Setiap pesanan mencakup tiga informasi: nama minuman, harga, dan waktu pesanan masuk. Selama kafe masih kecil, cara ini berjalan baik.

Namun seiring waktu, buku catatan menjadi penuh. Menemukan jawaban atas pertanyaan seperti *"Berapa banyak kopi yang terjual hari ini?"* atau *"Apa minuman termurah yang terjual pagi ini?"* menjadi sangat lambat dan sulit karena pemilik harus membaca halaman demi halaman dan menghitung pesanan secara manual. Di sinilah komputer dan database menjadi solusi yang jauh lebih efisien.

---

### Apa Itu Database?

Database bisa dibayangkan sebagai tempat di mana komputer menyimpan informasi secara **terorganisir**. Lebih spesifiknya, database ibarat **buku catatan digital yang tidak pernah kehabisan halaman**. Perbedaan utamanya dengan buku catatan biasa adalah kemampuannya untuk mencari, menghitung, dan mengurutkan informasi dengan sangat cepat — bahkan jika kafe memiliki ribuan pesanan sekalipun, database tetap bisa menjawab pertanyaan hanya dalam hitungan detik.

Di dalam database, seluruh informasi disimpan dalam bentuk **tabel**.

---

### Struktur Tabel: Kolom dan Baris

Sebuah tabel menyerupai spreadsheet, di mana informasi diorganisir dengan rapi ke dalam baris dan kolom. Berikut contoh tabel pesanan kafe:

| ID | Name | Price | Time |
|----|------|-------|------|
| 1 | Coffee | 2.00 | 11:00 AM |
| 2 | Tea | 1.50 | 11:10 AM |
| 3 | Muffin | 2.50 | 11:15 AM |

**Kolom** adalah judul-judul yang berada di bagian atas tabel. Setiap kolom mendeskripsikan satu jenis informasi yang disimpan — misalnya kolom `price` hanya berisi data harga, tidak ada data lain. Dalam contoh kafe, kolom yang digunakan bisa berupa: nomor pesanan, minuman, harga, dan waktu.

**Baris** membentang secara horizontal melintasi tabel. Setiap baris berisi satu set informasi yang lengkap tentang satu entri — dalam konteks kafe, satu baris berarti **satu pesanan kafe**. Jadi jika kafe menjual sepuluh minuman dalam satu hari, tabel akan berisi tepat sepuluh baris. Jika satu pelanggan lagi memesan, satu baris baru ditambahkan. Jika sebuah pesanan dihapus, hanya baris tersebut yang hilang — sisa tabel tetap utuh dan tidak terpengaruh.

---

### Pengenalan SQL dan Konsep Query

**SQL (Structured Query Language)** adalah bahasa yang digunakan untuk mengajukan pertanyaan kepada database. Daripada harus membaca tabel baris per baris secara manual seperti membaca buku catatan, SQL memungkinkan komputer melakukan pekerjaan itu untuk kita secara otomatis dan instan.

Sebagai contoh, pemilik kafe bisa mengajukan pertanyaan seperti:
- *"Tampilkan semua pesanan."*
- *"Tampilkan hanya pesanan kopi."*
- *"Tampilkan minuman termurah."*

Pertanyaan-pertanyaan yang dikirim ke database ini disebut **query**. Satu hal penting yang harus dipahami: sebuah query **tidak mengubah data sama sekali** — query hanya menampilkan informasi yang diminta dari tabel, tanpa menyentuh atau memodifikasi data aslinya.

---

## Rangkuman Task 3 — Menulis Query SQL Pertama

---

### Setup Lingkungan Latihan

Untuk task ini, digunakan sebuah database client berbasis browser bernama **Café SQL** — sebuah simulasi kafe virtual yang aman untuk berlatih. Tidak ada yang bisa rusak di sini; jika membuat kesalahan, cukup klik **Reset Data** dan mulai lagi dari awal.

Di bagian atas halaman Café SQL, terdapat dua tabel yang tersedia untuk digunakan:
- **Orders** dengan kolom: `id`, `drink`, `price`, `time`
- **Menu** dengan kolom: `drink`, `price`

Tujuan dari task ini adalah berlatih menulis query menggunakan **empat bagian inti SQL**: `SELECT`, `FROM`, `WHERE`, dan `ORDER BY`.

---

### Step 1: Lihat Semua Data dalam Tabel (SELECT + FROM)

Ini adalah query paling dasar dalam SQL — digunakan untuk menampilkan seluruh isi sebuah tabel sekaligus.

```sql
SELECT * FROM Orders;
```

Cara membacanya: `SELECT *` berarti "pilih semua kolom", dan `FROM Orders` berarti "dari tabel Orders". Simbol `*` adalah cara cepat untuk meminta semua kolom yang ada tanpa harus menuliskannya satu per satu. Saat dijalankan, query ini akan menampilkan setiap pesanan yang saat ini tersimpan di database — seluruh kolom id, drink, price, dan time sekaligus.

---

### Step 2: Tampilkan Hanya Kolom Tertentu (SELECT kolom spesifik)

Kadang kita tidak membutuhkan semua kolom — hanya data tertentu saja yang relevan. Untuk itu, daripada menggunakan `*`, kita bisa menyebutkan nama kolom yang diinginkan secara spesifik setelah `SELECT`, dipisahkan dengan koma.

```sql
SELECT drink, price FROM Orders;
```

Query ini hanya akan menampilkan dua kolom saja yaitu `drink` dan `price`, meskipun tabel Orders sebenarnya punya empat kolom. Kolom `id` dan `time` tidak akan muncul di hasil. Ini berguna saat kita hanya butuh informasi spesifik dan ingin tampilan hasil yang lebih bersih dan fokus.

---

### Step 3: Filter Hasil Berdasarkan Kondisi (WHERE)

`WHERE` adalah kata kunci yang digunakan untuk memfilter baris — hanya baris yang memenuhi kondisi tertentu yang akan ditampilkan, sisanya diabaikan.

```sql
SELECT * FROM Orders WHERE drink = 'Coffee';
```

Query ini akan menampilkan semua kolom, tapi hanya untuk baris-baris yang kolom `drink`-nya bernilai `'Coffee'`. Jika database berisi pesanan kopi, hanya baris-baris tersebut yang muncul. Perhatikan bahwa nilai teks dalam kondisi WHERE ditulis menggunakan tanda kutip tunggal `' '`.

Jika tidak yakin nama minuman apa saja yang tersedia di database, bisa menjalankan query berikut terlebih dahulu untuk melihat daftar menu:

```sql
SELECT * FROM Menu;
```

---

### Step 4: Urutkan Hasil (ORDER BY + DESC)

`ORDER BY` adalah kata kunci untuk mengurutkan hasil query berdasarkan kolom tertentu. Secara default, pengurutan dilakukan secara **ascending** — dari nilai terendah ke tertinggi, atau dari A ke Z.

```sql
SELECT * FROM Orders ORDER BY price;
```

Query ini menampilkan semua pesanan yang diurutkan berdasarkan harga dari yang termurah hingga termahal. Untuk membalik urutan menjadi **descending** (tertinggi ke terendah), cukup tambahkan kata `DESC` di akhir:

```sql
SELECT * FROM Orders ORDER BY price DESC;
```

Dengan `DESC`, pesanan dengan harga tertinggi akan muncul paling atas. Hasil query ini mengembalikan 50 baris — seluruh pesanan yang ada di tabel, diurutkan dari harga paling mahal.

---

### Step 5: Gabungkan Filter + Pengurutan (WHERE + ORDER BY)

Inilah kekuatan sesungguhnya dari SQL — kemampuan menggabungkan beberapa perintah sekaligus dalam satu query. Sebagian besar query di dunia nyata mengombinasikan berbagai bagian ini untuk mendapatkan hasil yang spesifik dan terorganisir.

```sql
SELECT * FROM Orders WHERE drink = 'Coffee' ORDER BY price DESC;
```

Query ini melakukan dua hal sekaligus: pertama memfilter hanya baris yang drinknya `Coffee`, kemudian mengurutkan hasil tersebut berdasarkan harga dari yang tertinggi ke terendah. Hasilnya mengembalikan 10 baris — semua pesanan Coffee yang sudah terurut rapi dari harga paling mahal.

Urutan penulisan yang benar adalah: `SELECT` → `FROM` → `WHERE` → `ORDER BY`. Urutan ini tidak bisa ditukar-tukar karena SQL membacanya secara berurutan.

---

### Ringkasan Pola Query SQL

| Tujuan | Contoh Query |
|--------|-------------|
| Lihat semua data | `SELECT * FROM Orders;` |
| Pilih kolom tertentu | `SELECT drink, price FROM Orders;` |
| Filter berdasarkan kondisi | `SELECT * FROM Orders WHERE drink = 'Coffee';` |
| Urutkan ascending | `SELECT * FROM Orders ORDER BY price;` |
| Urutkan descending | `SELECT * FROM Orders ORDER BY price DESC;` |
| Filter + urutkan | `SELECT * FROM Orders WHERE drink = 'Coffee' ORDER BY price DESC;` |

---

## Rangkuman Task 4 — Kesimpulan

---

### Apa yang Sudah Dipelajari di Course Ini

Di course ini, kita belajar bagaimana komputer menyimpan informasi dalam database dan bagaimana SQL digunakan untuk mengajukan pertanyaan yang jelas dan efisien terhadap informasi tersebut. Menggunakan contoh kafe sebagai benang merah dari awal hingga akhir, kita melihat secara nyata bagaimana tabel mengorganisir pesanan ke dalam baris dan kolom, dan bagaimana perintah SQL sederhana bisa menampilkan, memfilter, mengurutkan, dan mengambil data yang kita butuhkan.

---

### Skills yang Berhasil Dikuasai

- **Memahami apa itu database** — bukan sekadar tempat penyimpanan biasa, melainkan sistem terstruktur yang mampu mengelola dan menjawab pertanyaan terhadap data dalam hitungan detik, bahkan untuk ribuan entri sekalipun.
- **Mengetahui apa itu tabel, baris, dan kolom** — tiga komponen struktural utama yang menjadi fondasi dari seluruh cara kerja database relasional.
- **Mengajukan pertanyaan sederhana menggunakan SQL** — menulis query dengan empat perintah inti yang memungkinkan kita berkomunikasi langsung dengan database tanpa harus membaca data satu per satu secara manual.
- **Membaca hasil yang dikembalikan oleh database** — memahami output query berupa tabel hasil yang berisi baris-baris data sesuai kondisi yang kita tentukan.

---

### Empat Perintah SQL Inti yang Wajib Diingat

- `SELECT` — menentukan **data apa** yang ingin ditampilkan, bisa semua kolom dengan `*` atau kolom spesifik dengan menyebutkan namanya.
- `FROM` — menentukan **dari tabel mana** data diambil, karena dalam satu database bisa terdapat banyak tabel sekaligus.
- `WHERE` — memfilter baris berdasarkan **kondisi tertentu**, sehingga hanya data yang relevan yang ditampilkan.
- `ORDER BY` — mengurutkan hasil berdasarkan kolom tertentu, secara ascending (default) atau descending dengan tambahan `DESC`.

---

### Pertanyaan Refleksi: Keamanan Data

Course ini ditutup dengan sebuah pertanyaan yang mengajak kita berpikir lebih jauh:

*"Apa yang bisa terjadi jika seseorang diizinkan untuk mengubah atau menghapus pesanan kafe tanpa izin?"*

Pertanyaan ini menyentuh konsep yang sangat penting dalam dunia database dan keamanan siber — yaitu **integritas data**. Jika data bisa diubah atau dihapus oleh sembarang orang tanpa kontrol, maka seluruh informasi dalam database menjadi tidak bisa dipercaya. Pesanan bisa hilang, catatan keuangan bisa dimanipulasi, dan keputusan bisnis bisa didasarkan pada data yang salah. Inilah mengapa dalam sistem database nyata selalu ada mekanisme **kontrol akses** — hanya pengguna dengan izin tertentu yang boleh melakukan operasi tertentu terhadap data.

---