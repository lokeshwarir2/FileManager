#!/usr/bin/python
from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_otherfiles(object):
    def __init__(self):
        user = os.popen("whoami").read()
        ruser = user.splitlines()
        com = "cut -d: -f1,3 /etc/group | egrep ':[0-9]{4}$' | cut -d: -f1|grep -E '" + ruser[0] + "[[:space:]#]|" + \
              ruser[0] + "$'"
        gnames = os.popen(com).read()
        gname = gnames.splitlines()
        for i in gname:
            command = "find /fileshared -group " + i
            filess = os.popen(command).read()
            files1 = filess.splitlines()
            self.pfiles = list()
            for i in files1:
                file = [i.split('/')]
                f = file[0][2]
                self.pfiles.append(f)
        super().__init__()

    def openWindow3(self,pushbutton):
        file=pushbutton.text()
        if(file!="No files shared"):
            filename = "/fileshared/"
            command = "geany '" + filename + "/"+file+"'"
            os.system(command)

    def openWindow(self, pushbutton):
        delete = pushbutton.text()
        if (delete != "No file selected"):
                command = "rm '/fileshared/" + delete + "'"
                os.system(command)

    def refreshfile(self):
         self.__init__()
         self.setupUi(otherfiles)

    def setupUi(self, otherfiles):
        otherfiles.setObjectName("otherfiles")
        otherfiles.resize(645, 560)
        self.centralwidget = QtWidgets.QWidget(otherfiles)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow3(self.pushButton))
        self.pushButton.setGeometry(QtCore.QRect(60, 100, 231, 101))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow3(self.pushButton_2))
        self.pushButton_2.setGeometry(QtCore.QRect(350, 100, 231, 101))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow3(self.pushButton_3))
        self.pushButton_3.setGeometry(QtCore.QRect(60, 240, 231, 101))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow3(self.pushButton_4))
        self.pushButton_4.setGeometry(QtCore.QRect(350, 240, 231, 101))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow3(self.pushButton_5))
        self.pushButton_5.setGeometry(QtCore.QRect(60, 380, 231, 101))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow3(self.pushButton_6))
        self.pushButton_6.setGeometry(QtCore.QRect(350, 380, 231, 101))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow(self.pushButton))
        self.pushButton_7.setGeometry(QtCore.QRect(250, 110, 31, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow(self.pushButton_2))
        self.pushButton_8.setGeometry(QtCore.QRect(540, 110, 31, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow(self.pushButton_3))
        self.pushButton_9.setGeometry(QtCore.QRect(250, 250, 31, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow(self.pushButton_4))
        self.pushButton_10.setGeometry(QtCore.QRect(540, 250, 31, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow(self.pushButton_5))
        self.pushButton_11.setGeometry(QtCore.QRect(250, 390, 31, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow(self.pushButton_6))
        self.pushButton_12.setGeometry(QtCore.QRect(540, 390, 31, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.refresh = QtWidgets.QPushButton(self.centralwidget,clicked=lambda : self.refreshfile())
        self.refresh.setGeometry(QtCore.QRect(496, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.refresh.setFont(font)
        otherfiles.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(otherfiles)
        self.statusbar.setObjectName("statusbar")
        otherfiles.setStatusBar(self.statusbar)

        self.retranslateUi(otherfiles)
        QtCore.QMetaObject.connectSlotsByName(otherfiles)

        def display_file(self, files):
            n = len(files)
            for i in range(n):
                def switch(i):
                    if i == 0:
                        self.pushButton.setText(files[0])
                    elif i == 1:
                        self.pushButton_2.setText(files[1])
                    elif i == 2:
                        self.pushButton_3.setText(files[2])
                    elif i == 3:
                        self.pushButton_4.setText(files[3])
                    elif i == 4:
                        self.pushButton_5.setText(files[4])
                    elif i == 5:
                        self.pushButton_6.setText(files[5])

                switch(i)

        display_file(self, self.pfiles)

    def retranslateUi(self, otherfiles):
        _translate = QtCore.QCoreApplication.translate
        otherfiles.setWindowTitle(_translate("otherfiles", "OTHER FILES >> FILE MANAGER"))
        self.label.setText(_translate("otherfiles", "OTHER FILES"))
        self.pushButton.setText(_translate("otherfiles", "No files shared"))
        self.pushButton_2.setText(_translate("otherfiles", "No files shared"))
        self.pushButton_3.setText(_translate("otherfiles", "No files shared"))
        self.pushButton_4.setText(_translate("otherfiles", "No files shared"))
        self.pushButton_5.setText(_translate("otherfiles", "No files shared"))
        self.pushButton_6.setText(_translate("otherfiles", "No files shared"))
        self.pushButton_7.setText(_translate("otherfiles", "x"))
        self.pushButton_8.setText(_translate("otherfiles", "x"))
        self.pushButton_9.setText(_translate("otherfiles", "x"))
        self.pushButton_10.setText(_translate("otherfiles", "x"))
        self.pushButton_11.setText(_translate("otherfiles", "x"))
        self.pushButton_12.setText(_translate("otherfiles", "x"))
        self.refresh.setText(_translate("otherfiles", "REFRESH"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    otherfiles = QtWidgets.QMainWindow()
    ui = Ui_otherfiles()
    ui.setupUi(otherfiles)
    otherfiles.show()
    sys.exit(app.exec_())
