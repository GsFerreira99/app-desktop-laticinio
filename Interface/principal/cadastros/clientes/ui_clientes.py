# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clienteskFQSZo.ui'
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
        Form.resize(1320, 737)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"font: 75 13pt \"Roboto Cn\";")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.busca = QFrame(self.frame)
        self.busca.setObjectName(u"busca")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.busca.sizePolicy().hasHeightForWidth())
        self.busca.setSizePolicy(sizePolicy)
        self.busca.setMinimumSize(QSize(0, 0))
        self.busca.setFrameShape(QFrame.StyledPanel)
        self.busca.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.busca)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.busca_simples = QFrame(self.busca)
        self.busca_simples.setObjectName(u"busca_simples")
        self.busca_simples.setMinimumSize(QSize(0, 60))
        self.busca_simples.setMaximumSize(QSize(16777215, 60))
        self.busca_simples.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"}")
        self.busca_simples.setFrameShape(QFrame.StyledPanel)
        self.busca_simples.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.busca_simples)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.adicionar_cliente = QPushButton(self.busca_simples)
        self.adicionar_cliente.setObjectName(u"adicionar_cliente")
        self.adicionar_cliente.setMinimumSize(QSize(150, 40))
        self.adicionar_cliente.setMaximumSize(QSize(100, 40))
        self.adicionar_cliente.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color: rgb(39, 39, 39);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(71, 71, 71);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(29, 29, 29);\n"
"}")

        self.horizontalLayout.addWidget(self.adicionar_cliente)

        self.frame_6 = QFrame(self.busca_simples)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(550, 40))
        self.frame_6.setMaximumSize(QSize(550, 40))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.input_busca = QLineEdit(self.frame_6)
        self.input_busca.setObjectName(u"input_busca")
        self.input_busca.setMinimumSize(QSize(500, 35))
        self.input_busca.setMaximumSize(QSize(500, 35))
        self.input_busca.setStyleSheet(u"QLineEdit {\n"
"border-bottom: 1px solid black;\n"
"border-radius: none;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border-bottom: 2px solid black;\n"
"}")

        self.horizontalLayout_2.addWidget(self.input_busca)

        self.btn_busca_simples = QPushButton(self.frame_6)
        self.btn_busca_simples.setObjectName(u"btn_busca_simples")
        self.btn_busca_simples.setMinimumSize(QSize(50, 35))
        self.btn_busca_simples.setMaximumSize(QSize(50, 35))
        self.btn_busca_simples.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color: rgb(39, 39, 39);\n"
