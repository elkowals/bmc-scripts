#!/usr/bin/python

import sys
import os

base_address=[0x80,0x100,0x180,0x200,0x280,0x300,0x380,0x400,0x480,0x500,0x580,0x600,0x680,0x700,0x780,0x800];
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

if len(sys.argv) < 2 :
    print(colored(255, 0, 0, "\n missing bus argument\n"));
    print(colored(0, 128, 0, "example: ./i2c_recovery.py 3\n"));
    print("it will recover i2cbus 3 from index = 0\n");

else:
    if sys.argv[1].isnumeric():
        i2c_bus=str(int(sys.argv[1]));
        #print(str(hex(base_address[int(sys.argv[1])])));
        offset_address=hex(base_address[int(sys.argv[1])] | 0x14);
        #print("\n "+str(offset_address)+"\n");
        offset_address_string=str(offset_address);
        #print(offset_address_string+"\n");

        while len(offset_address_string) != 5:
            offset_address_string="0x0"+offset_address_string[2:]
        
        
        register_data=(int(os.popen("devmem 0x1e78a"+offset_address_string[2:]+" 32").read(),16));
        string_reg=str(hex(register_data));
        while len(string_reg) != 10:
            string_reg="0x0"+string_reg[2:]
        #print(string_reg+"\n");
        updated_reg=str(hex(register_data | 0x00008000));
        while len(updated_reg) != 10:
            updated_reg="0x0"+updated_reg[2:]
        #print(updated_reg+"\n");
        
        if os.system("devmem 0x1e78a"+offset_address_string[2:]+" 32 "+updated_reg)==0:
            print(colored(0, 128, 0, "\nsuccessful recovery attempt of bus"+str(int(i2c_bus.strip()))+" \n"));
            print(colored(0, 128, 0, "devmem 0x1e78a"+offset_address_string[2:]+" 32 "+updated_reg+"\n"));
        else:
            print(colored(255, 0, 0, "\ninvalid argument or devmem is not enabled\n"));
            print(colored(255, 0, 0, "if you can't detect devmem\n"));
            print(colored(255, 0, 0, "run the following commands to enable devmem:\n"));
            print(colored(255, 0, 0, "fw_setenv bootargs $(fw_printenv bootargs | sed -r 's/bootargs=//') mem.devmem=y\n"));
            print(colored(255, 0, 0, "then reboot command\n"));
    else:
        print(colored(255, 0, 0,"\n please use a numeric argument to specify i2cbus\n"));
        print(colored(255, 0, 0,"example: ./i2c_recovery.py 3\n"));
        print(colored(255, 0, 0,"it will recover i2cbus 3 from index = 0\n"));