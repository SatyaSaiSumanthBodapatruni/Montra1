from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from predefinedwidgets import CustomLabel
from themes import mainbgcolor


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.logincentrallayout = QVBoxLayout(self)
        self.setStyleSheet(f"""QWidget {{background-color : {mainbgcolor}}}
        
                               QLabel {{color : white; font-size : 30px}}
                               
                               QLineEdit {{background-color : grey}}
                            
                            """)

        self.usernamelabel = CustomLabel("Username : ",bgcolor= None, color = "white", size=30)
        self.logincentrallayout.addWidget(self.usernamelabel, alignment = Qt.AlignCenter)

        self.usernamelineedit = QLineEdit()
        self.logincentrallayout.addWidget(self.usernamelineedit, alignment = Qt.AlignCenter)

        self.passwordlabel = CustomLabel("Password")
        self.logincentrallayout.addWidget(self.passwordlabel, alignment = Qt.AlignCenter)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())