# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Projects\pyqt_diplom\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1013, 572)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftSideW = QtWidgets.QWidget(self.centralwidget)
        self.leftSideW.setMinimumSize(QtCore.QSize(230, 0))
        self.leftSideW.setMaximumSize(QtCore.QSize(250, 16777215))
        self.leftSideW.setObjectName("leftSideW")
        self.formLayout = QtWidgets.QFormLayout(self.leftSideW)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.leftSideW)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.otverCB = QtWidgets.QComboBox(self.groupBox_3)
        self.otverCB.setMinimumSize(QtCore.QSize(100, 0))
        self.otverCB.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.otverCB.setObjectName("otverCB")
        self.otverCB.addItem("")
        self.otverCB.addItem("")
        self.verticalLayout_2.addWidget(self.otverCB)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.groupBox_3)
        self.calcB = QtWidgets.QPushButton(self.leftSideW)
        self.calcB.setObjectName("calcB")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.calcB)
        self.groupBox_2 = QtWidgets.QGroupBox(self.leftSideW)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.materialCB = QtWidgets.QComboBox(self.groupBox_2)
        self.materialCB.setMinimumSize(QtCore.QSize(100, 0))
        self.materialCB.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.materialCB.setObjectName("materialCB")
        self.materialCB.addItem("")
        self.materialCB.addItem("")
        self.materialCB.addItem("")
        self.materialCB.addItem("")
        self.materialCB.addItem("")
        self.materialCB.addItem("")
        self.materialCB.addItem("")
        self.materialCB.addItem("")
        self.materialCB.addItem("")
        self.materialCB.addItem("")
        self.materialCB.addItem("")
        self.materialCB.addItem("")
        self.materialCB.addItem("")
        self.materialCB.addItem("")
        self.horizontalLayout_2.addWidget(self.materialCB)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.leftSideW)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.diamL = QtWidgets.QLabel(self.groupBox)
        self.diamL.setObjectName("diamL")
        self.gridLayout_2.addWidget(self.diamL, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.diametrLE = QtWidgets.QLineEdit(self.groupBox)
        self.diametrLE.setMinimumSize(QtCore.QSize(60, 0))
        self.diametrLE.setMaximumSize(QtCore.QSize(70, 16777215))
        self.diametrLE.setObjectName("diametrLE")
        self.gridLayout_2.addWidget(self.diametrLE, 0, 2, 1, 1)
        self.shagL = QtWidgets.QLabel(self.groupBox)
        self.shagL.setObjectName("shagL")
        self.gridLayout_2.addWidget(self.shagL, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 1, 1, 1)
        self.shagCB = QtWidgets.QComboBox(self.groupBox)
        self.shagCB.setMinimumSize(QtCore.QSize(60, 0))
        self.shagCB.setMaximumSize(QtCore.QSize(70, 16777215))
        self.shagCB.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.shagCB.setObjectName("shagCB")
        self.shagCB.addItem("")
        self.shagCB.addItem("")
        self.shagCB.addItem("")
        self.shagCB.addItem("")
        self.shagCB.addItem("")
        self.shagCB.addItem("")
        self.shagCB.addItem("")
        self.shagCB.addItem("")
        self.shagCB.addItem("")
        self.shagCB.addItem("")
        self.shagCB.addItem("")
        self.shagCB.addItem("")
        self.gridLayout_2.addWidget(self.shagCB, 1, 2, 1, 1)
        self.tochnL = QtWidgets.QLabel(self.groupBox)
        self.tochnL.setObjectName("tochnL")
        self.gridLayout_2.addWidget(self.tochnL, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 1, 1, 1)
        self.tochnCB = QtWidgets.QComboBox(self.groupBox)
        self.tochnCB.setMinimumSize(QtCore.QSize(60, 0))
        self.tochnCB.setMaximumSize(QtCore.QSize(70, 16777215))
        self.tochnCB.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.tochnCB.setObjectName("tochnCB")
        self.tochnCB.addItem("")
        self.tochnCB.addItem("")
        self.tochnCB.addItem("")
        self.tochnCB.addItem("")
        self.tochnCB.addItem("")
        self.gridLayout_2.addWidget(self.tochnCB, 2, 2, 1, 1)
        self.dlinaL = QtWidgets.QLabel(self.groupBox)
        self.dlinaL.setObjectName("dlinaL")
        self.gridLayout_2.addWidget(self.dlinaL, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 3, 1, 1, 1)
        self.dlinaLE = QtWidgets.QLineEdit(self.groupBox)
        self.dlinaLE.setMinimumSize(QtCore.QSize(60, 0))
        self.dlinaLE.setMaximumSize(QtCore.QSize(70, 16777215))
        self.dlinaLE.setObjectName("dlinaLE")
        self.gridLayout_2.addWidget(self.dlinaLE, 3, 2, 1, 1)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.groupBox)
        self.horizontalLayout.addWidget(self.leftSideW)
        self.rightSideW = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightSideW.sizePolicy().hasHeightForWidth())
        self.rightSideW.setSizePolicy(sizePolicy)
        self.rightSideW.setMinimumSize(QtCore.QSize(380, 0))
        self.rightSideW.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.rightSideW.setObjectName("rightSideW")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.rightSideW)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.webW = QtWidgets.QWidget(self.rightSideW)
        self.webW.setObjectName("webW")
        self.verticalLayout.addWidget(self.webW)
        self.obrabB = QtWidgets.QPushButton(self.rightSideW)
        self.obrabB.setMaximumSize(QtCore.QSize(120, 16777215))
        self.obrabB.setObjectName("obrabB")
        self.verticalLayout.addWidget(self.obrabB)
        self.horizontalLayout.addWidget(self.rightSideW)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.openSettingsAction = QtWidgets.QAction(MainWindow)
        self.openSettingsAction.setObjectName("openSettingsAction")
        self.saveSettingsAction = QtWidgets.QAction(MainWindow)
        self.saveSettingsAction.setObjectName("saveSettingsAction")
        self.saveAsSettingsAction = QtWidgets.QAction(MainWindow)
        self.saveAsSettingsAction.setObjectName("saveAsSettingsAction")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Вид отверстия"))
        self.otverCB.setCurrentText(_translate("MainWindow", "Глухое"))
        self.otverCB.setItemText(0, _translate("MainWindow", "Глухое"))
        self.otverCB.setItemText(1, _translate("MainWindow", "Сквозное"))
        self.calcB.setText(_translate("MainWindow", "Рассчитать"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Обрабатываемые материалы"))
        self.materialCB.setCurrentText(_translate("MainWindow", "Углеродистые конструкционные "))
        self.materialCB.setItemText(0, _translate("MainWindow", "Углеродистые конструкционные "))
        self.materialCB.setItemText(1, _translate("MainWindow", "Инструментальные "))
        self.materialCB.setItemText(2, _translate("MainWindow", "Хромистые, хромоникелевые, марганцовистые "))
        self.materialCB.setItemText(3, _translate("MainWindow", "Теплоустойчивые аустенитного, мартенситного и ферритного классов "))
        self.materialCB.setItemText(4, _translate("MainWindow", "Конструкционные легированные"))
        self.materialCB.setItemText(5, _translate("MainWindow", "Коррозионно-стойкие"))
        self.materialCB.setItemText(6, _translate("MainWindow", "Коррозионно-стойкие, жаростойкие "))
        self.materialCB.setItemText(7, _translate("MainWindow", "Жаропрочные, жаростойкие"))
        self.materialCB.setItemText(8, _translate("MainWindow", "Высокопрочные "))
        self.materialCB.setItemText(9, _translate("MainWindow", "Жаропрочные деформируемые на железоникелевой основе "))
        self.materialCB.setItemText(10, _translate("MainWindow", "Жаропрочные литейные"))
        self.materialCB.setItemText(11, _translate("MainWindow", "Титановые"))
        self.materialCB.setItemText(12, _translate("MainWindow", "Цветные типа алюминиевых, магниевых, медных"))
        self.materialCB.setItemText(13, _translate("MainWindow", "Чугуны всех марок"))
        self.groupBox.setTitle(_translate("MainWindow", "Параметры резьбы"))
        self.diamL.setText(_translate("MainWindow", "Диаметр"))
        self.diametrLE.setText(_translate("MainWindow", "0"))
        self.shagL.setText(_translate("MainWindow", "Шаг"))
        self.shagCB.setCurrentText(_translate("MainWindow", "0.35"))
        self.shagCB.setItemText(0, _translate("MainWindow", "0.35"))
        self.shagCB.setItemText(1, _translate("MainWindow", "0.4"))
        self.shagCB.setItemText(2, _translate("MainWindow", "0.45"))
        self.shagCB.setItemText(3, _translate("MainWindow", "0.5"))
        self.shagCB.setItemText(4, _translate("MainWindow", "0.75"))
        self.shagCB.setItemText(5, _translate("MainWindow", "0.8"))
        self.shagCB.setItemText(6, _translate("MainWindow", "1"))
        self.shagCB.setItemText(7, _translate("MainWindow", "1.25"))
        self.shagCB.setItemText(8, _translate("MainWindow", "1.5"))
        self.shagCB.setItemText(9, _translate("MainWindow", "2.5"))
        self.shagCB.setItemText(10, _translate("MainWindow", "3"))
        self.shagCB.setItemText(11, _translate("MainWindow", "3.5"))
        self.tochnL.setText(_translate("MainWindow", "Точность"))
        self.tochnCB.setCurrentText(_translate("MainWindow", "4"))
        self.tochnCB.setItemText(0, _translate("MainWindow", "4"))
        self.tochnCB.setItemText(1, _translate("MainWindow", "5"))
        self.tochnCB.setItemText(2, _translate("MainWindow", "6"))
        self.tochnCB.setItemText(3, _translate("MainWindow", "7"))
        self.tochnCB.setItemText(4, _translate("MainWindow", "8"))
        self.dlinaL.setText(_translate("MainWindow", "Длина"))
        self.dlinaLE.setText(_translate("MainWindow", "0"))
        self.obrabB.setText(_translate("MainWindow", "Условия обработки"))
        self.openSettingsAction.setText(_translate("MainWindow", "Открыть файл"))
        self.saveSettingsAction.setText(_translate("MainWindow", "Сохранить"))
        self.saveAsSettingsAction.setText(_translate("MainWindow", "Сохранить как"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

