canids_3W_MCU = [1544, 522, 1367, 1366, 1365, 1364, 1363, 1362, 1361, 1360, 1025, 1028, 1303, 1288, 1287, 1291, 1285, 1283, 1284, 1286]
json_3W_MCU ={
    "513": {
        "name": "BAT_INFO_SOC",
        "id": 513,
        "signals": [
            {
                "name": "BAT_INFO_SOC",
                "start_bit": 39,
                "bit_length": 16,
                "bitindexes": [
                    32,
                    40,
                    40,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "Percentage",
                "min": "",
                "max": 100,
                "comment": "",
                "row": 0,
                "state": {}
            }
        ]
    },
    "1544": {
        "name": "MCU_PM_TEMP",
        "id": 1544,
        "signals": [
            {
                "name": "MCU_PM_TEMP1_signal",
                "start_bit": 7,
                "bit_length": 8,
                "bitindexes": [
                    0,
                    8,
                    16,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": -55,
                "unit": "",
                "min": -55,
                "max": 200,
                "comment": "",
                "row": 1,
                "state": {}
            },
            {
                "name": "MCU_PM_TEMP2_signal",
                "start_bit": 15,
                "bit_length": 8,
                "bitindexes": [
                    8,
                    16,
                    24,
                    24
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": -55,
                "unit": "",
                "min": -55,
                "max": 200,
                "comment": "",
                "row": 2,
                "state": {}
            },
            {
                "name": "MCU_PM_TEMP3_signal",
                "start_bit": 23,
                "bit_length": 8,
                "bitindexes": [
                    16,
                    24,
                    32,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": -55,
                "unit": "",
                "min": -55,
                "max": 200,
                "comment": "",
                "row": 3,
                "state": {}
            }
        ]
    },
    "522": {
        "name": "BMS_Bat_Volt_Mon",
        "id": 522,
        "signals": [
            {
                "name": "BMS_batVoltMon_VoltErr",
                "start_bit": 7,
                "bit_length": 8,
                "bitindexes": [
                    0,
                    8,
                    16,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 4,
                "state": {}
            },
            {
                "name": "Battery_Temp_Fault",
                "start_bit": 31,
                "bit_length": 8,
                "bitindexes": [
                    24,
                    32,
                    40,
                    40
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 5,
                "state": {}
            }
        ]
    },
    "1367": {
        "name": "Cfg_Msg4_Tx",
        "id": 1367,
        "signals": [
            {
                "name": "Cfg_Max_EcoModeSpeed_Tx",
                "start_bit": 7,
                "bit_length": 14,
                "bitindexes": [
                    0,
                    8,
                    10,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "rpm",
                "min": "",
                "max": 16383,
                "comment": "",
                "row": 6,
                "state": {}
            },
            {
                "name": "Cfg_Max_ParkModeSpeed_Tx",
                "start_bit": 23,
                "bit_length": 12,
                "bitindexes": [
                    16,
                    24,
                    28,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "rpm",
                "min": "",
                "max": 4095,
                "comment": "",
                "row": 7,
                "state": {}
            },
            {
                "name": "Cfg_Max_ReverseSpeed_Tx",
                "start_bit": 39,
                "bit_length": 10,
                "bitindexes": [
                    32,
                    40,
                    46,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "Rpm",
                "min": "",
                "max": 1023,
                "comment": "",
                "row": 8,
                "state": {}
            }
        ]
    },
    "1366": {
        "name": "Cfg_Msg3_Tx",
        "id": 1366,
        "signals": [
            {
                "name": "Cfg_PowerModeMaxCurrent_Tx",
                "start_bit": 7,
                "bit_length": 10,
                "bitindexes": [
                    0,
                    8,
                    14,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "Amps",
                "min": "",
                "max": 230,
                "comment": "",
                "row": 9,
                "state": {}
            },
            {
                "name": "Cfg_MotorDirection_Tx",
                "start_bit": 13,
                "bit_length": 1,
                "bitindexes": [
                    12,
                    13,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": "",
                "comment": "",
                "row": 10,
                "state": {}
            },
            {
                "name": "Cfg_Regen_MaxVoltage_Tx",
                "start_bit": 23,
                "bit_length": 8,
                "bitindexes": [
                    16,
                    24,
                    32,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 70,
                "comment": "",
                "row": 11,
                "state": {}
            },
            {
                "name": "Cfg_MinVolt_For_PowerMode_Tx",
                "start_bit": 31,
                "bit_length": 8,
                "bitindexes": [
                    24,
                    32,
                    40,
                    40
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 70,
                "comment": "",
                "row": 12,
                "state": {}
            },
            {
                "name": "Cfg_PowerModeMaxCurr_TL_Tx",
                "start_bit": 39,
                "bit_length": 8,
                "bitindexes": [
                    32,
                    40,
                    48,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "S",
                "min": "",
                "max": 100,
                "comment": "",
                "row": 13,
                "state": {}
            },
            {
                "name": "Cfg_Regen_MinVoltage_Tx",
                "start_bit": 47,
                "bit_length": 8,
                "bitindexes": [
                    40,
                    48,
                    56,
                    56
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "%",
                "min": "",
                "max": 50,
                "comment": "",
                "row": 14,
                "state": {}
            }
        ]
    },
    "1365": {
        "name": "Cfg_Msg2_Tx",
        "id": 1365,
        "signals": [
            {
                "name": "Cfg_Regen_Ena_Dis_Tx",
                "start_bit": 7,
                "bit_length": 1,
                "bitindexes": [
                    6,
                    7,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "Bool",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 15,
                "state": {}
            },
            {
                "name": "Cfg_Regen_Max_Current_Tx",
                "start_bit": 6,
                "bit_length": 10,
                "bitindexes": [
                    0,
                    7,
                    13,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "Amps",
                "min": "",
                "max": 100,
                "comment": "",
                "row": 16,
                "state": {}
            },
            {
                "name": "Cfg_Regen_MinSpeed_Tx",
                "start_bit": 23,
                "bit_length": 14,
                "bitindexes": [
                    16,
                    24,
                    26,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "rpm",
                "min": 500,
                "max": 16383,
                "comment": "",
                "row": 17,
                "state": {}
            },
            {
                "name": "Cfg_Regen_Max_SOC_Tx",
                "start_bit": 39,
                "bit_length": 8,
                "bitindexes": [
                    32,
                    40,
                    48,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "%",
                "min": "",
                "max": 100,
                "comment": "",
                "row": 18,
                "state": {}
            },
            {
                "name": "Cfg_Regen_NegTorque_Tx",
                "start_bit": 47,
                "bit_length": 8,
                "bitindexes": [
                    40,
                    48,
                    56,
                    56
                ],
                "byte_order": "big_endian",
                "scale": -0.5,
                "offset": 0,
                "unit": "Nm",
                "min": -25.6,
                "max": "",
                "comment": "",
                "row": 19,
                "state": {}
            },
            {
                "name": "Cfg_MinBattVoltage_Tx",
                "start_bit": 55,
                "bit_length": 8,
                "bitindexes": [
                    48,
                    56,
                    64,
                    64
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 50,
                "comment": "",
                "row": 20,
                "state": {}
            }
        ]
    },
    "1364": {
        "name": "Cfg_Msg1_Tx",
        "id": 1364,
        "signals": [
            {
                "name": "Cfg_Max_DriveModeSpeed_Tx",
                "start_bit": 7,
                "bit_length": 14,
                "bitindexes": [
                    0,
                    8,
                    10,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "rpm",
                "min": "",
                "max": 16383,
                "comment": "",
                "row": 21,
                "state": {}
            },
            {
                "name": "Cfg_Max_PhaseCurrent_Tx",
                "start_bit": 23,
                "bit_length": 10,
                "bitindexes": [
                    16,
                    24,
                    30,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "Amps",
                "min": "",
                "max": 690,
                "comment": "",
                "row": 22,
                "state": {}
            },
            {
                "name": "Cfg_Max_PowerModeSpeed_Tx",
                "start_bit": 39,
                "bit_length": 14,
                "bitindexes": [
                    32,
                    40,
                    42,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "RPM",
                "min": "",
                "max": 16383,
                "comment": "",
                "row": 23,
                "state": {}
            },
            {
                "name": "Cfg_Max_DCBusCurrent_Tx",
                "start_bit": 55,
                "bit_length": 10,
                "bitindexes": [
                    48,
                    56,
                    62,
                    64
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "Amps",
                "min": "",
                "max": 230,
                "comment": "",
                "row": 24,
                "state": {}
            }
        ]
    },
    "1363": {
        "name": "Cfg_Msg4_Rx",
        "id": 1363,
        "signals": [
            {
                "name": "Cfg_Max_EcoModeSpeed_Rx",
                "start_bit": 7,
                "bit_length": 14,
                "bitindexes": [
                    0,
                    8,
                    10,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "rpm",
                "min": "",
                "max": 16383,
                "comment": "",
                "row": 25,
                "state": {}
            },
            {
                "name": "Cfg_Max_ParkModeSpeed_Rx",
                "start_bit": 23,
                "bit_length": 12,
                "bitindexes": [
                    16,
                    24,
                    28,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "rpm",
                "min": "",
                "max": 4095,
                "comment": "",
                "row": 26,
                "state": {}
            },
            {
                "name": "Cfg_Max_ReverseSpeed_Rx",
                "start_bit": 39,
                "bit_length": 10,
                "bitindexes": [
                    32,
                    40,
                    46,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "Rpm",
                "min": "",
                "max": 1023,
                "comment": "",
                "row": 27,
                "state": {}
            }
        ]
    },
    "1362": {
        "name": "Cfg_Msg3_Rx",
        "id": 1362,
        "signals": [
            {
                "name": "Cfg_MotorDirection_Rx",
                "start_bit": 2,
                "bit_length": 1,
                "bitindexes": [
                    1,
                    2,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 28,
                "state": {}
            },
            {
                "name": "Cfg_PowerModeMaxCurrent_Rx",
                "start_bit": 1,
                "bit_length": 10,
                "bitindexes": [
                    0,
                    2,
                    8,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "Amps",
                "min": "",
                "max": 1023,
                "comment": "",
                "row": 29,
                "state": {}
            },
            {
                "name": "Cfg_Regen_MaxVoltage_Rx",
                "start_bit": 23,
                "bit_length": 8,
                "bitindexes": [
                    16,
                    24,
                    32,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 30,
                "state": {}
            },
            {
                "name": "Cfg_MinVolt_For_PowerMode_Rx",
                "start_bit": 31,
                "bit_length": 8,
                "bitindexes": [
                    24,
                    32,
                    40,
                    40
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 31,
                "state": {}
            },
            {
                "name": "Cfg_PowerModeMaxCurr_TL_Rx",
                "start_bit": 39,
                "bit_length": 8,
                "bitindexes": [
                    32,
                    40,
                    48,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "S",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 32,
                "state": {}
            },
            {
                "name": "Cfg_Regen_MinVoltage_Rx",
                "start_bit": 47,
                "bit_length": 8,
                "bitindexes": [
                    40,
                    48,
                    56,
                    56
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "%",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 33,
                "state": {}
            }
        ]
    },
    "1361": {
        "name": "Cfg_Msg2_Rx",
        "id": 1361,
        "signals": [
            {
                "name": "Cfg_Regen_Ena_Dis_Rx",
                "start_bit": 7,
                "bit_length": 1,
                "bitindexes": [
                    6,
                    7,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "Bool",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 34,
                "state": {}
            },
            {
                "name": "Cfg_Regen_Max_Current_Rx",
                "start_bit": 6,
                "bit_length": 10,
                "bitindexes": [
                    0,
                    7,
                    13,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "Amps",
                "min": "",
                "max": 100,
                "comment": "",
                "row": 35,
                "state": {}
            },
            {
                "name": "Cfg_Regen_Max_SOC_Rx",
                "start_bit": 23,
                "bit_length": 8,
                "bitindexes": [
                    16,
                    24,
                    32,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "%",
                "min": "",
                "max": 100,
                "comment": "",
                "row": 36,
                "state": {}
            },
            {
                "name": "Cfg_Regen_NegTorque_Rx",
                "start_bit": 31,
                "bit_length": 8,
                "bitindexes": [
                    24,
                    32,
                    40,
                    40
                ],
                "byte_order": "big_endian",
                "scale": -0.5,
                "offset": 0,
                "unit": "Nm",
                "min": -25.6,
                "max": "",
                "comment": "",
                "row": 37,
                "state": {}
            },
            {
                "name": "Cfg_Regen_MinSpeed_Rx",
                "start_bit": 39,
                "bit_length": 14,
                "bitindexes": [
                    32,
                    40,
                    42,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "rpm",
                "min": 500,
                "max": 16383,
                "comment": "",
                "row": 38,
                "state": {}
            },
            {
                "name": "Cfg_MinBattVoltage_Rx",
                "start_bit": 55,
                "bit_length": 8,
                "bitindexes": [
                    48,
                    56,
                    64,
                    64
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 50,
                "comment": "",
                "row": 39,
                "state": {}
            }
        ]
    },
    "1360": {
        "name": "Cfg_Msg1_Rx",
        "id": 1360,
        "signals": [
            {
                "name": "Cfg_Max_DriveModeSpeed_Rx",
                "start_bit": 7,
                "bit_length": 14,
                "bitindexes": [
                    0,
                    8,
                    10,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "rpm",
                "min": "",
                "max": 16383,
                "comment": "",
                "row": 40,
                "state": {}
            },
            {
                "name": "Cfg_Max_PhaseCurrent_Rx",
                "start_bit": 23,
                "bit_length": 10,
                "bitindexes": [
                    16,
                    24,
                    30,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "Amps",
                "min": "",
                "max": 690,
                "comment": "",
                "row": 41,
                "state": {}
            },
            {
                "name": "Cfg_Max_PowerModeSpeed_Rx",
                "start_bit": 39,
                "bit_length": 14,
                "bitindexes": [
                    32,
                    40,
                    42,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "RPM",
                "min": "",
                "max": 16383,
                "comment": "",
                "row": 42,
                "state": {}
            },
            {
                "name": "Cfg_Max_DCBusCurrent_Rx",
                "start_bit": 55,
                "bit_length": 10,
                "bitindexes": [
                    48,
                    56,
                    62,
                    64
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "Amps",
                "min": "",
                "max": 1023,
                "comment": "",
                "row": 43,
                "state": {}
            }
        ]
    },
    "1025": {
        "name": "CLS_VEHC_INFO_1",
        "id": 1025,
        "signals": [
            {
                "name": "VEHC_INFO_brake_oil",
                "start_bit": 0,
                "bit_length": 1,
                "bitindexes": [
                    0,
                    1,
                    16,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "Bool",
                "min": "",
                "max": "",
                "comment": "",
                "row": 44,
                "state": {}
            },
            {
                "name": "VEHC_INFO_vehicle_angle",
                "start_bit": 15,
                "bit_length": 16,
                "bitindexes": [
                    8,
                    16,
                    16,
                    24
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "Deg",
                "min": "",
                "max": 359,
                "comment": "",
                "row": 45,
                "state": {}
            }
        ]
    },
    "1028": {
        "name": "MCU_PID_REQUEST_MSG",
        "id": 1028,
        "signals": [
            {
                "name": "MCU_PARKMaxSpeedFrwd",
                "start_bit": 7,
                "bit_length": 13,
                "bitindexes": [
                    0,
                    8,
                    11,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 5000,
                "comment": "",
                "row": 46,
                "state": {}
            },
            {
                "name": "MCU_CANSpeedGainEN",
                "start_bit": 10,
                "bit_length": 1,
                "bitindexes": [
                    9,
                    10,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": "",
                "comment": "",
                "row": 47,
                "state": {}
            },
            {
                "name": "MCU_Reserved_5",
                "start_bit": 9,
                "bit_length": 2,
                "bitindexes": [
                    8,
                    10,
                    24,
                    24
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": "",
                "comment": "",
                "row": 48,
                "state": {}
            },
            {
                "name": "MCU_Spd_Req_Kp",
                "start_bit": 23,
                "bit_length": 16,
                "bitindexes": [
                    16,
                    24,
                    24,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 0.0001,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 2,
                "comment": "",
                "row": 49,
                "state": {}
            },
            {
                "name": "MCU_Spd_Req_Ki",
                "start_bit": 39,
                "bit_length": 16,
                "bitindexes": [
                    32,
                    40,
                    40,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 0.0001,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 2,
                "comment": "",
                "row": 50,
                "state": {}
            },
            {
                "name": "MCU_Spd_Req_Kd",
                "start_bit": 55,
                "bit_length": 16,
                "bitindexes": [
                    48,
                    56,
                    56,
                    64
                ],
                "byte_order": "big_endian",
                "scale": 0.0001,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 2,
                "comment": "",
                "row": 51,
                "state": {}
            }
        ]
    },
    "1303": {
        "name": "MCU_DATA_STATUS5",
        "id": 1303,
        "signals": [
            {
                "name": "MCU_Asw_machineSpeed",
                "start_bit": 7,
                "bit_length": 16,
                "bitindexes": [
                    0,
                    8,
                    8,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "RPM",
                "min": -32768,
                "max": 32767,
                "comment": "",
                "row": 52,
                "state": {}
            },
            {
                "name": "MCU_VehicleSpeed",
                "start_bit": 23,
                "bit_length": 8,
                "bitindexes": [
                    16,
                    24,
                    32,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "kmph",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 53,
                "state": {}
            },
            {
                "name": "MCU_PowerOn_Status",
                "start_bit": 31,
                "bit_length": 4,
                "bitindexes": [
                    27,
                    31,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 54,
                "state": {}
            },
            {
                "name": "Mcu_Flt_BMSVoltageSensor",
                "start_bit": 27,
                "bit_length": 1,
                "bitindexes": [
                    26,
                    27,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 55,
                "state": {
                    "1": "Fault",
                    "0": "No Fault "
                }
            },
            {
                "name": "MCU_ChargerConnectStatus",
                "start_bit": 25,
                "bit_length": 1,
                "bitindexes": [
                    24,
                    25,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 56,
                "state": {}
            },
            {
                "name": "MCU_EcoModeEn",
                "start_bit": 24,
                "bit_length": 1,
                "bitindexes": [
                    24,
                    25,
                    40,
                    40
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 57,
                "state": {}
            },
            {
                "name": "MCU_Ctrl_Mode_sts",
                "start_bit": 39,
                "bit_length": 8,
                "bitindexes": [
                    32,
                    40,
                    48,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 58,
                "state": {}
            },
            {
                "name": "MCU_Flt_LossofClusterMessage",
                "start_bit": 47,
                "bit_length": 1,
                "bitindexes": [
                    46,
                    47,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 59,
                "state": {}
            },
            {
                "name": "MCU_Flt_BatterySensorSTG",
                "start_bit": 45,
                "bit_length": 1,
                "bitindexes": [
                    44,
                    45,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 60,
                "state": {}
            },
            {
                "name": "MCU_Flt_BatterySensorSTB",
                "start_bit": 44,
                "bit_length": 1,
                "bitindexes": [
                    43,
                    44,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 61,
                "state": {}
            },
            {
                "name": "MCU_VehSliderSwitchStatus",
                "start_bit": 42,
                "bit_length": 3,
                "bitindexes": [
                    40,
                    43,
                    56,
                    56
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 7,
                "comment": "",
                "row": 62,
                "state": {
                    "5": "InvalidPosition",
                    "4": "PowerSwitchPosition",
                    "3": "DriveSwitchPosition",
                    "2": "EcoSwitchPosition",
                    "1": "ParkAssistSwitchPosition",
                    "0": "NeutralSwitchPosition"
                }
            },
            {
                "name": "MCU_NeutralModeEn",
                "start_bit": 55,
                "bit_length": 1,
                "bitindexes": [
                    54,
                    55,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 63,
                "state": {}
            },
            {
                "name": "MCU_DriveModeEn",
                "start_bit": 54,
                "bit_length": 1,
                "bitindexes": [
                    53,
                    54,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 64,
                "state": {}
            },
            {
                "name": "MCU_PowerModeEn",
                "start_bit": 53,
                "bit_length": 1,
                "bitindexes": [
                    52,
                    53,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 65,
                "state": {}
            },
            {
                "name": "MCU_Flt_CANDataOutOfRange",
                "start_bit": 52,
                "bit_length": 1,
                "bitindexes": [
                    51,
                    52,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 66,
                "state": {}
            },
            {
                "name": "MCU_Flt_RpmTooHigh",
                "start_bit": 51,
                "bit_length": 1,
                "bitindexes": [
                    50,
                    51,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 67,
                "state": {}
            },
            {
                "name": "MCU_Flt_PositiveCurrentGenMode",
                "start_bit": 50,
                "bit_length": 1,
                "bitindexes": [
                    49,
                    50,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 68,
                "state": {}
            },
            {
                "name": "MCU_Flt_OnAxis_Comm",
                "start_bit": 49,
                "bit_length": 1,
                "bitindexes": [
                    48,
                    49,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 69,
                "state": {}
            },
            {
                "name": "MCU_Flt_NegativeCurrentMotorMode",
                "start_bit": 48,
                "bit_length": 1,
                "bitindexes": [
                    48,
                    49,
                    64,
                    64
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 70,
                "state": {}
            },
            {
                "name": "MCU_PowerDown_en",
                "start_bit": 63,
                "bit_length": 1,
                "bitindexes": [
                    62,
                    63,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 71,
                "state": {}
            },
            {
                "name": "MCU_rtev_BMS_Ready_status",
                "start_bit": 61,
                "bit_length": 1,
                "bitindexes": [
                    60,
                    61,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "Status",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 72,
                "state": {}
            },
            {
                "name": "MCU_dio_phase_ctrl_status",
                "start_bit": 60,
                "bit_length": 1,
                "bitindexes": [
                    59,
                    60,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 73,
                "state": {}
            },
            {
                "name": "MCU_dio_over_curr_status",
                "start_bit": 59,
                "bit_length": 1,
                "bitindexes": [
                    58,
                    59,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 74,
                "state": {}
            },
            {
                "name": "MCU_dio_over_volt_status",
                "start_bit": 58,
                "bit_length": 1,
                "bitindexes": [
                    57,
                    58,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 75,
                "state": {}
            },
            {
                "name": "MCU_ParkAsstStatus",
                "start_bit": 57,
                "bit_length": 1,
                "bitindexes": [
                    56,
                    57,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 76,
                "state": {}
            },
            {
                "name": "MCU_handbrake_status",
                "start_bit": 56,
                "bit_length": 1,
                "bitindexes": [
                    56,
                    57,
                    72,
                    72
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 77,
                "state": {}
            }
        ]
    },
    "1288": {
        "name": "MCU_VERSION_INFO",
        "id": 1288,
        "signals": [
            {
                "name": "MCU_TimeSinceKeyOn",
                "start_bit": 7,
                "bit_length": 16,
                "bitindexes": [
                    0,
                    8,
                    8,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "bit",
                "min": "",
                "max": 65535,
                "comment": "",
                "row": 78,
                "state": {}
            },
            {
                "name": "MCU_Soft_Version_Year",
                "start_bit": 23,
                "bit_length": 6,
                "bitindexes": [
                    17,
                    23,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "bit",
                "min": 19,
                "max": 26,
                "comment": "",
                "row": 79,
                "state": {}
            },
            {
                "name": "MCU_Soft_Version_Minutes",
                "start_bit": 17,
                "bit_length": 6,
                "bitindexes": [
                    16,
                    18,
                    28,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "bit",
                "min": "",
                "max": 60,
                "comment": "",
                "row": 80,
                "state": {}
            },
            {
                "name": "MCU_Sub_Version",
                "start_bit": 27,
                "bit_length": 4,
                "bitindexes": [
                    24,
                    28,
                    40,
                    40
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "bit",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 81,
                "state": {}
            },
            {
                "name": "MCU_OEM_Version",
                "start_bit": 39,
                "bit_length": 3,
                "bitindexes": [
                    36,
                    39,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "bit",
                "min": "",
                "max": 7,
                "comment": "",
                "row": 82,
                "state": {}
            },
            {
                "name": "MCU_Soft_Version_Hour",
                "start_bit": 36,
                "bit_length": 5,
                "bitindexes": [
                    32,
                    37,
                    48,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "bit",
                "min": "",
                "max": 31,
                "comment": "",
                "row": 83,
                "state": {}
            },
            {
                "name": "MCU_Boot_Version_Major",
                "start_bit": 47,
                "bit_length": 4,
                "bitindexes": [
                    43,
                    47,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "bit",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 84,
                "state": {}
            },
            {
                "name": "MCU_Boot_Version_Minor",
                "start_bit": 43,
                "bit_length": 4,
                "bitindexes": [
                    40,
                    44,
                    56,
                    56
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 85,
                "state": {}
            },
            {
                "name": "MCU_Soft_Version_Day",
                "start_bit": 55,
                "bit_length": 5,
                "bitindexes": [
                    50,
                    55,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "bit",
                "min": "",
                "max": 31,
                "comment": "",
                "row": 86,
                "state": {}
            },
            {
                "name": "MCU_Soft_Version_Month",
                "start_bit": 50,
                "bit_length": 5,
                "bitindexes": [
                    48,
                    51,
                    62,
                    64
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "bit",
                "min": "",
                "max": 12,
                "comment": "",
                "row": 87,
                "state": {}
            },
            {
                "name": "MCU_Main_Version",
                "start_bit": 61,
                "bit_length": 5,
                "bitindexes": [
                    56,
                    61,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "bit",
                "min": "",
                "max": 31,
                "comment": "",
                "row": 88,
                "state": {}
            }
        ]
    },
    "1287": {
        "name": "MCU_PHASE_CUR_STATUS_INFO",
        "id": 1287,
        "signals": [
            {
                "name": "MCU_Phasecurrent_R",
                "start_bit": 7,
                "bit_length": 16,
                "bitindexes": [
                    0,
                    8,
                    8,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 0.1,
                "offset": 0,
                "unit": "A",
                "min": -3276.8,
                "max": 3276.7,
                "comment": "E-Machine phase R current",
                "row": 89,
                "state": {}
            },
            {
                "name": "MCU_Phasecurrent_Y",
                "start_bit": 23,
                "bit_length": 16,
                "bitindexes": [
                    16,
                    24,
                    24,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 0.1,
                "offset": 0,
                "unit": "A",
                "min": -3276.8,
                "max": 3276.7,
                "comment": "E-Machine phase Y current",
                "row": 90,
                "state": {}
            },
            {
                "name": "MCU_Phasecurrent_B",
                "start_bit": 39,
                "bit_length": 16,
                "bitindexes": [
                    32,
                    40,
                    40,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 0.1,
                "offset": 0,
                "unit": "A",
                "min": -3276.8,
                "max": 3276.7,
                "comment": "E-Machine phase B current",
                "row": 91,
                "state": {}
            },
            {
                "name": "rtev_abs_max_deltatheta",
                "start_bit": 55,
                "bit_length": 8,
                "bitindexes": [
                    48,
                    56,
                    64,
                    64
                ],
                "byte_order": "big_endian",
                "scale": 0.01,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 2.55,
                "comment": "",
                "row": 92,
                "state": {}
            },
            {
                "name": "rtev_abs_max_delta_phCt_r",
                "start_bit": 63,
                "bit_length": 8,
                "bitindexes": [
                    56,
                    64,
                    72,
                    72
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 93,
                "state": {}
            }
        ]
    },
    "1291": {
        "name": "MCU_DATA_STATUS4",
        "id": 1291,
        "signals": [
            {
                "name": "MCU_Ignition_Inp_Volt_monitor",
                "start_bit": 7,
                "bit_length": 16,
                "bitindexes": [
                    0,
                    8,
                    8,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 0.001373,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 89.979555,
                "comment": "Ignition monitoring voltage",
                "row": 94,
                "state": {}
            },
            {
                "name": "MCU_DcBusVolt_Monitor",
                "start_bit": 23,
                "bit_length": 16,
                "bitindexes": [
                    16,
                    24,
                    24,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 0.001373,
                "offset": 0,
                "unit": "V",
                "min": 12,
                "max": 82,
                "comment": "Motor Controller 72V Supply Monitor",
                "row": 95,
                "state": {}
            },
            {
                "name": "MCU_5v_Monitor",
                "start_bit": 39,
                "bit_length": 8,
                "bitindexes": [
                    32,
                    40,
                    48,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 0.0625,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 15.9375,
                "comment": "Motor Controller  5V Supply Monitor",
                "row": 96,
                "state": {}
            },
            {
                "name": "MCU_12v_battery_monitor",
                "start_bit": 47,
                "bit_length": 8,
                "bitindexes": [
                    40,
                    48,
                    56,
                    56
                ],
                "byte_order": "big_endian",
                "scale": 0.0714,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 18.207,
                "comment": "Motor Controller  12V Supply Monitor",
                "row": 97,
                "state": {}
            },
            {
                "name": "MCU_Machine_Temp",
                "start_bit": 55,
                "bit_length": 8,
                "bitindexes": [
                    48,
                    56,
                    64,
                    64
                ],
                "byte_order": "big_endian",
                "scale": 1.4,
                "offset": -55,
                "unit": "deg",
                "min": -55,
                "max": 302,
                "comment": "Machine temperature",
                "row": 98,
                "state": {}
            },
            {
                "name": "MCU_Board_Temp",
                "start_bit": 63,
                "bit_length": 8,
                "bitindexes": [
                    56,
                    64,
                    72,
                    72
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": -55,
                "unit": "deg",
                "min": -55,
                "max": 200,
                "comment": "Machine temperature",
                "row": 99,
                "state": {}
            }
        ]
    },
    "1285": {
        "name": "MCU_DATA_STATUS3",
        "id": 1285,
        "signals": [
            {
                "name": "MCU_Status_3_Res_001",
                "start_bit": 7,
                "bit_length": 6,
                "bitindexes": [
                    1,
                    7,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": "",
                "comment": "",
                "row": 100,
                "state": {}
            },
            {
                "name": "MCU_RegbreakCurrent",
                "start_bit": 1,
                "bit_length": 10,
                "bitindexes": [
                    0,
                    2,
                    8,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "A",
                "min": "",
                "max": 1023,
                "comment": "",
                "row": 101,
                "state": {}
            },
            {
                "name": "MCU_Status_3_Res_002",
                "start_bit": 23,
                "bit_length": 5,
                "bitindexes": [
                    18,
                    23,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": "",
                "comment": "",
                "row": 102,
                "state": {}
            },
            {
                "name": "MCU_Dc_Bus_Current",
                "start_bit": 18,
                "bit_length": 11,
                "bitindexes": [
                    16,
                    19,
                    24,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "A",
                "min": -1024,
                "max": 1023,
                "comment": "",
                "row": 103,
                "state": {}
            },
            {
                "name": "MCU_Regbreakvolt",
                "start_bit": 39,
                "bit_length": 8,
                "bitindexes": [
                    32,
                    40,
                    48,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 104,
                "state": {}
            },
            {
                "name": "MCU_Applied_PWM_duty_r",
                "start_bit": 47,
                "bit_length": 8,
                "bitindexes": [
                    40,
                    48,
                    56,
                    56
                ],
                "byte_order": "big_endian",
                "scale": 0.01,
                "offset": 0,
                "unit": "%",
                "min": "",
                "max": 100,
                "comment": "",
                "row": 105,
                "state": {}
            },
            {
                "name": "MCU_Applied_PWM_duty_y",
                "start_bit": 55,
                "bit_length": 8,
                "bitindexes": [
                    48,
                    56,
                    64,
                    64
                ],
                "byte_order": "big_endian",
                "scale": 0.01,
                "offset": 0,
                "unit": "%",
                "min": "",
                "max": 100,
                "comment": "",
                "row": 106,
                "state": {}
            },
            {
                "name": "MCU_Applied_PWM_duty_b",
                "start_bit": 63,
                "bit_length": 8,
                "bitindexes": [
                    56,
                    64,
                    72,
                    72
                ],
                "byte_order": "big_endian",
                "scale": 0.01,
                "offset": 0,
                "unit": "%",
                "min": "",
                "max": 100,
                "comment": "",
                "row": 107,
                "state": {}
            }
        ]
    },
    "1283": {
        "name": "MCU_DATA_STATUS1",
        "id": 1283,
        "signals": [
            {
                "name": "MCU_TrqAvailable",
                "start_bit": 7,
                "bit_length": 16,
                "bitindexes": [
                    0,
                    8,
                    8,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "Nm",
                "min": -32768,
                "max": 32767,
                "comment": "Torque Available",
                "row": 108,
                "state": {}
            },
            {
                "name": "MCU_TrqActual",
                "start_bit": 23,
                "bit_length": 16,
                "bitindexes": [
                    16,
                    24,
                    24,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "Nm",
                "min": -32768,
                "max": 32767,
                "comment": "Torque Actual",
                "row": 109,
                "state": {}
            },
            {
                "name": "MCU_AngleOffset",
                "start_bit": 39,
                "bit_length": 16,
                "bitindexes": [
                    32,
                    40,
                    40,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 0.001,
                "offset": -5,
                "unit": "",
                "min": -37.768,
                "max": 27.767,
                "comment": "Machine Offset",
                "row": 110,
                "state": {}
            },
            {
                "name": "MCU_RotorSpeed",
                "start_bit": 55,
                "bit_length": 16,
                "bitindexes": [
                    48,
                    56,
                    56,
                    64
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "RPM",
                "min": "",
                "max": 65535,
                "comment": "Rotor speed",
                "row": 111,
                "state": {}
            }
        ]
    },
    "1284": {
        "name": "MCU_DATA_STATUS2",
        "id": 1284,
        "signals": [
            {
                "name": "MCU_VehSliderSwitchStatus",
                "start_bit": 5,
                "bit_length": 3,
                "bitindexes": [
                    2,
                    5,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 7,
                "comment": "",
                "row": 112,
                "state": {
                    "5": "InvalidPosition",
                    "4": "PowerSwitchPosition",
                    "3": "DriveSwitchPosition",
                    "2": "EcoSwitchPosition",
                    "1": "ParkAssistSwitchPosition",
                    "0": "NeutralSwitchPosition"
                }
            },
            {
                "name": "MCU_PwmDriveEnable",
                "start_bit": 2,
                "bit_length": 1,
                "bitindexes": [
                    1,
                    2,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "bool",
                "min": "",
                "max": 1,
                "comment": "PWM Drive Enable",
                "row": 113,
                "state": {
                    "1": "Enable",
                    "0": "Disable"
                }
            },
            {
                "name": "MCU_BrakeInput",
                "start_bit": 1,
                "bit_length": 1,
                "bitindexes": [
                    0,
                    1,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "bool",
                "min": "",
                "max": 1,
                "comment": "Brake I/P",
                "row": 114,
                "state": {
                    "1": "Break Pressed",
                    "0": "Break Released"
                }
            },
            {
                "name": "MCU_VehicleFwdRevSt",
                "start_bit": 0,
                "bit_length": 1,
                "bitindexes": [
                    0,
                    1,
                    16,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "bool",
                "min": "",
                "max": 1,
                "comment": "Vehicle forward/reverse direction status",
                "row": 115,
                "state": {
                    "1": "Rev",
                    "0": "Fwd"
                }
            },
            {
                "name": "MCU_eep_state",
                "start_bit": 15,
                "bit_length": 4,
                "bitindexes": [
                    11,
                    15,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 116,
                "state": {
                    "12": "EEPROM_USED_BUF_HIGH",
                    "11": "EEPROM_FAIL",
                    "10": "EEPROM_COMPLETE",
                    "9": "EEPROM_VERIFY",
                    "8": "EEPROM_READ",
                    "7": "EEPROM_WRITE",
                    "6": "EEPROM_PREWRITE",
                    "5": "EEPROM_CALC_CHECKSUM",
                    "4": "EEPROM_RD_WR_CHECK",
                    "3": "EEPROM_VERIFY_ONCE",
                    "2": "EEPROM_DATA_DEFAULT",
                    "1": "EEPROM_READ_ONCE",
                    "0": "EEPROM_INIT"
                }
            },
            {
                "name": "MCU_MachineMode_status",
                "start_bit": 11,
                "bit_length": 4,
                "bitindexes": [
                    8,
                    12,
                    24,
                    24
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "bool",
                "min": "",
                "max": 15,
                "comment": "MCU Operating Mode State",
                "row": 117,
                "state": {
                    "15": "Derate",
                    "14": "Invalid",
                    "13": "RegenLevel2",
                    "12": "RegenLevel1",
                    "11": "Fault Mode",
                    "10": "Limp Mode",
                    "9": "ParkAssist Reverse",
                    "8": "ParkAssist Forward",
                    "7": "Reverse Mode",
                    "6": "Power Mode",
                    "5": "Drive Mode",
                    "4": "Eco Mode",
                    "3": "Neutral Mode",
                    "2": "Idle Mode",
                    "1": "Init Mode"
                }
            },
            {
                "name": "MCU_Immobilze_sig",
                "start_bit": 23,
                "bit_length": 10,
                "bitindexes": [
                    16,
                    24,
                    30,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "Hz",
                "min": "",
                "max": 500,
                "comment": "Immobilizer status",
                "row": 118,
                "state": {
                    "1": "ON",
                    "0": "OFF"
                }
            },
            {
                "name": "MCU_Curr_Ctrl_Mode",
                "start_bit": 29,
                "bit_length": 1,
                "bitindexes": [
                    28,
                    29,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "bool",
                "min": "",
                "max": "",
                "comment": "Vehicle forward/reverse direction status",
                "row": 119,
                "state": {
                    "1": "Enable",
                    "0": "Disable"
                }
            },
            {
                "name": "MCU_Ctrl_Mode_sts",
                "start_bit": 28,
                "bit_length": 4,
                "bitindexes": [
                    24,
                    28,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "bool",
                "min": "",
                "max": 15,
                "comment": "Vehicle Mode status (eco/sport/etc)",
                "row": 120,
                "state": {
                    "5": "DERATE_MODE",
                    "4": "REGEN_CTRL_L2",
                    "3": "REGEN_CTRL_L1",
                    "2": "SPEED_CTRL_FWD",
                    "1": "SPEED_CTRL_REV",
                    "0": "IDLE"
                }
            },
            {
                "name": "MCU_DerateActive",
                "start_bit": 24,
                "bit_length": 1,
                "bitindexes": [
                    24,
                    25,
                    40,
                    40
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "bool",
                "min": "",
                "max": 1,
                "comment": "derate active status",
                "row": 121,
                "state": {
                    "1": "Deactive",
                    "0": "Active"
                }
            },
            {
                "name": "MCU_Rotor_theta",
                "start_bit": 39,
                "bit_length": 16,
                "bitindexes": [
                    32,
                    40,
                    40,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 0.001,
                "offset": 0,
                "unit": "deg",
                "min": "",
                "max": 10.475,
                "comment": "Rotor Raw Theta",
                "row": 122,
                "state": {}
            },
            {
                "name": "MCU_Acceleration_Volt_St",
                "start_bit": 55,
                "bit_length": 16,
                "bitindexes": [
                    48,
                    56,
                    56,
                    64
                ],
                "byte_order": "big_endian",
                "scale": 0.001,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 65.535,
                "comment": "Accelerator throttle I/P",
                "row": 123,
                "state": {}
            }
        ]
    },
    "1286": {
        "name": "MCU_FAULT_STATUS_INFO",
        "id": 1286,
        "signals": [
            {
                "name": "Mcu_Flt_MOSFET_STB",
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
                "comment": "",
                "row": 124,
                "state": {
                    "1": "Fault",
                    "0": "No Fault "
                }
            },
            {
                "name": "Mcu_Flt_BatterySensorSTB",
                "start_bit": 7,
                "bit_length": 1,
                "bitindexes": [
                    6,
                    7,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 125,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_BatterySensorSTG",
                "start_bit": 6,
                "bit_length": 1,
                "bitindexes": [
                    5,
                    6,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 126,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_DcBusOverVoltage",
                "start_bit": 5,
                "bit_length": 1,
                "bitindexes": [
                    4,
                    5,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "48V Over voltage Fault",
                "row": 127,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_DcBusUnderVoltage",
                "start_bit": 4,
                "bit_length": 1,
                "bitindexes": [
                    3,
                    4,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "48V Under voltage Fault",
                "row": 128,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_WrongDirection",
                "start_bit": 3,
                "bit_length": 1,
                "bitindexes": [
                    2,
                    3,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 129,
                "state": {
                    "1": "Fault",
                    "0": "No Fault "
                }
            },
            {
                "name": "MCU_Flt_Iq_error",
                "start_bit": 2,
                "bit_length": 1,
                "bitindexes": [
                    1,
                    2,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 130,
                "state": {
                    "1": "Fault",
                    "0": "No Fault "
                }
            },
            {
                "name": "Mcu_Flt_BoardTempSensorSTB",
                "start_bit": 15,
                "bit_length": 1,
                "bitindexes": [
                    14,
                    15,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 131,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_Dc_Current_High",
                "start_bit": 14,
                "bit_length": 1,
                "bitindexes": [
                    13,
                    14,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "DC bus over current fault",
                "row": 132,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_MachineTemp_High",
                "start_bit": 13,
                "bit_length": 1,
                "bitindexes": [
                    12,
                    13,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "Machine temperature High fault",
                "row": 133,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_MachineTemp_Low",
                "start_bit": 12,
                "bit_length": 1,
                "bitindexes": [
                    11,
                    12,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "Machine temperature OC fault",
                "row": 134,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_BoardTempSensorSTG",
                "start_bit": 11,
                "bit_length": 1,
                "bitindexes": [
                    10,
                    11,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 135,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_BPhase_Current_High",
                "start_bit": 10,
                "bit_length": 1,
                "bitindexes": [
                    9,
                    10,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "Any phase over current sensor fault",
                "row": 136,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_BphaseSTB",
                "start_bit": 9,
                "bit_length": 1,
                "bitindexes": [
                    8,
                    9,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 137,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_BphaseSTG",
                "start_bit": 8,
                "bit_length": 1,
                "bitindexes": [
                    8,
                    9,
                    24,
                    24
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 138,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_CANDataOutOfRange",
                "start_bit": 23,
                "bit_length": 1,
                "bitindexes": [
                    22,
                    23,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 139,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_DCCurrentSensorSTB",
                "start_bit": 22,
                "bit_length": 1,
                "bitindexes": [
                    21,
                    22,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 140,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_DCCurrentSensorSTG",
                "start_bit": 21,
                "bit_length": 1,
                "bitindexes": [
                    20,
                    21,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 141,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_Rotor_Stall",
                "start_bit": 20,
                "bit_length": 1,
                "bitindexes": [
                    19,
                    20,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "Rotor stall protection",
                "row": 142,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_BoardTemp_High",
                "start_bit": 19,
                "bit_length": 1,
                "bitindexes": [
                    18,
                    19,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "Board Over Temperature  Fault",
                "row": 143,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_BoardTemp_Low",
                "start_bit": 18,
                "bit_length": 1,
                "bitindexes": [
                    17,
                    18,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "Board Over Temperature  Fault",
                "row": 144,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_BrakeLowOilFault",
                "start_bit": 17,
                "bit_length": 1,
                "bitindexes": [
                    16,
                    17,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 145,
                "state": {}
            },
            {
                "name": "Mcu_Flt_BuckConverte_12V_STB",
                "start_bit": 16,
                "bit_length": 1,
                "bitindexes": [
                    16,
                    17,
                    32,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 146,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_BuckConverte_12V_STG",
                "start_bit": 31,
                "bit_length": 1,
                "bitindexes": [
                    30,
                    31,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 147,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_LossofBMSMessage",
                "start_bit": 30,
                "bit_length": 1,
                "bitindexes": [
                    29,
                    30,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 148,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "MCU_Flt_RPhase_Current_High",
                "start_bit": 29,
                "bit_length": 1,
                "bitindexes": [
                    28,
                    29,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "Any phase over current sensor fault",
                "row": 149,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_MachineTempSTB",
                "start_bit": 28,
                "bit_length": 1,
                "bitindexes": [
                    27,
                    28,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 150,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_MachineTempSTG",
                "start_bit": 27,
                "bit_length": 1,
                "bitindexes": [
                    26,
                    27,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 151,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_OnAxisParity",
                "start_bit": 25,
                "bit_length": 1,
                "bitindexes": [
                    24,
                    25,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 152,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_OnAxisDataOutofRange",
                "start_bit": 24,
                "bit_length": 1,
                "bitindexes": [
                    24,
                    25,
                    40,
                    40
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 153,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_RphaseSTB",
                "start_bit": 38,
                "bit_length": 1,
                "bitindexes": [
                    37,
                    38,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 154,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_RphaseSTG",
                "start_bit": 37,
                "bit_length": 1,
                "bitindexes": [
                    36,
                    37,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 155,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_RpmTooHigh",
                "start_bit": 36,
                "bit_length": 1,
                "bitindexes": [
                    35,
                    36,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 156,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_ThrottleInvalidRange",
                "start_bit": 35,
                "bit_length": 1,
                "bitindexes": [
                    34,
                    35,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 157,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_ThrottleSTB",
                "start_bit": 34,
                "bit_length": 1,
                "bitindexes": [
                    33,
                    34,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 158,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_ThrottleSTG",
                "start_bit": 33,
                "bit_length": 1,
                "bitindexes": [
                    32,
                    33,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 159,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_OnAxisCommunication",
                "start_bit": 47,
                "bit_length": 1,
                "bitindexes": [
                    46,
                    47,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 160,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_YPhase_Current_High",
                "start_bit": 46,
                "bit_length": 1,
                "bitindexes": [
                    45,
                    46,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "Any phase over current sensor fault",
                "row": 161,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_YphaseSTB",
                "start_bit": 45,
                "bit_length": 1,
                "bitindexes": [
                    44,
                    45,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 162,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_YphaseSTG",
                "start_bit": 44,
                "bit_length": 1,
                "bitindexes": [
                    43,
                    44,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 163,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_LossofClusterMessage",
                "start_bit": 43,
                "bit_length": 1,
                "bitindexes": [
                    42,
                    43,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 164,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_App_Checksum",
                "start_bit": 42,
                "bit_length": 1,
                "bitindexes": [
                    41,
                    42,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "Application Checksum failure",
                "row": 165,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_CAN_Comm",
                "start_bit": 41,
                "bit_length": 1,
                "bitindexes": [
                    40,
                    41,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "CAN communication timeout fault",
                "row": 166,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_BatteryHighTempFault",
                "start_bit": 40,
                "bit_length": 1,
                "bitindexes": [
                    40,
                    41,
                    56,
                    56
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 167,
                "state": {
                    "1": "Fault",
                    "0": "No Fault"
                }
            },
            {
                "name": "Mcu_Flt_MOSFET_HighTemp",
                "start_bit": 55,
                "bit_length": 1,
                "bitindexes": [
                    54,
                    55,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 168,
                "state": {
                    "1": "Fault",
                    "0": "No Fault "
                }
            },
            {
                "name": "Mcu_Flt_Ideal_Voltage_error",
                "start_bit": 54,
                "bit_length": 1,
                "bitindexes": [
                    53,
                    54,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 169,
                "state": {
                    "1": "Fault",
                    "0": "No Fault "
                }
            },
            {
                "name": "Mcu_Flt_Phase_Current_Sensor",
                "start_bit": 53,
                "bit_length": 1,
                "bitindexes": [
                    52,
                    53,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 170,
                "state": {
                    "1": "Fault",
                    "0": "No Fault "
                }
            },
            {
                "name": "Mcu_Flt_Wrong_Offset_Angle",
                "start_bit": 52,
                "bit_length": 1,
                "bitindexes": [
                    51,
                    52,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 171,
                "state": {
                    "1": "Fault",
                    "0": "No Fault "
                }
            },
            {
                "name": "Mcu_Flt_KL30Low",
                "start_bit": 51,
                "bit_length": 1,
                "bitindexes": [
                    50,
                    51,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 172,
                "state": {
                    "1": "Fault",
                    "0": "No Fault "
                }
            },
            {
                "name": "Mcu_Flt_KL30High",
                "start_bit": 50,
                "bit_length": 1,
                "bitindexes": [
                    49,
                    50,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 173,
                "state": {
                    "1": "Fault",
                    "0": "No Fault "
                }
            },
            {
                "name": "Mcu_Flt_KL30_Sensor_STG",
                "start_bit": 49,
                "bit_length": 1,
                "bitindexes": [
                    48,
                    49,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 174,
                "state": {
                    "1": "Fault",
                    "0": "No Fault "
                }
            },
            {
                "name": "Mcu_Flt_KL30_Sensor_STB",
                "start_bit": 48,
                "bit_length": 1,
                "bitindexes": [
                    48,
                    49,
                    64,
                    64
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 175,
                "state": {
                    "1": "Fault",
                    "0": "No Fault "
                }
            },
            {
                "name": "Mcu_Flt_MOSFET_STG",
                "start_bit": 57,
                "bit_length": 1,
                "bitindexes": [
                    56,
                    57,
                    999,
                    999
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 176,
                "state": {
                    "1": "Fault",
                    "0": "No Fault "
                }
            },
            {
                "name": "Mcu_Flt_mtrDirflt_sts",
                "start_bit": 56,
                "bit_length": 1,
                "bitindexes": [
                    56,
                    57,
                    72,
                    72
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 177,
                "state": {
                    "1": "Fault",
                    "0": "No Fault "
                }
            }
        ]
    }
}