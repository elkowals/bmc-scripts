set -eu
function get_pin() {
        local pin=$1

        case $pin in
                1) echo "amon $pin - 12V Bulk = "  ;;
                2) echo "amon $pin - 5P0VA_USB = "  ;;
                3) echo "amon $pin - 5P0V BP = "  ;;
                 4) echo "amon $pin - 3P3VA = "  ;;
                 5) echo "amon $pin - 3P3VB = "  ;;
                 6) echo "amon $pin - 1P5V_AVDD = "  ;;
                 7) echo "amon $pin - 1P1VA_USB = "  ;;
                 8) echo "amon $pin - VDDA_DCM0 = "  ;;
                 9) echo "amon $pin - VDDB_DCM0 = "  ;;
                 10) echo "amon $pin - VDDA_DCM1 = "  ;;
                 11) echo "amon $pin - VDDB_DCM1 = "  ;;
                 12) echo "amon $pin - 12P0VCS_CURR = "  ;;
                 13) echo "amon $pin - 3P3VCS_CURR = "  ;;
                 14) echo "amon $pin - 1P1V_USB_CURR = "  ;;
                 15) echo "amon $pin - 5P0V_US_CURR = "  ;;
                 16) echo "amon $pin - 5P0V_BPLANES_CURR = "  ;;
                 17) echo "amon $pin - 12P0VN= "  ;;
                 18) echo "amon $pin - 12P0VP = "  ;;
                 19) echo "amon $pin - 12P0VQ = "  ;;
                 20) echo "amon $pin - 12P0VR = "  ;;
                 21) echo "amon $pin - TDIODE_C1 = "  ;;
                 22) echo "amon $pin - TDIODE_C3 = "  ;;
                 23) echo "amon $pin - TDIODE_C7 = "  ;;
                 24) echo "amon $pin - TDIODE_C10 = "  ;;
                 25) var=`expr $pin - 24`
                         echo "dmon $var - VRRDY_D0_VDN = "  ;;
                 26) var=`expr $pin - 24`
                         echo "dmon $var - VRRDY_D1_VDN = "  ;;
                 27) var=`expr $pin - 24`
                         echo "dmon $var - VRRDY_D0_VCS = "  ;;
                 28) var=`expr $pin - 24`
                         echo "dmon $var - VRRDY_D1_VCS = "  ;;
                 29) var=`expr $pin - 24`
                         echo "dmon $var - VRRDY_D0_VIO = "  ;;
                 30) var=`expr $pin - 24`
                         echo "dmon $var - VRRDY_D1_VIO = "  ;;
                 31) var=`expr $pin - 24`
                         echo "dmon $var - VRRDY_D0_VPCIE = "  ;;
                 32) var=`expr $pin - 24`
                         echo "dmon $var - VRRDY_D1_VPCIE = "  ;;
                *) cat $0 ;;
        esac
}


for n in {1..32}
do

if [ $n -gt 24 ]
then
	index=`expr $n + 47`
	
	
	var=$(gpioget gpiochip3 $index)
	pin=$(get_pin $n)
	echo ${pin}logic ${var}
	
else
	var=$( cat /sys/bus/i2c/drivers/ucd9000/8-0011/hwmon/hwmon*/in${n}_input )
	
	if [ "$var" == "0" ]
	then
		pin=$(get_pin $n)
		
		echo ${pin}0 volts
	else
		
        if [ ${#var} -lt 4 ];
        then
			if [[ $(($var % 1000)) == 0 ]]; 
			then
				remainder="0"
			else
				remainder=`expr $var % 1000`
				
			fi
        
        pin=$(get_pin $n)
        echo ${pin}"0".${remainder} volts
        else
		
			if [[ $(($var / 1000)) == 0 ]]; 
			then
				integer="0"
			else
				integer=`expr $var / 1000`
			fi
			
			if [[ $(($var % 1000)) == 0 ]]; 
			then
				remainder="0"
			else
				remainder=`expr $var % 1000`
				
			fi
        
        
        pin=$(get_pin $n)
        echo ${pin}${integer}.${remainder} volts
        fi
		
fi
	
	
fi


done
