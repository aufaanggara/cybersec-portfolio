# === HTB - Appointment | Resume Materi ===
### [02 Mei 2026]

---

## 📌 SQL (Structured Query Language)
Bahasa untuk berkomunikasi dengan database relasional.
Contoh query login di server:
```sql
SELECT * FROM users WHERE username='admin' AND password='1234'
```

---

## 📌 SQL INJECTION (SQLi)
Teknik menyisipkan karakter SQL khusus ke input user untuk memanipulasi query database.

**Konsep inti:** "Breaking Out of Context"
Karakter `'` dipakai untuk **kabur dari string SQL**, lalu diikuti payload berbahaya.

**OWASP Top 10 2021:** A03 - Injection

---

## 📌 KARAKTER KOMENTAR MySQL
| Karakter | Contoh | Keterangan |
|----------|--------|------------|
| `#` | `admin'#` | Single line comment |
| `--` | `admin'-- -` | Butuh spasi setelah -- |
| `/* */` | `/* komentar */` | Multi line comment |

Fungsi: **memotong sisa query** agar password diabaikan server.

---

## 📌 PAYLOAD SQLi BYPASS LOGIN
| Situasi | Payload | Keterangan |
|---------|---------|------------|
| Tau username | `admin'#` | Skip cek password |
| Tidak tau username | `' OR 1=1#` | Selalu TRUE, masuk sebagai user pertama di DB |
| Form pakai email | `' OR 1=1#` | Sama saja, yang diserang query nya |

**Cara kerja `' OR 1=1#`:**
```sql
-- Normal:
SELECT * FROM users WHERE username='' AND password='...'

-- Setelah inject:
SELECT * FROM users WHERE username='' OR 1=1#' AND password='...'
-- OR 1=1 selalu TRUE → login berhasil tanpa tau username apapun!
```

---

## 📌 CARA BEDAIN TARGET DATABASE vs BROWSER
| Situasi | Teknik |
|---------|--------|
| Form login / URL parameter `?id=1` | → SQLi ke **database** |
| Search bar / comment box yang tampil ke user | → XSS ke **browser** |

**Cara test cepat:** masukkan karakter `'`
- Muncul error SQL → target **database** → coba SQLi
- Tidak ada error → coba **XSS**

---

## 📌 PERBEDAAN SQLi vs XSS
| | SQLi | XSS |
|--|------|-----|
| Target | Database | Browser/pengguna |
| Karakter untuk kabur | `'` | `"` atau `>` |
| Payload contoh | `' OR 1=1#` | `"><script>alert(1)</script>` |
| Tujuan | Manipulasi query DB | Inject script ke halaman |

**Konsep sama:** keduanya pakai karakter khusus untuk keluar dari konteks aslinya.

---

## 📌 KAPAN SQLi TIDAK BERHASIL
| Proteksi | Penjelasan |
|----------|------------|
| Prepared Statement | Input tidak menyentuh query langsung |
| ORM (Prisma, Eloquent) | Auto escape karakter berbahaya |
| `mysqli_real_escape_string()` | Karakter `'` di-escape jadi `\'` |
| NoSQL (Firebase) | Tidak pakai SQL sama sekali → kebal SQLi |

**Firebase** punya kerentanan sendiri yaitu **Misconfigured Security Rules** (bukan SQLi).

---

## 📌 NMAP - Switch Penting
| Switch | Fungsi |
|--------|--------|
| `nmap [IP]` | Scan 1000 port umum, lihat semua yang terbuka |
| `-sV` | Detect versi service |
| `-sC` | Jalankan default scripts |
| `-p 80` | Scan port spesifik |
| `-p 80,443` | Scan beberapa port sekaligus |
| `-p-` | Scan semua 65.535 port |

**Workflow wajib:**
```bash
# Step 1 - Recon
nmap [IP]

# Step 2 - Detail
nmap -sV -sC -p [port] [IP]
```

**Port yang wajib hapal:**
| Port | Service |
|------|---------|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 21 | FTP |
| 3306 | MySQL |

---

## 📌 GOBUSTER - Switch Penting
| Switch | Fungsi |
|--------|--------|
| `dir` | Mode **direktori** |
| `dns` | Mode subdomain |
| `-u` | URL target |
| `-w` | Wordlist |

```bash
gobuster dir -u http://[IP] -w /usr/share/wordlists/dirb/common.txt
```

---

## 📌 HTTP RESPONSE CODE PENTING
| Code | Nama | Arti di CTF |
|------|------|-------------|
| 200 | OK | Halaman ditemukan ✅ |
| 301/302 | Redirect | Ikuti redirect! |
| 401 | Unauthorized | Butuh login |
| 403 | Forbidden | Ada tapi dilarang akses |
| 404 | Not Found | Tidak ada |
| 500 | Internal Server Error | Server error |

---

## 📌 ENUMERATION MINDSET
| Nmap nemuin port | Langkah logis berikutnya |
|-----------------|--------------------------|
| 80 / 443 | Buka browser |
| 22 | Coba SSH |
| 21 | Coba FTP |
| 3306 | Coba konek MySQL |

> Tidak selalu ada instruksi eksplisit — harus berpikir sendiri dari hasil recon!

---

## 📌 ISTILAH PENTING
| Istilah | Arti |
|---------|------|
| SQLi | SQL Injection — manipulasi query database |
| XSS | Cross Site Scripting — inject script ke browser |
| Bypass | Melewati mekanisme keamanan |
| Payload | Input berbahaya yang dikirim ke target |
| Enumerate | Identifikasi detail sistem (port, service, versi) |
| Raw Query | Query SQL yang ditulis langsung tanpa proteksi |
| ORM | Object Relational Mapper — layer aman antara kode dan DB |
| NoSQL | Database tanpa SQL (Firebase, MongoDB) |