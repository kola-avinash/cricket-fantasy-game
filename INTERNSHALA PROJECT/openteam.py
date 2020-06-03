# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openteam.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3
ovs=sqlite3.connect('cricket.db')
cursov=ovs.cursor()



class Ui_open(object):
    def setupUi(self, open):
        open.setObjectName("open")
        open.resize(470, 336)
        self.verticalLayout = QtWidgets.QVBoxLayout(open)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(open)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.open_team_comboBox = QtWidgets.QComboBox(self.frame)
        self.open_team_comboBox.setObjectName("open_team_comboBox")
        self.verticalLayout_2.addWidget(self.open_team_comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.open_btn = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.open_btn.setFont(font)
        self.open_btn.setObjectName("open_btn")
        self.verticalLayout_2.addWidget(self.open_btn)
        self.verticalLayout.addWidget(self.frame)
        tms=cursov.execute("SELECT DISTINCT Name FROM teams;")
        x=tms.fetchall()
        for i in x:                                 #access the data from database and add the same to combo box
            self.open_team_comboBox.addItem(i[0])

        self.retranslateUi(open)
        QtCore.QMetaObject.connectSlotsByName(open)

    def retranslateUi(self, open):
        _translate = QtCore.QCoreApplication.translate
        open.setWindowTitle(_translate("open", "Form"))
        self.label.setText(_translate("open", "            open team"))
        self.open_btn.setText(_translate("open", "open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    open = QtWidgets.QWidget()
    ui = Ui_open()
    ui.setupUi(open)
    open.show()
    sys.exit(app.exec_())
