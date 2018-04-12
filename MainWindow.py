from Ui_MainWindow import *
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QHBoxLayout

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
