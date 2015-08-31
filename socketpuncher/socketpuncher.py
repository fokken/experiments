#!/usr/bin/python
# fokken
import argparse,datetime,logging
import input_parser
from data_generator import *


if __name__ == "__main__":
	"""
	Its not designed to destroy, its just how it runs
	"""
	default_base_payload_file = "default_payloads.bp"
	
	aparser = argparse.ArgumentParser(description='Socketpuncher O=(-_-Q) netwörk application fuzzer')
	aparser.add_argument('-g','--generator',help="which generator to use for data generation: 1. Radamsa 2.Scapy 3. Derper")
	aparser.add_argument('-m','--mutation',help="which kind of mutation thats used(only with derper): 1.Padding 2.Random injection 3.Padding & Random injection")
	aparser.add_argument('-t','--tcp',help='send tcp packets',action='store_true')
	aparser.add_argument('-u','--udp',help='send udp packets',action='store_true')
	argparser.add_argument('-p','--port',help='which port to send packets to')
	aparser.add_argument('-h','-host',help='ip address of where to send the packets')
	aparser.add_argument('-sh','--spoofedhost',help='spoof ze source ip')
	aparser.add_argument('-i','--interface',help='interface to use when sending packets')
	aparser.add_argument('-s','--samples',help='sample file')
	aparser.add_argument('-c','--count',help='how many packets to craft/send')

	args = aparser.parse_args()

	iparser = InputParser(default_base_payload_file)

	catapult = packet_sender.PacketFiddler(
											args.tcp,
											args.udp,
											args.port,
											args.host,
											args.interface,
											args.spoofedhost
										)

	try:
		if (int(args.generator) == 1):
			swag_file = radamsa_gen(args.count)
			while open(swag_file,'r') as rad_junk:
				for junkage in rad_junk:
					catapult.send_packet(junkage)
					
		elif (int(args.generator) == 2):
			for n in range(0,int(args.count)):
				junkage = fuzz(Raw())
				catapult.send_packet(junkage)
				

		elif (int(args.generator) == 3):
			for n in range(0,int(args.count)):
				junkage = home_made_gen(sample)
				catapult.send_packet(junkage)

		else:
			print "You didnt specify valid generator!"
	except:
		print "Something bad happened..."
	
