canids_3W_CLUSTER = [777, 259, 1025, 258, 257, 515, 518, 341, 513, 1283]
json_3W_CLUSTER = {
    "777": {
        "name": "Charging_LED_Condition",
        "id": 777,
        "signals": [
            {
                "name": "Sig_Charge_LED_condition",
                "start_bit": 7,
                "bit_length": 8,
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": 0,
                "max": 255,
                "comment": "",
                "row": 0,
                "state": {
                    "1": "OFF",
                    "0": "Solid_ON"
                }
            }
        ]
    },
    "259": {
        "name": "ODO_TX_Fare_Meter",
        "id": 259,
        "signals": [
            {
                "name": "ODO_TX",
                "start_bit": 7,
                "bit_length": 32,
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "km",
                "min": 0,
                "max": 10000000,
                "comment": "",
                "row": 1,
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
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": 0,
                "max": 1,
                "comment": "",
                "row": 2,
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
                "byte_order": "big_endian",
                "scale": 0.01,
                "offset": 0,
                "unit": "",
                "min": 0,
                "max": 9900,
                "comment": "",
                "row": 3,
                "state": {}
            },
            {
                "name": "Mode_TX",
                "start_bit": 23,
                "bit_length": 16,
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": 0,
                "max": 65535,
                "comment": "",
                "row": 4,
                "state": {}
            },
            {
                "name": "SOC_TX",
                "start_bit": 39,
                "bit_length": 16,
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "%",
                "min": 0,
                "max": 100,
                "comment": "",
                "row": 5,
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
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "km",
                "min": 0,
                "max": 10000000,
                "comment": "",
                "row": 6,
                "state": {}
            },
            {
                "name": "TripA_TX",
                "start_bit": 39,
                "bit_length": 16,
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "km",
                "min": 0,
                "max": 99999.9,
                "comment": "",
                "row": 7,
                "state": {}
            },
            {
                "name": "TripB_TX",
                "start_bit": 55,
                "bit_length": 16,
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": 0,
                "max": 9999.9,
                "comment": "",
                "row": 8,
                "state": {}
            }
        ]
    },
    "515": {
        "name": "charging_indication",
        "id": 515,
        "signals": [
            {
                "name": "Charging",
                "start_bit": 7,
                "bit_length": 16,
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": 0,
                "max": 65535,
                "comment": "",
                "row": 9,
                "state": {
                    "1": "LED_blink",
                    "0": "LED_OFF"
                }
            }
        ]
    },
    "518": {
        "name": "BAT_Temperature",
        "id": 518,
        "signals": [
            {
                "name": "BAT_Temp1",
                "start_bit": 7,
                "bit_length": 8,
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "deg",
                "min": 0,
                "max": 100,
                "comment": "",
                "row": 10,
                "state": {}
            },
            {
                "name": "BAT_Temp2",
                "start_bit": 15,
                "bit_length": 8,
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": 0,
                "max": 100,
                "comment": "",
                "row": 11,
                "state": {}
            },
            {
                "name": "BAT_Temp3",
                "start_bit": 23,
                "bit_length": 8,
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": 0,
                "max": 100,
                "comment": "",
                "row": 12,
                "state": {}
            },
            {
                "name": "BAT_Temp4",
                "start_bit": 31,
                "bit_length": 8,
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": 0,
                "max": 100,
                "comment": "",
                "row": 13,
                "state": {}
            },
            {
                "name": "BAT_Temp5",
                "start_bit": 39,
                "bit_length": 8,
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": 0,
                "max": 100,
                "comment": "",
                "row": 14,
                "state": {}
            },
            {
                "name": "BAT_Temp6",
                "start_bit": 47,
                "bit_length": 8,
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": 0,
                "max": 100,
                "comment": "",
                "row": 15,
                "state": {}
            }
        ]
    },
    "1284": {
        "name": "Mode",
        "id": 1284,
        "signals": [
            {
                "name": "Vehicle_Mode",
                "start_bit": 7,
                "bit_length": 8,
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "indication",
                "min": 0,
                "max": 16,
                "comment": "",
                "row": 16,
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
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": 0,
                "max": 255,
                "comment": "",
                "row": 17,
                "state": {}
            }
        ]
    },
    "513": {
        "name": "SOC",
        "id": 513,
        "signals": [
            {
                "name": "SOC_Percentage",
                "start_bit": 39,
                "bit_length": 16,
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "",
                "min": 0,
                "max": 100,
                "comment": "",
                "row": 18,
                "state": {}
            }
        ]
    },
    "1283": {
        "name": "Speed",
        "id": 1283,
        "signals": [
            {
                "name": "Speed_RPM",
                "start_bit": 55,
                "bit_length": 16,
                "byte_order": "big_endian",
                "scale": 1,
                "offset": 0,
                "unit": "rpm",
                "min": 0,
                "max": 65535,
                "comment": "",
                "row": 19,
                "state": {}
            }
        ]
    }
}