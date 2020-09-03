echo setting up speed to 200mhz
#Set phase clock magic settings for 200mhz
devmem 0x1e7500F4 32 0x0700FF

#disable clocks and set clock dividers
devmem 0x1e75012c 32 0xe00000

#enable MPLL clock for emmc
devmem 0x1e6e2300 32 0xf3928C00

#enable clocks
devmem 0x1e75012c 32 0xe00007
echo done
