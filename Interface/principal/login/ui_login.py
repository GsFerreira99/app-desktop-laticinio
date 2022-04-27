# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginRnpvFe.ui'
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
        Form.resize(900, 610)
        Form.setMinimumSize(QSize(900, 610))
        Form.setMaximumSize(QSize(900, 610))
        Form.setStyleSheet(u"QWidget {\n"
"	background-color: #ECF2FD;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"image: url(:/newPrefix/Logo-Limpa.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"\n"
"\n"
"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background: #E7E7E7;\n"
"	border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(60, -1, 60, -1)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Raleway")
        font.setPointSize(43)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"margin-bottom: 50px;\n"
"margin-top: 50px")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_msg = QLabel(self.frame)
        self.label_msg.setObjectName(u"label_msg")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_msg.sizePolicy().hasHeightForWidth())
        self.label_msg.setSizePolicy(sizePolicy1)
        self.label_msg.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamily(u"Raleway")
        font1.setPointSize(9)
        self.label_msg.setFont(font1)
        self.label_msg.setStyleSheet(u"    border: 1px solid;\n"
"    border-radius: 5px;\n"
"    color: #721c24;\n"
"    background-color: #f8d7da;\n"
"    border-color: #f5c6cb;")
        self.label_msg.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_msg)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(0, 250))
        self.frame_3.setMaximumSize(QSize(16777215, 400))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamily(u"Raleway")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        font2.setKerning(True)
        self.label_2.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_2)

        self.input_usuario = QLineEdit(self.frame_3)
        self.input_usuario.setObjectName(u"input_usuario")
        self.input_usuario.setMaximumSize(QSize(16777215, 40))
        self.input_usuario.setFont(font1)
        self.input_usuario.setStyleSheet(u"padding-left: 20px")

        self.verticalLayout_2.addWidget(self.input_usuario)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamily(u"Raleway")
        font3.setPointSize(11)
        self.label_3.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_3)

        self.input_senha = QLineEdit(self.frame_3)
        self.input_senha.setObjectName(u"input_senha")
        self.input_senha.setMaximumSize(QSize(16777215, 40))
        self.input_senha.setFont(font1)
        self.input_senha.setStyleSheet(u"padding-left: 20px")
        self.input_senha.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.input_senha)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.btn_entrar = QPushButton(self.frame_3)
        self.btn_entrar.setObjectName(u"btn_entrar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_entrar.sizePolicy().hasHeightForWidth())
        self.btn_entrar.setSizePolicy(sizePolicy2)
        self.btn_entrar.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamily(u"Raleway")
        font4.setPointSize(10)
        self.btn_entrar.setFont(font4)
        self.btn_entrar.setStyleSheet(u"QPushButton {\n"
"	background: #000920;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: rgb(0, 23, 81);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_entrar)


        self.verticalLayout.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label_msg.setText(QCoreApplication.translate("Form", u"Usuario ou senha incorretos", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Usuario", None))
        self.input_usuario.setPlaceholderText(QCoreApplication.translate("Form", u"insira o usuario", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Senha", None))
        self.input_senha.setPlaceholderText(QCoreApplication.translate("Form", u"insira a senha", None))
        self.label_4.setText("")
        self.btn_entrar.setText(QCoreApplication.translate("Form", u"Entrar", None))
    # retranslateUi

