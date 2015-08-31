#!/usr/bin/python
# fokken
# DataGenerator
# data generation module for socketpuncher
# employs radamsa,scapy & ?

import subprocess,datetime,random
from scapy.all import *
from misc_f import *

def radamsa_gen(seed_payload,res_count):
	"""
	uses radamsa to generate payloads, based on origin sample
	"""
	subprocess.call("radamsa","-n "+res_count)

def home_made_gen(self,input_sample):
	"""
	takes hexstrings...
	"""

	raw = input_sample
	# split to arr
	sample = re.findall('..',input_sample)

	# improbability drive engage!
	if bool(random.getrandbits(1)):
		# inject in to arr
	    for n in range(0,random.randrange(0,len(sample))):
    	    sample[n] = binascii.b2a_hex(os.urandom(1))

		# rebuild arr
		packet = str(''.join(sample)).decode('hex')

		#pad?
		if bool(random.getrandbits(1)):
			packet = packet/fuzz(Raw())


	elif bool(random.getrandbits(1)):
		# inject fuzzed raw
	    for n in range(0,random.randrange(0,len(sample))):
    	    sample[n] = fuzz(Raw())

		packet = Raw(load=sample)
	else:
		# just pad with junk..
		packet = Raw(load=raw.decode('hex')/fuzz(Raw()))

	return packet

if __name__ == "__main__":
	print "Just a support lib for data generation..."
