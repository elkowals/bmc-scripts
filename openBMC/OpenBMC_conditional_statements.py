#!/usr/bin/python

import sys
import os
import re
import datetime
import time

apss_id="none"
ucd_id="none"
ps_string=os.popen("ps | grep apss_readings.py").read()
split_ps=ps_string.split("\n")
for s in split_ps:
    if "python" in s:
        apss_id=s.split(" ")[0]

ps_string=os.popen("ps | grep ucd_readings.py").read()
split_ps=ps_string.split("\n")
for s in split_ps:
    if "python" in s:
        ucd_id=s.split(" ")[0]


pins=sys.argv[1].split(",");
gpiochip=os.popen("gpiodetect | grep ucd").read()
gpiochip=gpiochip.split(" ")[0]


for pin in pins:
    state=os.popen("gpioget "+gpiochip+" "+pin).read()
    state=re.sub(r"[\n\t\s]*", "", state)
    if state == "0":
        print("pgood fail on "+pin)
        sleep(60)
        if apss_id !="none" :
            os.system("kill "+apss_id)
        if ucd_id !="none" :
            os.system("kill "+ucd_id)
        exit()

