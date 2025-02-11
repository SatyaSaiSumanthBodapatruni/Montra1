canids_3W = [259, 1544, 772, 1367, 1366, 1365, 1364, 1363, 1362, 1361, 1360, 1313, 1025, 1312, 1028, 1303, 1288, 1287, 1291, 1285, 1283, 1284, 1286, 774, 513, 514, 515, 516, 517, 518, 528, 529, 530, 531, 778, 776, 512, 523, 665, 526, 544, 545, 546, 547, 770, 548, 524, 522, 258, 257, 341, 777]

json_3W = {
    "259": {
        "name": "ODO_TX_Fare_Meter",
        "id": 259,
        "signals": [
            {
                "name": "ODO_TX",
                "start_bit": 7,
                "bit_length": 32,
                "bitindexes": [
                    0,
                    8,
                    -8,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 10000000.0,
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
                "scale": 2,
                "offset": -55,
                "unit": "",
                "min": -311,
                "max": 199,
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
                "scale": 2,
                "offset": -55,
                "unit": "",
                "min": -311,
                "max": 199,
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
                "scale": 2,
                "offset": -55,
                "unit": "",
                "min": -311,
                "max": 199,
                "comment": "",
                "row": 3,
                "state": {}
            }
        ]
    },
    "772": {
        "name": "BMSReady",
        "id": 772,
        "signals": [
            {
                "name": "BMSReady",
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
                "comment": "0x00 --> BMS Not ready0xAA --> BMS Ready0xFF --> Invalid",
                "row": 4,
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
                "row": 5,
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
                "row": 6,
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
                "row": 7,
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
                "row": 8,
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
                "max": 1,
                "comment": "",
                "row": 9,
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
                "row": 10,
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
                "row": 11,
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
                "row": 12,
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
                "row": 13,
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
                "row": 14,
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
                "row": 15,
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
                "row": 16,
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
                "row": 17,
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
                "min": -25.5,
                "max": "",
                "comment": "",
                "row": 18,
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
                "row": 19,
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
                "row": 20,
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
                "row": 21,
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
                "row": 22,
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
                "row": 23,
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
                "row": 24,
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
                "row": 25,
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
                "row": 26,
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
                "row": 27,
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
                "row": 28,
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
                "row": 29,
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
                "row": 30,
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
                "row": 31,
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
                "row": 32,
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
                "row": 33,
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
                "row": 34,
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
                "row": 35,
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
                "min": -25.5,
                "max": "",
                "comment": "",
                "row": 36,
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
                "row": 37,
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
                "row": 38,
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
                "row": 39,
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
                "row": 40,
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
                "row": 41,
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
                "row": 42,
                "state": {}
            }
        ]
    },
    "1313": {
        "name": "MCU_FAULT_COUNT_STATUS2",
        "id": 1313,
        "signals": [
            {
                "name": "MCU_Flt_RphaseSTG_Cnt",
                "start_bit": 7,
                "bit_length": 4,
                "bitindexes": [
                    3,
                    7,
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
                "row": 43,
                "state": {}
            },
            {
                "name": "MCU_Flt_RphaseSTB_Cnt",
                "start_bit": 3,
                "bit_length": 4,
                "bitindexes": [
                    0,
                    4,
                    16,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 44,
                "state": {}
            },
            {
                "name": "MCU_Flt_YphaseSTG_Cnt",
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
                "row": 45,
                "state": {}
            },
            {
                "name": "MCU_Flt_YphaseSTB_Cnt",
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
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 46,
                "state": {}
            },
            {
                "name": "MCU_Flt_BphaseSTG_Cnt",
                "start_bit": 23,
                "bit_length": 4,
                "bitindexes": [
                    19,
                    23,
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
                "row": 47,
                "state": {}
            },
            {
                "name": "MCU_Flt_BphaseSTB_Cnt",
                "start_bit": 19,
                "bit_length": 4,
                "bitindexes": [
                    16,
                    20,
                    32,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 48,
                "state": {}
            },
            {
                "name": "MCU_Flt_DCCrntSensorSTG_Cnt",
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
                "row": 49,
                "state": {}
            },
            {
                "name": "MCU_Flt_DCCrntSensorSTB_Cnt",
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
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 50,
                "state": {}
            },
            {
                "name": "MCU_Flt_MachineTempSTG_Cnt",
                "start_bit": 39,
                "bit_length": 4,
                "bitindexes": [
                    35,
                    39,
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
                "row": 51,
                "state": {}
            },
            {
                "name": "MCU_Flt_MachineTempSTB_Cnt",
                "start_bit": 35,
                "bit_length": 4,
                "bitindexes": [
                    32,
                    36,
                    48,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 52,
                "state": {}
            },
            {
                "name": "rtev_OnAxis_Total_SampleCnt",
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
                "unit": "",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 53,
                "state": {}
            },
            {
                "name": "rtev_OnAxis_Pass__SampleCnt",
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
                "unit": "",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 54,
                "state": {}
            },
            {
                "name": "rtev_OnAxis_Fail__SampleCnt",
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
                "row": 55,
                "state": {}
            }
        ]
    },
    "1025": {
        "name": "Break_oil_TX",
        "id": 1025,
        "signals": [
            {
                "name": "Break_Oil_INTX",
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
                "max": 1,
                "comment": "",
                "row": 56,
                "state": {}
            }
        ]
    },
    "1312": {
        "name": "MCU_FAULT_COUNT_STATUS1",
        "id": 1312,
        "signals": [
            {
                "name": "Mcu_Flt_OnAxis_Cnt",
                "start_bit": 7,
                "bit_length": 4,
                "bitindexes": [
                    3,
                    7,
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
                "row": 57,
                "state": {}
            },
            {
                "name": "Mcu_Flt_CAN_Cnt",
                "start_bit": 3,
                "bit_length": 4,
                "bitindexes": [
                    0,
                    4,
                    16,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 58,
                "state": {}
            },
            {
                "name": "Mcu_Flt_BMS_MsgLoss_Cnt",
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
                "row": 59,
                "state": {}
            },
            {
                "name": "Mcu_Flt_Cluster_MsgLoss_Cnt",
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
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 60,
                "state": {}
            },
            {
                "name": "MCU_Flt_BatSensorSTB_Cnt",
                "start_bit": 23,
                "bit_length": 4,
                "bitindexes": [
                    19,
                    23,
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
                "row": 61,
                "state": {}
            },
            {
                "name": "MCU_Flt_MicroUnderVolt_Cnt",
                "start_bit": 19,
                "bit_length": 4,
                "bitindexes": [
                    16,
                    20,
                    32,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 62,
                "state": {}
            },
            {
                "name": "MCU_Flt_KL30SensorSTB_Cnt",
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
                "row": 63,
                "state": {}
            },
            {
                "name": "MCU_Flt_KL30SensorSTG_Cnt",
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
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 64,
                "state": {}
            },
            {
                "name": "MCU_Flt_ThrottleSTB_Cnt",
                "start_bit": 39,
                "bit_length": 4,
                "bitindexes": [
                    35,
                    39,
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
                "row": 65,
                "state": {}
            },
            {
                "name": "MCU_Flt_ThrottleSTG_Cnt",
                "start_bit": 35,
                "bit_length": 4,
                "bitindexes": [
                    32,
                    36,
                    48,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 66,
                "state": {}
            },
            {
                "name": "MCU_Flt_MachineTempSTB_Cnt",
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
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 67,
                "state": {}
            },
            {
                "name": "MCU_Flt_MachineTempSTG_Cnt",
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
                "row": 68,
                "state": {}
            },
            {
                "name": "MCU_Flt_BoardTempSensorSTB_Cnt",
                "start_bit": 55,
                "bit_length": 4,
                "bitindexes": [
                    51,
                    55,
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
                "row": 69,
                "state": {}
            },
            {
                "name": "MCU_Flt_BoardTmpSensorSTG_Cnt",
                "start_bit": 51,
                "bit_length": 4,
                "bitindexes": [
                    48,
                    52,
                    64,
                    64
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 70,
                "state": {}
            },
            {
                "name": "MCU_Flt_RphaseSTG_Cnt",
                "start_bit": 63,
                "bit_length": 4,
                "bitindexes": [
                    59,
                    63,
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
                "row": 71,
                "state": {}
            },
            {
                "name": "MCU_Flt_MicroSensorSTB_Cnt",
                "start_bit": 59,
                "bit_length": 4,
                "bitindexes": [
                    56,
                    60,
                    72,
                    72
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 15,
                "comment": "",
                "row": 72,
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
                "row": 73,
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
                "max": 1,
                "comment": "",
                "row": 74,
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
                "max": 3,
                "comment": "",
                "row": 75,
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
                "row": 76,
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
                "row": 77,
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
                "row": 78,
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
                "row": 79,
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
                "row": 80,
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
                "row": 81,
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
                "row": 82,
                "state": {
                    "0": "No Fault ",
                    "1": "Fault"
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
                "row": 83,
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
                "row": 84,
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
                "row": 85,
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
                "row": 86,
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
                "row": 87,
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
                "row": 88,
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
                "row": 89,
                "state": {
                    "0": "NeutralSwitchPosition",
                    "1": "ParkAssistSwitchPosition",
                    "2": "EcoSwitchPosition",
                    "3": "DriveSwitchPosition",
                    "4": "PowerSwitchPosition",
                    "5": "InvalidPosition"
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
                "row": 90,
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
                "row": 91,
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
                "row": 92,
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
                "row": 93,
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
                "row": 94,
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
                "row": 95,
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
                "row": 96,
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
                "row": 97,
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
                "row": 98,
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
                "row": 99,
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
                "row": 100,
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
                "row": 101,
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
                "row": 102,
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
                "row": 103,
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
                "row": 104,
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
                "row": 105,
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
                "row": 106,
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
                "row": 107,
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
                "row": 108,
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
                "row": 109,
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
                "row": 110,
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
                "row": 111,
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
                "row": 112,
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
                "row": 113,
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
                "row": 114,
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
                "row": 115,
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
                "row": 116,
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
                "row": 117,
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
                "max": 89.9796,
                "comment": "Ignition monitoring voltage",
                "row": 118,
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
                "max": 81.9997,
                "comment": "Motor Controller 72V Supply Monitor",
                "row": 119,
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
                "row": 120,
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
                "row": 121,
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
                "row": 122,
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
                "row": 123,
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
                "max": 63,
                "comment": "",
                "row": 124,
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
                "row": 125,
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
                "max": 31,
                "comment": "",
                "row": 126,
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
                "row": 127,
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
                "row": 128,
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
                "max": 2.55,
                "comment": "",
                "row": 129,
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
                "max": 2.55,
                "comment": "",
                "row": 130,
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
                "max": 2.55,
                "comment": "",
                "row": 131,
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
                "row": 132,
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
                "row": 133,
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
                "row": 134,
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
                "max": 32767,
                "comment": "Rotor speed",
                "row": 135,
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
                "row": 136,
                "state": {
                    "0": "NeutralSwitchPosition",
                    "1": "ParkAssistSwitchPosition",
                    "2": "EcoSwitchPosition",
                    "3": "DriveSwitchPosition",
                    "4": "PowerSwitchPosition",
                    "5": "InvalidPosition"
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
                "row": 137,
                "state": {
                    "0": "Disable",
                    "1": "Enable"
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
                "row": 138,
                "state": {
                    "0": "Break Released",
                    "1": "Break Pressed"
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
                "row": 139,
                "state": {
                    "0": "Fwd",
                    "1": "Rev"
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
                "row": 140,
                "state": {
                    "0": "EEPROM_INIT",
                    "1": "EEPROM_READ_ONCE",
                    "2": "EEPROM_DATA_DEFAULT",
                    "3": "EEPROM_VERIFY_ONCE",
                    "4": "EEPROM_RD_WR_CHECK",
                    "5": "EEPROM_CALC_CHECKSUM",
                    "6": "EEPROM_PREWRITE",
                    "7": "EEPROM_WRITE",
                    "8": "EEPROM_READ",
                    "9": "EEPROM_VERIFY",
                    "10": "EEPROM_COMPLETE",
                    "11": "EEPROM_FAIL",
                    "12": "EEPROM_USED_BUF_HIGH"
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
                "row": 141,
                "state": {
                    "1": "Init Mode",
                    "2": "Idle Mode",
                    "3": "Neutral Mode",
                    "4": "Eco Mode",
                    "5": "Drive Mode",
                    "6": "Power Mode",
                    "7": "Reverse Mode",
                    "8": "ParkAssist Forward",
                    "9": "ParkAssist Reverse",
                    "10": "Limp Mode",
                    "11": "Fault Mode",
                    "12": "RegenLevel1",
                    "13": "RegenLevel2",
                    "14": "Invalid",
                    "15": "Derate"
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
                "row": 142,
                "state": {
                    "0": "OFF",
                    "1": "ON"
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
                "max": 1,
                "comment": "Vehicle forward/reverse direction status",
                "row": 143,
                "state": {
                    "0": "Disable",
                    "1": "Enable"
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
                "row": 144,
                "state": {
                    "0": "IDLE",
                    "1": "SPEED_CTRL_REV",
                    "2": "SPEED_CTRL_FWD",
                    "3": "REGEN_CTRL_L1",
                    "4": "REGEN_CTRL_L2",
                    "5": "DERATE_MODE"
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
                "row": 145,
                "state": {
                    "0": "Active",
                    "1": "Deactive"
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
                "row": 146,
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
                "row": 147,
                "state": {}
            }
        ]
    },
    "1286": {
        "name": "MCU_FAULT_STATUS_INFO",
        "id": 1286,
        "signals": [
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
                "row": 148,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
                }
            },
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
                "row": 149,
                "state": {
                    "0": "No Fault ",
                    "1": "Fault"
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
                "row": 150,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 151,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 152,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 153,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 154,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 155,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 156,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 157,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 158,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 159,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 160,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 161,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 162,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 163,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 164,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 165,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 166,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 167,
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
                "row": 168,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 169,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 170,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 171,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 172,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 173,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 174,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 175,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 176,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 177,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 178,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 179,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 180,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 181,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 182,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 183,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 184,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 185,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 186,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 187,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 188,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 189,
                "state": {
                    "0": "No Fault",
                    "1": "Fault"
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
                "row": 190,
                "state": {
                    "0": "No Fault ",
                    "1": "Fault"
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
                "row": 191,
                "state": {
                    "0": "No Fault ",
                    "1": "Fault"
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
                "row": 192,
                "state": {
                    "0": "No Fault ",
                    "1": "Fault"
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
                "row": 193,
                "state": {
                    "0": "No Fault ",
                    "1": "Fault"
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
                "row": 194,
                "state": {
                    "0": "No Fault ",
                    "1": "Fault"
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
                "row": 195,
                "state": {
                    "0": "No Fault ",
                    "1": "Fault"
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
                "row": 196,
                "state": {
                    "0": "No Fault ",
                    "1": "Fault"
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
                "row": 197,
                "state": {
                    "0": "No Fault ",
                    "1": "Fault"
                }
            }
        ]
    },
    "774": {
        "name": "BMS_V_A_Demand",
        "id": 774,
        "signals": [
            {
                "name": "Voltage",
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
                "unit": "V",
                "min": "",
                "max": 6553.5,
                "comment": "",
                "row": 198,
                "state": {}
            },
            {
                "name": "Current",
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
                "offset": -400,
                "unit": "A",
                "min": 5.96046e-06,
                "max": 6153.5,
                "comment": "",
                "row": 199,
                "state": {}
            },
            {
                "name": "ConstanVoltage",
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
                "comment": "01-Constant Voltage03-Constant Current",
                "row": 200,
                "state": {}
            },
            {
                "name": "Constan_SOC_Percent",
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
                "unit": "",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 201,
                "state": {}
            },
            {
                "name": "Estimtd_Remain_Chrg_Time",
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
                "unit": "",
                "min": "",
                "max": 1000,
                "comment": "Estimated Remaining Charge time",
                "row": 202,
                "state": {}
            }
        ]
    },
    "513": {
        "name": "BMS_Batt_Info_x201",
        "id": 513,
        "signals": [
            {
                "name": "Total_Volt",
                "start_bit": 7,
                "bit_length": 16,
                "bitindexes": [
                    0,
                    8,
                    8,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 0.001,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 65.535,
                "comment": "Total stack voltage from battery",
                "row": 203,
                "state": {}
            },
            {
                "name": "Current",
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
                "unit": "A",
                "min": "",
                "max": 1000,
                "comment": "Total discharge current",
                "row": 204,
                "state": {}
            },
            {
                "name": "SOC",
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
                "unit": "%",
                "min": "",
                "max": 100,
                "comment": "Available capacity of battery",
                "row": 205,
                "state": {}
            },
            {
                "name": "Full_Capacity",
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
                "unit": "AH",
                "min": "",
                "max": 1000,
                "comment": "Total capacity of battery",
                "row": 206,
                "state": {}
            }
        ]
    },
    "514": {
        "name": "BMS_Batt_Info_x202",
        "id": 514,
        "signals": [
            {
                "name": "SOH",
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
                "unit": "%",
                "min": "",
                "max": 100,
                "comment": "health of Battery",
                "row": 207,
                "state": {}
            },
            {
                "name": "Running_Times",
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
                "unit": "hr",
                "min": "",
                "max": 65535,
                "comment": "Total battery pack running times",
                "row": 208,
                "state": {}
            },
            {
                "name": "Cycles_Times",
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
                "unit": "Count",
                "min": "",
                "max": 1000,
                "comment": "Total cycle count of charge & discharge",
                "row": 209,
                "state": {}
            },
            {
                "name": "PCB_Temp",
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
                "unit": "*C",
                "min": "",
                "max": 255,
                "comment": "PCB Temperature",
                "row": 210,
                "state": {}
            },
            {
                "name": "IC_Temp",
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
                "unit": "*C",
                "min": "",
                "max": 255,
                "comment": "IC Temperature",
                "row": 211,
                "state": {}
            }
        ]
    },
    "515": {
        "name": "BMS_Batt_Info_x203",
        "id": 515,
        "signals": [
            {
                "name": "PackStatus",
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
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 4,
                "comment": "Present battery pack status1 - Charging2 - Discharging3 - Standby4 - Regen",
                "row": 212,
                "state": {}
            },
            {
                "name": "PWR_ON_Status",
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
                "max": 255,
                "comment": "Power ON Status",
                "row": 213,
                "state": {}
            }
        ]
    },
    "516": {
        "name": "BMS_Batt_Info_x204",
        "id": 516,
        "signals": [
            {
                "name": "Vmax",
                "start_bit": 7,
                "bit_length": 16,
                "bitindexes": [
                    0,
                    8,
                    8,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 0.001,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 65.535,
                "comment": "Maximum Voltage of cells connected",
                "row": 214,
                "state": {}
            },
            {
                "name": "Vmin",
                "start_bit": 23,
                "bit_length": 16,
                "bitindexes": [
                    16,
                    24,
                    24,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 0.001,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 65.535,
                "comment": "Minimum Voltage of cells connected",
                "row": 215,
                "state": {}
            },
            {
                "name": "Vmax_Number",
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
                "max": 13,
                "comment": "Maximum number of cells connected",
                "row": 216,
                "state": {}
            },
            {
                "name": "Vmin_Number",
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
                "unit": "",
                "min": "",
                "max": 13,
                "comment": "Minimum number of cells connected",
                "row": 217,
                "state": {}
            }
        ]
    },
    "517": {
        "name": "BMS_Batt_Info_x205",
        "id": 517,
        "signals": [
            {
                "name": "Max_Temp",
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
                "unit": "*C",
                "min": "",
                "max": 100,
                "comment": "Maximum temperature of sensors connected",
                "row": 218,
                "state": {}
            },
            {
                "name": "Min_Temp",
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
                "unit": "*C",
                "min": "",
                "max": 100,
                "comment": "Minimum temperature of sensors connected",
                "row": 219,
                "state": {}
            },
            {
                "name": "Avg_Temp",
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
                "unit": "*C",
                "min": "",
                "max": 100,
                "comment": "Average Temperature",
                "row": 220,
                "state": {}
            }
        ]
    },
    "518": {
        "name": "BMS_Batt_Temp_Sts",
        "id": 518,
        "signals": [
            {
                "name": "T1",
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
                "unit": "*C",
                "min": "",
                "max": 100,
                "comment": "NTC1 temperature",
                "row": 221,
                "state": {}
            },
            {
                "name": "T2",
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
                "offset": 0,
                "unit": "*C",
                "min": "",
                "max": 100,
                "comment": "NTC2 temperature",
                "row": 222,
                "state": {}
            },
            {
                "name": "T3",
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
                "unit": "*C",
                "min": "",
                "max": 100,
                "comment": "NTC3 temperature",
                "row": 223,
                "state": {}
            },
            {
                "name": "T4",
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
                "unit": "*C",
                "min": "",
                "max": 100,
                "comment": "NTC4 temperature",
                "row": 224,
                "state": {}
            },
            {
                "name": "T5",
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
                "unit": "*C",
                "min": "",
                "max": 100,
                "comment": "NTC5 temperature",
                "row": 225,
                "state": {}
            },
            {
                "name": "T6",
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
                "unit": "*C",
                "min": "",
                "max": 100,
                "comment": "NTC6 temperature",
                "row": 226,
                "state": {}
            }
        ]
    },
    "528": {
        "name": "BMS_Batt_Volt_Sts_x210",
        "id": 528,
        "signals": [
            {
                "name": "Vcell1_Volt",
                "start_bit": 7,
                "bit_length": 16,
                "bitindexes": [
                    0,
                    8,
                    8,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 0.001,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 65.535,
                "comment": "Voltage of Cell1",
                "row": 227,
                "state": {}
            },
            {
                "name": "Vcell2_Volt",
                "start_bit": 23,
                "bit_length": 16,
                "bitindexes": [
                    16,
                    24,
                    24,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 0.001,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 65.535,
                "comment": "Voltage of Cell2",
                "row": 228,
                "state": {}
            },
            {
                "name": "Vcell3_Volt",
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
                "unit": "V",
                "min": "",
                "max": 65.535,
                "comment": "Voltage of Cell3",
                "row": 229,
                "state": {}
            },
            {
                "name": "Vcell4_Volt",
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
                "comment": "Voltage of Cell4",
                "row": 230,
                "state": {}
            }
        ]
    },
    "529": {
        "name": "BMS_Batt_Volt_Sts_x211",
        "id": 529,
        "signals": [
            {
                "name": "Vcell5_Volt",
                "start_bit": 7,
                "bit_length": 16,
                "bitindexes": [
                    0,
                    8,
                    8,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 0.001,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 65.535,
                "comment": "Voltage of Cell5",
                "row": 231,
                "state": {}
            },
            {
                "name": "Vcell6_Volt",
                "start_bit": 23,
                "bit_length": 16,
                "bitindexes": [
                    16,
                    24,
                    24,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 0.001,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 65.535,
                "comment": "Voltage of Cell6",
                "row": 232,
                "state": {}
            },
            {
                "name": "Vcell7_Volt",
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
                "unit": "V",
                "min": "",
                "max": 65.535,
                "comment": "Voltage of Cell7",
                "row": 233,
                "state": {}
            },
            {
                "name": "Vcell8_Volt",
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
                "comment": "Voltage of Cell8",
                "row": 234,
                "state": {}
            }
        ]
    },
    "530": {
        "name": "BMS_Batt_Volt_Sts_x212",
        "id": 530,
        "signals": [
            {
                "name": "Vcell9_Volt",
                "start_bit": 7,
                "bit_length": 16,
                "bitindexes": [
                    0,
                    8,
                    8,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 0.001,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 65.535,
                "comment": "Voltage of Cell9",
                "row": 235,
                "state": {}
            },
            {
                "name": "Vcell10_Volt",
                "start_bit": 23,
                "bit_length": 16,
                "bitindexes": [
                    16,
                    24,
                    24,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 0.001,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 65.535,
                "comment": "Voltage of Cell10",
                "row": 236,
                "state": {}
            },
            {
                "name": "Vcell11_Volt",
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
                "unit": "V",
                "min": "",
                "max": 65.535,
                "comment": "Voltage of Cell11",
                "row": 237,
                "state": {}
            },
            {
                "name": "Vcell12_Volt",
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
                "comment": "Voltage of Cell12",
                "row": 238,
                "state": {}
            }
        ]
    },
    "531": {
        "name": "BMS_Batt_Volt_Sts_x213",
        "id": 531,
        "signals": [
            {
                "name": "Vcell13_Volt",
                "start_bit": 7,
                "bit_length": 16,
                "bitindexes": [
                    0,
                    8,
                    8,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 0.001,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 65.535,
                "comment": "Voltage of Cell13",
                "row": 239,
                "state": {}
            },
            {
                "name": "Vcell14_Volt",
                "start_bit": 23,
                "bit_length": 16,
                "bitindexes": [
                    16,
                    24,
                    24,
                    32
                ],
                "byte_order": "big_endian",
                "scale": 0.001,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 65.535,
                "comment": "Voltage of Cell14",
                "row": 240,
                "state": {}
            }
        ]
    },
    "778": {
        "name": "BMS_ChargErrorNotify",
        "id": 778,
        "signals": [
            {
                "name": "Timeout",
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
                "comment": "0x00 --> No Timeout0x01 --> CHM receive timeout0x02 --> CML receive timeout0x03 --> CRO receive timeout0x04 --> CCS receive timeout0xFF --> Invalid",
                "row": 241,
                "state": {}
            }
        ]
    },
    "776": {
        "name": "BMS_ChargeStop",
        "id": 776,
        "signals": [
            {
                "name": "ChargerStop",
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
                "comment": "Cause for charging stop0x00 --> Normal0x01 --> Reached SOC 100%0XFF --> Error",
                "row": 242,
                "state": {}
            }
        ]
    },
    "512": {
        "name": "BMS_Charger_Info",
        "id": 512,
        "signals": [
            {
                "name": "Chgr_Output_Volt",
                "start_bit": 7,
                "bit_length": 16,
                "bitindexes": [
                    0,
                    8,
                    8,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 0.001,
                "offset": 0,
                "unit": "V",
                "min": "",
                "max": 65.535,
                "comment": "Output charging voltage from charger",
                "row": 243,
                "state": {}
            },
            {
                "name": "Chgr_Output_Amp",
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
                "unit": "A",
                "min": "",
                "max": 1000,
                "comment": "Charging current consumed by battery pack",
                "row": 244,
                "state": {}
            },
            {
                "name": "Cntrl_Chgr_Output",
                "start_bit": 32,
                "bit_length": 1,
                "bitindexes": [
                    32,
                    33,
                    48,
                    48
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "Status of charger",
                "row": 245,
                "state": {}
            }
        ]
    },
    "523": {
        "name": "BMS_Charging_Indication",
        "id": 523,
        "signals": [
            {
                "name": "Charging_Indication",
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
                "comment": "Charging Indication1--> Charging0--> No Charging",
                "row": 246,
                "state": {}
            },
            {
                "name": "FWDATE",
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
                "row": 247,
                "state": {}
            },
            {
                "name": "FWMONTH",
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
                "unit": "",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 248,
                "state": {}
            },
            {
                "name": "FWYEAR1",
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
                "unit": "",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 249,
                "state": {}
            },
            {
                "name": "FWYEAR2",
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
                "row": 250,
                "state": {}
            }
        ]
    },
    "665": {
        "name": "BMS_Elektronika_Internal_Debug",
        "id": 665,
        "signals": []
    },
    "526": {
        "name": "BMS_Error_bits",
        "id": 526,
        "signals": [
            {
                "name": "Thermal_Runaway",
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
                "comment": "1 - Error0 - No Error",
                "row": 251,
                "state": {}
            },
            {
                "name": "Error_bits",
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
                "comment": "1st bit - Regen Error2nd bit - short circuit Error3rd bit - LV Error4th Bit - HV Error5th Bit - Discharge OV Current Error6th Bit -  Charge Over Current Error7th Bit - IGN Key Status",
                "row": 252,
                "state": {}
            }
        ]
    },
    "544": {
        "name": "BMS_Firmware_V220",
        "id": 544,
        "signals": []
    },
    "545": {
        "name": "BMS_Firmware_V221",
        "id": 545,
        "signals": []
    },
    "546": {
        "name": "BMS_Firmware_V222",
        "id": 546,
        "signals": []
    },
    "547": {
        "name": "BMS_HW_FW_V223",
        "id": 547,
        "signals": [
            {
                "name": "HW_V1",
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
                "row": 253,
                "state": {}
            },
            {
                "name": "HW_V2",
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
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 254,
                "state": {}
            },
            {
                "name": "HW_V3",
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
                "unit": "",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 255,
                "state": {}
            },
            {
                "name": "HW_V4",
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
                "max": 255,
                "comment": "",
                "row": 256,
                "state": {}
            },
            {
                "name": "HW_V5",
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
                "row": 257,
                "state": {}
            },
            {
                "name": "HW_V6",
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
                "unit": "",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 258,
                "state": {}
            },
            {
                "name": "HW_V7",
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
                "unit": "",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 259,
                "state": {}
            },
            {
                "name": "HW_V8",
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
                "row": 260,
                "state": {}
            }
        ]
    },
    "770": {
        "name": "BMS_Major_version",
        "id": 770,
        "signals": [
            {
                "name": "MajorVersion",
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
                "row": 261,
                "state": {}
            },
            {
                "name": "MinorVersion",
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
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 262,
                "state": {}
            },
            {
                "name": "BugFixVersion",
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
                "unit": "",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 263,
                "state": {}
            }
        ]
    },
    "548": {
        "name": "BMS_SW_FW_V224",
        "id": 548,
        "signals": [
            {
                "name": "SW_V1",
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
                "row": 264,
                "state": {}
            },
            {
                "name": "SW_V2",
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
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 265,
                "state": {}
            },
            {
                "name": "SW_V3",
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
                "unit": "",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 266,
                "state": {}
            },
            {
                "name": "SW_V4",
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
                "max": 255,
                "comment": "",
                "row": 267,
                "state": {}
            },
            {
                "name": "SW_V5",
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
                "row": 268,
                "state": {}
            },
            {
                "name": "SW_V6",
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
                "unit": "",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 269,
                "state": {}
            },
            {
                "name": "SW_V7",
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
                "unit": "",
                "min": "",
                "max": 255,
                "comment": "",
                "row": 270,
                "state": {}
            },
            {
                "name": "SW_V8",
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
                "row": 271,
                "state": {}
            }
        ]
    },
    "524": {
        "name": "BMS_Temp_Sensor_Error",
        "id": 524,
        "signals": [
            {
                "name": "Temp_Error",
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
                "comment": "Temperature Error 1st bit to 6th bit - Temp sensor7th Bit - Board Temp8th bit - IC Temp--------------------1--> Error0--> No Error",
                "row": 272,
                "state": {}
            },
            {
                "name": "Total_Capacity",
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
                "unit": "",
                "min": "",
                "max": 65535,
                "comment": "",
                "row": 273,
                "state": {}
            },
            {
                "name": "Cell_Diff_Prot",
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
                "unit": "",
                "min": "",
                "max": 65535,
                "comment": "1 - Flag_set0 - Flag_clear",
                "row": 274,
                "state": {}
            },
            {
                "name": "Cumulative_pwr",
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
                "unit": "",
                "min": "",
                "max": 65535,
                "comment": "1 - Flag_set0 - Flag_clear",
                "row": 275,
                "state": {}
            }
        ]
    },
    "522": {
        "name": "BMS_Voltage_Error",
        "id": 522,
        "signals": [
            {
                "name": "Voltage_Error_Cell_1to8",
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
                "comment": "Voltage error for cell number 1 to 81--> error0--> No error",
                "row": 276,
                "state": {}
            },
            {
                "name": "Voltage_Error_Cell_9to14",
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
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 255,
                "comment": "Voltage error for cell number 9 to 14",
                "row": 277,
                "state": {}
            },
            {
                "name": "Temp_error_flag",
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
                "row": 278,
                "state": {}
            }
        ]
    },
    "258": {
        "name": "SOC_Mode_Speed_TX",
        "id": 258,
        "signals": [
            {
                "name": "Speed_TX",
                "start_bit": 7,
                "bit_length": 16,
                "bitindexes": [
                    0,
                    8,
                    8,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 0.01,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 655.35,
                "comment": "",
                "row": 279,
                "state": {}
            },
            {
                "name": "Mode_TX",
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
                "unit": "",
                "min": "",
                "max": 65535,
                "comment": "",
                "row": 280,
                "state": {}
            },
            {
                "name": "SOC_TX",
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
                "unit": "%",
                "min": "",
                "max": 100,
                "comment": "",
                "row": 281,
                "state": {}
            }
        ]
    },
    "257": {
        "name": "ODO_Trip_TX",
        "id": 257,
        "signals": [
            {
                "name": "ODO_TX",
                "start_bit": 7,
                "bit_length": 32,
                "bitindexes": [
                    0,
                    8,
                    -8,
                    16
                ],
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": "",
                "max": 10000000.0,
                "comment": "",
                "row": 282,
                "state": {}
            },
            {
                "name": "TripA_TX",
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
                "unit": "km",
                "min": "",
                "max": 65535,
                "comment": "",
                "row": 283,
                "state": {}
            },
            {
                "name": "TripB_TX",
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
                "unit": "",
                "min": "",
                "max": 10000,
                "comment": "",
                "row": 284,
                "state": {}
            }
        ]
    },
    "341": {
        "name": "DTE",
        "id": 341,
        "signals": [
            {
                "name": "DTE",
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
                "row": 285,
                "state": {}
            }
        ]
    },
    "777": {
        "name": "ChargingStatusLED_ON",
        "id": 777,
        "signals": [
            {
                "name": "ChargingStateSolid_ON",
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
                "unit": "",
                "min": "",
                "max": 1,
                "comment": "",
                "row": 286,
                "state": {}
            }
        ]
    }
}