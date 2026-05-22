import socket
import time


def scan_port(host, port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(0.5)
        client_socket.connect((host, port))
        client_socket.close()
        return True
    except (socket.timeout, socket.error):
        client_socket.close()
        return False


def validate_port_range(port_input):
    try:
        parts = port_input.split("-")
        start = int(parts[0])
        end = int(parts[1])
        if start < 1 or end > 65535 or start > end:
            return None, None
        return start, end
    except:
        return None, None


def main():
    print("=" * 40)
    print("           Simple Port Scanner")
    print("=" * 40)

    ip = input("Target IP: ")
    port_range = input("Port range (ex: 1-1000): ")

    start_port, end_port = validate_port_range(port_range)
    if start_port is None:
        print("[-] Port range tidak valid!")
        return

    print(f"\n[*] Scanning {ip} port {start_port}-{end_port}...\n")

    open_ports = []
    start_time = time.time()

    for port in range(start_port, end_port + 1):
        if scan_port(ip, port):
            print(f"[+] Port {port} OPEN")
            open_ports.append(port)

    elapsed = round(time.time() - start_time, 2)

    print(f"\n{'=' * 40}")
    print(f"[*] Scan selesai dalam {elapsed} detik")
    print(f"[*] {len(open_ports)} port open ditemukan")


if __name__ == "__main__":
    main()
