from Ui_MainWindow import *
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
import os
import io

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)



        self.web = QWebEngineView(self.webW)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.web.sizePolicy().hasHeightForWidth())
        self.web.setSizePolicy(sizePolicy)

        hbox = QHBoxLayout()
        hbox.addWidget(self.web)
        QWebEngineSettings.globalSettings().setAttribute(
            QWebEngineSettings.PluginsEnabled, True)

        self.pic = Pictures()

        self.calcB.clicked.connect(self.on_calcB)
        self.obrabB.clicked.connect(self.on_obrabB)
        self.materialCB.activated.connect(self.on_materialCB)
        self.diametrLE.editingFinished.connect(self.on_diametrLE)
        self.shagCB.activated.connect(self.on_shagCB)
        self.tochnCB.activated.connect(self.on_tochnCB)
        self.otverCB.activated.connect(self.on_otverCB)

    def createWebPage(self, diam_otver, photo_count):


        str = "<html>\n"\
              "<meta charset=\"UTF-8\">\n"\
              "<body>\n"

        str += "Диаметр отверстия под резьбу - {}\n".format(diam_otver)
        str += "<h3>Инструмент для обработки отверстия под резьбу</h3>\n"
        str += "<figure>\n" \
               "<img src={} alt=\"my img\"/>\n"\
               "<figcaption> Подпись 1 </figcaption>\n"\
               "</figure>\n".format(self.pic.get_metchik())

        str += "<body>\n"\
               "<html>"

        print(str)
        with io.open("test.html", 'w', encoding="utf-8") as f:
            f.write(str)
        return "test.html"


    def on_calcB(self):
        fileName = self.createWebPage(0, 2)
        self.web.load(QtCore.QUrl(os.path.abspath(fileName)))


    def on_obrabB(self):
        pass

    def on_materialCB(self):
        pass

    def on_diametrLE(self):
        pass

    def on_shagCB(self):
        pass

    def on_tochnCB(self):
        pass

    def on_otverCB(self):
        pass

class Pictures():
    def __init__(self):
        self.folder = "\Pictures\\"
        self.metchik = "metchik.jpg"
        self.patron = "patron.jpg"
        self.razvertka = "razvertka.jpg"
        self.sverlo = "sverlo.jpg"
        self.zenker = "zenker.jpg"

    def get_metchik(self):
        return os.getcwd() + self.folder + self.metchik

    def get_patron(self):
        return self.folder + self.patron

    def get_razvertka(self):
        return self.folder + self.razvertka

    def get_sverlo(self):
        return self.folder + self.sverlo

    def get_zenker(self):
        return self.folder + self.zenker