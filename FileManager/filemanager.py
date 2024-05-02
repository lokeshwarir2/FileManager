#!/usr/bin/python
import os

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_filemanager(object):
    def setupUi(self, filemanager):
        filemanager.setObjectName("filemanager")
        filemanager.resize(702, 552)
        self.centralwidget = QtWidgets.QWidget(filemanager)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 50, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow1())
        self.pushButton.setGeometry(QtCore.QRect(230, 160, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow2())
        self.pushButton_2.setGeometry(QtCore.QRect(230, 240, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow3())
        self.pushButton_3.setGeometry(QtCore.QRect(230, 320, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.openWindow4())
        self.pushButton_4.setGeometry(QtCore.QRect(230, 400, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_3")
        filemanager.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(filemanager)
        self.statusbar.setObjectName("statusbar")
        filemanager.setStatusBar(self.statusbar)

        self.retranslateUi(filemanager)
        QtCore.QMetaObject.connectSlotsByName(filemanager)

    def retranslateUi(self, filemanager):
        _translate = QtCore.QCoreApplication.translate
        filemanager.setWindowTitle(_translate("filemanager", "FILE MANAGER"))
        self.label.setText(_translate("filemanager", "FILE MANAGER"))
        self.pushButton.setText(_translate("filemanager", "MY FILES"))
        self.pushButton_2.setText(_translate("filemanager", "OTHER FILES"))
        self.pushButton_3.setText(_translate("filemanager", "MESSENGER"))
        self.pushButton_4.setText(_translate("filemanager", "MY MESSAGES"))

    def openWindow1(self):
        command="python /FileManager/myfiles.py"
        os.system(command)


    def openWindow2(self):
        command = "python /FileManager/otherfiles.py"
        os.system(command)


    def openWindow3(self):
        command = "sudo python /FileManager/messenger.py"
        os.system(command)
    def openWindow4(self):
        command = "python /FileManager/mymessages.py"
        os.system(command)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    filemanager = QtWidgets.QMainWindow()
    ui = Ui_filemanager()
    ui.setupUi(filemanager)
    filemanager.show()
    sys.exit(app.exec_())

def whoami():
    us1 = os.popen("whoami").read()
    return us1
