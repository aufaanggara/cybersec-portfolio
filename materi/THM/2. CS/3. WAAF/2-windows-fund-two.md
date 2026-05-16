```
=== Windows Fundamentals 2 - Resume Materi ===
[16 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SYSTEM CONFIGURATION (MSConfig)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Advanced troubleshooting, diagnosa masalah startup
Buka via : Start Menu → ketik "msconfig" | Win+R → msconfig
Syarat   : Harus punya local administrator rights

5 Tab MSConfig :
  General  → Pilih mode startup Windows
             Normal    = load semua driver & service
             Diagnostic= load komponen dasar saja
             Selective = pilih manual apa yang di-load

  Boot     → Konfigurasi boot OS (Safe boot, No GUI boot,
             Boot log, Base video, OS boot info, Timeout)

  Services → Daftar semua service (running/stopped)
             Bisa hide Microsoft services untuk filter

  Startup  → Di Windows Server: KOSONG
             Gunakan Task Manager (taskmgr) untuk manage startup
             Atau akses via Win+R → shell:startup

  Tools    → Daftar utilitas yang bisa dilaunch langsung
             Ada "Selected command" = path lengkap tool tersebut
             Bisa dijalankan via Run/CMD menggunakan path itu

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TOOLS PENTING DI TAB TOOLS MSConfig
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tool Name              Command (Win+R)       Fungsi
─────────────────────────────────────────────────────
About Windows          winver                Info versi & lisensi Windows
Change UAC Settings    (via Control Panel)   Ubah level UAC
Windows Troubleshoot   control /name         Troubleshoot masalah komputer
                       Microsoft.Troublesh..
Computer Management    compmgmt.msc          Kelola sistem, storage, services
System Information     msinfo32              Info lengkap hardware & software
Event Viewer           eventvwr              Log semua kejadian sistem
Programs               (appwiz.cpl)          Tambah/hapus program
System Properties      control system        Info dasar sistem
Internet Options       inetcpl.cpl           Pengaturan internet
Registry Editor        regedit               Edit Windows Registry
Resource Monitor       resmon                Monitor CPU/Disk/Network/Memory
Command Prompt         cmd                   Terminal perintah teks
Performance Monitor    perfmon               Monitor performa real-time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 UAC (USER ACCOUNT CONTROL) SETTINGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4 Level Slider (atas ke bawah) :
  Always notify       = notif SEMUA perubahan + layar redup (keamanan max)
  Notify for apps     = notif hanya jika APP yang ubah (DEFAULT)
  Notify w/o dimming  = sama seperti atas tapi layar TIDAK redup
  Never notify        = TIDAK ADA notifikasi sama sekali (berbahaya)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 COMPUTER MANAGEMENT (compmgmt.msc)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3 Bagian Utama :

[1] SYSTEM TOOLS
  Task Scheduler  → Buat & kelola task otomatis
                    Bisa trigger : saat login, logoff, jadwal, startup
                    Lihat task   : Task Scheduler Library
                    Buat task    : Create Basic Task (panel Actions kanan)

  Event Viewer    → Log semua kejadian komputer (audit trail)
                    3 Panel : kiri (tree), tengah (overview), kanan (actions)
                    5 Tipe Event :
                      Error         = masalah signifikan (service gagal load)
                      Warning       = potensi masalah masa depan (disk hampir penuh)
                      Information   = operasi berhasil (driver load sukses)
                      Success Audit = akses security BERHASIL (login sukses)
                      Failure Audit = akses security GAGAL (login gagal)
                    4 Standard Log (Windows Logs) :
                      Application   = event dari aplikasi
                      Security      = logon attempt valid/invalid, akses file
                      System        = event komponen sistem (driver gagal)
                      CustomLog     = event dari app yang buat log sendiri

  Shared Folders  → Daftar semua folder yang dibagikan di jaringan
                    Default shares Windows : ADMIN$ | C$ | IPC$
                    Sessions   = user yang sedang terhubung
                    Open Files = file yang sedang dibuka user terhubung

  Local Users     → Sama seperti lusrmgr.msc (dibahas di WinFun1)
  & Groups

  Performance     → Performance Monitor (perfmon)
                    Lihat data performa real-time atau dari log file

  Device Manager  → Lihat & konfigurasi hardware
                    Bisa enable/disable hardware yang terpasang

[2] STORAGE
  Disk Management → Advanced storage tasks :
                    - Set up a new drive
                    - Extend a partition
                    - Shrink a partition
                    - Assign or change a drive letter (ex. E:)

[3] SERVICES AND APPLICATIONS
  Services        → Daftar semua service + status
                    Klik kanan → Properties untuk detail :
                      Service name  = nama teknis (beda dari display name)
                      Path          = lokasi executable
                      Startup type  :
                        Automatic = jalan otomatis saat boot
                        Manual    = jalan hanya jika dipicu
                        Disabled  = tidak boleh jalan sama sekali
  WMI Control     → Kelola Windows Management Instrumentation
                    Deprecated di Win10 21H1 → diganti PowerShell

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SYSTEM INFORMATION (msinfo32)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Kumpulkan & tampilkan info lengkap hardware, komponen, software
3 Bagian :
  Hardware Resources → Info teknis tingkat lanjut (bukan untuk user biasa)
                       Sub : Conflicts/Sharing, DMA, Forced Hardware,
                             I/O, IRQs, Memory

  Components         → Info hardware yang terpasang
                       Sub : Multimedia, Display, Input, Network,
                             Storage, Ports, USB, dll
                       Yang ada data : Display & Input

  Software Environ.  → Info software & OS
                       Sub : System Drivers, Environment Variables,
                             Network Connections, Running Tasks,
                             Loaded Modules, Services, Startup Programs, dll

Environment Variables :
  Definisi : Variabel yang simpan info path/konfigurasi OS
  Contoh   : %windir% = C:\Windows | %TEMP% = folder temporary
  2 Jenis  :
    User variables   = berlaku untuk user tertentu saja
    System variables = berlaku untuk semua user di komputer
  Akses via : Control Panel → System → Advanced → Environment Variables
              ATAU Settings → System → About → Advanced system settings

Search bar msinfo32 :
  Ada di bagian paling bawah
  Centang "Search selected category only" untuk hasil lebih spesifik

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ADVANCED SYSTEM SETTINGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Buka via : Cari "View advanced system settings" di search bar

Tab Hardware :
  Device Manager          → List semua hardware, ubah properties
  Device Install Settings → Pilih apakah Windows download driver otomatis

Tab Advanced :
  Performance    → Visual effects, processor scheduling,
                   memory usage, virtual memory (page file)
  User Profiles  → Desktop settings per user
  Startup & Recovery → Konfigurasi boot & crash dump

Page File (Virtual Memory) :
  Fungsi : Ruang RAM cadangan di hard disk saat RAM fisik penuh
  Lihat/ubah : Advanced → Performance → Settings → Advanced → Change
  Info yang tersedia :
    - Drive tempat page file disimpan
    - Initial size (MB)
    - Maximum size
    - Apakah Windows manage otomatis

Crash Dump (Startup and Recovery) :
  Fungsi : File yang dibuat Windows saat terjadi error kritis (BSOD)
  Berguna untuk : analisis apa yang salah saat crash
  Tipe dump yang tersedia :
    Automatic memory dump
    Kernel memory dump
    Small memory dump (256 KB)
    Complete memory dump
    None
  File default : %SystemRoot%\MEMORY.DMP

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 RESOURCE MONITOR (resmon)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Monitor penggunaan CPU, memory, disk, network per proses
           Bisa start/stop/pause/resume service langsung dari sini
           Bisa identifikasi deadlocked process & file locking conflict
Target   : Advanced user untuk advanced troubleshooting

5 Tab :
  Overview → Ringkasan semua 4 bagian sekaligus
  CPU      → Processes + Services + Associated Handles + Modules
  Memory   → Processes + Physical Memory (bar visual)
             Physical Memory terbagi : Hardware Reserved | In Use |
                                       Modified | Standby | Free
  Disk     → Processes with Disk Activity + Disk Activity + Storage
  Network  → Processes with Network Activity + Network Activity +
             TCP Connections + Listening Ports

Panel kanan = grafik real-time untuk setiap bagian

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 COMMAND PROMPT (cmd)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Command Dasar :
  hostname     → tampilkan nama komputer
  whoami       → tampilkan nama user yang sedang login
  cls          → bersihkan layar terminal

Command Troubleshooting Network :
  ipconfig     → tampilkan network address settings
  ipconfig /?  → tampilkan help manual ipconfig
  ipconfig /all→ tampilkan semua info konfigurasi network

  netstat      → tampilkan protocol statistics & TCP/IP connections aktif
  Syntax       : NETSTAT [-a] [-b] [-e] [-f] [-n] [-o] [-p proto]
                         [-r] [-s] [-x] [-t] [interval]

  net          → kelola network resources (punya sub-commands)
  net help     → tampilkan help untuk command net
                 (BUKAN net /? karena /? tidak bekerja di net)
  net help user→ help untuk sub-command user

Sub-commands net yang penting :
  net user      → kelola user accounts
  net localgroup→ kelola local groups
  net use       → kelola network connections
  net share     → kelola shared resources
  net session   → lihat sesi yang aktif
  net start/stop→ start atau stop service

Cara baca help :
  command /?   = tampilkan manual (berlaku untuk SEBAGIAN BESAR command)
  net help     = khusus untuk command NET

Perbedaan \ dan / :
  \  = pemisah folder dalam PATH  → C:\Windows\System32\file.exe
  /  = parameter/opsi command     → ipconfig /all | netstat -a

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 REGISTRY EDITOR (regedit)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Database hierarkis terpusat untuk konfigurasi sistem
Isi      : Profil user, aplikasi terinstall, setting folder/ikon,
           hardware yang ada, port yang digunakan
WARNING  : Perubahan registry bisa rusak sistem → hati-hati!

5 Hive Utama :
  HKEY_CLASSES_ROOT    → File associations (.txt → Notepad, dll)
  HKEY_CURRENT_USER    → Konfigurasi & preferensi user yang sedang login
  HKEY_LOCAL_MACHINE   → Konfigurasi hardware & software seluruh sistem
  HKEY_USERS           → Profil semua user yang pernah login
  HKEY_CURRENT_CONFIG  → Hardware profile yang dipakai saat boot ini

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Service         = aplikasi khusus yang berjalan di background
Hive            = folder utama/root dalam struktur Registry
Page File       = area di hard disk yang dipakai Windows sebagai RAM cadangan
Crash Dump      = file rekaman kondisi sistem saat terjadi crash/BSOD
Audit Trail     = catatan kronologis semua aktivitas sistem (via Event Viewer)
Environment Var = variabel yang simpan path/info penting untuk OS & program
Startup Type    = pengaturan kapan service boleh jalan (Auto/Manual/Disabled)
Deadlock        = kondisi dua proses saling tunggu → keduanya tidak bisa jalan
.msc file       = Microsoft Console file, shortcut ke panel manajemen Windows
Selected Command= path lengkap tool di tab Tools MSConfig, bisa dijalankan
                  langsung via Run/CMD tanpa buka MSConfig
```