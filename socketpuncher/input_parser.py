#!/usr/bin/python
# InputParser
# parses different kind of base payloads for mutation
import re

class InputParser:
	def __init(self,defaultfile="badass_payloads.payme"):
		self.defaultf = defaultfile

	def read_raw_textfile(self,self.defaultf):
		base_payloads = []
		raw_payload_file = open(raw_fh,'r')

		for payload in raw_payload_file:
			base_payloads.append(payload)

		return base_payloads
		
