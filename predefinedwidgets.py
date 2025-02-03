from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class CustomLabel(QLabel):
    def __init__(self, text:str, bgcolor = str|None, color = str|None, size = int|None):
        super().__init__()

        self.setText(text)
        self.setStyleSheet(f"background-color : {bgcolor}; color : {color}; font-size : {size}px" )



class CustomTable(QTableWidget):
    def __init__(self):
        super().__init__()

        header = self.horizontalHeader()
        header_font = header.font()
        header_font.setBold(True)  # Set bold
        header_font.setPointSize(12)  # Set font size
        header.setFont(header_font)

        self.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # self.verticalHeader().hide()
        # self.setFrameStyle(QTableWidget.NoFrame)

        # self.setShowGrid(False)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setAlternatingRowColors(True)

        self.setColumnCount(5)
        self.setRowCount(100)

        # Change table color
        # bg1 = "#10111F"
        # self.setStyleSheet(f"""
        #                     QTableWidget {{
        #                         background-color: {Theme().mainframecolor};   /* # #E3FFA8;  /* Light blue for base row  */
        #                         alternate-background-color: {Theme().mainframecolor}; /*#FFFFA8;  /* Light cyan for alternate row */
        #                         font-weight : bold;
        #                         font-size : 20 px;
        #                         border : 2px solid white;
        #                         color : white;
        #
        #                     }}
        #                     QHeaderView::section {{
        #                         background-color:{Theme().mainframecolor}; /* Header background color #C0CA33 */
        #                         color: white; /* Header text color */
        #                         padding : 5px;
        #                         border : none;
        #                     }}
        #
        #                     QTableCornerButton::section {{
        #                     background-color: {Theme().mainframecolor};  /* Corner button same as header */
        #                     border: none;  /* Remove border if necessary */
        #
        # }}
        #                 """)