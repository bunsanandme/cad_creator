# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 272)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openfile_btn = QtWidgets.QPushButton(self.centralwidget)
        self.openfile_btn.setGeometry(QtCore.QRect(10, 20, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.openfile_btn.setFont(font)
        self.openfile_btn.setObjectName("openfile_btn")
        self.eval_btn = QtWidgets.QPushButton(self.centralwidget)
        self.eval_btn.setGeometry(QtCore.QRect(10, 80, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.eval_btn.setFont(font)
        self.eval_btn.setObjectName("eval_btn")
        self.filepath_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.filepath_text.setGeometry(QtCore.QRect(220, 20, 291, 41))
        self.filepath_text.setObjectName("filepath_text")
        self.evalresult_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.evalresult_text.setGeometry(QtCore.QRect(220, 80, 291, 171))
        self.evalresult_text.setObjectName("evalresult_text")
        self.demonstate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.demonstate_btn.setGeometry(QtCore.QRect(10, 210, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.demonstate_btn.setFont(font)
        self.demonstate_btn.setObjectName("demonstate_btn")
        self.savecad_btn = QtWidgets.QPushButton(self.centralwidget)
        self.savecad_btn.setGeometry(QtCore.QRect(10, 150, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.savecad_btn.setFont(font)
        self.savecad_btn.setObjectName("savecad_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openfile_btn.setText(_translate("MainWindow", "Открыть STP файл"))
        self.eval_btn.setText(_translate("MainWindow", "Провести расчеты"))
        self.demonstate_btn.setText(_translate("MainWindow", "Демонстрация модели"))
        self.savecad_btn.setText(_translate("MainWindow", "Сохранить CAD"))