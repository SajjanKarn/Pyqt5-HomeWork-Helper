# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hmw.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import wikipedia


class Ui_MainWindow(object):

    def search_answer(self):
        self.textEdit.insertPlainText("")
        answer = wikipedia.summary(self.lineEdit.text(), sentences=6)
        self.textEdit.insertPlainText(answer)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(956, 823)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 961, 811))
        self.frame.setStyleSheet("#frame{\n"
"background: black;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 100, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("#label{\n"
"color: white;\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(310, 20, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("#label{\n"
"color: white;\n"
"}\n"
"\n"
"#label_2{\n"
"color: white;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(270, 100, 521, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("#lineEdit{\n"
"color: gray;\n"
"background: transparent;\n"
"border: none;\n"
"border-bottom: 1px solid white;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(60, 180, 831, 491))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("#textEdit{\n"
"border: none;\n"
"color: gray;\n"
"background: transparent;\n"
"border-bottom: 1px solid white;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(60, 700, 841, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.search_answer)
        self.pushButton.setStyleSheet("#pushButton{\n"
"border: none;\n"
"border-radius: 30px;\n"
"background: orange;\n"
"color: white;\n"
"}\n"
"\n"
"#pushButton:hover{\n"
"background: red;\n"
"color: black;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Answer Finde"))
        self.label.setText(_translate("MainWindow", "Enter Query"))
        self.label_2.setText(_translate("MainWindow", "Answer Finder"))
        self.pushButton.setText(_translate("MainWindow", "Search Answer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
