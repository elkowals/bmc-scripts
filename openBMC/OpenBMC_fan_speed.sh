#!/bin/bash

if [ "$#" -lt 1 ]; then
  echo "
NAME
    fan_speed - MAX/LOW/VALUE(rpm) fan speed
SYNOPSIS
    fan_speed [MAX|LOW|VALUE]
              [11200|6000|anyvalue]
EXAMPLE:
    fan_speed 6000
    fan_speed MAX
    fan_speed LOW
  " && exit 1
fi
rpm_value="$1"
if [ "${rpm_value}" == "MAX" ]; then
    # set to 11200 rpms
    systemctl stop phosphor-fan-control@0.service
    busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan0_0` /xyz/openbmc_project/sensors/fan_tach/fan0_0 xyz.openbmc_project.Control.FanSpeed Target t 11200 && busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan1_0` /xyz/openbmc_project/sensors/fan_tach/fan1_0 xyz.openbmc_project.Control.FanSpeed Target t 11200 &&  busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan2_0` /xyz/openbmc_project/sensors/fan_tach/fan2_0 xyz.openbmc_project.Control.FanSpeed Target t 11200 && busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan3_0` /xyz/openbmc_project/sensors/fan_tach/fan3_0 xyz.openbmc_project.Control.FanSpeed Target t 11200 && busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan4_0` /xyz/openbmc_project/sensors/fan_tach/fan4_0 xyz.openbmc_project.Control.FanSpeed Target t 11200 && busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan5_0` /xyz/openbmc_project/sensors/fan_tach/fan5_0 xyz.openbmc_project.Control.FanSpeed Target t 11200
	echo "Fan speeds set to 11200rpms"
elif [ "${rpm_value}" == "LOW" ]; then
    # set to 6000 rpms
    systemctl stop phosphor-fan-control@0.service
    busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan0_0` /xyz/openbmc_project/sensors/fan_tach/fan0_0 xyz.openbmc_project.Control.FanSpeed Target t 6000 && busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan1_0` /xyz/openbmc_project/sensors/fan_tach/fan1_0 xyz.openbmc_project.Control.FanSpeed Target t 6000 &&  busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan2_0` /xyz/openbmc_project/sensors/fan_tach/fan2_0 xyz.openbmc_project.Control.FanSpeed Target t 6000 && busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan3_0` /xyz/openbmc_project/sensors/fan_tach/fan3_0 xyz.openbmc_project.Control.FanSpeed Target t 6000 && busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan4_0` /xyz/openbmc_project/sensors/fan_tach/fan4_0 xyz.openbmc_project.Control.FanSpeed Target t 6000 && busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan5_0` /xyz/openbmc_project/sensors/fan_tach/fan5_0 xyz.openbmc_project.Control.FanSpeed Target t 6000
	echo "Fan speeds set to 6000rpms"
else
    # set by user rpms
	
	systemctl stop phosphor-fan-control@0.service
	b=11200
    if [ $1 -ge $b ]; then
	
		  busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan0_0` /xyz/openbmc_project/sensors/fan_tach/fan0_0 xyz.openbmc_project.Control.FanSpeed Target t 11200 && busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan1_0` /xyz/openbmc_project/sensors/fan_tach/fan1_0 xyz.openbmc_project.Control.FanSpeed Target t 11200 &&  busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan2_0` /xyz/openbmc_project/sensors/fan_tach/fan2_0 xyz.openbmc_project.Control.FanSpeed Target t 11200 && busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan3_0` /xyz/openbmc_project/sensors/fan_tach/fan3_0 xyz.openbmc_project.Control.FanSpeed Target t 11200 && busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan4_0` /xyz/openbmc_project/sensors/fan_tach/fan4_0 xyz.openbmc_project.Control.FanSpeed Target t 11200 && busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan5_0` /xyz/openbmc_project/sensors/fan_tach/fan5_0 xyz.openbmc_project.Control.FanSpeed Target t 11200
		  echo "Fan speeds set to MAX 11200rpms"
	else
			busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan0_0` /xyz/openbmc_project/sensors/fan_tach/fan0_0 xyz.openbmc_project.Control.FanSpeed Target t $rpm_value && busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan1_0` /xyz/openbmc_project/sensors/fan_tach/fan1_0 xyz.openbmc_project.Control.FanSpeed Target t $rpm_value &&  busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan2_0` /xyz/openbmc_project/sensors/fan_tach/fan2_0 xyz.openbmc_project.Control.FanSpeed Target t $rpm_value && busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan3_0` /xyz/openbmc_project/sensors/fan_tach/fan3_0 xyz.openbmc_project.Control.FanSpeed Target t $rpm_value && busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan4_0` /xyz/openbmc_project/sensors/fan_tach/fan4_0 xyz.openbmc_project.Control.FanSpeed Target t $rpm_value && busctl set-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan5_0` /xyz/openbmc_project/sensors/fan_tach/fan5_0 xyz.openbmc_project.Control.FanSpeed Target t $rpm_value
			echo "Fan speeds set to ${rpm_value} rpms"
	fi
	
fi

echo busctl get-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan0_0` /xyz/openbmc_project/sensors/fan_tach/fan0_0 xyz.openbmc_project.Control.FanSpeed Target && busctl get-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan1_0` /xyz/openbmc_project/sensors/fan_tach/fan1_0 xyz.openbmc_project.Control.FanSpeed Target &&  busctl get-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan2_0` /xyz/openbmc_project/sensors/fan_tach/fan2_0 xyz.openbmc_project.Control.FanSpeed Target && busctl get-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan3_0` /xyz/openbmc_project/sensors/fan_tach/fan3_0 xyz.openbmc_project.Control.FanSpeed Target && busctl get-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan4_0` /xyz/openbmc_project/sensors/fan_tach/fan4_0 xyz.openbmc_project.Control.FanSpeed Target && busctl get-property `mapper get-service /xyz/openbmc_project/sensors/fan_tach/fan5_0` /xyz/openbmc_project/sensors/fan_tach/fan5_0 xyz.openbmc_project.Control.FanSpeed Target