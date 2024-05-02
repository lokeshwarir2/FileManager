#!/usr/bin/python
import sys
sys.path.insert(0, '/FileManager')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QFormLayout,QGroupBox,QScrollArea,QVBoxLayout
import shareto
import os

class Ui_myfiles(QWidget):

    def __init__(self):
        u=os.popen("whoami").read()
        user=u.splitlines()
        command = "find /fileshared -user "+user[0]
        filess = os.popen(command).read()
        files1 = filess.splitlines()
        self.files = list()
        for i in files1:
            file = [i.split('/')]
            f = file[0][2]
            self.files.append(f)
        super().__init__()



    def setupUi(self, myfiles):
        myfiles.setObjectName("myfiles")
        myfiles.resize(701, 550)
        self.centralwidget = QtWidgets.QWidget(myfiles)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow1())
        self.pushButton.setGeometry(QtCore.QRect(290, 90, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow3(self.pushButton_2))
        self.pushButton_2.setGeometry(QtCore.QRect(90, 160, 231, 101))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow3(self.pushButton_3))
        self.pushButton_3.setGeometry(QtCore.QRect(370, 160, 231, 101))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow3(self.pushButton_4))
        self.pushButton_4.setGeometry(QtCore.QRect(90, 290, 231, 101))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow3(self.pushButton_5))
        self.pushButton_5.setGeometry(QtCore.QRect(370, 290, 231, 101))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow3(self.pushButton_6))
        self.pushButton_6.setGeometry(QtCore.QRect(90, 420, 231, 101))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow3(self.pushButton_7))
        self.pushButton_7.setGeometry(QtCore.QRect(370, 420, 231, 101))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow2(self.pushButton_2))
        self.pushButton_8.setGeometry(QtCore.QRect(280, 170, 31, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow2(self.pushButton_3))
        self.pushButton_9.setGeometry(QtCore.QRect(560, 170, 31, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow2(self.pushButton_4))
        self.pushButton_10.setGeometry(QtCore.QRect(280, 300, 31, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow2(self.pushButton_5))
        self.pushButton_11.setGeometry(QtCore.QRect(560, 300, 31, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow2(self.pushButton_6))
        self.pushButton_12.setGeometry(QtCore.QRect(280, 430, 31, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.openWindow2(self.pushButton_7))
        self.pushButton_13.setGeometry(QtCore.QRect(560, 430, 31, 23))
        self.pushButton_13.setObjectName("pushButton_13")
        self.refresh = QtWidgets.QPushButton(self.centralwidget,clicked=lambda : self.refreshfile())
        self.refresh.setGeometry(QtCore.QRect(496, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.refresh.setFont(font)
        myfiles.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(myfiles)
        self.statusbar.setObjectName("statusbar")
        myfiles.setStatusBar(self.statusbar)

        self.retranslateUi(myfiles)

        def display_file(self, files):
            n = len(files)
            for i in range(n):
                    def switch(i):
                        if i == 0:
                            self.pushButton_2.setText(files[0])
                        elif i == 1:
                            self.pushButton_3.setText(files[1])
                        elif i == 2:
                            self.pushButton_4.setText(files[2])
                        elif i == 3:
                            self.pushButton_5.setText(files[3])
                        elif i == 4:
                            self.pushButton_6.setText(files[4])
                        elif i == 5:
                            self.pushButton_7.setText(files[5])

                    switch(i)


        display_file(self,self.files)

    def retranslateUi(self, myfiles):
        _translate = QtCore.QCoreApplication.translate
        myfiles.setWindowTitle(_translate("myfiles", "MY FILES >> FILE MANAGER"))
        self.label.setText(_translate("myfiles", "MY FILES"))
        self.pushButton.setText(_translate("myfiles", "NEW"))
        self.pushButton_2.setText(_translate("myfiles", "No file selected"))
        self.pushButton_3.setText(_translate("myfiles", "No file selected"))
        self.pushButton_4.setText(_translate("myfiles", "No file selected"))
        self.pushButton_5.setText(_translate("myfiles", "No file selected"))
        self.pushButton_6.setText(_translate("myfiles", "No file selected"))
        self.pushButton_7.setText(_translate("myfiles", "No file selected"))
        self.pushButton_8.setText(_translate("myfiles", "X"))
        self.pushButton_9.setText(_translate("myfiles", "X"))
        self.pushButton_10.setText(_translate("myfiles", "X"))
        self.pushButton_11.setText(_translate("myfiles", "X"))
        self.pushButton_12.setText(_translate("myfiles", "X"))
        self.pushButton_13.setText(_translate("myfiles", "X"))
        self.refresh.setText(_translate("myfiles", "REFRESH"))

    def openWindow1(self):
        self.window=QtWidgets.QMainWindow()
        u = (os.popen("cut -d: -f1,3 /etc/passwd | egrep ':[0-9]{4}$' | cut -d: -f1").read())
        u += ""
        user = u.splitlines()
        self.ui=shareto.Ui_MainWindow()
        self.ui.setupUi(self.window,user)
        self.window.show()

    def openWindow2(self,pushbutton):
        delete=pushbutton.text()
        if(delete!="No file selected"):
            command="rm '/fileshared/"+delete+"'"
            os.system(command)

    def refreshfile(self):
         self.__init__()
         self.setupUi(myfiles)
    def openWindow3(self,pushbutton):
        file=pushbutton.text()
        if(file!="No file selected"):
            filename = "'/fileshared/" + file+"'"
            command = "geany " + filename + ""
            os.system(command)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myfiles = QtWidgets.QMainWindow()
    ui = Ui_myfiles()
    ui.setupUi(myfiles)
    myfiles.show()
    sys.exit(app.exec_())
