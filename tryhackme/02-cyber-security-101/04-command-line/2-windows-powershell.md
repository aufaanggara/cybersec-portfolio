```
=== PowerShell - Resume Materi ===
[08 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU POWERSHELL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Cross-platform task automation solution dari Microsoft
Isi      : Command-line shell + scripting language + config management
Basis    : Dibangun di atas framework .NET
Sifat    : Object-oriented (bukan text-based seperti CMD)
Platform : Awalnya Windows only → sejak 2016 support macOS & Linux
Dibuat   : Jeffrey Snover (2006) → solusi keterbatasan CMD & batch files
Prompt   : Ditandai dengan PS di awal baris

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONSEP OBJECT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Object     : Unit data yang punya Properties + Methods
Properties : Karakteristik/data (contoh: Name, Length, Status)
Methods    : Aksi yang bisa dilakukan (contoh: Drive(), Refuel())
Bedanya    : CMD output = teks biasa
             PowerShell output = object lengkap dengan properties & methods
Manfaat    : Tidak perlu parsing teks → langsung manipulasi data

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CARA LAUNCH POWERSHELL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Start Menu   : Ketik powershell → klik Windows PowerShell
Run Dialog   : Win+R → ketik powershell → Enter
File Explorer: Ketik powershell di address bar → Enter
Task Manager : File > Run new task → ketik powershell → Enter
CMD          : Ketik powershell → Enter

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 BASIC SYNTAX : VERB-NOUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Format  : Verb-Noun
Verb    : Aksi yang dilakukan (Get, Set, New, Remove, dll)
Noun    : Objek yang dikenai aksi (ChildItem, Location, Content, dll)
Contoh  : Get-Content  → ambil isi file
          Set-Location → pindah direktori

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CMDLETS DASAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Get-Command
  → List semua cmdlets, functions, aliases, scripts yang tersedia
  -CommandType "Function"  → filter berdasarkan tipe command
  -Name "Remove*"          → filter nama yang dimulai kata tertentu

Get-Help <cmdlet>
  → Tampilkan dokumentasi lengkap sebuah cmdlet
  -examples   → tampilkan contoh penggunaan
  -detailed   → info lebih lengkap
  -full        → info teknis lengkap
  -online     → buka dokumentasi online

Get-Alias
  → List semua alias yang tersedia
  Contoh alias : dir  → Get-ChildItem
                 cd   → Set-Location
                 cat  → Get-Content
                 echo → Write-Output

Find-Module -Name "pattern*"
  → Cari module di repositori online (PowerShell Gallery)

Install-Module -Name "NamaModule"
  → Download & install module dari repositori

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NAVIGASI FILE SYSTEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Get-ChildItem
  → List isi direktori (setara dir / ls)
  -Path ".\folder"  → tentukan lokasi
  -Hidden           → tampilkan file tersembunyi
  -Recurse          → masuk ke semua subfolder

Set-Location -Path ".\folder"
  → Pindah direktori (setara cd)

New-Item -Path ".\nama" -ItemType "Directory"
  → Buat folder baru
New-Item -Path ".\nama.txt" -ItemType "File"
  → Buat file baru

Remove-Item -Path ".\nama"
  → Hapus file atau folder (setara del & rmdir sekaligus)

Copy-Item -Path .\asal -Destination .\tujuan
  → Salin file/folder (setara copy)

Move-Item -Path .\asal -Destination .\tujuan
  → Pindah file/folder (setara move)

Get-Content -Path ".\file.txt"
  → Baca & tampilkan isi file (setara type / cat)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CARA BACA MODE FILE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Posisi 1 : d = directory  | - = file
Posisi 2 : r = read-only  | - = tidak
Posisi 3 : a = archive    | - = tidak
Posisi 4 : h = hidden     | - = tidak
Posisi 5 : s = system     | - = tidak
Posisi 6 : l = symlink    | - = tidak

Contoh   : d--h-- = folder hidden
           -a-hs- = file archive + hidden + system

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PIPING, FILTERING, SORTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pipe ( | ) : Kirim OUTPUT satu cmdlet jadi INPUT cmdlet berikutnya
             PowerShell pipe = kirim OBJECT (bukan teks)

Sort-Object <property>
  → Urutkan berdasarkan property
  Default      : Ascending (kecil ke besar)
  -Descending  : Descending (besar ke kecil)

Where-Object -Property "nama" -operator "nilai"
  → Filter object berdasarkan kondisi
  Operator comparison :
  -eq  = equal to
  -ne  = not equal
  -gt  = greater than (strict)
  -ge  = greater than or equal to
  -lt  = less than (strict)
  -le  = less than or equal to
  -like "pola*" = cocokkan dengan pola wildcard

Select-Object <property1,property2>
  → Pilih property tertentu yang ditampilkan
  -First 1  → ambil hanya 1 object pertama

Select-String -Path ".\file" -Pattern "kata"
  → Cari pola teks dalam file (setara grep / findstr)
  → Support regex untuk pattern matching kompleks

Contoh pipeline lengkap :
Get-ChildItem | Sort-Object Length -Descending | Select-Object -First 1
→ Cari file terbesar di direktori

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SYSTEM & NETWORK INFORMATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Get-ComputerInfo
  → Info sistem lengkap : OS, hardware, BIOS, dll
  → Lebih lengkap dari systeminfo di CMD

Get-LocalUser
  → List semua akun user lokal
  → Tampilkan : Name, Enabled, Description

Get-NetIPConfiguration
  → Info konfigurasi jaringan : IP, DNS, Gateway
  → Setara ipconfig di CMD

Get-NetIPAddress
  → Detail semua IP address di sistem
  → Termasuk yang sedang tidak aktif

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 REAL-TIME SYSTEM ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Get-Process
  → List semua proses yang sedang berjalan
  → Tampilkan : CPU, memory, PID, nama proses

Get-Service
  → Status semua services : Running/Stopped/Paused
  → Berguna untuk forensics cari anomalous service

Get-NetTCPConnection
  → List semua koneksi TCP aktif
  → Tampilkan : LocalAddress, LocalPort, RemoteAddress,
                RemotePort, State, OwningProcess
  → OwningProcess = PID proses yang membuka koneksi
  → Berguna : deteksi backdoor & koneksi mencurigakan

Get-FileHash -Path ".\file"
  → Generate hash file (default: SHA256)
  → Berguna : verifikasi integritas file, deteksi tampering

Get-Item -Path ".\file" -Stream *
  → Lihat semua Alternate Data Streams (ADS) pada file
  → :$DATA   = stream default isi normal file
  → Nama lain = ADS tersembunyi (potensi malware)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SCRIPTING & REMOTE EXECUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Script     : File .ps1 berisi kumpulan perintah PowerShell
Manfaat    : Otomasi tugas → hemat waktu, kurangi error
Kegunaan   :
  Blue team : log analysis, deteksi anomali, ekstrak IOC
  Red team  : enumeration, remote command, bypass defence
  SysAdmin  : integrity check, enforce policy, monitor health

Invoke-Command
  → Eksekusi perintah di sistem remote
  -ComputerName NamaKomputer         → tentukan target
  -Credential Domain\User            → pakai kredensial tertentu
  -FilePath c:\scripts\file.ps1      → jalankan script di remote
  -ScriptBlock { perintah }          → jalankan perintah langsung
  Contoh :
  Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Service }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cmdlet      : Perintah PowerShell, format Verb-Noun, diucap "command-let"
Alias       : Nama pendek/alternatif untuk sebuah cmdlet
Pipeline    : Rangkaian cmdlets yang dihubungkan dengan pipe ( | )
Object      : Unit data dengan properties & methods
ADS         : Alternate Data Stream → stream tersembunyi dalam file NTFS
Hash        : Sidik jari unik file → berubah jika file dimodifikasi
IOC         : Indicator of Compromise → bukti sistem telah dikompromasi
Wildcard    : Karakter * untuk mencocokkan pola (contoh: Remove*)
PSGallery   : Repositori online untuk download modules PowerShell
ScriptBlock : Blok perintah dalam { } yang dijalankan oleh Invoke-Command
```