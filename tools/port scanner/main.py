port = input("Masukkan range port, ex 1-1000: ")
splitPort = port.split("-")
print(f"Range Port: {splitPort}")

start_port = int(splitPort[0])
end_port = int(splitPort[1])

print(start_port)
print(end_port)

for i in range(start_port, end_port + 1):
    print(f"port:{i}")

ip = input("Masukkan IP Address: ")
print(f"ip: {ip}")
