#!/usr/bin/python

import sys
import os

#i2c4 = C0/1/2/3/     4
#i2c9 = C6/7/8/9/    10/11

#led0_3_register=hex(0x06)
#led4_7_register=hex(0x07)
reg6_i2c4=bytearray(4)
reg7_i2c4=bytearray(4)
reg6_i2c9=bytearray(4)
reg7_i2c9=bytearray(4)
#MSB to LSB
if len(sys.argv) < 2:
	print("missing slot parameters")
	print("example:")
	print("ENABLE_RSVD_SLOTS.py 0,1,2,3")
else:

	slots=sys.argv[1].split(",")
	slots=[int(numeric_slot) for numeric_slot in slots]
	for slot in slots:
		if slot <=3:
			reg6_i2c4[slot]=1
		elif slot ==4:
			reg7_i2c4[0]=1
		elif slot >=6 and slot <=9:
			reg6_i2c9[slot-6]=1
		elif slot >=10 and slot <=11:
			reg7_i2c9[slot-10]=1
		else:
			print("slot doesn't exist")

	reg6_i2c4.reverse()
	reg7_i2c4.reverse()
	reg6_i2c9.reverse()
	reg7_i2c9.reverse()

	reg6_i2c4_data=hex(int(reg6_i2c4.hex(),2))
	reg7_i2c4_data=hex(int(reg7_i2c4.hex(),2))
	reg6_i2c9_data=hex(int(reg6_i2c9.hex(),2))
	reg7_i2c9_data=hex(int(reg7_i2c9.hex(),2))
	
	os.system("i2cset -f -a -y 3 0x61 0x06 "+reg6_i2c4_data)
	os.system("i2cset -f -a -y 3 0x61 0x07 "+reg7_i2c4_data)
	os.system("i2cset -f -a -y 8 0x61 0x06 "+reg6_i2c9_data)
	os.system("i2cset -f -a -y 8 0x61 0x07 "+reg7_i2c9_data)
	
	inputReg1="{0:b}".format(int(os.popen("i2cget -f -a -y 3 0x61 0x00").read(),16))
	inputReg2="{0:b}".format(int(os.popen("i2cget -f -a -y 8 0x61 0x00").read(),16))
	while len(inputReg1) != 8:
		inputReg1="0"+inputReg1
	while len(inputReg2) != 8:
		inputReg2="0"+inputReg2
	
	inputReg1=inputReg1[::-1]
	inputReg2=inputReg2[::-1]
	
	for i in range(5):
		if inputReg1[i] == "1":
			print("Reserved bits for Slot C"+str(i)+" are ENABLED")
		else:
			print("Reserved bits for Slot C"+str(i)+" are disabled")
	
	for i in range(6):
		if inputReg2[i] == "1":
			print("Reserved bits for Slot C"+str(i+6)+" are ENABLED")
		else:
			print("Reserved bits for Slot C"+str(i+6)+" are disabled")
		
		
		
		
