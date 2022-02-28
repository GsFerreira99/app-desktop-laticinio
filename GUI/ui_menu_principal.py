# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_principalqsUiwZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import GUI.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1174, 793)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Conteudo = QWidget(self.centralwidget)
        self.Conteudo.setObjectName(u"Conteudo")
        self.Conteudo.setStyleSheet(u"background-color: rgb(130, 130, 130)")
        self.gridLayout_2 = QGridLayout(self.Conteudo)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(15, 15, 15, 15)
        self.titulo = QLabel(self.Conteudo)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setMinimumSize(QSize(0, 50))
        self.titulo.setMaximumSize(QSize(16777215, 50))
        self.titulo.setStyleSheet(u"font: 20pt \"Segoe UI Variable Display Semib\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(248, 248, 248)")
        self.titulo.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.titulo, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.Conteudo)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.gridLayout_5 = QGridLayout(self.Home)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.titulo_2 = QLabel(self.Home)
        self.titulo_2.setObjectName(u"titulo_2")
        self.titulo_2.setMinimumSize(QSize(0, 50))
        self.titulo_2.setMaximumSize(QSize(16777215, 50))
        self.titulo_2.setStyleSheet(u"font: 20pt \"Segoe UI Variable Display Semib\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(248, 248, 248)")
        self.titulo_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.titulo_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Home)
        self.Vendas = QWidget()
        self.Vendas.setObjectName(u"Vendas")
        self.gridLayout_6 = QGridLayout(self.Vendas)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.titulo_3 = QLabel(self.Vendas)
        self.titulo_3.setObjectName(u"titulo_3")
        self.titulo_3.setMinimumSize(QSize(0, 50))
        self.titulo_3.setMaximumSize(QSize(16777215, 50))
        self.titulo_3.setStyleSheet(u"font: 20pt \"Segoe UI Variable Display Semib\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(248, 248, 248)")
        self.titulo_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.titulo_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Vendas)
        self.Clientes = QWidget()
        self.Clientes.setObjectName(u"Clientes")
        self.gridLayout_7 = QGridLayout(self.Clientes)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.titulo_4 = QLabel(self.Clientes)
        self.titulo_4.setObjectName(u"titulo_4")
        self.titulo_4.setMinimumSize(QSize(0, 50))
        self.titulo_4.setMaximumSize(QSize(16777215, 50))
        self.titulo_4.setStyleSheet(u"font: 20pt \"Segoe UI Variable Display Semib\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(248, 248, 248)")
        self.titulo_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.titulo_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Clientes)
        self.Financeiro = QWidget()
        self.Financeiro.setObjectName(u"Financeiro")
        self.gridLayout_8 = QGridLayout(self.Financeiro)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.titulo_5 = QLabel(self.Financeiro)
        self.titulo_5.setObjectName(u"titulo_5")
        self.titulo_5.setMinimumSize(QSize(0, 50))
        self.titulo_5.setMaximumSize(QSize(16777215, 50))
        self.titulo_5.setStyleSheet(u"font: 20pt \"Segoe UI Variable Display Semib\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(248, 248, 248)")
        self.titulo_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.titulo_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Financeiro)
        self.Configuracoes = QWidget()
        self.Configuracoes.setObjectName(u"Configuracoes")
        self.gridLayout_3 = QGridLayout(self.Configuracoes)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Home_2 = QLabel(self.Configuracoes)
        self.Home_2.setObjectName(u"Home_2")
        self.Home_2.setMinimumSize(QSize(0, 50))
        self.Home_2.setMaximumSize(QSize(16777215, 50))
        self.Home_2.setStyleSheet(u"font: 20pt \"Segoe UI Variable Display Semib\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(248, 248, 248)")
        self.Home_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Home_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Configuracoes)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.Conteudo, 0, 1, 1, 1)

        self.MenuLateral = QWidget(self.centralwidget)
        self.MenuLateral.setObjectName(u"MenuLateral")
        self.MenuLateral.setMinimumSize(QSize(160, 0))
        self.MenuLateral.setMaximumSize(QSize(160, 16777215))
        self.MenuLateral.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.489, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(81, 81, 81, 255));")
        self.verticalLayout = QVBoxLayout(self.MenuLateral)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Logo = QWidget(self.MenuLateral)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setMinimumSize(QSize(0, 80))
        self.Logo.setMaximumSize(QSize(16777215, 80))
        self.Logo.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.gridLayout = QGridLayout(self.Logo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_logo = QPushButton(self.Logo)
        self.btn_logo.setObjectName(u"btn_logo")
        self.btn_logo.setMinimumSize(QSize(0, 70))
        self.btn_logo.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily(u"Segoe UI Variable")
        font.setPointSize(20)
        self.btn_logo.setFont(font)
        self.btn_logo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/newPrefix/rancho.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:none;\n"
"color: white;\n"
"padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.btn_logo, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.Logo)

        self.nav_bar = QWidget(self.MenuLateral)
        self.nav_bar.setObjectName(u"nav_bar")
        self.nav_bar.setStyleSheet(u"QWidget {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 13pt \"Segoe UI Variable Display Semib\";\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:none;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 2px solid rgb(124, 199, 73);\n"
"}\n"
"QPushButton:pressed {\n"
"	border-bottom: 4px solid rgb(97, 157, 58);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.nav_bar)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 20, 0, 0)
        self.btn_home = QPushButton(self.nav_bar)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 50))
        self.btn_home.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Variable Display Semib")
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.btn_home.setFont(font1)
        self.btn_home.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_home)

        self.btn_vendas = QPushButton(self.nav_bar)
        self.btn_vendas.setObjectName(u"btn_vendas")
        self.btn_vendas.setMinimumSize(QSize(0, 50))
        self.btn_vendas.setMaximumSize(QSize(16777215, 50))
        self.btn_vendas.setFont(font1)
        self.btn_vendas.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_vendas)

        self.btn_clientes = QPushButton(self.nav_bar)
        self.btn_clientes.setObjectName(u"btn_clientes")
        self.btn_clientes.setMinimumSize(QSize(0, 50))
        self.btn_clientes.setMaximumSize(QSize(16777215, 50))
        self.btn_clientes.setFont(font1)
        self.btn_clientes.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_clientes)

        self.btn_financeiro = QPushButton(self.nav_bar)
        self.btn_financeiro.setObjectName(u"btn_financeiro")
        self.btn_financeiro.setMinimumSize(QSize(0, 50))
        self.btn_financeiro.setMaximumSize(QSize(16777215, 50))
        self.btn_financeiro.setFont(font1)
        self.btn_financeiro.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_financeiro)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.configuracoes = QPushButton(self.nav_bar)
        self.configuracoes.setObjectName(u"configuracoes")
        self.configuracoes.setMinimumSize(QSize(0, 50))
        self.configuracoes.setMaximumSize(QSize(16777215, 50))
        self.configuracoes.setFont(font1)
        self.configuracoes.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.configuracoes)


        self.verticalLayout.addWidget(self.nav_bar)


        self.gridLayout_4.addWidget(self.MenuLateral, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"TITULO DA P\u00c1GINA", None))
        self.titulo_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.titulo_3.setText(QCoreApplication.translate("MainWindow", u"Vendas", None))
        self.titulo_4.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.titulo_5.setText(QCoreApplication.translate("MainWindow", u"Financeiro", None))
        self.Home_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_logo.setText("")
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_vendas.setText(QCoreApplication.translate("MainWindow", u"Vendas", None))
        self.btn_clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn_financeiro.setText(QCoreApplication.translate("MainWindow", u"Financeiro", None))
        self.configuracoes.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00e3o", None))
    # retranslateUi

