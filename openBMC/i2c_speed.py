#!/usr/bin/python

import sys
import os

base_address=[0x80,0x100,0x180,0x200,0x280,0x300,0x380,0x400,0x480,0x500,0x580,0x600,0x680,0x700,0x780,0x800];

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

if len(sys.argv) < 3 :
    print(colored(255, 0, 0, "\n missing bus and 50|100|200|400|600\n"));
    print(colored(0, 128, 0, "example: ./i2c_speed.py set|get 3 400\n"));
    print("it will increase the i2cbus 3 from index = 0 to 400khz\n");

else:
    if sys.argv[2].isnumeric():
        i2c_bus=str(int(sys.argv[2]));
        #print(str(hex(base_address[int(sys.argv[1])])));
        offset_address=hex(base_address[int(sys.argv[2])] | 0x04);
        #print("\n "+str(offset_address)+"\n");
        offset_address_string=str(offset_address);
        #print(offset_address_string+"\n");

        while len(offset_address_string) != 5:
            offset_address_string="0x0"+offset_address_string[2:]
        
        
        register_data=(int(os.popen("devmem 0x1e78a"+offset_address_string[2:]+" 32").read(),16));
        
        
        string_reg=str(hex(register_data));
        if(sys.argv[1].lower()=="get"):
            last_byte=string_reg[-1];
            if last_byte=='2':
                print("\n speed in i2c-"+str(int(i2c_bus.strip()))+" is 600\n");
            elif last_byte=='3':
                print("\n speed in i2c-"+str(int(i2c_bus.strip()))+" is 400\n");
            elif last_byte=='4':
                print("\n speed in i2c-"+str(int(i2c_bus.strip()))+" is 200\n");
            elif last_byte=='5':
                print("\n speed in i2c-"+str(int(i2c_bus.strip()))+" is 100\n");
            elif last_byte=='6':
                print("\n speed in i2c-"+str(int(i2c_bus.strip()))+" is 50\n");
        else:
        
            while len(string_reg) != 10:
                string_reg="0x0"+string_reg[2:]
            #print(string_reg+"\n");
            speed_used=sys.argv[3];
            if int(sys.argv[3]) == 50:
                updated_reg=string_reg[:-1]+"6";
            elif int(sys.argv[3]) == 100:
                updated_reg=string_reg[:-1]+"5";
            elif int(sys.argv[3]) == 200:
                updated_reg=string_reg[:-1]+"4";
            elif int(sys.argv[3]) == 400:
                updated_reg=string_reg[:-1]+"3";
            elif int(sys.argv[3]) == 600:
                updated_reg=string_reg[:-1]+"2";
            else:
                updated_reg=string_reg[:-1]+"5";
                speed_used="100";
            
            while len(updated_reg) != 10:
                updated_reg="0x0"+updated_reg[2:]
            #print(updated_reg+"\n");
            
            if os.system("devmem 0x1e78a"+offset_address_string[2:]+" 32 "+updated_reg)==0:
                print(colored(0, 128, 0, "\nsuccessful increase of speed @"+speed_used+" on i2cbus-"+str(int(i2c_bus.strip()))+" \n"));
                print(colored(0, 128, 0, "devmem 0x1e78a"+offset_address_string[3:]+" 32 "+updated_reg+"\n"));
            else:
                print(colored(255, 0, 0, "\ninvalid argument or devmem is not enabled\n"));
                print(colored(255, 0, 0, "if you can't detect devmem\n"));
                print(colored(255, 0, 0, "run the following commands to enable devmem:\n"));
                print(colored(255, 0, 0, "fw_setenv bootargs $(fw_printenv bootargs | sed -r 's/bootargs=//') mem.devmem=y\n"));
                print(colored(255, 0, 0, "then reboot command\n"));
    else:
        print(colored(255, 0, 0,"\n please use a numeric argument to specify i2cbus\n and select speed: 50/100/200/400/600 or use get"));
        print(colored(255, 0, 0,"example: ./i2c_speed.py set 3 400\n"));
        print(colored(255, 0, 0,"example: ./i2c_speed.py get 3\n"));
        print("it will increase the i2cbus 3 from index = 0 to 400khz\n");