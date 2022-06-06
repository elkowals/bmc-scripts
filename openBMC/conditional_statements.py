#!/usr/bin/python

import sys
import os
import re
import datetime
import time


ps_string=os.popen("ps | grep apss_readings.py").read()
split_ps=ps_string.split("\n")
for s in split_ps:
    if "python" in s:
        print(s.split(" ")[0])
        print("here")