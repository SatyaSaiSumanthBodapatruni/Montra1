import time
from http.client import responses

from PyQt5.QtCore import QThread, pyqtSignal

from json_files.AUTO.AUTO import canids_3W, json_3W
from json_files.AUTO.BMS import canids_3W_BMS, json_3W_BMS
from json_files.AUTO.CLUSTER import canids_3W_CLUSTER, json_3W_CLUSTER
from json_files.AUTO.MCU import json_3W_MCU, canids_3W_MCU
from json_files.SCV.TELEMATICS import canids_SCV_TELEMATICS, json_SCV_TELEMATICS


class ParseDataThread(QThread):

    parsed_signal_emitted = pyqtSignal(list)

    def __init__(self, segment):
        super().__init__()

        self.responsed_time = None
        self.canid = None
        self.candata = None

        if segment == "3W":
            # self.canids = [canids_3W_BMS,canids_3W_CLUSTER,canids_3W_MCU]
            self.canids = [canids_3W]
            # self.jsons = [json_3W_BMS,json_3W_CLUSTER,json_3W_MCU]
            self.jsons = [json_3W]

        if segment == "SCV":
            self.canids = [canids_SCV_TELEMATICS]
            self.jsons = [json_SCV_TELEMATICS]



        self.running = True

        self.parse = False


    def run(self):

        while self.running:
            if self.parse == True:
                try:
                    self.parse_data()

                except Exception as e:
                    print(self.candata,self.canid,e)
                    pass
                    # print(self.candata)
                    # print("in parse data run", e)
                self.parse = False
            time.sleep(0.001)

    def send_response(self, canid, data, resp_time):
        self.canid = canid
        self.candata = data
        self.responsed_time = resp_time
        self.parse = True


    def parse_data(self):

        data = ''.join(format(int(h, 16), '08b') for h in self.candata.split())

        for ids in self.canids:
            if self.canid in ids:
                ecu_index = self.canids.index(ids)

                for signal in self.jsons[ecu_index][str(self.canid)]["signals"]:
                    # if signal[]
                    signal_name = signal['name']
                    bit_indexes = signal['bitindexes']
                    bit_length = int(signal['bit_length'])
                    byte_order = signal['byte_order']
                    scale = signal['scale']
                    offset = signal['offset']
                    unit = signal['unit']
                    row = signal['row']

                    if byte_order == "little_endian" and bit_length > 8:
                        print("little")

                    try:
                        bits = data[bit_indexes[0]:bit_indexes[1]] + data[bit_indexes[2]:bit_indexes[3]]

                    except Exception as e:
                        print(e)

                    value = (int(bits, 2) * scale )+ offset

                    value = str(value)

                    try:
                        if signal['state'][str(value)]:
                            value = signal['state'][str(value)]

                    except Exception as e:
                        pass



                    self.parsed_signal_emitted.emit([signal_name, value, self.canid, ecu_index,row, self.responsed_time])





