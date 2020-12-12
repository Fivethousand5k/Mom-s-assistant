# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1561, 856)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(430, 10, 1191, 831))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1189, 829))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.treeWidget = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 1121, 831))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(7, 270, 421, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setGeometry(QtCore.QRect(80, 300, 281, 24))
        self.label_title.setObjectName("label_title")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 350, 391, 391))
        self.widget.setObjectName("widget")
        self.label_address = QtWidgets.QLabel(Form)
        self.label_address.setGeometry(QtCore.QRect(10, 780, 411, 24))
        self.label_address.setText("")
        self.label_address.setObjectName("label_address")
        self.btn_search = QtWidgets.QPushButton(Form)
        self.btn_search.setGeometry(QtCore.QRect(10, 10, 171, 91))
        self.btn_search.setObjectName("btn_search")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(0, 110, 431, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.spinBox_timerange = QtWidgets.QSpinBox(Form)
        self.spinBox_timerange.setGeometry(QtCore.QRect(230, 50, 101, 51))
        self.spinBox_timerange.setProperty("value", 3)
        self.spinBox_timerange.setObjectName("spinBox_timerange")
        self.label_title_2 = QtWidgets.QLabel(Form)
        self.label_title_2.setGeometry(QtCore.QRect(190, 10, 211, 24))
        self.label_title_2.setObjectName("label_title_2")
        self.btn_export = QtWidgets.QPushButton(Form)
        self.btn_export.setGeometry(QtCore.QRect(10, 130, 171, 121))
        self.btn_export.setObjectName("btn_export")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_title.setText(_translate("Form", "拖拽文件到此处或单击"))
        self.btn_search.setText(_translate("Form", "查询"))
        self.label_title_2.setText(_translate("Form", "时间范围：（分钟）"))
        self.btn_export.setText(_translate("Form", "导出"))

