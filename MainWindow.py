from Ui_MainWindow import *
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QScrollArea, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
import os
import io

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        layout = QHBoxLayout(self.webW)
        self.web = QWebEngineView()
        self.web.setMinimumWidth(575)
        self.web.setMaximumWidth(600)
        scroll = QScrollArea()
        scroll.setWidget(self.web)
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        layout.addWidget(scroll)

        self.pic = Pictures()

        self.calc_clicked = False
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
                        "width: 50;\n" \
                    "}\n"\
                    "td {\n"\
                        "padding: 0px;\n" \
                        "border: 1px double #333;" \
                    "}\n" \
               "</style>\n"

        str += "Диаметр отверстия под резьбу - {}<br>\n".format(diam_otver)
        str += "Точность – 6Н. Вид обработки - получистовой.\n"
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

        if photo_count == 3:
            str += "<td>\n"
            str += "<figure>\n" \
                   "<img style=\"max-width: 110px; height: auto; \" src={} alt=\"my img\"/>\n" \
                   "<figcaption> Развертка </figcaption>\n" \
                   "</figure>\n".format(self.pic.get_razvertka())
            str += "</td>\n"

        str += "</tr>\n"
        str += "</table>\n"

        str += "<h3>Инструмент для нарезания резьбы</h3>\n"
        str += "<figure>\n" \
               "<img style=\"max-width: 400px; height: auto; \" src={} alt=\"my img\"/>\n" \
               "<figcaption> Метчик </figcaption>\n" \
               "</figure>\n".format(self.pic.get_metchik())

        str += "<h5>Характеристики инструмента</h5>\n"
        str += "<img style=\"max-width: 500px; height: auto; \" src={} alt=\"my img\"/>\n"\
            .format(self.pic.get_table())
        str += "<ul>"\
                   "<li>Покрытие-DLC</li>"\
                   "<li>Порошковая быстрорежущая сталь</li>"\
                   "<li>Прямые канавки с подточкой центра</li>"\
               "</ul>"
        str += "Рекомендуемая конструкция метчика:"
        str += "</body>\n"\
               "</html>"
        print(str)
        return str


    def on_calcB(self):
        self.calc_clicked = True
        str = self.createWebPage(0, 2)
        self.file_name = "test.html"
        with io.open(self.file_name, 'w', encoding="utf-8") as f:
            f.write(str)
        self.web.load(QtCore.QUrl(os.path.abspath(self.file_name)))


    def on_obrabB(self):
        if not self.calc_clicked:
            QMessageBox.warning(self, "Сообщение", "Сначала нажмите кнопку рассчитать")
            return

        str = "<html>\n"\
              "<meta charset=\"UTF-8\">\n"\
              "<body>\n"

        str += "<style>\n"\
                    "table {\n"\
                        "width: 100;\n" \
                    "}\n"\
                    "td {\n"\
                        "padding: 0px;\n" \
                        "border: 1px double #333;" \
                    "}\n" \
               "</style>\n"

        str += "<h3>Режимы резания</h3>\n"
        str += "<table>\n"

        str += "<tr>\n"
        str += "<td>Стойкость инструмента, ч</td>\n"
        str += "<td>Подача, мм</td>\n"
        str += "<td>Скорость резания, м/мин</td>\n"
        str += "</tr>\n"

        str += "<tr>\n"
        str += "<td>30</td>\n"
        str += "<td>0,5</td>\n"
        str += "<td>6,96</td>\n"
        str += "</tr>\n"

        str += "</table>\n"
        str += "<h3>Вид патрона</h3>\n"
        str += "<figure>\n" \
               "<img style=\"max-width: 300px; height: auto; \" src={} alt=\"my img\"/>\n" \
               "<figcaption> Быстросменные патроны с безопасной фрикционной муфтой: для глухих отверстий. </figcaption>\n" \
               "</figure>\n".format(self.pic.get_patron())
        str += "<h3>Вид СОЖ</h3>\n"
        str += "ECOCOOL AL Plus."
        str += "</body>\n"\
               "</html>"

        self.file_name_window = "test_window.html"
        with io.open(self.file_name_window, 'w', encoding="utf-8") as f:
            f.write(str)

        self.window = QWebEngineView()
        self.window.load(QtCore.QUrl(os.path.abspath(self.file_name_window)))
        self.window.show()

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

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.file_name)
        os.remove(self.file_name_window)

class Pictures():
    def __init__(self):
        self.folder = "\Pictures\\"
        self.metchik = "metchik.jpg"
        self.patron = "patron.jpg"
        self.razvertka = "razvertka.jpg"
        self.sverlo = "sverlo.jpg"
        self.zenker = "zenker.jpg"
        self.table = "table.jpg"

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

    def get_table(self):
        return os.getcwd() + self.folder + self.table