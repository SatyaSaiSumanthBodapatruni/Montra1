from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.maincentrallayout = QVBoxLayout(self)

        self.loginwidgt
        self.maincentrallayout













if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())