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

        str += "<style>\n"\
                    "table {\n"\
                        "border-spacing: 1px 1px;\n"\
                        "width: 50;\n" \
                    "}\n"\
                    "td {\n"\
                        "padding: 0px;\n" \
                        "border: 1px double #333;" \
                    "}\n" \
               "</style>\n"

        str += "Диаметр отверстия под резьбу - {}\n".format(diam_otver)
        str += "<h3>Инструмент для обработки отверстия под резьбу</h3>\n"

        str += "<table>\n"
        str += "<tr>\n"

        str += "<td>\n"
        str += "<figure>\n" \
               "<img style=\"max-width: 160px; height: auto; \" src={} alt=\"my img\"/>\n"\
               "<figcaption> Сверло </figcaption>\n"\
               "</figure>\n".format(self.pic.get_sverlo())
        str += "</td>\n"

        str += "<td>"
        str += "<figure>\n" \
               "<img style=\"max-width: 160px; height: auto; \" src={} alt=\"my img\"/>\n" \
               "<figcaption> Зенкер </figcaption>\n" \
               "</figure>\n".format(self.pic.get_zenker())
        str += "</td>\n"

        str += "<td>\n"
        str += "<figure>\n" \
               "<img style=\"max-width: 110px; height: auto; \" src={} alt=\"my img\"/>\n" \
               "<figcaption> Развертка </figcaption>\n" \
               "</figure>\n".format(self.pic.get_razvertka())
        str += "</td>\n"

        str += "</tr>\n"
        str += "</table>\n"

        str += "<h3>Инструмент</h3>\n"
        str += "<figure>\n" \
               "<img style=\"max-width: 400px; height: auto; \" src={} alt=\"my img\"/>\n" \
               "<figcaption> Метчик </figcaption>\n" \
               "</figure>\n".format(self.pic.get_metchik())

        str += "</body>\n"\
               "</html>"

#         str = ''' <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="UTF-8">
#     <title></title>
#     <style >
#     table {
#         border: 4px double #333; /* Рамка вокруг таблицы */
#         border-collapse: separate; /* Способ отображения границы */
#         width: 25; /* Ширина таблицы */
#         border-spacing: 1px 2px; /* Расстояние между ячейками */
#    }
#    td {
#     padding: 1px; /* Поля вокруг текста */
#     border: 1px solid #a52a2a; /* Граница вокруг ячеек */
#    }
#     </style>
# </head>
# <body>
#     <table>
#         <tr>
#             <td>1</td><td>2</td>
#         </tr>
#         <tr>
#             <td>3</td><td>4</td>
#         </tr>
#     </table>
# </body>
# </html>'''


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
        return os.getcwd() + self.folder + self.patron

    def get_razvertka(self):
        return os.getcwd() + self.folder + self.razvertka

    def get_sverlo(self):
        return os.getcwd() + self.folder + self.sverlo

    def get_zenker(self):
        return os.getcwd() + self.folder + self.zenker