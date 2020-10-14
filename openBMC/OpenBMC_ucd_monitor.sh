set -eu
function get_pin() {
        local pin=$1

        case $pin in
                1) echo "amon $pin\t\t12V Bulk\t\t "  ;;
                2) echo "amon $pin\t\t5P0VA_USB\t\t "  ;;
                3) echo "amon $pin\t\t5P0V BP\t\t\t "  ;;
                 4) echo "amon $pin\t\t3P3VA\t\t\t "  ;;
                 5) echo "amon $pin\t\t3P3VB\t\t\t "  ;;
                 6) echo "amon $pin\t\t1P5V_AVDD\t\t "  ;;
                 7) echo "amon $pin\t\t1P1VA_USB\t\t "  ;;
                 8) echo "amon $pin\t\tVDDA_DCM0\t\t "  ;;
                 9) echo "amon $pin\t\tVDDB_DCM0\t\t "  ;;
                 10) echo "amon $pin\t\tVDDA_DCM1\t\t "  ;;
                 11) echo "amon $pin\t\tVDDB_DCM1\t\t "  ;;
                 12) echo "amon $pin\t\t12P0VCS_CURR\t\t "  ;;
                 13) echo "amon $pin\t\t3P3VCS_CURR\t\t "  ;;
                 14) echo "amon $pin\t\t1P1V_USB_CURR\t\t "  ;;
                 15) echo "amon $pin\t\t5P0V_US_CURR\t\t "  ;;
                 16) echo "amon $pin\t\t5P0V_BPLANES_CURR\t "  ;;
                 17) echo "amon $pin\t\t12P0VN\t\t\t "  ;;
                 18) echo "amon $pin\t\t12P0VP\t\t\t "  ;;
                 19) echo "amon $pin\t\t12P0VQ\t\t\t "  ;;
                 20) echo "amon $pin\t\t12P0VR\t\t\t "  ;;
                 21) echo "amon $pin\t\tTDIODE_C1\t\t "  ;;
                 22) echo "amon $pin\t\tTDIODE_C3\t\t "  ;;
                 23) echo "amon $pin\t\tTDIODE_C7\t\t "  ;;
                 24) echo "amon $pin\t\tTDIODE_C10\t\t "  ;;
                 25) var=`expr $pin - 24`
                         echo "dmon $var\t\tVRRDY_D0_VDN\t\t "  ;;
                 26) var=`expr $pin - 24`
                         echo "dmon $var\t\tVRRDY_D1_VDN\t\t "  ;;
                 27) var=`expr $pin - 24`
                         echo "dmon $var\t\tVRRDY_D0_VCS\t\t "  ;;
                 28) var=`expr $pin - 24`
                         echo "dmon $var\t\tVRRDY_D1_VCS\t\t "  ;;
                 29) var=`expr $pin - 24`
                         echo "dmon $var\t\tVRRDY_D0_VIO\t\t "  ;;
                 30) var=`expr $pin - 24`
                         echo "dmon $var\t\tVRRDY_D1_VIO\t\t "  ;;
                 31) var=`expr $pin - 24`
                         echo "dmon $var\t\tVRRDY_D0_VPCIE\t\t "  ;;
                 32) var=`expr $pin - 24`
                         echo "dmon $var\t\tVRRDY_D1_VPCIE\t\t "  ;;
                *) cat $0 ;;
        esac
}


for n in {1..32}
do

if [ $n -gt 24 ]
then
	index=`expr $n + 47`
	
	gpiochip=$(gpiodetect | grep ucd |cut -d ' ' -f1|tr '\n' ' ')
	var=$(gpioget $gpiochip $index)
	pin=$(get_pin $n)
	echo -e ${pin}logic ${var}
	
else
	var=$( cat /sys/bus/i2c/drivers/ucd9000/8-0011/hwmon/hwmon*/in${n}_input )
	
	if [ "$var" == "0" ]
	then
		pin=$(get_pin $n)
		
		
	else
		
		while [ ${#var} -lt 4 ];
		do
			var="0"${var}
			
		done
		
		
        if [ ${#var} -lt 5 ];
        then
			
        
			pin=$(get_pin $n)
			echo -e ${pin}${var:0:1}.${var:1} volts
        else

        
			pin=$(get_pin $n)
			echo -e ${pin}${var:0:2}.${var:2} volts
        fi
		
	fi
	
	
fi


done
 var=$(gpioget $gpiochip 43)
 echo -e "\t\t sys_pwrok \t\t logic ${var}"


