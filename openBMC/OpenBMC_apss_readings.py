#!/usr/bin/python

import sys
import os
import datetime
try:
    import apss_config
    OFFSETS=apss_config.OFFSETS
    GAINS=apss_config.GAINS
    
except ModuleNotFoundError:
    #error handling
    OFFSETS=[0,        #CH0
         0.001,        #CH1
         -0.001,    #CH2
         -0.001,    #CH3
         -0.001,    #CH4
         -0.001,    #CH5
         -0.001,    #CH6
         -0.002,    #CH7
         -0.006,    #CH8
         0,0,0,        #CH9-11
         -0.001,    #CH12
         -0.005,    #CH13
         -0.003,    #CH14
         -0.001]    #CH15
         
    GAINS=    [24.97, #CH0
         6.5,        #CH1
         26.54,        #CH2
         26.54,        #CH3
         18.6,        #CH4
         18.6,        #CH5
         40,        #CH6
         40,        #CH7
         78.2,        #CH8
         0,0,0,        #CH9-11
         5,            #CH12
         27.98,        #CH13
         40,        #CH14
         18.6]        #CH15
    pass


BUS=3

HEX_DIGITS="0123456789ABCDEF"
ADDR="0x38"

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
    file = open(sys.argv[2]+date_time+".txt","w")
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

else:
    today = datetime.datetime.now()
    date_time = today.strftime("%m_%d_%Y__%H_%M_%S")
    file = open(sys.argv[2]+date_time+".txt","w")
    channels=sys.argv[1].split(",");
    print(channels);
    while True:
        for x in channels:
            totalPower=0
            IDX=(int(x)*2)
            INDEX=int(x)

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
                print("CH"+str(INDEX)+"- "+CHANNELS[INDEX]+" *"+str(conversion)+"* V | Power = *"+str(totalPower)+"* W at  *"+date_time+"* \n")
                file.write("CH"+str(INDEX)+"- "+CHANNELS[INDEX]+" *"+str(conversion)+"* V | Power = *"+str(totalPower)+"* W at  *"+date_time+"* \n")
                continue
            elif INDEX >=9 and INDEX <=11:
                INDEX+=1
                IDX+=1
                continue
            else:
                if INDEX >0:
                    totalPower+=(conversion*12)
                print("CH"+str(INDEX)+"- "+CHANNELS[INDEX]+" *"+str(conversion)+"* Amps | Power = *"+str(totalPower)+"* W at *"+date_time+"* \n")
                file.write("CH"+str(INDEX)+"- "+CHANNELS[INDEX]+" *"+str(conversion)+"* Amps | Power = *"+str(totalPower)+"* W at *"+date_time+"* \n")
