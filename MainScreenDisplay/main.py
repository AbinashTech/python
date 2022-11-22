import os
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUiType

FROM_MAIN, _ = loadUiType(os.path.join(os.path.dirname(__file__), "MainScreen.ui"))
FROM_SETTINGS, _ = loadUiType(os.path.join(os.path.dirname(__file__), "settingscreen.ui"))


class Settings(QMainWindow, FROM_SETTINGS):
    def __init__(self, parent=None):
        super(Settings, self).__init__(parent)
        self.setupUi(self)
        pixmap = QPixmap("settingscreen.png")
        self.SettingScreen_Image.setPixmap(pixmap.scaled(800, 480))


class Main(QMainWindow, FROM_MAIN):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        pixmap = QPixmap("Mainscreen.png")
        self.bgMainScreen.setPixmap(pixmap.scaled(800, 480))
        self.btnSettings.clicked.connect(self.on_click_setting)

    def on_click_setting(self):
        self.hide()
        settings = Settings(self)
        settings.show()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    try:
        main()
    except Exception as why:
        print(why)
