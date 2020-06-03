# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'score.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fscore(object):
    def setupUi(self, fscore):
        fscore.setObjectName("fscore")
        fscore.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(fscore)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(375, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(fscore)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(fscore)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(fscore)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(375, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(fscore)
        QtCore.QMetaObject.connectSlotsByName(fscore)

    def retranslateUi(self, fscore):
        _translate = QtCore.QCoreApplication.translate
        fscore.setWindowTitle(_translate("fscore", "Form"))
        self.label.setText(_translate("fscore", "Your Score For The Game Is:"))
        self.label_2.setText(_translate("fscore", "Have a Nice Day"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fscore = QtWidgets.QWidget()
    ui = Ui_fscore()
    ui.setupUi(fscore)
    fscore.show()
    sys.exit(app.exec_())
