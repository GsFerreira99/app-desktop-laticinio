# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BasexchJWS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import media.resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1222, 637)
        Form.setStyleSheet(u"QWidget {\n"
"	background-color: #ECF2FD;\n"
"}\n"
"\n"
"")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background-color: #000920;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMinimumSize(QSize(50, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_toogle = QPushButton(self.frame_4)
        self.btn_toogle.setObjectName(u"btn_toogle")
        self.btn_toogle.setMinimumSize(QSize(50, 40))
        self.btn_toogle.setMaximumSize(QSize(50, 40))
        self.btn_toogle.setStyleSheet(u"QPushButton {\n"
"	image: url(:/newPrefix/toggle_button.png);\n"
"	padding: 3px\n"
"}\n"
"QPushButton:hover {\n"
"	padding: 0;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_toogle)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_notfy = QPushButton(self.frame_7)
        self.btn_notfy.setObjectName(u"btn_notfy")
        self.btn_notfy.setMinimumSize(QSize(50, 40))
        self.btn_notfy.setMaximumSize(QSize(50, 40))
        self.btn_notfy.setStyleSheet(u"QPushButton {\n"
"	image: url(:/newPrefix/sino.png);\n"
"	padding: 7px\n"
"}\n"
"QPushButton:hover {\n"
"	padding: 0;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_notfy)

        self.pushButton_3 = QPushButton(self.frame_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(50, 40))
        self.pushButton_3.setMaximumSize(QSize(50, 40))
        self.pushButton_3.setStyleSheet(u"image: url(:/newPrefix/user.png)")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"color: white;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 8, 0, 8)
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamily(u"Raleway")
        font.setPointSize(9)
        self.label_3.setFont(font)

        self.verticalLayout_5.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setFamily(u"Raleway")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_2.addWidget(self.frame_8)


        self.horizontalLayout.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.label_titulo = QLabel(self.frame)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setMinimumSize(QSize(0, 50))
        self.label_titulo.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setFamily(u"Raleway")
        font2.setPointSize(15)
        self.label_titulo.setFont(font2)
        self.label_titulo.setStyleSheet(u"color: white;\n"
"padding-left: 40px;")

        self.verticalLayout_4.addWidget(self.label_titulo)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.menu_lateral = QFrame(Form)
        self.menu_lateral.setObjectName(u"menu_lateral")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.menu_lateral.sizePolicy().hasHeightForWidth())
        self.menu_lateral.setSizePolicy(sizePolicy2)
        self.menu_lateral.setMinimumSize(QSize(0, 0))
        self.menu_lateral.setMaximumSize(QSize(200, 16777215))
        self.menu_lateral.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-right: 1px solid rgb(183, 182, 202)")
        self.menu_lateral.setFrameShape(QFrame.StyledPanel)
        self.menu_lateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.menu_lateral)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.menu_lateral)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 100))
        self.btn_home.setMaximumSize(QSize(16777215, 150))
        self.btn_home.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	image: url(:/newPrefix/Logo-Limpa.png);\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 9px;\n"
"}")

        self.verticalLayout.addWidget(self.btn_home)

        self.frame_5 = QFrame(self.menu_lateral)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"border:none")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_producao = QPushButton(self.frame_5)
        self.btn_producao.setObjectName(u"btn_producao")
        self.btn_producao.setMinimumSize(QSize(0, 30))
        font3 = QFont()
        font3.setFamily(u"Raleway")
        font3.setPointSize(8)
        self.btn_producao.setFont(font3)
        self.btn_producao.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	border-bottom: 2px solid rgb(236, 242, 253)\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(243, 243, 243)\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_producao)

        self.btn_recebimento = QPushButton(self.frame_5)
        self.btn_recebimento.setObjectName(u"btn_recebimento")
        self.btn_recebimento.setMinimumSize(QSize(0, 30))
        self.btn_recebimento.setFont(font3)
        self.btn_recebimento.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	border-bottom: 2px solid rgb(236, 242, 253)\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(243, 243, 243)\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_recebimento)


        self.verticalLayout.addWidget(self.frame_5, 0, Qt.AlignTop)


        self.gridLayout.addWidget(self.menu_lateral, 0, 0, 2, 1)

        self.conteudo_principal = QFrame(Form)
        self.conteudo_principal.setObjectName(u"conteudo_principal")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.conteudo_principal.sizePolicy().hasHeightForWidth())
        self.conteudo_principal.setSizePolicy(sizePolicy3)
        self.conteudo_principal.setStyleSheet(u"background-color: #ECF2FD;\n"
"border: none;")
        self.conteudo_principal.setFrameShape(QFrame.StyledPanel)
        self.conteudo_principal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.conteudo_principal)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.navWidget = QStackedWidget(self.conteudo_principal)
        self.navWidget.setObjectName(u"navWidget")

        self.horizontalLayout_3.addWidget(self.navWidget)


        self.gridLayout.addWidget(self.conteudo_principal, 1, 1, 1, 1)

        self.frame.raise_()
        self.menu_lateral.raise_()
        self.conteudo_principal.raise_()

        self.retranslateUi(Form)

        self.navWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_toogle.setText("")
        self.btn_notfy.setText("")
        self.pushButton_3.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Nome Completo", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Fun\u00e7\u00e3o", None))
        self.label_titulo.setText(QCoreApplication.translate("Form", u"Home", None))
        self.btn_home.setText("")
        self.btn_producao.setText(QCoreApplication.translate("Form", u"Produ\u00e7\u00e3o Di\u00e1ria", None))
        self.btn_recebimento.setText(QCoreApplication.translate("Form", u"Recebimento Leite", None))
    # retranslateUi

