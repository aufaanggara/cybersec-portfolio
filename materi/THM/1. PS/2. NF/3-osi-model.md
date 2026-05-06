```
=== OSI Model - Resume Materi ===
[05 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU MODEL OSI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kepanjangan : Open Systems Interconnection Model
Fungsi      : Kerangka kerja standar yang mengatur bagaimana perangkat
              jaringan mengirim, menerima, dan menginterpretasikan data
Manfaat     : Perangkat dengan fungsi & desain berbeda tetap bisa
              berkomunikasi satu sama lain dalam jaringan
Konsep kunci: Encapsulation → setiap layer menambahkan informasi ke data
              saat melewati layer tersebut
Jumlah layer: 7 layer, disusun dari Layer 7 (atas) ke Layer 1 (bawah)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 7 LAYER OSI (HAFALAN URUTAN)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mnemonic : "All People Seem To Need Data Processing"
           Application → Physical (dari atas ke bawah)

7. Application
6. Presentation
5. Session
4. Transport
3. Network
2. Data Link
1. Physical

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LAYER 1 - PHYSICAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Menangani komponen fisik hardware jaringan
Cara     : Menggunakan sinyal listrik untuk transfer data
Format   : Sistem biner → hanya mengenal angka 1 dan 0
Contoh   : Kabel Ethernet (RJ-45), Wi-Fi, kabel fiber optik, hub
Catatan  : Tidak peduli isi data → hanya memindahkan sinyal mentah

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LAYER 2 - DATA LINK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Pengalamatan FISIK dari transmisi data
Menerima : Paket dari Network Layer (sudah berisi IP address)
Menambah : MAC address perangkat penerima ke paket tersebut
Komponen : NIC (Network Interface Card) → kartu jaringan di setiap komputer
           → setiap NIC punya MAC address UNIK

MAC Address :
  → Ditetapkan oleh produsen hardware (manufacturer)
  → Dibakar langsung ke kartu (burnt in) → permanen
  → TIDAK bisa diubah, tapi BISA di-spoof (dipalsukan)
  → Digunakan untuk menentukan tujuan pengiriman data secara fisik

Fungsi tambahan : Menyajikan data dalam format yang sesuai untuk transmisi
Contoh perangkat : Switch, kartu jaringan (NIC)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LAYER 3 - NETWORK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Routing & re-assembly data
           (memecah data jadi paket kecil saat kirim,
            menyusun kembali jadi utuh saat terima)
Routing  : Menentukan jalur PALING OPTIMAL untuk mengirim paket

Faktor penentu rute :
  → Jalur terpendek  = jumlah perangkat paling sedikit yang dilalui
  → Jalur terandal   = jalur yang paling jarang kehilangan paket
  → Koneksi tercepat = tembaga (lambat) vs fiber optik (cepat)

Protokol :
  OSPF = Open Shortest Path First
  RIP  = Routing Information Protocol

Pengalamatan  : Menggunakan IP Address (contoh: 192.168.1.100)
Perangkat kunci: Router → disebut Layer 3 devices

Re-assembly   : Data dipecah jadi paket-paket kecil saat dikirim,
                lalu disusun kembali jadi utuh di sisi penerima

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LAYER 4 - TRANSPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Mentransmisikan data antar perangkat via dua protokol

── TCP (Transmission Control Protocol) ──
Sifat    : Mengutamakan KEANDALAN & JAMINAN
Cara     : Menjaga koneksi KONSTAN selama pengiriman berlangsung
           Memiliki error checking → pastikan data sampai urut & lengkap
Cocok    : File sharing, browsing internet, kirim email
           (layanan yang butuh data AKURAT & LENGKAP)

Kelebihan TCP            | Kekurangan TCP
─────────────────────────┼──────────────────────────────────────────
Menjamin akurasi data    | Butuh koneksi andal → 1 paket hilang =
                         | seluruh data tidak bisa digunakan
Sinkronisasi 2 perangkat | Koneksi lambat → bottleneck perangkat lain
agar tidak dibanjiri data| karena koneksi terus direservasi
Banyak proses keandalan  | Lebih LAMBAT dari UDP

── UDP (User Datagram Protocol) ──
Sifat    : Tidak secanggih TCP, tanpa jaminan & sinkronisasi
Cara     : Data dikirim entah sampai atau tidak → "hope for the best"
           Tidak ada error checking, tidak ada koneksi konstan
Cocok    : Video streaming, ARP, DHCP
           (data kecil atau tidak apa-apa jika sebagian hilang)

Kelebihan UDP                        | Kekurangan UDP
─────────────────────────────────────┼─────────────────────────────────────
Jauh lebih CEPAT dari TCP            | Tidak peduli data diterima atau tidak
Application layer yang kontrol       | Fleksibel tapi tidak ada kepastian
kecepatan pengiriman paket           |
Tidak mereservasi koneksi konstan    | Koneksi tidak stabil = pengalaman
                                     | buruk bagi pengguna

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LAYER 5 - SESSION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Membuat, mempertahankan, dan menutup SESI komunikasi
Sesi     : Terbentuk saat koneksi berhasil dibuat → aktif selama koneksi aktif
Menutup  : Otomatis tutup koneksi jika tidak digunakan atau terputus
Checkpoint: Jika data hilang → hanya data TERBARU yang perlu dikirim ulang
            → menghemat bandwidth
Sifat    : Sesi bersifat UNIK → data hanya bisa mengalir di dalam satu sesi
           tidak bisa berpindah ke sesi lain

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LAYER 6 - PRESENTATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Standarisasi format data agar bisa dipahami semua perangkat
Peran    : Translator antara Application Layer (7) dan layer di bawahnya
Dua arah :
  Mengirim  → enkripsi + kompresi data
  Menerima  → dekripsi + dekompresi data
Contoh   : Kamu dan temanmu pakai email client berbeda → isi email tetap sama
Keamanan : Enkripsi terjadi di layer ini → contoh: HTTPS saat akses situs aman

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LAYER 7 - APPLICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Layer yang paling dekat dengan pengguna (end user)
           Menyediakan protokol & aturan untuk interaksi pengguna dengan data
Antarmuka: GUI (Graphical User Interface) → tampilan ramah pengguna
Contoh   : Browser, email client, FileZilla (FTP client)
Protokol : DNS (Domain Name System) → menerjemahkan nama domain ke IP address
           Contoh: google.com → 142.250.x.x

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERBANDINGAN TCP vs UDP (RINGKAS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
               TCP              UDP
Kecepatan  : Lambat           Cepat
Keandalan  : Sangat andal     Tidak ada jaminan
Error check: Ada              Tidak ada
Koneksi    : Konstan          Tidak ada koneksi permanen
Cocok untuk: File, web, email Video streaming, ARP, DHCP

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Encapsulation  = proses penambahan informasi ke data di setiap layer
Re-assembly    = penyusunan ulang paket-paket kecil menjadi data utuh
Packet         = potongan kecil data yang dikirim melalui jaringan
MAC Address    = alamat fisik unik yang dibakar ke NIC oleh produsen
IP Address     = alamat logis yang digunakan di Layer 3 untuk routing
NIC            = Network Interface Card, kartu jaringan di setiap komputer
Routing        = proses menentukan jalur terbaik untuk mengirim paket
Spoofing       = memalsukan identitas → contoh: MAC spoofing
Bottleneck     = kondisi satu titik memperlambat seluruh sistem
Checkpoint     = penanda kemajuan di session layer agar tidak kirim ulang semua
GUI            = Graphical User Interface, antarmuka visual untuk pengguna
DNS            = Domain Name System, terjemahkan domain ke IP address
OSPF           = Open Shortest Path First, protokol routing Layer 3
RIP            = Routing Information Protocol, protokol routing Layer 3
```