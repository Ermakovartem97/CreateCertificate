import sys
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QGridLayout, QLineEdit, QRadioButton, \
    QDesktopWidget, QCompleter


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.new_img = "temp/new.jpg"
        self.initUI()

    def initUI(self):
        self.screen = QDesktopWidget().screenGeometry()
        # Первоначальные настройки
        self.setGeometry(0, 0, self.screen.width(), self.screen.height())
        self.showMaximized()
        self.setWindowTitle('Sertificat')

        # создаем рабочую область
        grid = QGridLayout()
        grid.setSpacing(10)

        self.imgWidth = int(self.screen.width() - self.screen.width() / 4)
        self.imgHeight = self.screen.height()

        # Пустой сертификат
        self.img = Image.open("image/first.jpg").resize((self.imgWidth, self.imgHeight))
        self.img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.image = QLabel(self)
        self.image.setPixmap(self.pixmap)

        grid.addWidget(self.image, 0, 0, 10, 1)

        # Выбор шаблона сертификата
        self.template = 0
        self.rbt0 = QRadioButton("Образец 1")
        self.rbt0.setChecked(True)
        self.rbt1 = QRadioButton("Образец 2")
        grid.addWidget(self.rbt0, 1, 1)
        grid.addWidget(self.rbt1, 1, 2)
        # radioBtn = self.sender()

        # Метка (Код)
        self.lbl_code = QLabel(text="Номер")
        grid.addWidget(self.lbl_code, 2, 1)
        # Поле ввода текста (Код)
        self.ent_code = QLineEdit()
        grid.addWidget(self.ent_code, 2, 2, 1, 4)

        # Метка (Имя)
        self.lbl_name = QLabel(text="Имя")
        grid.addWidget(self.lbl_name, 3, 1)
        # Поле ввода текста (Имя)
        self.ent_name = QLineEdit()
        grid.addWidget(self.ent_name, 3, 2, 1, 4)

        # Метка (Процедура1)
        self.lbl_pro1 = QLabel(text="Процедура")
        grid.addWidget(self.lbl_pro1, 4, 1)
        # Поле ввода текста (Процедура1)
        self.ent_pro1 = QLineEdit()

        pro1List = ['SPA Комплекс', 'SPA Комплекс 2']
        completer = QCompleter(pro1List, self.ent_pro1)
        self.ent_pro1.setCompleter(completer)

        grid.addWidget(self.ent_pro1, 4, 2, 1, 4)

        # Метка (Процедура2)
        self.lbl_pro2 = QLabel(text="Доплнение")
        grid.addWidget(self.lbl_pro2, 5, 1)
        # Поле ввода текста (Процедура2)
        self.ent_pro2 = QLineEdit()

        pro2List = ['Классика на двоих', 'Еще что-нибудь']
        completer = QCompleter(pro2List, self.ent_pro1)
        self.ent_pro2.setCompleter(completer)

        grid.addWidget(self.ent_pro2, 5, 2, 1, 4)

        # Метка (Дата)
        self.lbl_date = QLabel(text="Дата")
        grid.addWidget(self.lbl_date, 6, 1)
        # Фрейм ввода текста (Дата)

        # Создание даты
        self.lbl_dateEnd = QLabel(text=datetime.now().strftime("%d.%m.%Y"))
        grid.addWidget(self.lbl_dateEnd, 6, 2)
        self.ent_dateDel = QLineEdit()
        grid.addWidget(self.ent_dateDel, 6, 3, 1, 3)

        # Кнопка обновить
        button = QPushButton('Обновить', self)
        button.clicked.connect(self.but_upgrade)
        grid.addWidget(button, 7, 1, 1, 5)

        # Кнопка сохранить
        button = QPushButton('Сохранить', self)
        button.clicked.connect(self.but_save)
        grid.addWidget(button, 8, 1, 1, 5)

        self.ent_code.editingFinished.connect(self.but_upgrade)
        self.ent_name.editingFinished.connect(self.but_upgrade)
        self.ent_pro1.editingFinished.connect(self.but_upgrade)
        self.ent_pro2.editingFinished.connect(self.but_upgrade)
        self.ent_dateDel.editingFinished.connect(self.but_upgrade)

        self.setLayout(grid)
        self.show()

    def change_data(self):
        today = datetime.now()
        if len(self.ent_dateDel.text()) == 0 or not (self.ent_dateDel.text().isdigit()):
            self.ent_dateDel.setText("0")

        if (today.month + int(self.ent_dateDel.text())) // 12:
            yearDelta = 1
        else:
            yearDelta = 0
        dateEnd = str(today.day) + '.' + str((today.month + int(self.ent_dateDel.text())) % 12).zfill(2) + '.' + str(
            today.year + yearDelta)

        return dateEnd

    def but_save(self):
        path = str(
            "C:\\Users\\zdrav\\Desktop\\ПС, АБ, карты\\Подарочные сертификаты электронные\\готовые подарочные\\") + \
               str(datetime.now().strftime("%d.%m.%Y")) + ' ' + str(self.ent_name.text()) + '.jpg'
        self.img.save(path)

    def but_upgrade(self):

        if self.rbt0.isChecked():
            self.img = Image.open("image/first.jpg").resize((self.imgWidth, self.imgHeight))

            writeCodeX = self.imgWidth * 0.81
            writeCodeY = self.imgHeight * 0.15
            writeCodeColor = '#033'

            writeNameX = self.imgWidth * 0.56
            writeNameY = self.imgHeight * 0.56
            writeNameColor = '#009D91'

            writePro1X = self.imgWidth * 0.61
            writePro1Y = self.imgHeight * 0.62
            writePro1Color = '#009D91'

            writePro2X = self.imgWidth * 0.49
            writePro2Y = self.imgHeight * 0.67
            writePro2Color = '#009D91'

            writeDateX = self.imgWidth * 0.54
            writeDateY = self.imgHeight * 0.72
            writeDateColor = '#033'

            font1 = ImageFont.truetype("font/Appetite_Medium.otf", 40)
            font2 = ImageFont.truetype("font/arial_bold.ttf", 25)

        else:
            self.img = Image.open("image/second.jpg").resize((self.imgWidth, self.imgHeight))

            writeCodeX = self.imgWidth * 0.837
            writeCodeY = self.imgHeight * 0.13
            writeCodeColor = '#333'

            writeNameX = self.imgWidth * 0.57
            writeNameY = self.imgHeight * 0.475
            writeNameColor = '#654321'

            writePro1X = self.imgWidth * 0.63
            writePro1Y = self.imgHeight * 0.535
            writePro1Color = '#654321'

            writePro2X = self.imgWidth * 0.51
            writePro2Y = self.imgHeight * 0.585
            writePro2Color = '#654321'

            writeDateX = self.imgWidth * 0.59
            writeDateY = self.imgHeight * 0.64
            writeDateColor = '#033'

            font1 = ImageFont.truetype("font/Appetite_Medium.otf", 40)
            font2 = ImageFont.truetype("font/arial_bold.ttf", 25)

        # Код
        writeCode = ImageDraw.Draw(self.img)
        writeCode.text((writeCodeX, writeCodeY), self.ent_code.text(), font=font2, fill=writeCodeColor, anchor="ms")

        # Имя
        writeName = ImageDraw.Draw(self.img)
        writeName.text((writeNameX, writeNameY), self.ent_name.text(), font=font1, fill=writeNameColor, anchor="ms")

        # Процедура 1
        writePro1 = ImageDraw.Draw(self.img)
        writePro1.text((writePro1X, writePro1Y), self.ent_pro1.text(), font=font1, fill=writePro1Color, anchor="ms")

        # Процедура 2
        writePro2 = ImageDraw.Draw(self.img)
        writePro2.text((writePro2X, writePro2Y), self.ent_pro2.text(), font=font1, fill=writePro2Color, anchor="ms")

        # Дата
        writeDate = ImageDraw.Draw(self.img)
        writeDate.text((writeDateX, writeDateY), self.change_data(), font=font2, fill=writeDateColor, anchor="ms")

        # Показ фото
        self.img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = Example()
    sys.exit(app.exec_())
