```
=== Windows Fundamentals 1 - Resume Materi ===
[15 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 WINDOWS EDITIONS & SEJARAH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Berdiri  : 1985 → OS paling dominan di rumahan & korporat
Urutan   : XP → Vista (gagal) → 7 → 8.x (gagal) → 10 → 11
Sekarang : Desktop = Windows 11 (Home & Pro)
           Server  = Windows Server 2025
Penting  : End-of-life XP → kepanikan massal → vendor scramble ke Win7
           Win7 langsung ditandai end-of-support setelah rilis
Win 10   : Support berakhir 14 Oktober 2025
Win 11   : Dirilis 5 Oktober 2021

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 THE DESKTOP (GUI) - 7 KOMPONEN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GUI = Graphical User Interface
Login : harus lewat login screen dulu → username & password
        (local account ATAU Active Directory jika domain-joined)

1. Desktop
   → Tempat shortcut program, folder, file
   → Klik kanan → context menu → ubah ukuran ikon, susun, buat baru
   → Display Settings → resolusi, orientasi, multi-monitor
   → Personalize → wallpaper, font, tema, warna

2. Start Menu
   → Logo Windows (bukan tulisan "Start" lagi sejak Win10)
   → 3 bagian :
     Kiri bawah = shortcuts akun (Documents, Pictures, Settings, Power)
     Tengah     = Recently Added + semua app urut alfabet
     Kanan      = Tiles (bisa pin/unpin, resize, klik kanan untuk opsi)
   → Tombol hamburger (≡) = expand/collapse panel kiri

3. Search Box (Cortana)
   → Cari app, file, pengaturan langsung dari taskbar
   → Hidden = sembunyikan search box sepenuhnya

4. Task View
   → Tombol di taskbar untuk lihat semua window & virtual desktop
   → Opsi : Show Task View button (uncheck = hilang)

5. Taskbar
   → Semua app/file yang sedang terbuka muncul di sini
   → Hover icon → preview thumbnail + tooltip
   → Klik kanan taskbar → context menu pengaturan
   → Tutup app → hilang dari taskbar (kecuali di-pin)

6. Toolbars
   → Komponen opsional di taskbar
   → Diaktifkan/dinonaktifkan via klik kanan taskbar

7. Notification Area
   → Pojok kanan bawah → tampilkan jam, tanggal
   → Ikon : volume, network, Action Center, dll
   → Atur via : klik kanan taskbar → Taskbar settings →
                scroll ke Notification Area →
                "Select which icons appear on the taskbar"
                "Turn system icons on or off"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FILE SYSTEM - NTFS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Urutan   : FAT16/FAT32 → HPFS → NTFS (modern Windows)
FAT      : Masih dipakai di USB, MicroSD — BUKAN di PC/laptop/server
NTFS     : Journaling file system → auto-repair pakai log file jika gagal
           FAT TIDAK punya fitur journaling ini

Keunggulan NTFS vs FAT :
  ✓ Support file > 4GB
  ✓ Set permission spesifik pada folder & file
  ✓ Kompresi folder & file
  ✓ Enkripsi (EFS = Encryption File System)

Cek file system : klik kanan drive C → Properties

NTFS PERMISSIONS (6 jenis) :
┌─────────────────┬──────────────────────────┬─────────────────────────┐
│ Permission      │ Folder                   │ File                    │
├─────────────────┼──────────────────────────┼─────────────────────────┤
│ Read            │ Lihat & list isi folder  │ Lihat/akses isi file    │
│ Write           │ Tambah file & subfolder  │ Tulis ke file           │
│ Read & Execute  │ Lihat+list+eksekusi      │ Lihat+akses+eksekusi    │
│                 │ (diwariskan file+folder) │                         │
│ List Folder     │ Lihat+list+eksekusi      │ N/A                     │
│ Contents        │ (hanya diwariskan folder)│                         │
│ Modify          │ Baca+tulis+hapus folder  │ Baca+tulis+hapus file   │
│ Full Control    │ Baca+tulis+ubah+hapus    │ Baca+tulis+ubah+hapus   │
└─────────────────┴──────────────────────────┴─────────────────────────┘

Cara lihat permission :
  Klik kanan file/folder → Properties → tab Security →
  pilih user/group di "Group or user names"

ADS (Alternate Data Streams) :
  → Atribut file spesifik NTFS
  → Setiap file punya minimal 1 stream ($DATA)
  → ADS = file bisa punya LEBIH dari 1 stream data
  → Windows Explorer TIDAK menampilkan ADS secara default
  → Bisa dilihat via PowerShell atau tool pihak ketiga
  → Dipakai malware untuk SEMBUNYIKAN data
  → Penggunaan normal : tandai file yang diunduh dari internet
  → Bonus : eksplorasi Day 21 Advent of Cyber 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 WINDOWS\SYSTEM32 FOLDERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Windows folder : C:\Windows (default, tapi BISA di drive lain)
Env variable   : %windir% → selalu menunjuk ke lokasi folder Windows
                 (simpan info path OS, jumlah prosesor, lokasi temp folder)

System32 : C:\Windows\System32
           → Berisi 3.975+ item
           → Menyimpan file KRITIS untuk OS
           → JANGAN hapus file di sini → OS bisa tidak bisa jalan
           → Banyak tools Windows Fundamentals ada di sini

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 USER ACCOUNTS, PROFILES, PERMISSIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2 Tipe akun :
  Administrator → bisa: tambah/hapus user, modif grup, modif settings
  Standard User → hanya bisa ubah folder/file miliknya sendiri
                  TIDAK bisa: install program, perubahan system-level

Cara lihat akun :
  Start Menu → ketik "Other User" → System Settings > Other users
  ATAU : klik kanan Start Menu → Run → ketik lusrmgr.msc

lusrmgr.msc (Local User and Group Management) :
  → 2 folder : Users dan Groups
  → Users  : daftar semua akun lokal
  → Groups : daftar grup + deskripsi singkat
  → Setiap grup punya permission → user yang masuk grup = MEWARISI permission
  → 1 user bisa masuk ke BEBERAPA grup sekaligus

User Profile :
  → Dibuat otomatis saat user pertama kali login
  → Lokasi : C:\Users\[nama_user]  contoh: C:\Users\Max
  → Proses pembuatan : tampil pesan "User Profile Service" di login screen
  → Setiap profil punya folder default : Desktop, Documents,
    Downloads, Music, Pictures

Cara ubah tipe akun :
  Settings → Other users → klik akun → Change account type →
  pilih dari dropdown (Standard User / Administrator)
  Catatan : Standard User TIDAK bisa lihat opsi "Add someone else to this PC"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 USER ACCOUNT CONTROL (UAC)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Masalah  : User login sebagai admin → semua proses jalan dengan hak penuh
           → malware ikut dapat hak penuh → berbahaya
Solusi   : UAC → diperkenalkan sejak Windows Vista
Catatan  : UAC default TIDAK berlaku untuk built-in local administrator

Cara kerja :
  → Saat login sebagai admin → sesi TIDAK langsung elevated
  → Jika ada operasi butuh privilege tinggi → muncul PROMPT konfirmasi
  → User harus klik Yes atau masukkan password admin

Tanda UAC diperlukan :
  → Ada SHIELD ICON (perisai kuning-biru) di atas ikon program
  → Artinya : untuk jalankan/install program ini butuh konfirmasi UAC

Saat login sebagai Standard User coba install :
  → Prompt UAC muncul → minta username & password Administrator
  → Jika password tidak dimasukkan dalam waktu tertentu →
    prompt hilang sendiri → program TIDAK terinstall
  → Fitur ini KURANGI risiko malware berhasil masuk ke sistem

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SETTINGS vs CONTROL PANEL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Control Panel : → Sudah ada lama → pengaturan kompleks & lanjutan
                → Diakses via Start Menu atau tiles
                → View by: Category / Large icons / Small icons
                → Programs → Programs and Features → lihat app terinstall
                  (nama, publisher, versi)

Settings Menu : → Diperkenalkan Windows 8 (untuk touchscreen)
                → Sekarang jadi lokasi UTAMA pengaturan di Win10
                → Kategori : System, Devices, Network & Internet,
                  Personalization, Apps, Accounts, Time & Language,
                  Ease of Access, Privacy, Update & Security, Search

Hubungan keduanya :
  → Bisa mulai dari Settings → berakhir di Control Panel
  → Contoh : Settings → Network & Internet → Change adapter options
             → jendela yang muncul DARI Control Panel (Network Connections)

Tips : Tidak tahu harus buka yang mana?
       → Cari via Start Menu search → sistem akan tunjukkan hasil yang tepat

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TASK MANAGER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Monitor aplikasi & proses yang sedang berjalan
           + info penggunaan CPU & RAM (Performance)

Cara buka :
  → Klik kanan taskbar → Task Manager
  → Shortcut keyboard : Ctrl + Shift + Esc

Tampilan :
  Simple View  : hanya tampilkan app yang terbuka, tombol "More details"
  More details : tampilan lengkap dengan tab-tab berikut →
    • Processes   : daftar Apps + Background processes (CPU%, Memory)
    • Performance : grafik penggunaan CPU, RAM, Disk, Network
    • Users       : siapa saja yang login & resource usage-nya
    • Details     : detail teknis tiap proses (PID, status, dll)
    • Services    : daftar Windows services yang berjalan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 REMOTE DESKTOP (RDP)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Akses & kontrol komputer lain dari jarak jauh
Protocol : RDP (Remote Desktop Protocol)
Tool     : Remote Desktop Connection (bawaan Windows)
Cara     : Isi Computer = IP target, Show Options → isi username
           → Connect → masukkan password

Catatan penting :
  → Di sesi Remote Desktop, BEBERAPA display settings dinonaktifkan
    (Scale and Layout & Resolution tidak bisa diubah dari remote)
  → Untuk ganti akun di environment TryHackMe/VM :
    Buka RDP baru dengan kredensial akun yang berbeda

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GUI              = Graphical User Interface → tampilan visual OS
NTFS             = New Technology File System → file system modern Windows
FAT              = File Allocation Table → file system lama (USB, SD card)
Journaling       = sistem log perubahan → auto-repair jika terjadi kegagalan
EFS              = Encryption File System → enkripsi bawaan NTFS
ADS              = Alternate Data Streams → data tersembunyi dalam file NTFS
$DATA            = stream default yang dimiliki setiap file
%windir%         = environment variable yang menunjuk ke folder Windows
Environment Var  = variabel yang simpan info tentang lingkungan OS
UAC              = User Account Control → proteksi privilege elevation
Shield Icon      = tanda bahwa file/program butuh konfirmasi UAC
Elevated Priv    = hak akses tinggi (admin level) untuk jalankan operasi
Active Directory = sistem manajemen akun terpusat untuk jaringan domain
Domain-joined    = komputer yang tergabung dalam jaringan domain
lusrmgr.msc      = tool Local User and Group Management
End-of-life      = tanggal berakhirnya dukungan resmi untuk suatu produk
```