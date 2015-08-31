#!/usr/bin/python
# udp scapy fuzzer,b64 hashed payload storage...
# fokken
from scapy.all import *
import sys,time,base64

def build_packet(target,port):
	packet = Ether()/IP(dst=target)/UDP(dport=port)/fuzz(Raw())
	return packet

if __name__ == "__main__":
	conf.iface = str(sys.argv[1])
	target = str(sys.argv[2])
	port = int(sys.argv[3])
	pktcount = int(sys.argv[4])
	print time.strftime("%Y%m%d %H%M%S "),"generating payload.."
	pkt_arr = []
	for n in range(0,pktcount):
		if n == pktcount/2:
			print time.strftime("%Y%m%d %H%M%S "),"generated ~50%"
		pkt = build_packet(target,port)
		pkt_arr.append(pkt)
	print time.strftime("%Y%m%d %H%M%S"),"packet generation done!"
	print time.strftime("%Y%m%d %H%M%S"),"sending packets to: "+target+":"+str(port)
	f = open("udp_fuzz_payload_"+time.strftime("%Y%m%d_%H%M%S")+".fuzz","w")
	for p in pkt_arr:
		try:
			sendp(p)
			f.write(time.strftime("%Y%m%d %H%M%S : ")+base64.b64encode(str(p[Raw]))+"\n")
		except:
			print time.strftime("%Y%m%d %H%M%S "),"failed sending packet!"
