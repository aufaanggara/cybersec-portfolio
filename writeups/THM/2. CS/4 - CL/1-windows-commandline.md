```
=== Windows Command Line (CMD) - Resume Materi ===

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KENAPA CLI LEBIH BAIK DARI GUI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Lower Resource  = Tidak butuh grafis → cocok untuk hardware lama & cloud
Automation      = Mudah buat script/batch untuk otomatisasi tugas berulang
Remote Mgmt     = SSH ke server/router/IoT lewat jaringan lambat sekalipun
Speed           = Tidak perlu angkat tangan dari keyboard

Default CMD     = cmd.exe (command-line interpreter bawaan Windows)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TIPS UMUM CMD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
perintah /?     = tampilkan halaman bantuan perintah apapun
perintah | more = tampilkan output panjang halaman per halaman
                  Spacebar = next page | Enter = next line | CTRL+C = keluar
more file.txt   = baca isi file teks halaman per halaman
cls             = bersihkan layar CMD
help            = info bantuan untuk perintah tertentu

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SYSTEM INFORMATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
set             = lihat semua environment variable + Windows PATH
ver             = lihat versi OS Windows
systeminfo      = info lengkap sistem (OS, hardware, prosesor, memori)

PATH            = daftar direktori tempat Windows mencari executable
                  hanya perintah di dalam PATH yang bisa dijalankan langsung

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NETWORK CONFIGURATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ipconfig        = tampilkan IP address, subnet mask, default gateway
ipconfig /all   = info lengkap (MAC address, DHCP status, DNS server,
                  lease obtained/expires, dll)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NETWORK TROUBLESHOOTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ping target     = kirim paket ICMP → cek apakah target bisa dijangkau
                  Jika reply = koneksi OK | Jika timeout = tidak bisa reach
                  Output : bytes, time (ms), TTL, statistik packet loss

tracert target  = trace route → lacak semua router yang dilalui ke target
                  Tiap baris = 1 hop (router)
                  * = router tidak merespons (bukan berarti putus)
                  Singkatan dari : trace route

nslookup domain           = cari IP dari domain pakai DNS server default
nslookup domain 1.1.1.1   = cari IP dari domain pakai DNS server tertentu
                            Hasil sama tapi sumber berbeda

netstat         = tampilkan koneksi aktif yang sudah ESTABLISHED
netstat -h      = tampilkan semua opsi netstat

SWITCH NETSTAT :
  -a  = tampilkan semua koneksi + port LISTENING
  -b  = tampilkan nama executable/program tiap koneksi
  -o  = tampilkan PID tiap koneksi
  -n  = tampilkan alamat dalam bentuk numerik (bukan hostname)
  Kombinasi : netstat -abon → output lengkap semua info
  ⚠️  netstat -abon butuh Run as Administrator

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FILE & DIRECTORY MANAGEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
cd              = tampilkan posisi direktori saat ini (where am I?)
cd target       = pindah ke direktori target
cd ..           = naik satu level direktori
dir             = tampilkan isi direktori (nama, ukuran, tanggal)
tree            = tampilkan struktur direktori secara visual

SWITCH DIR :
  dir /a  = tampilkan file tersembunyi & system files
  dir /s  = tampilkan file di direktori ini + semua subdirektori

mkdir nama      = buat direktori baru (make directory)
rmdir nama      = hapus direktori (remove directory)

type file.txt   = tampilkan isi file teks langsung ke layar
copy A B        = salin file A ke B (A tetap ada, B baru dibuat)
move A tujuan   = pindahkan file A ke tujuan (A hilang dari asal)
del file        = hapus file
erase file      = hapus file (sama dengan del)

WILDCARD :
  *             = semua file / karakter apapun
  Contoh : copy *.md C:\Markdown → salin semua file .md ke C:\Markdown

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TASK & PROCESS MANAGEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
tasklist        = tampilkan semua proses yang berjalan (seperti Task Manager)
                  Kolom : Image Name | PID | Session Name | Session# | Mem Usage

tasklist /?     = lihat semua opsi & filter yang tersedia

FILTER TASKLIST :
  /FI "imagename eq nama.exe"  = filter berdasarkan nama program
  Contoh : tasklist /FI "imagename eq sshd.exe"

taskkill /PID nomor  = matikan proses berdasarkan PID
  Contoh : taskkill /PID 4567

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 BONUS COMMAND (TIDAK DIBAHAS DETAIL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
chkdsk          = periksa file sistem & disk dari error / bad sector
driverquery     = tampilkan daftar driver perangkat yang terinstal
sfc /scannow    = scan file sistem → perbaiki korupsi jika ditemukan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PID      = Process ID → nomor unik tiap proses yang berjalan
PATH     = variabel sistem berisi daftar folder tempat CMD cari executable
DHCP     = protokol yang otomatis kasih IP ke perangkat di jaringan
TTL      = Time To Live → batas berapa router boleh dilewati paket
Hop      = satu titik router yang dilalui dalam tracert
ICMP     = protokol yang dipakai ping untuk kirim & terima paket tes
LISTENING= port aktif menunggu koneksi masuk
ESTABLISHED = koneksi yang sudah terbentuk & aktif
```