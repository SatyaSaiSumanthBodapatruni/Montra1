import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from predefinedwidgets import CustomTable

import can

from receivecandata import DataReadThread


class DashBoard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("")

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.centrallayoutvbox = QVBoxLayout(self)
        self.centralwidget.setLayout(self.centrallayoutvbox)

        self.tophbox1 = QHBoxLayout(self)
        self.centrallayoutvbox.addLayout(self.tophbox1)

        self.tophbox1vbox1 = QVBoxLayout(self)
        self.tophbox1.addLayout(self.tophbox1vbox1)

        self.segmentcombobox = QComboBox(self)
        self.segmentcombobox.addItems(["Select Segment","3W", "HCV", "TRACTOR", "SCV"])
        self.tophbox1vbox1.addWidget(self.segmentcombobox)

        self.variantcombobox = QComboBox(self)
        self.variantcombobox.addItems(["Select Variant"])
        self.tophbox1vbox1.addWidget(self.variantcombobox)

        self.selecthardwarecombobox = QComboBox(self)
        self.selecthardwarecombobox.addItems(["Select Interface", "P-CAN", "V-LinkerBT", "V-Linker"])
        self.tophbox1vbox1.addWidget(self.selecthardwarecombobox)

        self.connectbutton = QPushButton("Connect")
        self.connectbutton.setStyleSheet("color : green")
        self.connectbutton.clicked.connect(self.on_connectbutton_click)
        self.tophbox1.addWidget(self.connectbutton)

        self.disconnectbutton = QPushButton("Disconnect")
        self.disconnectbutton.setStyleSheet("color : red")
        self.disconnectbutton.clicked.connect(self.on_disconnectbutton_click)
        self.tophbox1.addWidget(self.disconnectbutton)

        self.tophbox1.addStretch(1)


        self.tabbedwidget = QTabWidget(self)


        self.livedatatab = QTabWidget(self)
        self.livedatatab.setStyleSheet("color : blue")
        self.tabbedwidget.addTab(self.livedatatab, "Signals Monitor")

        self.faultanalysiswidget = QTabWidget(self)
        self.faultanalysiswidget.setStyleSheet("color : red")
        self.tabbedwidget.addTab(self.faultanalysiswidget, "Fault Analysis")

        self.tracewindowtable = CustomTable()
        self.tabbedwidget.addTab(self.tracewindowtable, "Trace Window")

        self.centrallayoutvbox.addWidget(self.tabbedwidget)

        # self.centrallayoutvbox.addStretch(1)

        self.collected_can_id = []
        self.collected_can_data = []
        self.time_data = []

        self.segment_ecus_list = []



    def on_connectbutton_click(self):

        self.connectbutton.setEnabled(False)
        self.disconnectbutton.setEnabled(True)

        for i in range(len(self.segment_ecus_list), -1, -1):
            self.livedatatab.removeTab(i)
            self.faultanalysiswidget.removeTab(i)

        self.segment_ecus_list = ["BMS", "CLUSTER","MCU", "TELEMATICS"]
        for i in self.segment_ecus_list:
            widget = CustomTable()
            widget1 = CustomTable()
            self.livedatatab.addTab(widget, i)
            self.faultanalysiswidget.addTab(widget1, i)

        try:
            self.datareadthread = DataReadThread("P-CAN", "PCAN_USBBUS1")
            self.datareadthread.rawdataemitted.connect(self.on_rawdata_emitted)
            self.datareadthread.start()

        except Exception as e:
            print(e)




    def on_disconnectbutton_click(self):
        self.connectbutton.setEnabled(True)
        self.disconnectbutton.setEnabled(False)
        self.datareadthread.stop()



    def on_rawdata_emitted(self, data):
        self.update_trace_table(data)




    def update_trace_table(self, data):

        try:
            if data[0] not in self.collected_can_id:
                self.collected_can_id.append(data[0])
                self.collected_can_data.append(data[1])
                self.time_data.append(data[2])

            else:
                index = self.collected_can_id.index(data[0])
                self.collected_can_data[index] = data[1]
                self.time_data[index] = data[2]
                self.tracewindowtable.setItem(index, 0, QTableWidgetItem(data[0]))
                self.tracewindowtable.setItem(index, 1, QTableWidgetItem(data[1]))

        except Exception as e:
            print("in update trace table", e)


        # self.selectvariant = QComboBox(self)




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = DashBoard()
    window.showMaximized()
    sys.exit(app.exec_())