"	border-radius: none;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"	image: url(:/newPrefix/icon_pesquisa.png);\n"
"	padding: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(71, 71, 71);\n"
"	padding: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(29, 29, 29);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_busca_simples)


        self.horizontalLayout.addWidget(self.frame_6)

        self.btn_busca_avancada = QPushButton(self.busca_simples)
        self.btn_busca_avancada.setObjectName(u"btn_busca_avancada")
        self.btn_busca_avancada.setMinimumSize(QSize(150, 40))
        self.btn_busca_avancada.setMaximumSize(QSize(100, 40))
        self.btn_busca_avancada.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(221, 221, 221);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(197, 197, 197);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_busca_avancada)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.busca_simples)

        self.busca_avancada = QFrame(self.busca)
        self.busca_avancada.setObjectName(u"busca_avancada")
        self.busca_avancada.setMinimumSize(QSize(0, 0))
        self.busca_avancada.setMaximumSize(QSize(16777215, 0))
        self.busca_avancada.setStyleSheet(u"QFrame {\n"
"	border: 1px dotted black;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}")
        self.busca_avancada.setFrameShape(QFrame.StyledPanel)
        self.busca_avancada.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.busca_avancada)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 9, 9)
        self.frame_8 = QFrame(self.busca_avancada)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QLineEdit {\n"
"	border:none;\n"
"	border-radius: 5px;\n"
"}\n"
"QFrame {\n"
"	border:none;\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(9)
        self.input_nome = QLineEdit(self.frame_8)
        self.input_nome.setObjectName(u"input_nome")
        self.input_nome.setMinimumSize(QSize(300, 30))
        self.input_nome.setMaximumSize(QSize(300, 30))
        self.input_nome.setStyleSheet(u"background-color: rgb(212, 212, 212);")

        self.gridLayout_4.addWidget(self.input_nome, 3, 0, 1, 1)

        self.input_codigo = QLineEdit(self.frame_8)
        self.input_codigo.setObjectName(u"input_codigo")
        self.input_codigo.setMinimumSize(QSize(300, 30))
        self.input_codigo.setMaximumSize(QSize(300, 30))
        self.input_codigo.setStyleSheet(u"background-color: rgb(212, 212, 212);")

        self.gridLayout_4.addWidget(self.input_codigo, 1, 1, 1, 1)

        self.input_tipo = QLineEdit(self.frame_8)
        self.input_tipo.setObjectName(u"input_tipo")
        self.input_tipo.setMinimumSize(QSize(300, 30))
        self.input_tipo.setMaximumSize(QSize(300, 30))
        self.input_tipo.setStyleSheet(u"background-color: rgb(212, 212, 212);\n"
"border-radius: 5px;")

        self.gridLayout_4.addWidget(self.input_tipo, 1, 0, 1, 1)

        self.lb_nome = QLabel(self.frame_8)
        self.lb_nome.setObjectName(u"lb_nome")
        self.lb_nome.setMinimumSize(QSize(300, 25))
        self.lb_nome.setMaximumSize(QSize(300, 25))
        self.lb_nome.setStyleSheet(u"border: none;")
        self.lb_nome.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_4.addWidget(self.lb_nome, 2, 0, 1, 1)

        self.lb_tipo = QLabel(self.frame_8)
        self.lb_tipo.setObjectName(u"lb_tipo")
        self.lb_tipo.setMinimumSize(QSize(300, 25))
        self.lb_tipo.setMaximumSize(QSize(300, 25))
        self.lb_tipo.setStyleSheet(u"border: none;")
        self.lb_tipo.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_4.addWidget(self.lb_tipo, 0, 0, 1, 1)

        self.input_cnpj = QLineEdit(self.frame_8)
        self.input_cnpj.setObjectName(u"input_cnpj")
        self.input_cnpj.setMinimumSize(QSize(300, 30))
        self.input_cnpj.setMaximumSize(QSize(300, 30))
        self.input_cnpj.setStyleSheet(u"background-color: rgb(212, 212, 212);")

        self.gridLayout_4.addWidget(self.input_cnpj, 1, 2, 1, 1)

        self.lb_codigo = QLabel(self.frame_8)
        self.lb_codigo.setObjectName(u"lb_codigo")
        self.lb_codigo.setMinimumSize(QSize(300, 25))
        self.lb_codigo.setMaximumSize(QSize(300, 25))
        self.lb_codigo.setStyleSheet(u"border: none;")
        self.lb_codigo.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_4.addWidget(self.lb_codigo, 0, 1, 1, 1)

        self.lb_cnpj = QLabel(self.frame_8)
        self.lb_cnpj.setObjectName(u"lb_cnpj")
        self.lb_cnpj.setMinimumSize(QSize(300, 25))
        self.lb_cnpj.setMaximumSize(QSize(300, 25))
        self.lb_cnpj.setStyleSheet(u"border: none;")
        self.lb_cnpj.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_4.addWidget(self.lb_cnpj, 0, 2, 1, 1)

        self.input_telefone = QLineEdit(self.frame_8)
        self.input_telefone.setObjectName(u"input_telefone")
        self.input_telefone.setMinimumSize(QSize(300, 30))
        self.input_telefone.setMaximumSize(QSize(300, 30))
        self.input_telefone.setStyleSheet(u"background-color: rgb(212, 212, 212);")

        self.gridLayout_4.addWidget(self.input_telefone, 3, 1, 1, 1)

        self.input_email = QLineEdit(self.frame_8)
        self.input_email.setObjectName(u"input_email")
        self.input_email.setMinimumSize(QSize(300, 30))
        self.input_email.setMaximumSize(QSize(300, 30))
        self.input_email.setStyleSheet(u"background-color: rgb(212, 212, 212);")

        self.gridLayout_4.addWidget(self.input_email, 3, 2, 1, 1)

        self.lb_telefone = QLabel(self.frame_8)
        self.lb_telefone.setObjectName(u"lb_telefone")
        self.lb_telefone.setMinimumSize(QSize(300, 25))
        self.lb_telefone.setMaximumSize(QSize(300, 25))
        self.lb_telefone.setStyleSheet(u"border: none;")
        self.lb_telefone.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_4.addWidget(self.lb_telefone, 2, 1, 1, 1)

        self.lb_email = QLabel(self.frame_8)
        self.lb_email.setObjectName(u"lb_email")
        self.lb_email.setMinimumSize(QSize(300, 25))
        self.lb_email.setMaximumSize(QSize(300, 25))
        self.lb_email.setStyleSheet(u"border: none;")
        self.lb_email.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_4.addWidget(self.lb_email, 2, 2, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.busca_avancada)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(210, 50))
        self.frame_7.setMaximumSize(QSize(210, 50))
        self.frame_7.setStyleSheet(u"border:none;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.buscar_avancado = QPushButton(self.frame_7)
        self.buscar_avancado.setObjectName(u"buscar_avancado")
        self.buscar_avancado.setMinimumSize(QSize(100, 40))
        self.buscar_avancado.setMaximumSize(QSize(100, 40))
        self.buscar_avancado.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(71, 212, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 231, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(69, 198, 0);\n"
"}")

        self.horizontalLayout_4.addWidget(self.buscar_avancado)

        self.limpar = QPushButton(self.frame_7)
        self.limpar.setObjectName(u"limpar")
        self.limpar.setMinimumSize(QSize(100, 40))
        self.limpar.setMaximumSize(QSize(100, 40))
        self.limpar.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(229, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(250, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(214, 0, 0);\n"
"}")

        self.horizontalLayout_4.addWidget(self.limpar)


        self.horizontalLayout_3.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.busca_avancada)


        self.verticalLayout.addWidget(self.busca)

        self.tabela = QFrame(self.frame)
        self.tabela.setObjectName(u"tabela")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabela.sizePolicy().hasHeightForWidth())
        self.tabela.setSizePolicy(sizePolicy1)
        self.tabela.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}")
        self.tabela.setFrameShape(QFrame.StyledPanel)
        self.tabela.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.tabela)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.deletar = QPushButton(self.tabela)
        self.deletar.setObjectName(u"deletar")
        self.deletar.setMinimumSize(QSize(100, 40))
        self.deletar.setMaximumSize(QSize(100, 40))
        self.deletar.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(229, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(250, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(214, 0, 0);\n"
"}")

        self.gridLayout_2.addWidget(self.deletar, 1, 3, 1, 1)

        self.tabela_clientes = QTableWidget(self.tabela)
        self.tabela_clientes.setObjectName(u"tabela_clientes")

        self.gridLayout_2.addWidget(self.tabela_clientes, 0, 0, 1, 4)

        self.detalhes = QPushButton(self.tabela)
        self.detalhes.setObjectName(u"detalhes")
        self.detalhes.setMinimumSize(QSize(100, 40))
        self.detalhes.setMaximumSize(QSize(100, 40))
        self.detalhes.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 74, 223);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 66, 198);\n"
