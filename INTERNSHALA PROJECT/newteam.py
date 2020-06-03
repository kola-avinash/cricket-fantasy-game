# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newteam.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_New_team(object):
    def setupUi(self, New_team):
        New_team.setObjectName("New_team")
        New_team.resize(451, 286)
        self.verticalLayout = QtWidgets.QVBoxLayout(New_team)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(New_team)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(New_team)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.inpteamname = QtWidgets.QLineEdit(New_team)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.inpteamname.setFont(font)
        self.inpteamname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inpteamname.setCursorPosition(0)
        self.inpteamname.setAlignment(QtCore.Qt.AlignCenter)
        self.inpteamname.setClearButtonEnabled(True)
        self.inpteamname.setObjectName("inpteamname")
        self.verticalLayout.addWidget(self.inpteamname)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.createteam = QtWidgets.QPushButton(New_team)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.createteam.setFont(font)
        self.createteam.setObjectName("createteam")
        self.verticalLayout.addWidget(self.createteam)

        self.retranslateUi(New_team)
        QtCore.QMetaObject.connectSlotsByName(New_team)

    def retranslateUi(self, New_team):
        _translate = QtCore.QCoreApplication.translate
        New_team.setWindowTitle(_translate("New_team", "Form"))
        self.label.setText(_translate("New_team", "Create a new team"))
        self.label_2.setText(_translate("New_team", "Enter your team name below"))
        self.inpteamname.setPlaceholderText(_translate("New_team", "your team name"))
        self.createteam.setText(_translate("New_team", "CREATE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    New_team = QtWidgets.QWidget()
    ui = Ui_New_team()
    ui.setupUi(New_team)
    New_team.show()
    sys.exit(app.exec_())
