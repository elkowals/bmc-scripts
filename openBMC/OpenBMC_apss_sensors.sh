#!/bin/sh - 
#===============================================================================
#
#          FILE: apss_sensors.sh
# 
#         USAGE: ./apss_sensors.sh 
# 
#   DESCRIPTION: Collects RAW sensor readings, need to use spreadsheet to
#   post-process readings into actual wattages
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: Created to help power team
#        AUTHOR: Emile Kowalski 
#  ORGANIZATION: 
#       CREATED: 06/03/2020 05:50:45 PM CST
#	   Based On: FSP2 
#      REVISION: 1 
#===============================================================================
BUS=3

HEX_DIGITS="0123456789ABCDEF"
ADDR="0x38"

dec2hex() {
    dec_value=$1
    hex_value=""
    
    until [ $dec_value == 0 ]; do

        rem_value=$((dec_value % 16))
        dec_value=$((dec_value / 16))

        hex_digit=${HEX_DIGITS:$rem_value:1}

        hex_value="${hex_digit}${hex_value}"

    done

    echo -e -n "${hex_value}" 
}

IDX=0
INDEX=0
while [ $IDX -lt 32 ] ; do
    REG=$(dec2hex $((IDX + 0x14)))
	BYTE0=$(i2cget -f -y $BUS $ADDR 0x$REG b)
    #BYTE0=`iicmaster -b /dev/iic/$BUS -a $ADDR -W 1 -o 0x$REG -r 1|sed -n 1p`
    IDX=$((IDX+1))
    REG=$(dec2hex $((IDX + 0x14)))
    BYTE1=$(i2cget -f -y $BUS $ADDR 0x$REG b)
	#BYTE1=`iicmaster -b /dev/iic/$BUS -a $ADDR -W 1 -o 0x$REG -r 1|sed -n 1p`
    BYTE00="$(echo -e "${BYTE0}" | sed -e 's/[[:space:]]*$//')" 
    BYTE11="$(echo -e "${BYTE1}" | sed -e 's/[[:space:]]*$//')" 
    BYTE00=${BYTE00:2}
    echo "CH$INDEX $BYTE11$BYTE00"
    INDEX=$((INDEX+1))
    IDX=$((IDX+1))
done

