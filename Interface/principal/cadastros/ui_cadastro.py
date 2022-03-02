# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastrotUNRtU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1311, 832)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"background-color: rgb(130, 130, 130);")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(-1, -1, -1, 9)
        self.nav_bar = QFrame(Form)
        self.nav_bar.setObjectName(u"nav_bar")
        self.nav_bar.setMinimumSize(QSize(0, 40))
        self.nav_bar.setMaximumSize(QSize(16777215, 40))
        self.nav_bar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(97, 157, 58);\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	color: white;\n"
"	font: 13pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(107, 172, 63)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(89, 143, 53)\n"
"}")
        self.nav_bar.setFrameShape(QFrame.StyledPanel)
        self.nav_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.nav_bar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 0, 0, 0)
        self.clientes_2 = QPushButton(self.nav_bar)
        self.clientes_2.setObjectName(u"clientes_2")
        self.clientes_2.setMinimumSize(QSize(150, 40))
        self.clientes_2.setMaximumSize(QSize(150, 40))
        self.clientes_2.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.clientes_2)

        self.fornecedores = QPushButton(self.nav_bar)
        self.fornecedores.setObjectName(u"fornecedores")
        self.fornecedores.setMinimumSize(QSize(150, 40))
        self.fornecedores.setMaximumSize(QSize(150, 40))

        self.horizontalLayout.addWidget(self.fornecedores)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.nav_bar, 0, 0, 1, 1)

        self.conteudo_principal = QWidget(Form)
        self.conteudo_principal.setObjectName(u"conteudo_principal")
        self.conteudo_principal.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.verticalLayout = QVBoxLayout(self.conteudo_principal)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.navegacao = QStackedWidget(self.conteudo_principal)
        self.navegacao.setObjectName(u"navegacao")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.navegacao.addWidget(self.home)
        self.clientes = QWidget()
        self.clientes.setObjectName(u"clientes")
        self.navegacao.addWidget(self.clientes)
        self.fornecedore = QWidget()
        self.fornecedore.setObjectName(u"fornecedore")
        self.navegacao.addWidget(self.fornecedore)

        self.verticalLayout.addWidget(self.navegacao)


        self.gridLayout.addWidget(self.conteudo_principal, 1, 0, 1, 1)


        self.retranslateUi(Form)

        self.navegacao.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.clientes_2.setText(QCoreApplication.translate("Form", u"Clientes", None))
        self.fornecedores.setText(QCoreApplication.translate("Form", u"Fornecedores", None))
    # retranslateUi

