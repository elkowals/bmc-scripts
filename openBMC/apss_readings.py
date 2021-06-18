#!/usr/bin/python

import sys
import os
import datetime

BUS=3

HEX_DIGITS="0123456789ABCDEF"
ADDR="0x38"
OFFSETS=[0,0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.002,-0.006,0,0,0,-0.001,-0.005,-0.003,-0.001]
GAINS=	[24.97,6.5,26.54,26.54,18.6,18.6,40,40,78.2				 ,0,0,0,5,27.98,40,18.6]
CHANNELS=["12V_IMONBUF_AUXCONN","12V_PSU","12V_CURR_IMONBUF_VRM_DCM0","12V_CURR_IMONBUF_VRM_DCM1","12V_A_C_IMONBUF_DCM0","12V_B_D_IMONBUF_DCM1","12V_E_F_G_DCM0_DDIM_CURR","12V_H_J_K_DCM1_DDIM_CURR","12V_IMONBUF_240VA","NA","NA","NA","12VCS_CURR","12V_CURR_FAN","12V_CURR_BPLANES","12V_L_M_IO_CURR"]
totalPower=0
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
		
		decimal=int(HEX1+HEX0[2:],16)
		calculatedVoltage=(decimal/4096)*2.048
		conversion=(calculatedVoltage+float(OFFSETS[INDEX]))*float(GAINS[INDEX])
		today = datetime.datetime.now()
		date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
		if INDEX==1:
			print("CH"+str(INDEX)+" "+CHANNELS[INDEX]+" "+str(conversion)+" V | "+HEX1+HEX0[2:]+" at  "+date_time)
			print(" ")
		elif INDEX >=9 and INDEX <=11:
			INDEX+=1
			IDX+=1
			continue
		else:
			print("CH"+str(INDEX)+" "+CHANNELS[INDEX]+" "+str(conversion)+" Amps | Power = "+str(conversion*12)+" W | "+HEX1+HEX0[2:]+" at  "+date_time)
			print(" ")
			if INDEX >0:
				totalPower+=(conversion*12)
		
		
		INDEX+=1
		IDX+=1
		
	print("System power = "+str(totalPower)+" W")
	
elif sys.argv[1] == "ALL":
	today = datetime.datetime.now()
	date_time = today.strftime("%m_%d_%Y__%H_%M_%S")
	file = open("APSS_SYSTEM_POWER"+date_time+".txt","w")
	while True:
		totalPower=0
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
			
			decimal=int(HEX1+HEX0[2:],16)
			calculatedVoltage=(decimal/4096)*2.048
			conversion=(calculatedVoltage+float(OFFSETS[INDEX]))*float(GAINS[INDEX])
			today = datetime.datetime.now()
			date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
			if INDEX==1:
				INDEX+=1
				IDX+=1
				continue
			elif INDEX >=9 and INDEX <=11:
				INDEX+=1
				IDX+=1
				continue
			else:
				if INDEX >0:
					totalPower+=(conversion*12)
			
			INDEX+=1
			IDX+=1
			
		print("System power = "+str(totalPower)+" W at  "+date_time)
		file.write("System power = "+str(totalPower)+" W at  "+date_time+" \n")
