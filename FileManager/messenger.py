#!/usr/bin/python
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import filemanager
class Ui_messenger(object):
    def setupUi(self, messenger):
        messenger.setObjectName("messenger")
        messenger.resize(677, 514)
        self.centralwidget = QtWidgets.QWidget(messenger)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 30, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 110, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(300, 110, 201, 22))
        self.comboBox.setObjectName("comboBox")
        u = (os.popen("cut -d: -f1,3 /etc/passwd | egrep ':[0-9]{4}$' | cut -d: -f1").read())
        u += ""
        users = u.splitlines()
        for i in users:
            self.comboBox.addItem(i)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 170, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QTextEdit(self.centralwidget,lineWrapMode=QtWidgets.QTextEdit.FixedColumnWidth,lineWrapColumnOrWidth=60,readOnly=False,acceptRichText=True)
        self.lineEdit.setGeometry(QtCore.QRect(170, 230, 321, 151))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:send())
        self.pushButton.setGeometry(QtCore.QRect(500, 410, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        messenger.setCentralWidget(self.centralwidget)
        ptime=os.popen("date +%T").read()
        ptime=ptime.replace("\n","")
        date=os.popen('date +%F').read()
        date=date.replace("\n","")
        fname="("+date+","+ptime+")"
        def send():

            us = str(self.comboBox.currentText())
            us1=filemanager.whoami()
            us1=us1.replace("\n","")
            filename="/home/"+us+"/messages/"+us1+fname+".txt"
            with open(filename,'w') as yourFile:
                yourFile.write(str(self.lineEdit.toPlainText()))

        self.statusbar = QtWidgets.QStatusBar(messenger)
        self.statusbar.setObjectName("statusbar")
        messenger.setStatusBar(self.statusbar)

        self.retranslateUi(messenger)
        QtCore.QMetaObject.connectSlotsByName(messenger)

    def retranslateUi(self, messenger):
        _translate = QtCore.QCoreApplication.translate
        messenger.setWindowTitle(_translate("messenger", "MESSENGER >> FILE MANAGER"))
        self.label.setText(_translate("messenger", "MESSENGER"))
        self.label_2.setText(_translate("messenger", "USER"))
        self.label_3.setText(_translate("messenger", "MESSAGE"))
        self.pushButton.setText(_translate("messenger", "SEND"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    messenger = QtWidgets.QMainWindow()
    ui = Ui_messenger()
    ui.setupUi(messenger)
    messenger.show()
    sys.exit(app.exec_())
