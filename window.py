from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

import easygui

from core import *

import os

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(601, 424)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 2, 1, 1, 1)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.webview = QWebEngineView(self.tab)
        self.webview.setObjectName(u"webview")
        self.webview.setUrl(QUrl("https://glowman554.github.io"))

        self.gridLayout.addWidget(self.webview, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.server_ip = QLineEdit(self.groupBox)
        self.server_ip.setObjectName(u"server_ip")
        self.server_ip.setEnabled(False)
        self.server_ip.setReadOnly(False)

        self.verticalLayout.addWidget(self.server_ip)

        self.server_port = QLineEdit(self.groupBox)
        self.server_port.setObjectName(u"server_port")
        self.server_port.setEnabled(False)
        self.server_port.setReadOnly(False)

        self.verticalLayout.addWidget(self.server_port)

        self.online_mode = QCheckBox(self.groupBox)
        self.online_mode.setObjectName(u"online_mode")

        self.verticalLayout.addWidget(self.online_mode)

        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 3)

        self.username = QLineEdit(Form)
        self.username.setObjectName(u"username")

        self.gridLayout_2.addWidget(self.username, 2, 0, 1, 1)

        self.launch_button = QPushButton(Form)
        self.launch_button.setObjectName(u"launch_button")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.launch_button.setFont(font)

        self.launch_button.clicked.connect(self.launch_game)

        self.gridLayout_2.addWidget(self.launch_button, 2, 2, 1, 1)

        self.retranslateUi(Form)
        self.online_mode.clicked.connect(self.server_port.setEnabled)
        self.online_mode.clicked.connect(self.server_ip.setEnabled)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Form)
        self.on_start()


    def on_start(self):

        if(os.path.isfile("user.json")):
            self.username.setText(load_username())

        if(os.path.isfile("server.json")):
            self.server_ip.setText(load_server()["host"])
            self.server_port.setText(load_server()["port"])

    def launch_game(self, Form):
        if(self.username.text() != ""):

            save_user_name(self.username.text())

            if(self.online_mode.isChecked()):
                if(self.server_ip.text() != "" and self.server_port.text() != ""):
                    save_server(self.server_ip.text(), self.server_port.text(), self.online_mode.isChecked())
                    print("LAUNCHING ONLINE MODE")
                    launch_game_server(self.username.text(), self.server_ip.text(), self.server_port.text())
                else:
                    easygui.msgbox("Please set server ip and port", "Launcher")
            else:
                print("LAUNCHING OFFLINE MODE")
                launch_game(self.username.text())
        else:
            easygui.msgbox("Please set username", "Launcher")


    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Main", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Server Settings", None))
        self.server_ip.setPlaceholderText(QCoreApplication.translate("Form", u"Server IP", None))
        self.server_port.setPlaceholderText(QCoreApplication.translate("Form", u"Server Port", None))
        self.online_mode.setText(QCoreApplication.translate("Form", u"Online Modus", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QCoreApplication.translate("Form", u"Settings", None))
        self.username.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.launch_button.setText(QCoreApplication.translate("Form", u"Launch", None))
    # retranslateUi
