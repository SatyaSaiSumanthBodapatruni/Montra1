from PyQt5.QtCore import QThread, pyqtSignal
import can
import time

class DataReadThread(QThread):

    rawdataemitted = pyqtSignal(list)

    def __init__(self, interface, bitrate):
        super().__init__()

        self.interface = interface
        self.bitrate = bitrate

        self.running = False

    def run(self):

        self.running = True

        if self.interface == "P-CAN":
            self.bus = can.Bus(interface="pcan", channel="PCAN_USBBUS1", bitrate=500 * 1000)
            reader = can.BufferedReader()
            notifier = can.Notifier(self.bus, [reader])
            while self.running:
                response = reader.get_message(1)
                # response = self.bus.recv(0.1)
                self.rawdataemitted.emit([hex(response.arbitration_id).split('x')[1], response.data.hex(), time.time()])


    def stop(self):
        self.running = False
        self.bus.shutdown()

