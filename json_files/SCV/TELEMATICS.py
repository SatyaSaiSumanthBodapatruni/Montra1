canids_SCV_TELEMATICS = [419399690, 419399434, 419399178, 419398922, 419403786, 419403586, 419403018, 419403274, 419401994, 419401482, 419401226, 419400970, 419399946, 419398410, 419398154]

json_SCV_TELEMATICS = {
    "419399690": {
        "name": "TP18_Vehicle_Status_Info",
        "id": 419399690,
        "signals": [
            {
                "name": "TS_Brake_Status",
                "start_bit": 0,
                "bit_length": 8,
                "bitindexes": [
                    0,
                    1,
                    9,
                    16
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 250,
                "comment": "This signal indicates the status of the Regeneration",
                "row": 0,
                "state": {
                    "1": "On",
                    "0": "Off"
                }
            },
            {
                "name": "TS_Vehicle_Status",
                "start_bit": 8,
                "bit_length": 8,
                "bitindexes": [
                    8,
                    9,
                    17,
                    24
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 250,
                "comment": "This signal indicates the status of the Regeneration",
                "row": 1,
                "state": {
                    "5": "Sleep",
                    "4": "Stop",
                    "3": "Idle",
                    "2": "Charging",
                    "1": "Moving",
                    "0": "No mode"
                }
            },
            {
                "name": "TS_Reserved_19",
                "start_bit": 16,
                "bit_length": 8,
                "bitindexes": [
                    16,
                    17,
                    25,
                    32
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 100,
                "comment": "",
                "row": 2,
                "state": {}
            },
            {
                "name": "TS_Reserved_15",
                "start_bit": 24,
                "bit_length": 8,
                "bitindexes": [
                    24,
                    25,
                    33,
                    40
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 250,
                "comment": "VCU Indicates the Vehicle Interior Temperature signal to IC",
                "row": 3,
                "state": {}
            },
            {
                "name": "TS_Reserved_16",
                "start_bit": 32,
                "bit_length": 8,
                "bitindexes": [
                    32,
                    33,
                    41,
                    48
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 250,
                "comment": "VCU Indicates the Vehicle Interior Temperature signal to IC",
                "row": 4,
                "state": {}
            }
        ]
    },
    "419399434": {
        "name": "TP17_MCU_Motor_Parameters",
        "id": 419399434,
        "signals": [
            {
                "name": "TS_MCU_Current_DC",
                "start_bit": 0,
                "bit_length": 16,
                "bitindexes": [
                    0,
                    1,
                    1,
                    16
                ],
                "byte_order": "little_endian",
                "scale": 0.05,
                "offset": -1600,
                "unit": "A",
                "min": -1000,
                "max": 1000,
                "comment": "",
                "row": 5,
                "state": {}
            },
            {
                "name": "TS_Motor_Phase_current_AC",
                "start_bit": 16,
                "bit_length": 16,
                "bitindexes": [
                    16,
                    17,
                    17,
                    32
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "A",
                "min": "",
                "max": 1000,
                "comment": "",
                "row": 6,
                "state": {}
            },
            {
                "name": "TS_Motor_Temperature",
                "start_bit": 32,
                "bit_length": 8,
                "bitindexes": [
                    32,
                    33,
                    41,
                    48
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": -40,
                "unit": "Deg C",
                "min": -40,
                "max": 210,
                "comment": "",
                "row": 7,
                "state": {}
            },
            {
                "name": "TS_Controller_Temperature",
                "start_bit": 40,
                "bit_length": 8,
                "bitindexes": [
                    40,
                    41,
                    49,
                    56
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": -40,
                "unit": "Deg C",
                "min": -40,
                "max": 210,
                "comment": "",
                "row": 8,
                "state": {}
            },
            {
                "name": "TS_Motor_RPM",
                "start_bit": 48,
                "bit_length": 16,
                "bitindexes": [
                    48,
                    49,
                    49,
                    64
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": -32127,
                "unit": "rpm",
                "min": -12000,
                "max": 12000,
                "comment": "",
                "row": 9,
                "state": {}
            }
        ]
    },
    "419399178": {
        "name": "TP16_Battery_Capacity_Info",
        "id": 419399178,
        "signals": [
            {
                "name": "TS_Battery_Capacity_Remaining",
                "start_bit": 0,
                "bit_length": 16,
                "bitindexes": [
                    0,
                    1,
                    1,
                    16
                ],
                "byte_order": "little_endian",
                "scale": 0.01,
                "offset": 0,
                "unit": "Ah",
                "min": "",
                "max": 642.55,
                "comment": "",
                "row": 10,
                "state": {}
            },
            {
                "name": "TS_Battery_Full_Capacity",
                "start_bit": 16,
                "bit_length": 16,
                "bitindexes": [
                    16,
                    17,
                    17,
                    32
                ],
                "byte_order": "little_endian",
                "scale": 0.01,
                "offset": 0,
                "unit": "Ah",
                "min": "",
                "max": 642.55,
                "comment": "",
                "row": 11,
                "state": {}
            },
            {
                "name": "TS_Reserved_22",
                "start_bit": 32,
                "bit_length": 8,
                "bitindexes": [
                    32,
                    33,
                    41,
                    48
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 250,
                "comment": "",
                "row": 12,
                "state": {}
            },
            {
                "name": "TS_Reserved_14",
                "start_bit": 40,
                "bit_length": 16,
                "bitindexes": [
                    40,
                    41,
                    41,
                    56
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 64255,
                "comment": "",
                "row": 13,
                "state": {}
            }
        ]
    },
    "419398922": {
        "name": "TP15_Trip_Details",
        "id": 419398922,
        "signals": [
            {
                "name": "TS_TripA_meter",
                "start_bit": 0,
                "bit_length": 24,
                "bitindexes": [
                    0,
                    1,
                    -7,
                    16
                ],
                "byte_order": "little_endian",
                "scale": 0.1,
                "offset": 0,
                "unit": "km",
                "min": "",
                "max": 1644953.5,
                "comment": "This signal indicates Trip A info.",
                "row": 14,
                "state": {}
            },
            {
                "name": "TS_TripB_Meter",
                "start_bit": 24,
                "bit_length": 24,
                "bitindexes": [
                    24,
                    25,
                    17,
                    40
                ],
                "byte_order": "little_endian",
                "scale": 0.1,
                "offset": 0,
                "unit": "km",
                "min": "",
                "max": 1644953.5,
                "comment": "This signal indicates Trip B info.",
                "row": 15,
                "state": {}
            },
            {
                "name": "TS_Reserved_10",
                "start_bit": 48,
                "bit_length": 16,
                "bitindexes": [
                    48,
                    49,
                    49,
                    64
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 64255,
                "comment": "This signal indicates that if any faults in electic drive system",
                "row": 16,
                "state": {}
            }
        ]
    },
    "419403786": {
        "name": "TP14_Battery_reserve_mode_status",
        "id": 419403786,
        "signals": [
            {
                "name": "TS_battery_reserve_enable_status",
                "start_bit": 0,
                "bit_length": 8,
                "bitindexes": [
                    0,
                    1,
                    9,
                    16
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 250,
                "comment": "Status information on battery reserved mode",
                "row": 17,
                "state": {
                    "1": "On",
                    "0": "Off"
                }
            }
        ]
    },
    "419403586": {
        "name": "TP13_Battery_Reserve_mode",
        "id": 419403586,
        "signals": [
            {
                "name": "TS_Reserved_SOC_Enable_Cmd",
                "start_bit": 0,
                "bit_length": 8,
                "bitindexes": [
                    0,
                    1,
                    9,
                    16
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "This signal is used to the enable reserved SOC.\n",
                "row": 18,
                "state": {
                    "1": "On",
                    "0": "Off"
                }
            }
        ]
    },
    "419403018": {
        "name": "TP11_EPAS_status_Info",
        "id": 419403018,
        "signals": [
            {
                "name": "TS_EPAS_status",
                "start_bit": 0,
                "bit_length": 2,
                "bitindexes": [
                    0,
                    1,
                    15,
                    16
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 3,
                "comment": "",
                "row": 19,
                "state": {
                    "3": "Reserved for future use",
                    "2": "EPAS is not working",
                    "1": "Reserved for future use",
                    "0": "EPAS is working normal"
                }
            },
            {
                "name": "TS_EPAS_CAN_health",
                "start_bit": 2,
                "bit_length": 4,
                "bitindexes": [
                    0,
                    3,
                    15,
                    16
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 20,
                "state": {}
            }
        ]
    },
    "419403274": {
        "name": "TP12_Fault_Codes",
        "id": 419403274,
        "signals": [
            {
                "name": "TS_BMS_Faults",
                "start_bit": 0,
                "bit_length": 8,
                "bitindexes": [
                    0,
                    1,
                    9,
                    16
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 250,
                "comment": "",
                "row": 21,
                "state": {
                    "6": "Charge current limit fault",
                    "5": "Dicharge current limit fault",
                    "4": "High cell temperature fault",
                    "3": "Low cell temperature fault",
                    "2": "Cell Over voltage fault",
                    "1": "Cell Under voltage fault",
                    "0": "No Fault Code"
                }
            },
            {
                "name": "TS_MCU_FaultCodes",
                "start_bit": 8,
                "bit_length": 8,
                "bitindexes": [
                    8,
                    9,
                    17,
                    24
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 250,
                "comment": "",
                "row": 22,
                "state": {
                    "36": "W phase current sensor fault",
                    "35": "V phase current sensor fault",
                    "34": "U phase current sensor fault",
                    "33": "Motor_Overspeed_fault",
                    "32": "Drive overtemp fault",
                    "31": "Drive overload",
                    "30": "W phase hall disconnection fault",
                    "29": "V phase hall disconnection fault",
                    "28": "U phase hall disconnection fault",
                    "27": "LV_PwrSupply_Undervoltage_fault",
                    "26": "PwrSuplyDriveborad_exceeds_limit",
                    "25": "Controller_drive_Abnormal_fault",
                    "24": "Resolver_Connector_is_loose",
                    "23": "Hardware_over_voltage_fault",
                    "22": "Drive board over run fault",
                    "21": "OverVolt_basline_HW_wrong",
                    "20": "Drive_parameter_R/W_Fault",
                    "19": "DriveTempSensor_Disconnected",
                    "18": "MotorOutputGND_ShortCkted",
                    "17": "Drive protection fault",
                    "16": "Software over voltage fault",
                    "15": "Software over current fault",
                    "14": "Communication fault",
                    "13": "CAN Enable fault",
                    "12": "Lost phase",
                    "11": "High voltage interlock",
                    "10": "12V uner voltage fault",
                    "9": "12V over voltage fault",
                    "8": "Stall detected",
                    "7": "Resolver fault",
                    "6": "Motor_Temp_Sensor_Fault",
                    "5": "Controller_Over_Temperature",
                    "4": "Motor_Over_Temperature",
                    "3": "HardwareOverCurrent",
                    "2": "OverVoltHV",
                    "1": "UnderVoltHV",
                    "0": "No fault"
                }
            },
            {
                "name": "TS_OBC_faults",
                "start_bit": 16,
                "bit_length": 4,
                "bitindexes": [
                    16,
                    17,
                    29,
                    32
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 23,
                "state": {
                    "15": "OBC_Communication_fault",
                    "14": "OBC_Inlet_tempsensor_fault",
                    "13": "OBC_Internal_shutdown",
                    "12": "OBC_Internal_Derate",
                    "11": "OBC_Overtemp_shutdown",
                    "10": "OBC_Overtemp_Derate",
                    "9": "OBC_InputOverCurrent_fault",
                    "8": "OBC_12V_fault",
                    "7": "OBC_OutputShortckt_fault",
                    "6": "OBC_OutputOvervolt_fault",
                    "5": "OBC_OutputUndervolt_fault",
                    "4": "OBC_InputUndervolt_fault",
                    "3": "OBC_InputOvervoltage fault",
                    "2": "OBC_Reserved1",
                    "1": "OBC_hardware_protection",
                    "0": "No fault"
                }
            },
            {
                "name": "TS_DC_DC_Faults",
                "start_bit": 20,
                "bit_length": 4,
                "bitindexes": [
                    16,
                    20,
                    999,
                    999
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 24,
                "state": {
                    "15": "DCDC_Reserved_fault",
                    "14": "DCDC_12V_fault",
                    "13": "Output_hardware_volt_over",
                    "12": "Output_hardware_open",
                    "11": "Hardware fault",
                    "10": "Output_Power_Over_Fault",
                    "9": "DCDC Communication_fault",
                    "8": "Internal_protection_fault",
                    "7": "Output_short_circuit_protection",
                    "6": "Input_Undervoltage_fault",
                    "5": "Input_Overvoltage_fault",
                    "4": "Output_Undervoltage_fault",
                    "3": "Output_Overvoltage_fault",
                    "2": "Output_Overcurrent_fault",
                    "1": "Over_Temperature_shutdown",
                    "0": "No Fault Code"
                }
            },
            {
                "name": "TS_EPAS_FaultCode",
                "start_bit": 24,
                "bit_length": 8,
                "bitindexes": [
                    24,
                    25,
                    33,
                    40
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 250,
                "comment": "EPAS Shall publish various type of errors to VCU",
                "row": 25,
                "state": {
                    "12": "Continus/PeakCurentDetectionFail",
                    "11": "CAN timeout fault",
                    "10": "ADC freeze fault",
                    "9": "ADC IRQ fault",
                    "8": "Feedback path fault",
                    "4": "Angle sensor fault",
                    "15": "Gate driver over temp",
                    "14": "Gate driver short",
                    "13": "PCB over temp fault",
                    "7": "Current sensor fault",
                    "6": "ADC reference voltage fault",
                    "5": "Torque sensor fault",
                    "3": "Motor drive fault",
                    "2": "5V fault",
                    "1": "12V Battery Supply fault",
                    "0": "No error"
                }
            },
            {
                "name": "TS_Thermal_system_faultcodes",
                "start_bit": 32,
                "bit_length": 8,
                "bitindexes": [
                    32,
                    33,
                    41,
                    48
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 250,
                "comment": "This signal represents the compressor error flags.",
                "row": 26,
                "state": {
                    "38": "Radiator_Fan_Failure",
                    "37": "TCS_PumpFailure",
                    "36": "TCS_CoolantLevel_sw_Short_Batt",
                    "35": "TCS_Cout_TempSensor_Short_Gnd",
                    "34": "TCS_Cin_TempSensor_Short_Battery",
                    "33": "TCS_Cin_TempSensor_Short_Gnd",
                    "32": "TCS_CoolantLevel_sw_Short_Batt",
                    "31": "TCS_CoolantLevel_sw_Short_GND",
                    "30": "TCS_Low_coolant_level",
                    "29": "Comp_stall_error",
                    "28": "Comp_Inpower_error",
                    "27": "Comp_Current_sensor_Error",
                    "26": "Comp_Temp_Sensor_error",
                    "25": "Comp_LIN_protocol_Error",
                    "24": "Comp_Communication_Error",
                    "23": "Comp_Over_load",
                    "22": "Comp_Over_heat",
                    "21": "Comp_LV_Over_voltage_error",
                    "20": "Comp_LV_Under_voltage_error",
                    "19": "Comp_HV_Over_voltage_fault",
                    "18": "Comp_HV_Under_Voltage_Fault",
                    "17": "Condensor Fan failure",
                    "16": "BCS pump failure",
                    "15": "Low Vehicle voltage",
                    "14": "Suction_PresseureSensrShort_Gnd",
                    "13": "Suction_PresseureSensrShort_Batt",
                    "12": "Dischrg_PresseureSensrShort_Gnd",
                    "11": "BCS_Cout_TempSensor_Short_Batt",
                    "10": "BCS_Cout_TempSensor_Short_Gnd",
                    "9": "BCS_Cin_TempSensor_Short_Battery",
                    "7": "Ambientsensor_Short_Battery",
                    "6": "Ambientsensor_Short_Ground",
                    "5": "BCS_CoolantLevel_sw_Short_Batt",
                    "3": "Referigerent leakage error",
                    "8": "BCS_Cin_TempSensor_Short_Gnd",
                    "4": "BCS_CoolantLevel_sw_Short_GND",
                    "2": "BCS_Low_coolant_level",
                    "1": "Dischrg_PresseureSensrShort_Bat",
                    "0": "No error"
                }
            },
            {
                "name": "TS_VCU_Faults",
                "start_bit": 40,
                "bit_length": 8,
                "bitindexes": [
                    40,
                    41,
                    49,
                    56
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 250,
                "comment": "",
                "row": 27,
                "state": {
                    "16": "SDNR_Not_in_Neutral",
                    "15": "Reserved for future use",
                    "14": "Emergency_Shutoff_Request",
                    "13": "Brake_Coherence_Fault",
                    "12": "Recovery_Throttle",
                    "11": "Brake_Not_pressed",
                    "10": "Throttle_Not_released",
                    "9": "HPD or Sequencing Fault",
                    "8": "Brakepot_High",
                    "7": "Brakepot_Low",
                    "6": "Primary_ThrottlePot_High",
                    "5": "Primary_ThrottlePot_Low",
                    "4": "MainContactorDidNotClose",
                    "3": "MainContactorWelded",
                    "2": "Service lamp indication",
                    "1": "Malfunction Indication",
                    "0": "No fault code"
                }
            }
        ]
    },
    "419401994": {
        "name": "TP10_Date_Time_Info",
        "id": 419401994,
        "signals": [
            {
                "name": "TS_Hour_Information",
                "start_bit": 0,
                "bit_length": 8,
                "bitindexes": [
                    0,
                    1,
                    9,
                    16
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "hr",
                "min": "",
                "max": 24,
                "comment": "This signal respresents the hour Information.\n",
                "row": 28,
                "state": {}
            },
            {
                "name": "TS_Minute_Information",
                "start_bit": 8,
                "bit_length": 8,
                "bitindexes": [
                    8,
                    9,
                    17,
                    24
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "min",
                "min": "",
                "max": 60,
                "comment": "This signal represents the minute information.",
                "row": 29,
                "state": {}
            },
            {
                "name": "TS_Milli_Seconds_Info",
                "start_bit": 16,
                "bit_length": 16,
                "bitindexes": [
                    16,
                    17,
                    17,
                    32
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "ms",
                "min": "",
                "max": 1000,
                "comment": "MilliSeconds Information on VCU from IC.\n",
                "row": 30,
                "state": {}
            },
            {
                "name": "TS_Date_Information",
                "start_bit": 32,
                "bit_length": 8,
                "bitindexes": [
                    32,
                    33,
                    41,
                    48
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 31,
                "comment": "Date Information.\n",
                "row": 31,
                "state": {}
            },
            {
                "name": "TS_Month_Information",
                "start_bit": 40,
                "bit_length": 4,
                "bitindexes": [
                    40,
                    41,
                    53,
                    56
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "Month Information on VCU from IC.\n",
                "row": 32,
                "state": {
                    "12": "December",
                    "11": "November",
                    "10": "October",
                    "9": "September",
                    "8": "August",
                    "7": "July",
                    "6": "June",
                    "5": "May",
                    "4": "April",
                    "3": "March",
                    "2": "February",
                    "1": "January",
                    "0": "Unused"
                }
            },
            {
                "name": "TS_Year_Information",
                "start_bit": 44,
                "bit_length": 16,
                "bitindexes": [
                    40,
                    45,
                    45,
                    56
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 1985,
                "unit": "year",
                "min": 1985,
                "max": 2235,
                "comment": "This signal represents the Year Information.\n",
                "row": 33,
                "state": {}
            },
            {
                "name": "TS_Clock_Mode",
                "start_bit": 60,
                "bit_length": 1,
                "bitindexes": [
                    59,
                    60,
                    999,
                    999
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "Clock Mode Information on VCU from IC.",
                "row": 34,
                "state": {
                    "1": "24 Hour Mode",
                    "0": "12 Hour Mode"
                }
            }
        ]
    },
    "419401482": {
        "name": "TP8_Driver_Info_parameters_3",
        "id": 419401482,
        "signals": [
            {
                "name": "TS_Vehicle_Odometer",
                "start_bit": 0,
                "bit_length": 24,
                "bitindexes": [
                    0,
                    1,
                    -7,
                    16
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "km",
                "min": "",
                "max": 16449535,
                "comment": "",
                "row": 35,
                "state": {}
            },
            {
                "name": "TS_TCS_Coolant_temperature",
                "start_bit": 24,
                "bit_length": 8,
                "bitindexes": [
                    24,
                    25,
                    33,
                    40
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": -40,
                "unit": "Deg C",
                "min": -40,
                "max": 210,
                "comment": "VCU Indicates the Vehicle Interior Temperature signal to IC",
                "row": 36,
                "state": {}
            },
            {
                "name": "TS_Vehicle_Interior_Temperature",
                "start_bit": 32,
                "bit_length": 8,
                "bitindexes": [
                    32,
                    33,
                    41,
                    48
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": -40,
                "unit": "Deg C",
                "min": -40,
                "max": 210,
                "comment": "This signal Indicates the Coolant Temperature.",
                "row": 37,
                "state": {}
            },
            {
                "name": "TS_BCS_Coolant_Temperature",
                "start_bit": 40,
                "bit_length": 8,
                "bitindexes": [
                    40,
                    41,
                    49,
                    56
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": -40,
                "unit": "Deg C",
                "min": -40,
                "max": 210,
                "comment": "This signal Indicates the Coolant Temperature.",
                "row": 38,
                "state": {}
            },
            {
                "name": "TS_Ambient_Temperature",
                "start_bit": 48,
                "bit_length": 8,
                "bitindexes": [
                    48,
                    49,
                    57,
                    64
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": -40,
                "unit": "Deg C",
                "min": -40,
                "max": 210,
                "comment": "VCU Indicates the Ambient temperature signal to IC.",
                "row": 39,
                "state": {}
            },
            {
                "name": "TS_Reserved_11",
                "start_bit": 56,
                "bit_length": 1,
                "bitindexes": [
                    56,
                    57,
                    72,
                    72
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "This signal indicates that if any faults in electic drive system",
                "row": 40,
                "state": {}
            },
            {
                "name": "TS_Reserved_12",
                "start_bit": 57,
                "bit_length": 1,
                "bitindexes": [
                    56,
                    57,
                    999,
                    999
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "This signal indicates that if any faults in electic drive system",
                "row": 41,
                "state": {}
            }
        ]
    },
    "419401226": {
        "name": "TP7_Driver_Info_parameters_2",
        "id": 419401226,
        "signals": [
            {
                "name": "TS_DTE_Info",
                "start_bit": 0,
                "bit_length": 8,
                "bitindexes": [
                    0,
                    1,
                    9,
                    16
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "km",
                "min": "",
                "max": 250,
                "comment": "This signal indicates distance to empty info.",
                "row": 42,
                "state": {}
            },
            {
                "name": "TS_TTC_Hour_Info",
                "start_bit": 8,
                "bit_length": 8,
                "bitindexes": [
                    8,
                    9,
                    17,
                    24
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "hr",
                "min": "",
                "max": 24,
                "comment": "This signal indicates the hour information of the time taken to complete the charge.",
                "row": 43,
                "state": {}
            },
            {
                "name": "TS_TTC_Minute_Info",
                "start_bit": 16,
                "bit_length": 8,
                "bitindexes": [
                    16,
                    17,
                    25,
                    32
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "min",
                "min": "",
                "max": 60,
                "comment": "This signal indicates the minute information of the time taken to complete the charge (TTC).",
                "row": 44,
                "state": {}
            },
            {
                "name": "TS_Reserved_8",
                "start_bit": 24,
                "bit_length": 16,
                "bitindexes": [
                    24,
                    25,
                    25,
                    40
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 64255,
                "comment": "This signal indicates that if any faults in electic drive system",
                "row": 45,
                "state": {}
            },
            {
                "name": "TS_Reserved_9",
                "start_bit": 40,
                "bit_length": 16,
                "bitindexes": [
                    40,
                    41,
                    41,
                    56
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 64255,
                "comment": "This signal indicates that if any faults in electic drive system",
                "row": 46,
                "state": {}
            }
        ]
    },
    "419400970": {
        "name": "TP6_Driver_Info_Parameters",
        "id": 419400970,
        "signals": [
            {
                "name": "TS_Customer_SOC",
                "start_bit": 0,
                "bit_length": 8,
                "bitindexes": [
                    0,
                    1,
                    9,
                    16
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "%",
                "min": "",
                "max": 100,
                "comment": "Customer SOC information  transmitted by VCU.",
                "row": 47,
                "state": {}
            },
            {
                "name": "TS_vehicle_speed",
                "start_bit": 8,
                "bit_length": 8,
                "bitindexes": [
                    8,
                    9,
                    17,
                    24
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "kmph",
                "min": "",
                "max": 150,
                "comment": "Vehicle speed information on IC.",
                "row": 48,
                "state": {}
            },
            {
                "name": "TS_Energy_Consumption",
                "start_bit": 16,
                "bit_length": 16,
                "bitindexes": [
                    16,
                    17,
                    17,
                    32
                ],
                "byte_order": "little_endian",
                "scale": 0.01953125,
                "offset": 0,
                "unit": "kWh/km",
                "min": "",
                "max": 1254.9804,
                "comment": "Energy consumption by the inverter.",
                "row": 49,
                "state": {}
            },
            {
                "name": "TS_Act_Drive_mode",
                "start_bit": 32,
                "bit_length": 3,
                "bitindexes": [
                    32,
                    33,
                    46,
                    48
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 7,
                "comment": "This signal represents the drive mode/gear selector mode.",
                "row": 50,
                "state": {
                    "4": "Limphome Mode",
                    "3": "Reverse Mode",
                    "2": "Neutral Mode",
                    "1": "Power Mode",
                    "0": "City Mode"
                }
            },
            {
                "name": "TS_Drive_Efficiency",
                "start_bit": 35,
                "bit_length": 3,
                "bitindexes": [
                    32,
                    35,
                    999,
                    999
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 7,
                "comment": "Represents the Drive efficiency of the inverter.",
                "row": 51,
                "state": {
                    "3": "Reserved",
                    "2": "Regen",
                    "1": "Reserved",
                    "0": "ECO"
                }
            }
        ]
    },
    "419399946": {
        "name": "TP5_ControllerDiagnosticParametr",
        "id": 419399946,
        "signals": [
            {
                "name": "TS_Drive_Enabled",
                "start_bit": 0,
                "bit_length": 1,
                "bitindexes": [
                    0,
                    1,
                    16,
                    16
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "This signal indicates the status of power stage enable signal\n",
                "row": 52,
                "state": {
                    "1": "ON",
                    "0": "OFF"
                }
            },
            {
                "name": "TS_Reserved_6",
                "start_bit": 1,
                "bit_length": 4,
                "bitindexes": [
                    0,
                    2,
                    14,
                    16
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "VCU Indicates the Vehicle Interior Temperature signal to IC",
                "row": 53,
                "state": {}
            },
            {
                "name": "TS_MCU_Error_Active",
                "start_bit": 5,
                "bit_length": 1,
                "bitindexes": [
                    4,
                    5,
                    999,
                    999
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "This signal indicates that If any error is active\n",
                "row": 54,
                "state": {
                    "1": "ON",
                    "0": "Off"
                }
            },
            {
                "name": "TS_MCU_Warning_Active",
                "start_bit": 6,
                "bit_length": 1,
                "bitindexes": [
                    5,
                    6,
                    999,
                    999
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "This signal indicats that If any warning is active\n",
                "row": 55,
                "state": {
                    "1": "ON",
                    "0": "Off"
                }
            },
            {
                "name": "TS_Nms_Status",
                "start_bit": 7,
                "bit_length": 2,
                "bitindexes": [
                    5,
                    7,
                    999,
                    999
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 3,
                "comment": "This signal indicates the status of Network management",
                "row": 56,
                "state": {
                    "3": "Error",
                    "2": "active",
                    "1": "sleep",
                    "0": "wakeup"
                }
            },
            {
                "name": "TS_Reserved_7",
                "start_bit": 9,
                "bit_length": 2,
                "bitindexes": [
                    8,
                    10,
                    24,
                    24
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 3,
                "comment": "This signal indicates that if any faults in electic drive system",
                "row": 57,
                "state": {}
            },
            {
                "name": "TS_Derating_signal_status",
                "start_bit": 11,
                "bit_length": 4,
                "bitindexes": [
                    8,
                    12,
                    24,
                    24
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "This signal indicates the status of Derating Mode or Limphome Mode.",
                "row": 58,
                "state": {
                    "1": "On",
                    "0": "Off"
                }
            },
            {
                "name": "TS_Regen_Status",
                "start_bit": 15,
                "bit_length": 1,
                "bitindexes": [
                    14,
                    15,
                    999,
                    999
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "This signal indicates the status of the Regeneration",
                "row": 59,
                "state": {
                    "1": "ON",
                    "0": "OFF"
                }
            }
        ]
    },
    "419398410": {
        "name": "TP2_Battery_thermal_parameters",
        "id": 419398410,
        "signals": [
            {
                "name": "TS_High_Temperature",
                "start_bit": 0,
                "bit_length": 16,
                "bitindexes": [
                    0,
                    1,
                    1,
                    16
                ],
                "byte_order": "little_endian",
                "scale": 0.03125,
                "offset": -273,
                "unit": "Deg C",
                "min": -40,
                "max": 210,
                "comment": "his signal indicates the highest temperature of the battery pack.",
                "row": 60,
                "state": {}
            },
            {
                "name": "TS_Reserved_20",
                "start_bit": 16,
                "bit_length": 8,
                "bitindexes": [
                    16,
                    17,
                    25,
                    32
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 250,
                "comment": "This is ID of the highest temperature thermistor.",
                "row": 61,
                "state": {}
            },
            {
                "name": "TS_Reserved_21",
                "start_bit": 24,
                "bit_length": 8,
                "bitindexes": [
                    24,
                    25,
                    33,
                    40
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 250,
                "comment": "This is the ID of the Lowest temperature thermistor.",
                "row": 62,
                "state": {}
            },
            {
                "name": "TS_Low_Temperature",
                "start_bit": 32,
                "bit_length": 16,
                "bitindexes": [
                    32,
                    33,
                    33,
                    48
                ],
                "byte_order": "little_endian",
                "scale": 0.03125,
                "offset": -273,
                "unit": "Deg C",
                "min": -40,
                "max": 210,
                "comment": "This signal indicates the location of cell  which is having Low temperature.",
                "row": 63,
                "state": {}
            },
            {
                "name": "TS_Reserved_2",
                "start_bit": 48,
                "bit_length": 8,
                "bitindexes": [
                    48,
                    49,
                    57,
                    64
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 250,
                "comment": "VCU Indicates the Vehicle Interior Temperature signal to IC",
                "row": 64,
                "state": {}
            },
            {
                "name": "TS_Reserved_3",
                "start_bit": 56,
                "bit_length": 8,
                "bitindexes": [
                    56,
                    57,
                    65,
                    72
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 250,
                "comment": "VCU Indicates the Vehicle Interior Temperature signal to IC",
                "row": 65,
                "state": {}
            }
        ]
    },
    "419398154": {
        "name": "TP1_Pack_Parameters",
        "id": 419398154,
        "signals": [
            {
                "name": "TS_Pack_current",
                "start_bit": 0,
                "bit_length": 16,
                "bitindexes": [
                    0,
                    1,
                    1,
                    16
                ],
                "byte_order": "little_endian",
                "scale": 0.05,
                "offset": -1600,
                "unit": "A",
                "min": -1000,
                "max": 1000,
                "comment": "The Current IN or OUT of the Battery pack.",
                "row": 66,
                "state": {}
            },
            {
                "name": "TS_Pack_Instant_Voltage",
                "start_bit": 16,
                "bit_length": 16,
                "bitindexes": [
                    16,
                    17,
                    17,
                    32
                ],
                "byte_order": "little_endian",
                "scale": 0.05,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 1000,
                "comment": "The voltage level of battery pack.",
                "row": 67,
                "state": {}
            },
            {
                "name": "TS_Pack_SOC",
                "start_bit": 32,
                "bit_length": 16,
                "bitindexes": [
                    32,
                    33,
                    33,
                    48
                ],
                "byte_order": "little_endian",
                "scale": 0.0015625,
                "offset": 0,
                "unit": "%",
                "min": "",
                "max": 100,
                "comment": "This signal indicates the state of Charge of battery pack. ",
                "row": 68,
                "state": {}
            },
            {
                "name": "TS_Reserved_1",
                "start_bit": 48,
                "bit_length": 16,
                "bitindexes": [
                    48,
                    49,
                    49,
                    64
                ],
                "byte_order": "little_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 64255,
                "comment": "VCU Indicates the Vehicle Interior Temperature signal to IC",
                "row": 69,
                "state": {}
            }
        ]
    }
}