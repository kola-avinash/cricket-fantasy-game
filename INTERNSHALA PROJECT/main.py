# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from newteam import Ui_New_team 
from openteam import Ui_open                
from evaluateteam import Ui_Evaluate_team   
from error import Ui_error      
from points import Player_points  

import sqlite3
fanta=sqlite3.connect('cricket.db')
cursfanta=fanta.cursor()

class Ui_MainWindow(object):
    def __init__(self):                        
        self.New_team=QtWidgets.QWidget()
        self.new_ui=Ui_New_team()
        self.new_ui.setupUi(self.New_team)

        self.open=QtWidgets.QWidget()
        self.open_ui=Ui_open()
        self.open_ui.setupUi(self.open)

        self.Evaluate_team = QtWidgets.QWidget()
        self.eva_ui = Ui_Evaluate_team()
        self.eva_ui.setupUi(self.Evaluate_team)

        self.Error = QtWidgets.QWidget()
        self.error_ui = Ui_error()
        self.error_ui.setupUi(self.Error)

    
    def new_team(self):
        self.New_team.show()
    
    def open_team(self):
        self.open.show()
        self.open_ui.open_btn.clicked.connect(self.opentm)
        

    def evaluate_team(self):
        self.Evaluate_team.show()
        
 
    def quit(self):
        print("You have exited the fantasy cricket game")
        print("Thank You for playing!")
        sys.exit(app.exec_())
        
    def err(self):
        self.Error.show()

    def setupUi(self, MainWindow):
        self.avp =1000 
        self.usdpnts = 0
        self.Bats = 0 
        self.bol = 0 
        self.alRn = 0 
        self.wkt = 0 
        self.total=0

        self.p=[]
        self.q=[]
        self.r=[]
        self.s=[]
        self.list = []
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(984, 826)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.batcount = QtWidgets.QLineEdit(self.centralwidget)
        self.batcount.setFocusPolicy(QtCore.Qt.NoFocus)
        self.batcount.setStyleSheet("\n"
"font: 8pt \"Comic Sans MS\";")
        self.batcount.setObjectName("batcount")
        self.horizontalLayout.addWidget(self.batcount)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.bowcount = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bowcount.setFont(font)
        self.bowcount.setObjectName("bowcount")
        self.horizontalLayout.addWidget(self.bowcount)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.arcount = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.arcount.setFont(font)
        self.arcount.setObjectName("arcount")
        self.horizontalLayout.addWidget(self.arcount)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.wkcount = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.wkcount.setFont(font)
        self.wkcount.setObjectName("wkcount")
        self.horizontalLayout.addWidget(self.wkcount)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.pointava = QtWidgets.QLineEdit(self.centralwidget)
        self.pointava.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pointava.setReadOnly(True)  #
        self.pointava.setObjectName("pointava")
        self.horizontalLayout_2.addWidget(self.pointava)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.pointused = QtWidgets.QLineEdit(self.centralwidget)
        self.pointused.setReadOnly(True)   #
        self.pointused.setObjectName("pointused")
        self.horizontalLayout_2.addWidget(self.pointused)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radbat = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radbat.setFont(font)
        self.radbat.setObjectName("radbat")
        self.radbat.setDisabled(True)
        self.radbat.clicked.connect(self.checkstate)#Bat radio button signal
        self.horizontalLayout_3.addWidget(self.radbat)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.radbow = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radbow.setFont(font)
        self.radbow.setObjectName("radbow")
        self.radbow.setDisabled(True)
        self.radbow.clicked.connect(self.checkstate)#Bow radio button signal
        self.horizontalLayout_3.addWidget(self.radbow)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.radar = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radar.setFont(font)
        self.radar.setObjectName("radar")
        self.radar.setDisabled(True)
        self.radar.clicked.connect(self.checkstate)#AR radio button signal
        self.horizontalLayout_3.addWidget(self.radar)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.radwk = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radwk.setFont(font)
        self.radwk.setObjectName("radwk")
        self.radwk.setDisabled(True)
        self.radwk.clicked.connect(self.checkstate)#WK radio button signal
        self.horizontalLayout_3.addWidget(self.radwk)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.teamname = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.teamname.setFont(font)
        self.teamname.setReadOnly(True)
        self.teamname.setObjectName("teamname")
        self.horizontalLayout_3.addWidget(self.teamname)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem15)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.teamavail = QtWidgets.QListWidget(self.centralwidget)
        self.teamavail.setObjectName("teamavail")
        self.teamavail.itemDoubleClicked.connect(self.removelist1)##Double click to remove
        self.horizontalLayout_4.addWidget(self.teamavail)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem16)
        self.teamselected = QtWidgets.QListWidget(self.centralwidget)
        self.teamselected.setObjectName("teamselected")
        self.teamselected.itemDoubleClicked.connect(self.removelist2)##Double click to remove
        self.horizontalLayout_4.addWidget(self.teamselected)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 984, 24))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menumanage_teams = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.menumanage_teams.setFont(font)
        self.menumanage_teams.setObjectName("menumanage_teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        self.actionAdd_Team.setFont(font)
        self.actionAdd_Team.setObjectName("actionAdd_Team")
        self.actionAdd_Team.triggered.connect(self.new_team) 
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        self.actionOpen_Team.setFont(font)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionOpen_Team.triggered.connect(self.open_team) 
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        self.actionSave_Team.setFont(font)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionSave_Team.triggered.connect(self.savetm)
        self.Evaluate_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        self.Evaluate_Team.setFont(font)
        self.Evaluate_Team.setObjectName("Evaluate_Team")
        self.Evaluate_Team.triggered.connect(self.evaluate_team)#Evaluate Team signal
        self.actionQuit = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        self.actionQuit.setFont(font)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.triggered.connect(self.quit)
        self.menumanage_teams.addAction(self.actionAdd_Team)
        self.menumanage_teams.addAction(self.actionOpen_Team)
        self.menumanage_teams.addAction(self.actionSave_Team)
        self.menumanage_teams.addAction(self.Evaluate_Team)
        self.menumanage_teams.addSeparator()
        self.menumanage_teams.addAction(self.actionQuit)
        self.menubar.addAction(self.menumanage_teams.menuAction())
        self.new_ui.createteam.clicked.connect(self.create) #new team signal
        self.error_ui.ok_btn.clicked.connect(self.close)    #error button signal
        self.stats={}       #stats list

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "Your selections:"))
        self.label.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.batcount.setText(_translate("MainWindow", "##"))
        self.label_2.setText(_translate("MainWindow", "Bowler(bowl)"))
        self.bowcount.setText(_translate("MainWindow", "##"))
        self.label_3.setText(_translate("MainWindow", "All Rounder(AR)"))
        self.arcount.setText(_translate("MainWindow", "##"))
        self.label_4.setText(_translate("MainWindow", "Wicket Keeper(WKT"))
        self.wkcount.setText(_translate("MainWindow", "##"))
        self.label_5.setText(_translate("MainWindow", " Points Available"))
        self.pointava.setText(_translate("MainWindow", "###"))
        self.label_6.setText(_translate("MainWindow", "Points Used"))
        self.pointused.setText(_translate("MainWindow", "###"))
        self.radbat.setText(_translate("MainWindow", "BAT"))
        self.radbow.setText(_translate("MainWindow", "BOW"))
        self.radar.setText(_translate("MainWindow", "AR"))
        self.radwk.setText(_translate("MainWindow", "WK"))
        self.label_7.setText(_translate("MainWindow", "Team Name"))
        self.menumanage_teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionAdd_Team.setText(_translate("MainWindow", "Add Team"))
        self.actionAdd_Team.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionOpen_Team.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionSave_Team.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

        
    def create(self):
        self.tname=self.new_ui.inpteamname.text()       #throws an error if name is left empty
        if len(self.tname) == 0:
            self.err()
            self.error_ui.error_text.setText("This field cannot be empty!")

        elif self.tname.isnumeric():            #throws an error if name is numbers only#
            self.err()
            self.error_ui.error_text.setText("Please enter a valid teamname\n(Name must contain atleast one character)!!")
            
        else:
            self.tname=self.new_ui.inpteamname.text()
            self.teamname.setText(" "+self.tname)      #creates the team with the given name#
            self.reset()
            self.New_team.close()

    def close(self):            #closes error window
        self.Error.close()

    def savetm(self):       #save team function#
        self.tname=self.teamname.text()         
        cursfanta.execute("SELECT DISTINCT Name FROM teams")
        y=cursfanta.fetchall()
        for i in y:
            if i[0]==self.tname:                        #checks if team already exists#
                self.err()
                self.error_ui.error_text.setText("Team with same name already exists!!\nPlease choose another name")
                return 0
            
        if self.mist():     #Error handler
            self.err()
            self.error_ui.error_text.setText("Insufficient Players or Points!!!")
            return 0
            
        elif self.teamselected.count() <=10: #counts the number of players if players are less throws an error
            self.err()
            self.error_ui.error_text.setText("Insufficient Players!!!")
            return 0
            
        else:
            try:
                cursfanta.execute("SELECT DISTINCT Name FROM teams;")
                h=cursfanta.fetchall()
                for k in h:                             
                    if self.teamname.text() == k[0]:
                        cursfanta.execute("DELETE FROM teams WHERE Name='"+ self.teamname.text() + "';")
            except:
                print("error1")
            for k in range(self.teamselected.count()):      #saves the players list into database 
                try:
                    cursfanta.execute("INSERT INTO teams (Name, Players, Value) VALUES (?,?,?);",(self.teamname.text(), self.list[k], Player_points[self.list[k]]))
                    fanta.commit()
                except:
                    print("error2")
            fanta.commit()         
        
    def reset(self):                                    #resets all the functions when new team or existing team is opened#
        self.enablebuttons()
        self.checkstate()
        self.avp =1000
        self.pointava.setText(str(self.avp))
        self.usdpnts = 0
        self.pointused.setText(str(self.usdpnts))
        self.Bats = 0
        self.batcount.setText(str(self.Bats))
        self.bol = 0
        self.bowcount.setText(str(self.bol))
        self.alRn = 0
        self.arcount.setText(str(self.alRn))
        self.wkt = 0
        self.wkcount.setText(str(self.wkt))
        self.list.clear()
        self.checkstate()
        self.teamselected.clear()
        
    def enablebuttons(self):
        self.radbat.setEnabled(True)
        self.radbow.setEnabled(True)
        self.radar.setEnabled(True)          #enables all the features once toolbar menu is clicked#
        self.radwk.setEnabled(True)
        
    def checkstate(self):

        sql1="SELECT * from stats WHERE Ctg='BAT';"
        sql2="SELECT * from stats WHERE Ctg='BWL';"     #fetches the data from stats table in database#
        sql3="SELECT * from stats WHERE Ctg='AR';"
        sql4="SELECT * from stats WHERE Ctg='WK';"
          
        cursfanta.execute(sql1)
        a=cursfanta.fetchall()
        bats=[] #batsmen list
        for w in a:
            bats.append(w[0]) #appends batsmen name into lists# 
            self.p.append(w[0])#copy of batsmen lists# 
            self.stats[w[0]]=w[5]#selects value of respective players into list#
    
        cursfanta.execute(sql2)
        b=cursfanta.fetchall()
        bwl=[] #bowlers lists#
        for x in b:
            bwl.append(x[0])#appends bowlers name into lists#
            self.q.append(x[0])#copy of bowlers lists# 
            self.stats[x[0]]=x[5]#selects value of respective players into list#

        cursfanta.execute(sql3)
        c=cursfanta.fetchall()
        alR=[] #all-rounders lists#
        for y in c:
            alR.append(y[0])#appends all-rounders name into lists#
            self.stats[y[0]]=y[5]#copy of all-rounders lists# 
            self.r.append(y[0])#selects value of respective players into list#

        cursfanta.execute(sql4)
        d=cursfanta.fetchall()
        wK=[] #wicket-keepers lists#
        for z in d:
            wK.append(z[0])#appends wicket-keepers name into lists#
            self.stats[z[0]]=z[5]#copy of wicket-keepers lists#
            self.s.append(z[0])#selects value of respective players into list#

        for j in self.list:
            if j in bats:      
                bats.remove(j)
            elif j in bwl:
                bwl.remove(j)            #avoids occurence of players once removed from list#
            elif j in alR:
                alR.remove(j)
            elif j in wK:
                wK.remove(j)
                
        if self.radbat.isChecked() == True:           #adds Batsmen list upon clicking bat radio button#
            self.teamavail.clear()
            for i in range(len(bats)):
                item = QtWidgets.QListWidgetItem(bats[i])
                self.teamavail.addItem(item)

        elif self.radbow.isChecked() == True:         #adds bowlers list upon clicking bwl radio button#
            self.teamavail.clear()
            for i in range(len(bwl)):
                item = QtWidgets.QListWidgetItem(bwl[i])
                self.teamavail.addItem(item)

        elif self.radar.isChecked() == True:         #adds allrounders list upon clicking ar radio button#
            self.teamavail.clear()
            for i in range(len(alR)):
                item = QtWidgets.QListWidgetItem(alR[i])
                self.teamavail.addItem(item)
                
        elif self.radwk.isChecked() == True:          #adds wicketkeeper list upon clicking wk radio button#
            self.teamavail.clear()
            for i in range(len(wK)):
                item = QtWidgets.QListWidgetItem(wK[i])
                self.teamavail.addItem(item)

        
    def removelist1(self, item):    #removes item from available player's list#
        self.total=self.teamselected.count()
        if self.total > 10:
            self.err()
            self.error_ui.error_text.setText("Not more or less than 11 players allowed!")
        
        else:
            self.test_1(item.text())
            self.teamavail.takeItem(self.teamavail.row(item))
            self.teamselected.addItem(item.text())
            self.list.append(item.text())
            self.mist()
    
    def test_1(self, pt): #adding points to used points and deducting from available points#
        self.avp -= self.stats[pt]
        self.usdpnts += self.stats[pt]
        if pt in self.p:
            self.Bats+= 1
        elif pt in self.q:
            self.bol+= 1
        elif pt in self.r:
            self.alRn+= 1
        elif pt in self.s:
            self.wkt+=1
        self.pointava.setText(str(self.avp))
        self.pointused.setText(str(self.usdpnts))
        self.batcount.setText(str(self.Bats))
        self.bowcount.setText(str(self.bol))
        self.arcount.setText(str(self.alRn))   
        self.wkcount.setText(str(self.wkt)) 
            
    def removelist2(self, item):#removes item from selected player's list#
        self.total=self.teamselected.count()
        self.teamselected.takeItem(self.teamselected.row(item))
        self.teamavail.addItem(item.text())
        self.list.remove(item.text())
        self.test_2(item.text())


    def test_2(self, pt):   #adding points to available points and deducting from used points#
        self.avp += self.stats[pt]
        self.usdpnts -= self.stats[pt]
        if pt in self.p:
            self.Bats-=1
        elif pt in self.q:
            self.bol-=1
        elif pt in self.r:
            self.alRn-=1
        elif pt in self.s:
            self.wkt-=1

        self.pointava.setText(str(self.avp))
        self.pointused.setText(str(self.usdpnts))
        self.batcount.setText(str(self.Bats))
        self.bowcount.setText(str(self.bol))
        self.arcount.setText(str(self.alRn))
        self.wkcount.setText(str(self.wkt))
        
        
    def opentm(self): #function to open team when clicked open button#
        self.reset()
        tmname=self.open_ui.open_team_comboBox.currentText()
        self.teamname.setText(tmname)
        cursfanta.execute("SELECT Players from teams WHERE Name= '" + tmname + "';")
        y=cursfanta.fetchall()
        score=[]
        for i in y:
            cursfanta.execute("SELECT Value from stats WHERE Player='"+i[0]+"';")
            z=cursfanta.fetchone()
            score.append(z[0])
        sum=0
        for i in score:
            sum+=i
        self.teamselected.clear()
        self.checkstate()
        for i in y:
            self.teamselected.addItem(i[0])
            self.list.append(i[0])
            self.test_1(i[0])
        self.usdpnts = sum
        self.avp = 1000-sum
        self.pointava.setText(str(self.avp))
        self.pointused.setText(str(self.usdpnts))
        self.open.close()

    def mist(self): #error handling function
         if self.wkt>1:
            self.err()
            self.error_ui.error_text.setText("Only one wicketkeeper allowed!")
            self.reset()
            return 0
         elif self.avp <= -1:
            self.err()
            self.error_ui.error_text.setText("Insufficient Points!")
            self.reset()
            return 0
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
