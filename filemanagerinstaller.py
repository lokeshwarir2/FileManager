#!/usr/bin/python
from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_filemanager(object):
    def setupUi(self, filemanager):
        filemanager.setObjectName("filemanager")
        filemanager.resize(493, 308)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        filemanager.setFont(font)
        self.label = QtWidgets.QLabel(filemanager)
        self.label.setGeometry(QtCore.QRect(60, 20, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(filemanager)
        self.label_2.setGeometry(QtCore.QRect(120, 100, 301, 41))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(filemanager,clicked=lambda :self.openWindow1())
        self.pushButton.setGeometry(QtCore.QRect(160, 160, 161, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(filemanager,clicked=lambda :self.openWindow2())
        self.pushButton_2.setGeometry(QtCore.QRect(160, 220, 161, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(filemanager)
        QtCore.QMetaObject.connectSlotsByName(filemanager)

    def retranslateUi(self, filemanager):
        _translate = QtCore.QCoreApplication.translate
        filemanager.setWindowTitle(_translate("filemanager", "FILE MANAGER INSTALLER"))
        self.label.setText(_translate("filemanager", "FILE   MANAGER  INSTALLER"))
        self.label_2.setText(_translate("filemanager", "SHOULD BE INSTALLED FOR??"))
        self.pushButton.setText(_translate("filemanager", "ONLY FOR ME"))
        self.pushButton_2.setText(_translate("filemanager", "ALL USERS"))

    def openWindow1(self):
        command = "sudo sh sourcefilemanager/onlyforme.sh"
        os.system(command)
        os.system("python sourcefilemanager/done.py")

    def openWindow2(self):
        u = (os.popen("cut -d: -f1,3 /etc/passwd | egrep ':[0-9]{4}$' | cut -d: -f1").read())
        u += ""
        user = u.splitlines()
        for i in user:
            command="sudo sh sourcefilemanager/forallusers.sh "+i
            os.system(command)
        os.system("python sourcefilemanager/done.py")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    filemanager = QtWidgets.QWidget()
    ui = Ui_filemanager()
    ui.setupUi(filemanager)
    filemanager.show()
    sys.exit(app.exec_())

