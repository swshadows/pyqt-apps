# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnResize = QtWidgets.QPushButton(self.centralwidget)
        self.btnResize.setObjectName("btnResize")
        self.gridLayout.addWidget(self.btnResize, 2, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.inputHeight = QtWidgets.QLineEdit(self.centralwidget)
        self.inputHeight.setObjectName("inputHeight")
        self.gridLayout.addWidget(self.inputHeight, 2, 3, 1, 1)
        self.inputWidth = QtWidgets.QLineEdit(self.centralwidget)
        self.inputWidth.setObjectName("inputWidth")
        self.gridLayout.addWidget(self.inputWidth, 2, 1, 1, 1)
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setObjectName("btnSave")
        self.gridLayout.addWidget(self.btnSave, 3, 4, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 493))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.imgLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.gridLayout_2.addWidget(self.imgLabel, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 5)
        self.btnChooseFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnChooseFile.setObjectName("btnChooseFile")
        self.gridLayout.addWidget(self.btnChooseFile, 1, 4, 1, 1)
        self.inputOpenFile = QtWidgets.QLineEdit(self.centralwidget)
        self.inputOpenFile.setObjectName("inputOpenFile")
        self.gridLayout.addWidget(self.inputOpenFile, 1, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Resizer"))
        self.btnResize.setText(_translate("MainWindow", "Redimensionar"))
        self.label_2.setText(_translate("MainWindow", "Altura"))
        self.label.setText(_translate("MainWindow", "Largura"))
        self.btnSave.setText(_translate("MainWindow", "Salvar"))
        self.btnChooseFile.setText(_translate("MainWindow", "Escolher arquivo"))