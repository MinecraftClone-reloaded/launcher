from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


import window
import core

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = window.Ui_Form()
    ui.setupUi(Form)
    Form.setWindowTitle("MinecraftClone Launcher")
    Form.showMaximized()
    #Form.show()

    sys.exit(app.exec_())
