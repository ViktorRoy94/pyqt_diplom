# !/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import MainWindow as mw
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('diplom')

    # create widget
    w = mw.MainWindow()
    w.setWindowTitle("Диплом")
    w.show()

    # execute application
    sys.exit(app.exec_())
