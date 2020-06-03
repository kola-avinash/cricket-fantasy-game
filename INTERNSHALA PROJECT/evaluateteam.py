# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluateteam.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from score import Ui_fscore

import sqlite3
evs=sqlite3.connect('cricket.db')
cursev=evs.cursor()


class Ui_Evaluate_team(object):
    def __init__(self):                     
        self.fscore = QtWidgets.QWidget()
        self.scr_ui = Ui_fscore()
        self.scr_ui.setupUi(self.fscore)

    def showsc(self):
        self.fscore.show()              
    

    def setupUi(self, Evaluate_team):
        Evaluate_team.setObjectName("Evaluate_team")
        Evaluate_team.resize(1023, 841)
        self.verticalLayout = QtWidgets.QVBoxLayout(Evaluate_team)
        self.verticalLayout.setObjectName("verticalLayout")
        self.evaluate_heading = QtWidgets.QLabel(Evaluate_team)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.evaluate_heading.setFont(font)
        self.evaluate_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.evaluate_heading.setObjectName("evaluate_heading")
        self.verticalLayout.addWidget(self.evaluate_heading)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Eval_team_name = QtWidgets.QLabel(Evaluate_team)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Eval_team_name.setFont(font)
        self.Eval_team_name.setObjectName("Eval_team_name")
        self.horizontalLayout.addWidget(self.Eval_team_name)
        self.team_name_list = QtWidgets.QComboBox(Evaluate_team)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.team_name_list.setFont(font)
        self.team_name_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.team_name_list.setObjectName("team_name_list")
        self.horizontalLayout.addWidget(self.team_name_list)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.Eval_match = QtWidgets.QLabel(Evaluate_team)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Eval_match.setFont(font)
        self.Eval_match.setObjectName("Eval_match")
        self.horizontalLayout.addWidget(self.Eval_match)
        self.match_list = QtWidgets.QComboBox(Evaluate_team)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.match_list.setFont(font)
        self.match_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.match_list.setObjectName("match_list")
        self.match_list.addItem("")
        self.match_list.addItem("")
        self.match_list.addItem("")
        self.horizontalLayout.addWidget(self.match_list)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.eval_players = QtWidgets.QLabel(Evaluate_team)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.eval_players.setFont(font)
        self.eval_players.setIndent(7)
        self.eval_players.setObjectName("eval_players")
        self.horizontalLayout_3.addWidget(self.eval_players)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.Eval_points = QtWidgets.QLabel(Evaluate_team)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Eval_points.setFont(font)
        self.Eval_points.setIndent(-2)
        self.Eval_points.setObjectName("Eval_points")
        self.horizontalLayout_3.addWidget(self.Eval_points)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Players_list = QtWidgets.QListWidget(Evaluate_team)
        self.Players_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Players_list.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Players_list.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Players_list.setLineWidth(2)
        self.Players_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.Players_list.setObjectName("Players_list")
        self.horizontalLayout_4.addWidget(self.Players_list)
        self.Points_list = QtWidgets.QListWidget(Evaluate_team)
        self.Points_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Points_list.setFrameShape(QtWidgets.QFrame.Box)
        self.Points_list.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Points_list.setLineWidth(2)
        self.Points_list.setObjectName("Points_list")
        self.horizontalLayout_4.addWidget(self.Points_list)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem8 = QtWidgets.QSpacerItem(998, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(998, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem9)
        self.line = QtWidgets.QFrame(Evaluate_team)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        spacerItem10 = QtWidgets.QSpacerItem(998, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem10)
        spacerItem11 = QtWidgets.QSpacerItem(998, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem11)
        self.calc_scr_btn = QtWidgets.QPushButton(Evaluate_team)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.calc_scr_btn.setFont(font)
        self.calc_scr_btn.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.calc_scr_btn.setIconSize(QtCore.QSize(10, 10))
        self.calc_scr_btn.setAutoDefault(True)
        self.calc_scr_btn.setDefault(False)
        self.calc_scr_btn.setFlat(False)
        self.calc_scr_btn.setObjectName("calc_scr_btn")
        self.calc_scr_btn.clicked.connect(self.final)
        self.verticalLayout.addWidget(self.calc_scr_btn)
        spacerItem12 = QtWidgets.QSpacerItem(998, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem12)

        chosenTeam = self.team_name_list.currentText()
        self.newName(chosenTeam)
        self.team_name_list.currentTextChanged.connect(self.newName) 

        self.retranslateUi(Evaluate_team)
        QtCore.QMetaObject.connectSlotsByName(Evaluate_team)

    def retranslateUi(self, Evaluate_team):
        _translate = QtCore.QCoreApplication.translate
        Evaluate_team.setWindowTitle(_translate("Evaluate_team", "Form"))
        self.evaluate_heading.setText(_translate("Evaluate_team", "Evaluate your team performance"))
        self.Eval_team_name.setText(_translate("Evaluate_team", "Team name"))
        self.Eval_match.setText(_translate("Evaluate_team", "Match"))
        self.match_list.setItemText(0, _translate("Evaluate_team", "Match1"))
        self.match_list.setItemText(1, _translate("Evaluate_team", "Match2"))
        self.match_list.setItemText(2, _translate("Evaluate_team", "Match3"))
        self.eval_players.setText(_translate("Evaluate_team", "Players"))
        self.Eval_points.setText(_translate("Evaluate_team", "Points"))
        self.calc_scr_btn.setText(_translate("Evaluate_team", "Calculate Score"))

        z=cursev.execute("SELECT DISTINCT Name from teams;")
        tm=z.fetchall()
        for i in tm:
            self.team_name_list.addItem(i[0])

    def newName(self, c): #function to change players and points list whenever team name is changed#
        self.Players_list.clear()
        self.Points_list.clear()
        d=cursev.execute("SELECT Players from teams WHERE Name='" + c + "';")
        pl=d.fetchall()
        for i in pl:
            self.Players_list.addItem(i[0])
        e=cursev.execute("SELECT Value from teams WHERE Name='" + c + "';")
        val=e.fetchall()
        for m in val:
            self.Points_list.addItem(str(m[0]))

    def final(self): #function to calculate final score
        total_scr=0
        a=self.team_name_list.currentText()
        b=cursev.execute("SELECT Value from teams WHERE Name='" + a +"';")
        val=b.fetchall()
        for j in val:
            total_scr+=j[0]
        self.scr_ui.lineEdit.setText(str(total_scr))
        self.showsc()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Evaluate_team = QtWidgets.QWidget()
    ui = Ui_Evaluate_team()
    ui.setupUi(Evaluate_team)
    Evaluate_team.show()
    sys.exit(app.exec_())