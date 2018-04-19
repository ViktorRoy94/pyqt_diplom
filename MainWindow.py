from Ui_MainWindow import *
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QScrollArea, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os
import io


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        layout = QHBoxLayout()
        self.web = QWebEngineView()
        scroll = QScrollArea()
        scroll.setWidget(self.web)
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        layout.addWidget(scroll)
        self.webW.setLayout(layout)

        self.window = QWebEngineView()
        self.window.setMinimumWidth(500)
        self.window.setMaximumWidth(600)

        self.pic = Pictures()
        self.file_name = "test.html"
        self.file_name_window = "test_window.html"

        self.calc_clicked = False
        self.calcB.clicked.connect(self.on_calc_b)
        self.obrabB.clicked.connect(self.on_obrab_b)

        self.shag_diam = {0.35: -0.379, 0.4: -0.433, 0.45: -0.487, 0.5: -0.541,
                          0.75: -0.812, 0.8: -0.866, 1: -1.083, 1.25: -1.353,
                          1.5: -1.624, 2.5: -3.706, 3: 3.248, 3.5: -3.789}
        self.tochn = {4: "чистовой", 5: "чистовой", 6: "получистовой",
                      7: "черновой", 8: "черновой"}

    def create_web_page(self, diam_otver, photo_count, tochn, vid_obrab):

        html_str = "<html>\n" \
              "<meta charset=\"UTF-8\">\n" \
              "<body>\n"

        html_str += "<style>\n" \
               "td {\n" \
               "padding: 0px;\n" \
               "border: 1px double #333;" \
               "}\n" \
               "</style>\n"

        html_str += "Диаметр отверстия под резьбу - {}<br>\n".format(diam_otver)
        html_str += "Точность – {}Н. Вид обработки - {}.\n".format(tochn, vid_obrab)
        html_str += "<h3>Инструмент для обработки отверстия под резьбу</h3>\n"

        html_str += "<table>\n"
        html_str += "<tr>\n"

        html_str += "<td>\n"
        html_str += "<figure>\n" \
               "<img style=\"max-width: 160px; height: auto; \" src={} " \
               "alt=\"my img\"/>\n" \
               "<figcaption> Сверло </figcaption>\n" \
               "</figure>\n".format(self.pic.get_sverlo())
        html_str += "</td>\n"

        html_str += "<td>"
        html_str += "<figure>\n" \
               "<img style=\"max-width: 160px; height: auto; \" src={} " \
               "alt=\"my img\"/>\n" \
               "<figcaption> Зенкер </figcaption>\n" \
               "</figure>\n".format(self.pic.get_zenker())
        html_str += "</td>\n"

        if photo_count == 3:
            html_str += "<td>\n"
            html_str += "<figure>\n" \
                   "<img style=\"max-width: 110px; height: auto; \" src={} " \
                   "alt=\"my img\"/>\n" \
                   "<figcaption> Развертка </figcaption>\n" \
                   "</figure>\n".format(self.pic.get_razvertka())
            html_str += "</td>\n"

        html_str += "</tr>\n"
        html_str += "</table>\n"

        html_str += "<h3>Инструмент для нарезания резьбы</h3>\n"
        html_str += "<figure>\n" \
               "<img style=\"max-width: 400px; height: auto; \" src={} " \
               "alt=\"my img\"/>\n" \
               "<figcaption> Метчик </figcaption>\n" \
               "</figure>\n".format(self.pic.get_metchik())

        html_str += "<h5>Характеристики инструмента</h5>\n"
        html_str += "<img style=\"max-width: 500px; height: auto; \" src={} " \
               "alt=\"my img\"/>\n".format(self.pic.get_table())
        html_str += "<ul>" \
               "<li>Покрытие-DLC</li>" \
               "<li>Порошковая быстрорежущая сталь</li>" \
               "<li>Прямые канавки с подточкой центра</li>" \
               "</ul>"
        html_str += "Рекомендуемая конструкция метчика:"
        html_str += "</body>\n" \
               "</html>"
        return html_str

    def on_calc_b(self):
        self.web.setHtml("")
        self.calc_clicked = True

        diam = self.get_diam_otver()
        if diam is None:
            return
        tochn = self.tochnCB.currentText()
        vid_obrab = self.tochn[int(tochn)]
        str = self.create_web_page(diam, 3, tochn, vid_obrab)

        with io.open(self.file_name, 'w', encoding="utf-8") as f:
            f.write(str)
        self.web.load(QtCore.QUrl(os.path.abspath(self.file_name)))

    def on_obrab_b(self):
        if not self.calc_clicked:
            QMessageBox.warning(self, "Сообщение",
                                "Сначала нажмите кнопку рассчитать")
            return

        html_str = "<html>\n" \
              "<meta charset=\"UTF-8\">\n" \
              "<body>\n"

        html_str += "<style>\n" \
               "table {\n" \
               "width: 60%;\n" \
               "}\n" \
               "td {\n" \
               "padding: 6px;\n" \
               "border: 1px double #333;" \
               "}\n" \
               "</style>\n"

        html_str += "<h3>Режимы резания</h3>\n"
        html_str += "<table>\n"

        html_str += "<tr>\n"
        html_str += "<td>Стойкость инструмента, ч</td>\n"
        html_str += "<td>Подача, мм</td>\n"
        html_str += "<td>Скорость резания, м/мин</td>\n"
        html_str += "</tr>\n"

        html_str += "<tr>\n"
        html_str += "<td>30</td>\n"
        html_str += "<td>0,5</td>\n"
        html_str += "<td>6,96</td>\n"
        html_str += "</tr>\n"

        html_str += "</table>\n"
        html_str += "<h3>Вид патрона</h3>\n"
        html_str += "<figure>\n" \
               "<img style=\"max-width: 300px; height: auto; \" src={} " \
               "alt=\"my img\"/>\n" \
               "<figcaption> Быстросменные патроны с безопасной фрикционной" \
               "муфтой: для глухих отверстий. </figcaption>\n" \
               "</figure>\n".format(self.pic.get_patron())
        html_str += "<h3>Вид СОЖ</h3>\n"
        html_str += "ECOCOOL AL Plus."
        html_str += "</body>\n" \
               "</html>"

        with io.open(self.file_name_window, 'w', encoding="utf-8") as f:
            f.write(html_str)

        self.window.load(QtCore.QUrl(os.path.abspath(self.file_name_window)))
        self.window.show()

    def get_diam_otver(self):
        try:
            diam = float(self.diametrLE.text())
            shag = float(self.shagCB.currentText())
            diam = self.shag_diam[shag] + diam
            return round(diam, 3)
        except ValueError:
            QMessageBox.warning(self, "Ошибка",
                                "Диаметр отверстия задан неправильно")

    def closeEvent(self, *args, **kwargs):
        os.remove(self.file_name)
        os.remove(self.file_name_window)


class Pictures:
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
