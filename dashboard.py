import time
from signal import signal

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from json_files.AUTO.BMS import canids_3W_BMS, json_3W_BMS
from json_files.AUTO.CLUSTER import canids_3W_CLUSTER, json_3W_CLUSTER
from json_files.AUTO.MCU import canids_3W_MCU, json_3W_MCU
from json_files.AUTO.AUTO import canids_3W,json_3W
from json_files.SCV.TELEMATICS import json_SCV_TELEMATICS
from parsedata import ParseDataThread
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

        self.selectinterfacecombobox = QComboBox(self)
        self.selectinterfacecombobox.addItems(["Select Interface", "P-CAN", "V-LinkerBT", "V-Linker"])
        self.selectinterfacecombobox.currentIndexChanged.connect(self.on_interface_changed)
        self.tophbox1vbox1.addWidget(self.selectinterfacecombobox)

        self.selectportcombobox = QComboBox(self)
        self.tophbox1vbox1.addWidget(self.selectportcombobox)

        self.selectchannelcombobox = QComboBox(self)
        self.selectchannelcombobox.addItems(["CHANNEL1(6,14)", "CHANNEL2(12,13)", "CHANNEl3(1,9)"])
        self.tophbox1vbox1.addWidget(self.selectchannelcombobox)

        self.tophbox1vbox2 = QVBoxLayout(self)
        self.tophbox1.addLayout(self.tophbox1vbox2)

        self.segmentcombobox = QComboBox(self)
        self.segmentcombobox.addItems(["3W", "HCV", "TRACTOR", "SCV"])
        self.segmentcombobox.currentIndexChanged.connect(self.modify_tables)
        self.tophbox1vbox2.addWidget(self.segmentcombobox)

        self.variantcombobox = QComboBox(self)
        self.variantcombobox.addItems(["Select Variant"])
        self.tophbox1vbox2.addWidget(self.variantcombobox)

        self.connectbutton = QPushButton("Connect")
        self.connectbutton.setStyleSheet("color : green")
        self.connectbutton.clicked.connect(self.on_connectbutton_click)
        self.tophbox1.addWidget(self.connectbutton)

        self.disconnectbutton = QPushButton("Disconnect")
        self.disconnectbutton.setEnabled(False)
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

        self.segmentcombobox.setCurrentIndex(0)
        self.selectinterfacecombobox.setCurrentIndex(1)


        self.on_interface_changed(1)
        self.modify_tables()



        self.emitcount = 0




    def on_connectbutton_click(self):

        self.connectbutton.setEnabled(False)
        self.disconnectbutton.setEnabled(True)

        # for i in range(len(self.segment_ecus_list), -1, -1):
        #     self.livedatatab.removeTab(i)
        #     self.faultanalysiswidget.removeTab(i)

        try:
            self.datareadthread = DataReadThread(self.selectinterfacecombobox.currentText(), 500, self.selectportcombobox.currentText(), self.selectchannelcombobox.currentText())
            self.datareadthread.rawdataemitted.connect(self.on_rawdata_emitted)
            self.datareadthread.start()

            self.parsedatathread1 = ParseDataThread(self.segmentcombobox.currentText())
            self.parsedatathread1.parsed_signal_emitted.connect(self.on_data_parsed)
            self.parsedatathread1.start()

            self.parsedatathread2 = ParseDataThread(self.segmentcombobox.currentText())
            self.parsedatathread2.parsed_signal_emitted.connect(self.on_data_parsed)
            self.parsedatathread2.start()

            self.parsedatathread3 = ParseDataThread(self.segmentcombobox.currentText())
            self.parsedatathread3.parsed_signal_emitted.connect(self.on_data_parsed)
            self.parsedatathread3.start()

            # self.parsedatathread4 = ParseDataThread(self.segmentcombobox.currentText())
            # self.parsedatathread4.parsed_signal_emitted.connect(self.on_data_parsed)
            # self.parsedatathread4.start()
            #
            # self.parsedatathread5 = ParseDataThread(self.segmentcombobox.currentText())
            # self.parsedatathread5.parsed_signal_emitted.connect(self.on_data_parsed)
            # self.parsedatathread5.start()
            #
            # self.parsedatathread6 = ParseDataThread(self.segmentcombobox.currentText())
            # self.parsedatathread6.parsed_signal_emitted.connect(self.on_data_parsed)
            # self.parsedatathread6.start()
            #
            # self.parsedatathread7 = ParseDataThread(self.segmentcombobox.currentText())
            # self.parsedatathread7.parsed_signal_emitted.connect(self.on_data_parsed)
            # self.parsedatathread7.start()
            #
            # self.parsedatathread8 = ParseDataThread(self.segmentcombobox.currentText())
            # self.parsedatathread8.parsed_signal_emitted.connect(self.on_data_parsed)
            # self.parsedatathread8.start()
            #
            # self.parsedatathread9 = ParseDataThread(self.segmentcombobox.currentText())
            # self.parsedatathread9.parsed_signal_emitted.connect(self.on_data_parsed)
            # self.parsedatathread9.start()
            #
            # self.parsedatathread10 = ParseDataThread(self.segmentcombobox.currentText())
            # self.parsedatathread10.parsed_signal_emitted.connect(self.on_data_parsed)
            # self.parsedatathread10.start()
            #
            # self.parsedatathread11 = ParseDataThread(self.segmentcombobox.currentText())
            # self.parsedatathread11.parsed_signal_emitted.connect(self.on_data_parsed)
            # self.parsedatathread11.start()


        except Exception as e:
            print(e)

    def on_data_parsed(self, data):
        # parsed_data = [signal_name, value, self.canid, ecu_index,row, self.responsed_time]
        # print(data)
        signalname = data[0]
        value = data[1]
        id = data[2]
        table_index = data[3]
        table_row = data[4]
        responsed_time = data[5]

        table = self.livedatatab.widget(table_index)
        # table.setItem(table_row, 0, QTableWidgetItem(signalname))
        table.setItem(table_row, 1, QTableWidgetItem(str(value)))
        table.setItem(table_row, 2, QTableWidgetItem(str(responsed_time)))

        if value == "Fault":
            print("in fault")
            faulttable = self.faultanalysiswidget.widget(table_index)
            faulttable.setItem(table_row, 1, QTableWidgetItem(str(value)))
            faulttable.setItem(table_row, 2, QTableWidgetItem(str(responsed_time)))

    def on_disconnectbutton_click(self):
        self.connectbutton.setEnabled(True)
        self.disconnectbutton.setEnabled(False)
        self.datareadthread.stop()



    def on_rawdata_emitted(self, data):
        self.update_trace_table(data)
        # self.parsedatathread.send_response(data[0], data[1], data[2])

        if self.emitcount == 0:
            self.parsedatathread1.send_response(data[0], data[1], data[2])
        elif self.emitcount == 1:
            self.parsedatathread2.send_response(data[0], data[1], data[2])
        elif self.emitcount == 2:
            self.parsedatathread3.send_response(data[0], data[1], data[2])
        # elif self.emitcount == 3:
        #     self.parsedatathread4.send_response(data[0], data[1], data[2])
        # elif self.emitcount == 4:
        #     self.parsedatathread5.send_response(data[0], data[1], data[2])
        # elif self.emitcount == 5:
        #     self.parsedatathread6.send_response(data[0], data[1], data[2])
        # elif self.emitcount == 6:
        #     self.parsedatathread7.send_response(data[0], data[1], data[2])
        # elif self.emitcount == 7:
        #     self.parsedatathread8.send_response(data[0], data[1], data[2])
        # elif self.emitcount == 8:
        #     self.parsedatathread9.send_response(data[0], data[1], data[2])
        # elif self.emitcount == 9:
        #     self.parsedatathread10.send_response(data[0], data[1], data[2])
        # elif self.emitcount == 10:
        #     self.parsedatathread11.send_response(data[0], data[1], data[2])
            self.emitcount = 0



        self.emitcount += 1


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
                self.tracewindowtable.setItem(index, 0, QTableWidgetItem(hex(data[0]).split('x')[1].upper()))
                self.tracewindowtable.setItem(index, 1, QTableWidgetItem(data[1].upper()))
                self.tracewindowtable.setItem(index, 2, QTableWidgetItem(data[2]))

        except Exception as e:
            print("in update trace table", e)


        # self.selectvariant = QComboBox(self)

    def modify_tables(self):

        for i in range(len(self.segment_ecus_list), -1, -1):
            self.livedatatab.removeTab(i)

        self.faultanalysiswidget.removeTab(0)

        if self.segmentcombobox.currentText() == "3W":

            # self.segment_ecus_list = ["BMS", "CLUSTER", "MCU", "TELEMATICS"]
            self.segment_ecus_list = ["3W"]
            for i in self.segment_ecus_list:
                widget = CustomTable()
                self.livedatatab.addTab(widget, i)

            # self.canids = [canids_3W_BMS, canids_3W_CLUSTER, canids_3W_MCU]
            self.jsondatas = [json_3W_BMS, json_3W_CLUSTER, json_3W_MCU]
            self.jsondatas = [json_3W]


        if self.segmentcombobox.currentText() == "SCV":
            self.segment_ecus_list = ["TELEMATICS"]
            for i in self.segment_ecus_list:
                widget = CustomTable()
                self.livedatatab.addTab(widget, i)

            self.jsondatas = [json_SCV_TELEMATICS]

        self.faultanalysiswidget.addTab(CustomTable(), "Errors")

        for jsondata, tableindex in zip(self.jsondatas, range(len(self.jsondatas))):
            table = self.livedatatab.widget(tableindex)
            count = 0
            for msgs in jsondata.items():
                for signalname in jsondata[msgs[0]]['signals']:
                    print(signalname['name'])
                    table.setItem(count, 0, QTableWidgetItem(signalname['name']))
                    count += 1
            table.setRowCount(count)


    def on_interface_changed(self, interface_index):
        self.connectbutton.setEnabled(True)
        if interface_index == 1:
            self.selectportcombobox.clear()
            self.selectportcombobox.addItem("PCAN_USBBUS1")
        elif interface_index == 2:
            self.selectportcombobox.clear()
            self.selectportcombobox.addItem("COM5")
        elif interface_index == 3:
            self.selectportcombobox.clear()
            self.selectportcombobox.addItem("COM3")
        else:
            self.connectbutton.setEnabled(False)








if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = DashBoard()
    window.showMaximized()
    sys.exit(app.exec_())