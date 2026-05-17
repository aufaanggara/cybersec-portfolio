```
=== Windows Fundamentals 3 - Resume Materi ===
[17 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 WINDOWS UPDATE (Task 2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Layanan Microsoft untuk kirim security updates,
           feature enhancements, dan patches untuk Windows OS
           dan produk Microsoft lainnya (misal: Defender)

Patch    : Biasanya dirilis Selasa ke-2 tiap bulan
Tuesday    → Kalau update KRITIS/MENDESAK, Microsoft langsung push
             tanpa nunggu jadwal

Lokasi   : Settings → Update & Security → Windows Update
CMD/Run  : control /name Microsoft.WindowsUpdate

Windows  : Di Win 10, update TIDAK BISA diabaikan selamanya
10 Forced  → Hanya bisa diTUNDA, tapi akhirnya tetap terjadi
             → Komputer PASTI restart setelah update

Opsi     : Pause updates for 7 days
tersedia   Change active hours (default 7:00 AM - 12:00 AM)
           View update history
           Advanced options

Status   : "managed" → dikelola oleh organisasi (bukan user biasa)
VM         "Your organization has turned off automatic updates"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 WINDOWS SECURITY (Task 3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : "Home to manage the tools that protect your device
           and your data" - Microsoft
Lokasi   : Settings → Update & Security → Windows Security

4 Protection Areas :
  1. Virus & threat protection
  2. Firewall & network protection
  3. App & browser control
  4. Device security

Arti     : 🟢 Hijau  = aman, tidak ada tindakan perlu
Ikon       🟡 Kuning = ada rekomendasi keamanan untuk ditinjau
           🔴 Merah  = PERINGATAN, butuh tindakan SEGERA

Catatan  : Windows Server 2019 tampilannya BERBEDA dari
           Windows 10 Home/Professional
           Win 10 punya lebih banyak area (Account protection,
           Device performance & health, Family options)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 VIRUS & THREAT PROTECTION (Task 4)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dibagi 2 : Current Threats
bagian     Virus & Threat Protection Settings

── CURRENT THREATS ──
Scan     : Quick scan  → cek folder rawan saja (cepat)
Options    Full scan   → cek SEMUA file & program (>1 jam)
           Custom scan → pilih sendiri folder yang dicek

Threat   : Last scan        → scan otomatis oleh Defender
History    Quarantined      → ancaman DIISOLASI, tidak bisa jalan,
                              dihapus berkala
           Allowed threats  → ancaman yang KAMU izinkan jalan
                              ⚠️ Izinkan HANYA jika 100% yakin!

── VIRUS & THREAT PROTECTION SETTINGS ──
Manage   : Real-time protection    → deteksi & hentikan malware
Settings   Cloud-delivered protect → perlindungan lebih cepat via cloud
           Auto sample submission  → kirim sampel ke Microsoft
           Controlled folder access→ proteksi folder dari app tidak dikenal
           Exclusions              → kecualikan file dari scan
                                    ⚠️ Bisa jadi celah! Pakai hati-hati!
           Notifications           → notif kesehatan & keamanan device

Updates  : Check for updates → update definisi antivirus secara manual

Ransomware: Controlled folder access HARUS aktif
Protection → Real-time protection HARUS aktif dulu

Catatan  : Real-time protection di VM sengaja DIMATIKAN
VM         karena VM tidak ada internet & tidak ada ancaman
           → Di perangkat PRIBADI harus selalu AKTIF!

Tip      : Klik kanan file/folder → "Scan with Microsoft Defender"
           untuk scan on-demand langsung

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FIREWALL & NETWORK PROTECTION (Task 5)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : "Traffic flows into and out via ports. A firewall
           controls what is and isn't allowed to pass through
           those ports" - Microsoft

3 Profil : Domain  → autentikasi ke domain controller
Firewall           (jaringan kantor/enterprise)
           Private → jaringan yang dipercaya user sendiri
                     (rumah/kantor kecil) ← active di VM
           Public  → jaringan publik (kafe, bandara, hotspot)
                     ← profil DEFAULT, paling ketat

Opsi per : Turn the firewall ON/OFF
profil     Block all incoming connections
           ⚠️ Jangan matikan kecuali 100% yakin!

Tautan   : Allow an app through firewall
penting    Network and Internet troubleshooter
           Firewall notification settings
           Advanced settings
           Restore firewalls to default

Allowed  : Daftar app yang boleh lewat firewall
Apps       kolom Private & Public bisa diatur terpisah
           Tombol Details → info tambahan per app

Advanced : Inbound Rules  → koneksi MASUK tidak cocok rule = BLOK
Settings   Outbound Rules → koneksi KELUAR tidak cocok rule = IZIN
(WF.msc)   Connection Security Rules (IPsec)
           Monitoring
           Actions: Import/Export Policy, Restore Default, Diagnose

CMD      : WF.msc → buka Windows Defender Firewall langsung

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APP & BROWSER CONTROL (Task 6)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Kelola pengaturan Microsoft Defender SmartScreen
Definisi : "Protects against phishing or malware websites and
SmartScreen applications, and downloading of malicious files" - Microsoft

Check    : SmartScreen cek app & file tidak dikenal dari web
Apps &     → Block  = langsung TOLAK
Files      → Warn   = beri PERINGATAN, user yang putuskan ✅ default
             → Off    = matikan SmartScreen total

Pop-up   : "Windows protected your PC"
SmartScreen "Windows Defender SmartScreen prevented an
             unrecognized app from starting."
             Tombol: Don't run | More info

Exploit  : Built-in di Windows 10 & Server 2019
Protection → sudah aktif out of the box
           → Exploit protection settings ada 2 tab:
             System settings & Program settings

System   : Control flow guard (CFG)
Settings   → Ensures control flow integrity for indirect calls
           → Default: On

           Data Execution Prevention (DEP)
           → Prevents code from running from data-only memory
           → Default: On

           Force randomization for images (Mandatory ASLR)
           → Relokasi paksa images tidak dikompilasi /DYNAMICBASE
           → Default: Off

           Randomize memory allocations (Bottom-up ASLR)
           → Acak lokasi virtual memory allocations

           ⚠️ Jangan ubah kecuali 100% yakin!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DEVICE SECURITY (Task 7)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Keamanan yang sudah TERTANAM LANGSUNG di perangkat
           (bukan software tambahan)

Core     : Pakai virtualization-based security
Isolation → Lindungi bagian inti perangkat
           → Memory Integrity : cegah injeksi kode berbahaya
             ke high-security processes
             Status di VM: OFF

TPM      : Trusted Platform Module
(Security  → Chip crypto-processor di hardware
Processor) → Lakukan operasi kriptografi
           → Tamper-resistant (tidak bisa diutak-atik software)
           → Beri enkripsi tambahan untuk device

Detail   : Manufacturer          : Intel (INTC)
TPM        Manufacturer version  : 303.12.0.0
           Specification version : 2.0
           PPI spec version      : 1.2
           TPM spec sub-version  : 1.16 (9/21/2016)
           PC client spec version: 1.00
           Status Attestation    : Ready
           Status Storage        : Ready

           ⚠️ Jangan ubah default kecuali 100% yakin!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 BITLOCKER (Task 8)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : "Data protection feature that integrates with OS
           and addresses threats of data theft from lost,
           stolen, or decommissioned computers" - Microsoft

Cara     : Enkripsi SELURUH drive
Kerja      → Data tidak terbaca tanpa kunci yang benar
           → Bahkan kalau hardisk dicabut & dipasang ke PC lain

Dengan   : BitLocker + TPM = PERLINDUNGAN TERBAIK
TPM        → TPM versi 1.2 atau lebih baru
           → TPM cegah perangkat diutak-atik saat offline
           → Tanpa TPM → wajib simpan STARTUP KEY di removable drive
             (flashdisk HARUS ditancapkan saat boot)

Syarat   : TPM 1.2 atau lebih baru untuk system integrity check
Sistem     Tanpa TPM → startup key di removable drive = WAJIB

Catatan  : Fitur BitLocker TIDAK ADA di VM yang dilampirkan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 VOLUME SHADOW COPY SERVICE / VSS (Task 9)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Koordinasi pembuatan shadow copy (snapshot /
           point-in-time copy) dari data yang akan di-backup

Lokasi   : Folder System Volume Information
Simpan     → di setiap drive yang proteksinya aktif

Jika VSS : Create a restore point
Aktif      Perform system restore
(System    Configure restore settings
Protection Delete restore points
ON)

Cara     : This PC → klik kanan drive (C:\)
Akses      → Configure Shadow Copies...
           → Enable volume yang diinginkan
           → Create Now untuk buat snapshot

Status   : Di VM: C:\ = Disabled, \\?\Vol... = Disabled
VM

Bahaya   : Ransomware TAHU fitur ini!
Keamanan   → Malware akan HAPUS shadow copies lebih dulu
           → Setelah shadow copy habis, tidak bisa recovery
           → Solusi: backup OFFLINE / OFF-SITE yang terpisah

Bonus    : Pelajari VSS lebih dalam → Advent of Cyber 2, Day 23

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Patch Tuesday     = Selasa ke-2 tiap bulan, jadwal update rutin Microsoft
Shadow Copy       = Snapshot kondisi sistem di titik waktu tertentu
VSS               = Volume Shadow Copy Service
TPM               = Trusted Platform Module, chip keamanan di hardware
BitLocker         = Enkripsi seluruh drive bawaan Windows
SmartScreen       = Filter anti-phishing & malware untuk app dan web
Real-time Protect = Perlindungan aktif 24 jam, blok malware saat masuk
Quarantine        = Isolasi ancaman agar tidak bisa berjalan
Exclusion         = File/folder yang dikecualikan dari scan antivirus
DEP               = Data Execution Prevention, cegah eksekusi dari memori data
CFG               = Control Flow Guard, jaga alur eksekusi program
ASLR              = Address Space Layout Randomization, acak lokasi memori
Core Isolation    = Keamanan berbasis virtualisasi untuk proses inti Windows
Living Off Land   = Taktik attacker pakai tools bawaan Windows agar tidak
                    terdeteksi (singkatan: LotL)
Startup Key       = Kunci boot BitLocker di removable drive (pengganti TPM)
Managed Settings  = Pengaturan dikontrol organisasi, bukan user biasa

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FURTHER READING (Task 10)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Antimalware Scan Interface (AMSI)
- Credential Guard
- Windows 10 Hello
- CSO Online - The best new Windows 10 security features
- Living Off The Land (LotL) techniques
```