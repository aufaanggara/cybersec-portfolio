```
=== Wireshark: The Basics - Resume Materi ===
[10 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU WIRESHARK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Open-source, cross-platform network packet analyser
Fungsi   : Sniffing & investigasi live traffic + inspeksi PCAP
Penting  : BUKAN IDS → hanya BACA paket, tidak modifikasi
           Hasil analisis bergantung pada keahlian analistnya

Use Cases:
  → Deteksi & troubleshoot masalah jaringan (load failure, congestion)
  → Deteksi anomali keamanan (rogue host, abnormal port, suspicious traffic)
  → Investigasi detail protokol (response code, payload data)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 5 BAGIAN UTAMA GUI WIRESHARK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Toolbar          → Menu & shortcut (filter, sort, export, merge)
Display Filter   → Kolom query & filtering utama
Recent Files     → File PCAP yang baru dibuka (double-click untuk buka)
Capture Filter   → Filter & sniffing interfaces (lo, eth0, ens33, dll)
  & Interfaces
Status Bar       → Status tool, profil, info numerik paket

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 3 PANEL SAAT PCAP DIBUKA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Packet List Pane    → Ringkasan tiap paket (src, dst, protokol, info)
                      Klik untuk pilih → detail muncul di panel bawah
Packet Details Pane → Breakdown protokol detail dari paket yang dipilih
Packet Bytes Pane   → Representasi Hex + ASCII dari paket yang dipilih
                      Menyorot field sesuai yang diklik di details pane

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FITUR MANAJEMEN FILE PCAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Load PCAP    → File menu / drag-drop / double-click
Merge PCAP   → File → Merge → gabung 2 file jadi 1 (harus di-save dulu)
View Details → Statistics → Capture File Properties
               Isi : hash (MD5/SHA256), waktu capture, interface,
                     komentar file, total paket

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TRAFFIC SNIFFING (TOMBOL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Biru  (Shark) → START sniffing
Merah         → STOP sniffing
Hijau         → RESTART sniffing

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 7 LAYER PACKET DISSECTION (OSI)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Layer 1 - Frame/Packet   → Info fisik: ukuran, waktu tiba, interface,
                            protokol dalam frame, coloring rule
Layer 2 - Source [MAC]   → MAC address src & dst (Data Link Layer)
                            Ethernet II, Type: IPv4/IPv6
Layer 3 - Source [IP]    → IP address src & dst (Network Layer)
                            TTL, protokol, flags, checksum
Layer 4 - Protocol       → TCP/UDP: port src & dst, seq/ack number,
                            flags (SYN/ACK/PSH), window size
Protocol Errors          → Lanjutan Layer 4: TCP segments yang di-reassemble
                            Contoh: 2 segment digabung jadi 1 data utuh
Layer 5 - App Protocol   → Detail protokol aplikasi: HTTP, FTP, SMB
                            Header HTTP: status code, server, content-type
App Data                 → Isi konten aplikasi: HTML, XML, teks mentah

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TTL (TIME TO LIVE) - WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Batas maksimum hop sebelum paket dibuang router
Cara     : Tiap melewati 1 router → TTL dikurang 1
           TTL = 0 → paket DIBUANG (tidak diteruskan)
Tujuan   : Cegah paket nyasar selamanya di jaringan

TTL Awal per OS (untuk analisis):
  Windows → 128
  Linux   → 64
  Cisco   → 255

Contoh   : TTL tersisa 47 + OS Linux (64) → 64-47 = 17 hop sudah dilewati
Catatan  : Bisa dimodifikasi manual → gunakan sebagai petunjuk awal saja

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 E-TAG & HTTP CACHE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
E-Tag        → "Sidik jari" versi konten dari server
Last-Modified→ Tanggal terakhir konten diubah di server
200 OK       → FRESH download → server kirim konten baru + Content-Length > 0
304 Not Mod. → CACHE → server bilang "sama aja, pakai yang lama"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NAVIGASI PAKET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Go to Packet → Ctrl+G → loncat ke nomor paket tertentu
Find Packet  → Ctrl+F → cari paket berdasarkan konten
               4 tipe input : Display Filter / Hex / String / Regex
               3 search field: Packet List / Packet Details / Packet Bytes
               PENTING: cari di tempat yang BENAR sesuai letak informasinya

Mark Packet  → Edit / right-click → tandai paket penting
               Warna HITAM saat di-mark
               HILANG setelah file ditutup (tidak permanen)

Comment      → Right-click → Packet Comments → tambah catatan
               PERMANEN di dalam file sampai dihapus manual

Export Packet→ File → Export Packets
               Opsi: All / Selected / Marked / Range / First-Last Marked

Export Object→ File → Export Objects → HTTP/FTP/SMB/DICOM/TFTP
               Untuk ekstrak file yang dikirim lewat jaringan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PEWARNAAN PAKET (COLORING)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Temporary → Right-click → Colorize Conversation (hilang saat restart)
Permanent → View → Coloring Rules (tersimpan di profil)
Toggle    → View → Colorize Packet List (aktif/nonaktif)
Reset     → View → Colorize Conversation → Reset Colourisation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TIME DISPLAY FORMAT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Default  → Seconds Since Beginning of Capture (angka detik dari awal)
Rekomend → UTC Time Display Format (waktu nyata, mudah korelasi dengan log)
Ganti    → View → Time Display Format

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 EXPERT INFO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Akses    → Analyse → Expert Information / klik ikon pojok kiri bawah
Fungsi   → Deteksi otomatis anomali & masalah protokol

Severity :
  Chat  (Biru)   → Info alur kerja normal
  Note  (Cyan)   → Event penting, error code aplikasi
  Warn  (Kuning) → Peringatan, error code tidak biasa
  Error (Merah)  → Masalah serius, paket malformed

Group    :
  Checksum  → Checksum errors
  Comment   → Packet comment detection
  Deprecated→ Deprecated protocol usage
  Malformed → Malformed packet detection

Info     → Menampilkan: nomor paket, summary, group protokol, total kemunculan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PACKET FILTERING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2 Jenis Filter:
  Capture Filter  → Filter SAAT merekam (hanya tangkap paket tertentu)
  Display Filter  → Filter SAAT melihat (sembunyikan paket yang tidak relevan)

Golden Rule: "If you can click on it, you can filter and copy it"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CARA-CARA FILTERING (RIGHT-CLICK)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Apply as Filter      → Filter langsung 1 nilai, filter LANGSUNG diterapkan
Prepare as Filter    → Tambah query dulu, BELUM diterapkan sampai tekan Enter
                       Bisa kombinasi dengan AND/OR
Conversation Filter  → Tampilkan SEMUA paket terkait percakapan itu
                       (berdasarkan IP & port) → paket lain disembunyikan
Colourise Convers.   → Sorot paket terkait dengan warna TANPA hide yang lain
Apply as Column      → Tambah field sebagai kolom baru di Packet List Pane
Follow Stream        → Rekonstruksi percakapan lengkap level aplikasi
                       Merah = dari client, Biru = dari server
                       Opsi: TCP Stream / HTTP Stream / UDP Stream / TLS Stream
                       HTTP Stream = lebih bersih (sudah diparse)
                       TCP Stream  = lebih raw (termasuk header)
                       Hapus filter stream: klik X di Display Filter Bar

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DISPLAY FILTER QUERIES - WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Filter by Protocol Name:
  http        → tampilkan hanya HTTP
  dns         → tampilkan hanya DNS
  tcp         → tampilkan hanya TCP
  arp / dhcp / ftp / smtp / pop / imap

Filter by Port:
  tcp.port == 80      → HTTP lewat TCP port 80
  udp.port == 53      → DNS lewat UDP port 53

Filter by IP:
  ip.addr == 192.168.1.2    → semua paket yang melibatkan IP ini
  ip.src == 192.168.1.2     → hanya paket DARI IP ini
  ip.dst == 192.168.1.2     → hanya paket KE IP ini

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HASHING FILE DI TERMINAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MD5    → md5sum namafile
SHA256 → sha256sum namafile
Output → 32 karakter (MD5) / 64 karakter (SHA256) + nama file

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PCAP         = Packet Capture, format file rekaman traffic jaringan
Sniffing     = Proses menangkap/merekam traffic jaringan
Dissection   = Membedah paket dengan decode protokol layer per layer
Reassemble   = Menyatukan kembali potongan paket TCP yang dipecah
Hop          = Satu lompatan paket melewati satu router
Payload      = Isi data/konten dalam sebuah paket
Stream       = Rangkaian paket yang membentuk satu percakapan utuh
Interface    = Titik koneksi antara komputer dan jaringan (eth0, lo, dll)
Capture File = File PCAP yang berisi rekaman traffic jaringan
Malformed    = Paket yang strukturnya rusak/tidak sesuai standar protokol
ASCII Art    = Gambar/teks yang dibuat dari karakter teks biasa
Monospace    = Font yang tiap karakternya punya lebar sama (penting ASCII art)
```