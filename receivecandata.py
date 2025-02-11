from PyQt5.QtCore import QThread, pyqtSignal
import can
import serial
import time
from datetime import datetime



class DataReadThread(QThread):

    rawdataemitted = pyqtSignal(list)

    def __init__(self, interface, bitrate, port, channel = None):
        super().__init__()

        self.interface = interface
        self.port = port
        self.bitrate = bitrate
        self.channel = channel


        self.running = False

    def run(self):

        self.running = True

        if self.interface == "P-CAN":

            try:
                self.bus = can.Bus(interface="pcan", channel=self.port, bitrate=500 * 1000)

                while self.running:
                    try:
                        response = self.bus.recv(0.1)
                        # time.sleep(0.001)
                        if response:
                            # response = can.Message(arbitration_id=0x504, data = [0x28, 0x42, 0x20, 0x30, 0x18, 0x87, 0x03, 0x2F])
                            self.rawdataemitted.emit([response.arbitration_id, ' '.join(f'{byte:02x}' for byte in response.data), str(datetime.now()).split()[1][:-3]])
                    except Exception as e:
                        print(e)

                    # time.sleep(2)
            except Exception as e:
                print("in data read thread , run", e)

        elif self.interface == "V-LinkerBT":
            try:
                self.ser = serial.Serial(port = self.port,baudrate=115200, timeout=1, write_timeout=1)
                cmd_list = ['atz', 'atz', 'atsp6', 'ATD', 'ate0', 'ATCFC1', 'ATD1', 'ATBD',
                            'ATAL', 'ath1', 'atCAF0', 'atL0', 'atS1', 'ATCSM0', 'atcea hh', 'atma']
                # cmd_list = ["atma"]

                for cmd in cmd_list:
                    self.ser.write(cmd.encode() + b'\r\n')
                    time.sleep(0.5)
                    response = self.ser.read(self.ser.in_waiting).decode().split('\r')
                    print(response)

                while True:

                    if self.ser.in_waiting > 0:
                        responses = self.ser.read(self.ser.in_waiting).decode().split('\r')

                        if responses:
                            for response  in responses[:-1]:
                                try:
                                    res1 = response.split()

                                    if len(res1[1]) != 1:

                                        canid = ''.join(res1[:4])
                                        data = ' '.join(res1[5:])
                                    else:
                                        canid = res1[0]
                                        data = " ".join(res1[2:])


                                    self.rawdataemitted.emit([int(canid, 16), data, str(datetime.now()).split()[1][:-3]])
                                except Exception as e:
                                    print("in vlinker data read", e)
                        if "BUFFER FULL" in responses:
                            time1 = datetime.now()
                            print(responses)
                            print("BUFFER FULL")

                            # Handling buffer overflow
                            cmd_list1 = ['ATSP6', 'ATAL', 'atCAF0', 'ATH1', 'atL0', 'atma']
                            for cmd in cmd_list1:
                                self.ser.write(cmd.encode() + b'\r\n')
                                time.sleep(0.2)
                            responses = self.ser.read(self.ser.in_waiting).decode().split('\r')
                            time2 = datetime.now()
                            diff = time2 - time1

            except Exception as e:
                print("in data read run, vlinkerBT", e)

    def stop(self):
        self.running = False
        self.bus.shutdown()
        self.bus = None