"}")

        self.gridLayout_2.addWidget(self.detalhes, 1, 1, 1, 1)

        self.editar = QPushButton(self.tabela)
        self.editar.setObjectName(u"editar")
        self.editar.setMinimumSize(QSize(100, 40))
        self.editar.setMaximumSize(QSize(100, 40))
        self.editar.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(238, 159, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(254, 169, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(216, 144, 0);\n"
"}")

        self.gridLayout_2.addWidget(self.editar, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.tabela)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.adicionar_cliente.setText(QCoreApplication.translate("Form", u"Adicionar Cliente", None))
        self.btn_busca_simples.setText("")
        self.btn_busca_avancada.setText(QCoreApplication.translate("Form", u"Busca Avan\u00e7ada", None))
        self.lb_nome.setText(QCoreApplication.translate("Form", u"Nome/Raz\u00e3o Social", None))
        self.lb_tipo.setText(QCoreApplication.translate("Form", u"Tipo", None))
        self.lb_codigo.setText(QCoreApplication.translate("Form", u"Codigo", None))
        self.lb_cnpj.setText(QCoreApplication.translate("Form", u"CPF/CNPJ", None))
        self.lb_telefone.setText(QCoreApplication.translate("Form", u"Telefone", None))
        self.lb_email.setText(QCoreApplication.translate("Form", u"Email", None))
        self.buscar_avancado.setText(QCoreApplication.translate("Form", u"Buscar", None))
        self.limpar.setText(QCoreApplication.translate("Form", u"Limpar", None))
        self.deletar.setText(QCoreApplication.translate("Form", u"Deletar", None))
        self.detalhes.setText(QCoreApplication.translate("Form", u"Detalhes", None))
        self.editar.setText(QCoreApplication.translate("Form", u"Editar", None))
    # retranslateUi

