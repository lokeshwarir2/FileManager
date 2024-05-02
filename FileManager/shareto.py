#!/usr/bin/python
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os
class Ui_MainWindow(QtWidgets.QWidget):
    filename=""
    fname=tuple()
    f=list()
    def setupUi(self, MainWindow,users):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 204)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(160, 30, 161, 31))
        self.comboBox.setObjectName("comboBox")
        for i in users:
            self.comboBox.addItem(i)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :files())
        self.user1 = os.popen("whoami").read()
        self.file="/home/"+self.user1
        self.comboBox_2.setGeometry(QtCore.QRect(160, 91, 161, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(50, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :share())
        self.pushButton.setGeometry(QtCore.QRect(300, 150, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        def files():
            self.fname = QFileDialog.getOpenFileNames(self, "open file", self.file,
                                                 "All Files(*);;Python files(*.py)")

            if self.fname:
                    self.f = self.fname[0]
                    if len(self.f)>0:
                         self.filename = self.f[0]
                         self.comboBox_2.setText(self.filename)
                    else:
                        self.comboBox_2.setText("NO FILE SELECTED")

        def share():
            if len(self.f)>0:
                current_user = self.comboBox.currentText()
                command="sh /FileManager/new.sh "+current_user+" "+self.filename
                os.popen(command).read()
                QMessageBox.critical(self,"DONE","FILE CREATED")





        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SHARE TO:"))
        self.label.setText(_translate("MainWindow", "USER"))
        self.label_2.setText(_translate("MainWindow", "FILE"))
        self.pushButton.setText(_translate("MainWindow", "SEND"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    u = (os.popen("cut -d: -f1,3 /etc/passwd | egrep ':[0-9]{4}$' | cut -d: -f1").read())
    u += ""
    users = u.splitlines()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,users)
    MainWindow.show()
    sys.exit(app.exec_())
