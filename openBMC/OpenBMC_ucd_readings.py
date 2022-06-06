#!/usr/bin/python

import sys
import os
import re
import datetime
import time


rainier_amon =["12V_BULK","5VA_USB","5P0V_BPLANES_PG","3P3VA","3P3VB","1P5V_AVDD","1P1VA_USB","VDDA_DCM0_PG","VDDB_DCM0_PG","VDDA_DCM1_PG","VDDB_DCM1_PG","12VCS_CURR","3P3VCS_CURR","1P1V_USB_CURR","5P0V_USB_CURR","5P0V_BPLANES_CURR","12P0VN_CURR","12P0VP_CURR","12P0VQ_CURR","12P0VR_CURR","TDIODE_OCD_SLOT1","TDIODE_OCD_SLOT3","TDIODE_OCD_SLOT7","TDIODE_OCD_SLOT10"]
data=os.popen("ls /sys/bus/i2c/drivers/ucd9000/8-0011/hwmon/").read()
hwmon   = re.sub(r"[\n\t\s]*", "", data)
file = open(sys.argv[1]+".txt","w")
last_time = time.time()
while True:
    for index in range(1,25):
        amon=os.popen("cat /sys/bus/i2c/drivers/ucd9000/8-0011/hwmon/"+hwmon+"/in"+str(index)+"_input").read()
        amon=re.sub(r"[\n\t\s]*", "", amon)
        print("Amon"+str(index)+"|"+rainier_amon[index-1]+"|"+amon+"mV")
        today = datetime.datetime.now()
        date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
        file.write("Amon"+str(index)+"|"+rainier_amon[index-1]+"|"+str(int(amon)/1000)+"V|"+date_time+"|\n")

    if (time.time() - last_time) >=3600:
        file.truncate(0)
        last_time=time.time()
