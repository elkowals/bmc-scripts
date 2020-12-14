#!/usr/bin/python
# Created by: Emile Kowalski
# 12/14/2020
# Testing bootfail controlling io


import sys
import os


def drive(signal_name, logic_state):
	if signal_name.lower() == "bmc_rstind":
		if logic_state == "1":
			os.system("devmem 0x1e780088 32 0xD700C000") # = high for BMC_RSTIND (arm core reset)
			print("setting bmc_rstind (arm_core_reset) = high")
		else:
			os.system("devmem 0x1e780088 32 0xD500C000") # = low for BMC_RSTIND (arm core reset)
			print("setting bmc_rstind (arm_core_reset) = low")
	else:
		if logic_state == "1":
			os.system("devmem 0x1e780000 32 0x134159FF") # = high for userspace_rstind (SW_PGOOD)
			print("setting userspace_rstind (SW_PGOOD) = high")
		else:
			os.system("devmem 0x1e780000 32 0x134158FF") # = low for userspace_rstind (SW_PGOOD)
			print("setting userspace_rstind (SW_PGOOD) = low")

def direction_control():

	os.system("devmem 0x1e780004 32 0x00000100") # = output control for userspace_rstind
	os.system("devmem 0x1e78008C 32 0x02000000") # = output control for bmc_rstind


if len(sys.argv) < 2:
	print("missing arguments... setting controls to outputs")
	direction_control()
else:
	direction_control()
	drive("bmc_rstind", sys.argv[1])
	print("write your code in here??")





