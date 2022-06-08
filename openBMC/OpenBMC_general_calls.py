#!/usr/bin/python

import sys
import os
import re
import datetime
import time

def conditional_statements():
    apss_id="none"
    ucd_id="none"
    ps_string=os.popen("ps | grep apss_read").read()
    if ps_string[0] == ' ':
        ps_string=ps_string[1:]
    split_ps=ps_string.split("\n")
    for s in split_ps:
        if "apss_readings" in s:
            apss_id=s.split(" ")[0]

    ps_string=os.popen("ps | grep ucd_read").read()
    if ps_string[0] == ' ':
        ps_string=ps_string[1:]
    split_ps=ps_string.split("\n")
    for s in split_ps:
        if "ucd_readings" in s:
            ucd_id=s.split(" ")[0]

    print(apss_id)

    pins=sys.argv[2].split(",");
    gpiochip=os.popen("gpiodetect | grep ucd").read()
    gpiochip=gpiochip.split(" ")[0]
    pins_values=sys.argv[3].split(",");
    while True:
        for index in range(len(pins)):
            state=os.popen("gpioget "+gpiochip+" "+pins[index]).read()
            state=re.sub(r"[\n\t\s]*", "", state)
            if state == pins_values[index]:
                printedValue="echo \"Power-Telemetry triggered: index = "+pins[index]+" and value that triggered = "+pins_values[index]+"\" | systemd-cat";
                os.system(printedValue)
                time.sleep(1)
                if apss_id !="none" :
                    os.system("kill "+apss_id)
                if ucd_id !="none" :
                    os.system("kill "+ucd_id)
                exit()

def stop_background_scripts():
    apss_id="none"
    ucd_id="none"
    conditional_id="none"
    ps_string=os.popen("ps | grep apss_read").read()
    if ps_string[0] == ' ':
        ps_string=ps_string[1:]
    split_ps=ps_string.split("\n")
    for s in split_ps:
        if "apss_readings" in s:
            apss_id=s.split(" ")[0]

    ps_string=os.popen("ps | grep ucd_read").read()
    if ps_string[0] == ' ':
        ps_string=ps_string[1:]
    split_ps=ps_string.split("\n")
    for s in split_ps:
        if "ucd_readings" in s:
            ucd_id=s.split(" ")[0]


    ps_string=os.popen("ps | grep conditional_state").read()
    if ps_string[0] == ' ':
        ps_string=ps_string[1:]
    split_ps=ps_string.split("\n")
    for s in split_ps:
        if "conditional_statements" in s:
            conditional_id=s.split(" ")[0]


    if apss_id !="none" :
        os.system("kill "+apss_id)
    if ucd_id !="none" :
        os.system("kill "+ucd_id)
    if conditional_id !="none" :
        os.system("kill "+conditional_id)
    exit()



if sys.argv[1] == "stop_background_scripts":
    stop_background_scripts()
elif sys.argv[1]=="conditional_statements":
    conditional_statements()

