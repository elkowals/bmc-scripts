#!/usr/bin/python

import sys
import os
import re
import datetime
import time

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
