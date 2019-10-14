#!/usr/bin/env python2
# Coded By : Khaled Nassar @knassar702
# Facebook & GITHUB : knassar702
# GPL-2.0
# EX : whoup('192.168.1.1/24') .. For show who up in network
# EX : portscanner('127.0.0.1',80,443) .. For port start scan
import nmap

nm = nmap.PortScanner()
def whoup(ip):
     data = nm.scan(hosts=ip, arguments='-sP')
     re= [ip for ip, result in data['scan'].iteritems() if result['status']['state'] == 'up']
     for i in re:
		print (i)
def portscanner(ip,port1,port2):
    nm.scan(ip,str(port1)+'-'+str(port2))
    print ('HOST : {}'.format(nm[ip].hostname()))
    print ('STATUS : {}'.format(nm[ip].state()))
    for proto in nm[ip].all_protocols():
        print('----------')
        print('Protocol : %s\n\n' % proto)
        lport = nm[ip][proto].keys()
        lport.sort()
        for port in lport:
            print ('port : %s | state : %s | name : %s' % (port, nm[ip][proto][port]['state'],nm[ip][proto][port]['name']))
	    print ('-'*44)

