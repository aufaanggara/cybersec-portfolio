import socket # komunikasi jaringan
import threading # banyak scan paralel
import queue # antrian
import time # durasi scan
from datetime import datetime # waktu mulai scan
from port import COMMON_PORTS # dictionary port

#!/usr/bin/env python3
"""
===============================================
  PORT SCANNER — Dibuat untuk tujuan belajar
  Gunakan HANYA di environment legal:
  - Localhost / lab pribadi
  - CTF
  - Target dengan izin eksplisit
===============================================
"""

import socket
import threading
import queue
import time
from datetime import datetime

# ─────────────────────────────────────────────
# DATABASE SERVICE NAME
# ─────────────────────────────────────────────
COMMON_PORTS = {
    21: "FTP",        22: "SSH",         23: "Telnet",
    25: "SMTP",       53: "DNS",         80: "HTTP",
    110: "POP3",      135: "RPC",        139: "NetBIOS",
    143: "IMAP",      443: "HTTPS",      445: "SMB",
    3306: "MySQL",    3389: "RDP",       5432: "PostgreSQL",
    5900: "VNC",      6379: "Redis",     8080: "HTTP-Alt",
    8443: "HTTPS-Alt",27017: "MongoDB",
}

# ─────────────────────────────────────────────
# CORE: SCAN SATU PORT
# ─────────────────────────────────────────────
def scan_port(host, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except socket.error:
        return False

# ─────────────────────────────────────────────
# WORKER THREAD
# ─────────────────────────────────────────────
def worker(host, port_queue, results, timeout):
    while not port_queue.empty():
        try:
            port = port_queue.get_nowait()
        except queue.Empty:
            break
        if scan_port(host, port, timeout):
            results.append(port)
        port_queue.task_done()

# ─────────────────────────────────────────────
# DISPLAY HASIL
# ─────────────────────────────────────────────
def display_results(host, open_ports, start_port, end_port, duration):
    total_scanned = end_port - start_port + 1
    print(f"\n{'='*55}")
    print(f"  HASIL SCAN")
    print(f"{'='*55}")
    if not open_ports:
        print(f"  Tidak ada port terbuka di range {start_port}-{end_port}")
    else:
        print(f"  {'PORT':<10} {'STATUS':<12} {'SERVICE'}")
        print(f"  {'-'*45}")
        for port in open_ports:
            service = COMMON_PORTS.get(port, "Unknown")
            print(f"  {port:<10} {'OPEN':<12} {service}")
    print(f"\n{'='*55}")
    print(f"  SUMMARY")
    print(f"{'='*55}")
    print(f"  Host yang di-scan : {host}")
    print(f"  Total port scan   : {total_scanned}")
    print(f"  Port terbuka      : {len(open_ports)}")
    print(f"  Durasi            : {duration:.2f} detik")
    print(f"{'='*55}\n")

# ─────────────────────────────────────────────
# FUNGSI UTAMA SCANNER
# ─────────────────────────────────────────────
def run_scanner(host, start_port, end_port, num_threads=100, timeout=1):
    print(f"\n{'='*55}")
    print(f"  PORT SCANNER")
    print(f"{'='*55}")
    print(f"  Target  : {host}")
    print(f"  Range   : {start_port} - {end_port}")
    print(f"  Threads : {num_threads}")
    print(f"  Dimulai : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*55}\n")

    try:
        target_ip = socket.gethostbyname(host)
        if target_ip != host:
            print(f"  Resolved: {host} → {target_ip}\n")
    except socket.gaierror:
        print(f"  [ERROR] Tidak bisa resolve hostname: {host}")
        return

    port_queue = queue.Queue()
    for port in range(start_port, end_port + 1):
        port_queue.put(port)

    results = []
    start_time = time.time()

    threads = []
    actual_threads = min(num_threads, end_port - start_port + 1)

    for _ in range(actual_threads):
        t = threading.Thread(
            target=worker,
            args=(target_ip, port_queue, results, timeout)
        )
        t.daemon = True
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    duration = time.time() - start_time
    results.sort()
    display_results(host, results, start_port, end_port, duration)

# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────
def get_input():
    print("\n" + "="*55)
    print("  PYTHON PORT SCANNER — Ethical Use Only")
    print("="*55)
    host = input("\n  Target IP/Hostname: ").strip()
    if not host:
        print("  [ERROR] Host tidak boleh kosong!")
        return None, None, None
    try:
        start_port = int(input("  Port awal (default 1): ").strip() or "1")
        end_port = int(input("  Port akhir (default 1024): ").strip() or "1024")
        if not (0 <= start_port <= 65535) or not (0 <= end_port <= 65535):
            print("  [ERROR] Port harus antara 0-65535!")
            return None, None, None
        if start_port > end_port:
            print("  [ERROR] Port awal tidak boleh lebih besar dari port akhir!")
            return None, None, None
    except ValueError:
        print("  [ERROR] Port harus berupa angka!")
        return None, None, None
    return host, start_port, end_port

if __name__ == "__main__":
    host, start_port, end_port = get_input()
    if host:
        run_scanner(host, start_port, end_port)