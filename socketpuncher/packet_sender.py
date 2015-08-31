#!/usr/bin/python
# fokken
# PacketSender
from scapy.all import *
import socket,datetime,logging

class PacketFiddler:
	def __init__(self,tcp=False,udp=False,port,host,interface,spoof_addr=0):
		"""
		class for packet fiddling..
		"""
		conf.iface=interface
		self.host = host
		self.port = port
		if spoof_addr:
			self.spoof_addr=spoof_addr

	def setup_tcp_socket(self):
		"""
		sets up a tcp socket,returns StreamSocket
		"""
	
		tcp_socket = socket.socket((self.host,self.port))
		streamsock = StreamSocket(tcp_socket)

		return streamsock


	def send_packet(self,udp,tcp,payload):
		"""
		well... it sends packets...
		"""
		if udp:
			try:
				# INSERT LOGGER WITH TIMESTAMP HERE

				if self.spoof:
					ip_hdr = IP(dst=self.host,src=self.spoof)
				else:
					ip_hdr = IP(dst=self.host)

				udp_packet = Ether()/ip_hdr/UDP(dport=self.port)/Raw(load=payload)

				sendp(udp_packet)
			except IOError as e:
				print "ERROR: couldnt send packet:",e

		if tcp:
			try:
				tcp_socket = self.setup_tcp_socket(self.host,self.port)
				for packet in packet_list:
					try:
						# INSERT LOGGER WITH TIMESTAMP HERE
						tcp_socket.send(payload)
					except:
						print "ERROR: packet sending problem, retrying connection since TCP..."
						try:
							tcp_socket = setup_tcp_socket(self.host,self.port)
							tcp_socket.send(payload)
						except:
							print "ERROR: Retry didnt work... maybe it crashed?"
							# INSERT LOGGING OF POTENTIAL CRASH
						

			except:
				print "ERROR: socket failed"

			# in any case try to close the socket...
			if tcp_socket:
				tcp_socket.close()

if __name__ == "__main__":
	print "Just a support module..."
