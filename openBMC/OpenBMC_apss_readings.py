#!/usr/bin/python

import sys
import os
import datetime

BUS=3

HEX_DIGITS="0123456789ABCDEF"
ADDR="0x38"

if len(sys.argv) < 2:
	
	IDX=0
	INDEX=0
	while IDX < 32:
		REG=hex(IDX + int("0x14",16))
		BYTE0="{0:b}".format(int(os.popen("i2cget -f -a -y " + str(BUS) +" " + ADDR + " " + REG).read(),16))
		while len(BYTE0) != 8:
			BYTE0="0"+BYTE0
		
		IDX=((IDX+1))
		REG=hex(IDX + int("0x14",16))
		BYTE1="{0:b}".format(int(os.popen("i2cget -f -a -y " + str(BUS) +" " + ADDR + " " + REG).read(),16))
		while len(BYTE1) != 8:
			BYTE1="0"+BYTE1
		
		HEX0=hex(int(BYTE0,2))
		while len(HEX0) != 4:
			HEX0="0x0"+HEX0[2:]
		
		HEX1=hex(int(BYTE1,2))
		while len(HEX1) != 4:
			HEX1="0x0"+HEX1[2:]
		
		
		print("CH"+str(INDEX)+" "+HEX1+HEX0[2:])
		INDEX+=1
		IDX+=1

elif sys.argv[1] == "help":
	print("python apss_readings.py [channel] [offset] [gain]")
	print("examples:")
	print("python apss_readings.py 2 0.001 6.5")
	

else:

	offset=sys.argv[2]
	gain=sys.argv[3]
	channel=sys.argv[1]
	IDX=0
	
	while True:
		REG=hex((int(channel,2)*2) + int("0x14",16))
		BYTE0="{0:b}".format(int(os.popen("i2cget -f -a -y " + str(BUS) +" " + ADDR + " " + REG).read(),16))
		while len(BYTE0) != 8:
			BYTE0="0"+BYTE0
		
		REG=hex((int(channel,2)*2) + 1 + int("0x14",16))
		BYTE1="{0:b}".format(int(os.popen("i2cget -f -a -y " + str(BUS) +" " + ADDR + " " + REG).read(),16))
		while len(BYTE1) != 8:
			BYTE1="0"+BYTE1
		
		HEX0=hex(int(BYTE0,2))
		while len(HEX0) != 4:
			HEX0="0x0"+HEX0[2:]
		
		HEX1=hex(int(BYTE1,2))
		while len(HEX1) != 4:
			HEX1="0x0"+HEX1[2:]
		
		decimal=int(HEX1+HEX0[2:],16)
		calculatedVoltage=(decimal/4096)*2.048
		conversion=(calculatedVoltage+float(offset))*float(gain)
		today = datetime.datetime.now()
		date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
		print("CH"+str(channel)+" "+str(conversion)+" - "+HEX1+HEX0[2:]+" at  "+date_time)
		
	
