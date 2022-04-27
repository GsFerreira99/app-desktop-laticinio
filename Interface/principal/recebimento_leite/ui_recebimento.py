# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recebimento-leitebBhuvT.ui'
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
        Form.resize(1264, 738)
        Form.setStyleSheet(u"QWidget {\n"
"	background-color: #ECF2FD;\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(50, 40, 50, 25)
        self.label_msg = QLabel(Form)
        self.label_msg.setObjectName(u"label_msg")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_msg.sizePolicy().hasHeightForWidth())
        self.label_msg.setSizePolicy(sizePolicy)
        self.label_msg.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamily(u"Raleway")
        font.setPointSize(9)
        self.label_msg.setFont(font)
        self.label_msg.setStyleSheet(u"    border: 1px solid;\n"
"    border-radius: 5px;\n"
"    color: #721c24;\n"
"    background-color: #f8d7da;\n"
"    border-color: #f5c6cb;")
        self.label_msg.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_msg)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(210, 216, 225);")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(250, 50, 250, 10)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamily(u"Raleway")
        font1.setPointSize(18)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"border: None;")

        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background: #E7E7E7;\n"
"	border-radius: 10px;\n"
"	padding-left: 20px\n"
"}\n"
"\n"
"QDateTimeEdit {\n"
"	background: #E7E7E7;\n"
"	border-radius: 10px;\n"
"	padding-left: 20px\n"
"}\n"
"\n"
"QComboBox {\n"
"	background: #E7E7E7;\n"
"	border-radius: 10px;\n"
"	padding-left: 20px\n"
"}\n"
"\n"
"QComboBox::down-arrow, QDateTimeEdit::down-arrow {\n"
"	image: url(:/newPrefix/drop-down.png);\n"
"	height: 15px\n"
"}\n"
"\n"
"QComboBox::drop-down, QDateTimeEdit::drop-down {\n"
"	border: none;\n"
"	margin-right: 10px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: none;\n"
"	border-radius: none;\n"
"    selection-background-color: lightgray;\n"
"	padding: 5px\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btnSalvar = QPushButton(self.frame)
        self.btnSalvar.setObjectName(u"btnSalvar")
        self.btnSalvar.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setFamily(u"Raleway")
        font2.setPointSize(11)
        self.btnSalvar.setFont(font2)
        self.btnSalvar.setStyleSheet(u"QPushButton {\n"
"	background: #000920;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: rgb(0, 23, 81);\n"
"}")

        self.gridLayout_2.addWidget(self.btnSalvar, 3, 0, 1, 2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamily(u"Raleway")
        font3.setPointSize(10)
        self.label_2.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_2)

        self.inputQuantidade = QLineEdit(self.frame_3)
        self.inputQuantidade.setObjectName(u"inputQuantidade")
        self.inputQuantidade.setMaximumSize(QSize(16777215, 40))
        self.inputQuantidade.setClearButtonEnabled(False)

        self.verticalLayout_2.addWidget(self.inputQuantidade)


        self.gridLayout_2.addWidget(self.frame_3, 2, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setFont(font3)

        self.verticalLayout.addWidget(self.label)

        self.inputData = QDateTimeEdit(self.frame_2)
        self.inputData.setObjectName(u"inputData")
        self.inputData.setMaximumSize(QSize(16777215, 40))
        self.inputData.setFont(font3)
        self.inputData.setStyleSheet(u"QCalendarWidget QToolButton {\n"
"  	height: 30px;\n"
"  	width: 100px;\n"
"  	color: black;\n"
"  	font-size: 13px;\n"
"  	icon-size: 20px;\n"
"	border: none;\n"
"  	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"  }\n"
"\n"
"QCalendarWidget QMenu {\n"
"  	width: 100px;\n"
"  	left: 20px;\n"
"  	color: black;\n"
"  	font-size: 15px;\n"
"  	background-color: rgb(232, 238, 249);\n"
"  }\n"
"\n"
"QCalendarWidget QWidget { alternate-background-color: rgb(232, 238, 249); }\n"
"\n"
"  /* normal days */\n"
"  QCalendarWidget QAbstractItemView:enabled \n"
"  {\n"
"  	font-size:15px;  \n"
"  	color: black;  \n"
"  	background-color: rgb(232, 238, 249);  \n"
"  	selection-background-color: rgb(232, 238, 249); \n"
"  	selection-color:rgb(0, 163, 0)\n"
"  }\n"
"   \n"
"  /* days in other months */\n"
"  /* navigation bar */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar\n"
"{ \n"
"  background-color:rgb(232, 238, 249); \n"
"}"
                        "\n"
"")
        self.inputData.setTime(QTime(0, 0, 0))
        self.inputData.setMinimumDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.inputData.setMaximumTime(QTime(23, 59, 59))
        self.inputData.setMinimumTime(QTime(0, 0, 0))
        self.inputData.setCalendarPopup(True)
        self.inputData.setTimeSpec(Qt.LocalTime)

        self.verticalLayout.addWidget(self.inputData)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMaximumSize(QSize(16777215, 100))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_3)

        self.inputFornecedor = QComboBox(self.frame_4)
        self.inputFornecedor.addItem("")
        self.inputFornecedor.addItem("")
        self.inputFornecedor.setObjectName(u"inputFornecedor")
        self.inputFornecedor.setMaximumSize(QSize(16777215, 40))
        self.inputFornecedor.setFont(font2)

        self.verticalLayout_3.addWidget(self.inputFornecedor)


        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 2, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_msg.setText(QCoreApplication.translate("Form", u"Usuario ou senha incorretos", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Inserir Recebimento de Leite", None))
        self.btnSalvar.setText(QCoreApplication.translate("Form", u"Salvar", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Quantidade (L)", None))
        self.inputQuantidade.setPlaceholderText(QCoreApplication.translate("Form", u"ex.: 52.31", None))
        self.label.setText(QCoreApplication.translate("Form", u"Data", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Fornecedor", None))
        self.inputFornecedor.setItemText(0, "")
        self.inputFornecedor.setItemText(1, QCoreApplication.translate("Form", u"Parananema", None))

    # retranslateUi

