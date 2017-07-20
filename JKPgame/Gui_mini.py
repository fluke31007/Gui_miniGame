import sys
from PySide import QtGui,QtCore
import JKPgame.Func  as Fun
reload (Fun)
a = Fun.Function()
class Main(QtGui.QDialog):
    def __init__(self):
        super(Main,self).__init__()
        self.setGeometry(450,200,400,400)
        self.Widget()
        self.Layout()
        self.Connect()
        
    def Widget(self):
        self.btn1 = QtGui.QPushButton('OK')
        self.bar = QtGui.QMenuBar()
        self.mass = QtGui.QMenu('Massage')
        self.reset = QtGui.QAction('Reset',self)
        self.exit = QtGui.QAction('Exit',self)        
        self.gameName = QtGui.QLabel('Game Name')
        self.hp1 = QtGui.QLabel('HP')
        self.hp2 = QtGui.QLabel('HP')
        self.turn = QtGui.QLabel('00')
        self.heroN = QtGui.QLabel('Hero')
        self.heroImg = QtGui.QPixmap('D:/Icon_jkp/PHero.png')
        self.MonsImg = QtGui.QPixmap('D:/Icon_jkp/PDemon.png')
        self.backImg = QtGui.QPixmap('C:/Program Files/Autodesk/Maya2016/icons/blank.png')
        self.RockImg = QtGui.QIcon('D:/Icon_jkp/Rk.png')
        self.ScImg = QtGui.QIcon('D:/Icon_jkp/Sc.png')
        self.PpImg = QtGui.QIcon('D:/Icon_jkp/Pp.png')
        self.heroPic= QtGui.QLabel()
        self.heroPic.setPixmap(QtGui.QPixmap(self.heroImg))
        self.heroPic2= QtGui.QLabel()
        self.heroPic2.setPixmap(QtGui.QPixmap(self.heroImg))
        self.MonsPic= QtGui.QLabel()
        self.MonsN = QtGui.QLabel('Monster')
        self.MonsPic.setPixmap(QtGui.QPixmap(self.MonsImg))
        self.blank = QtGui.QLabel()
        self.blank.setPixmap(QtGui.QPixmap(self.backImg))
        self.MonsC = QtGui.QLabel()
        self.MonsC.setPixmap(QtGui.QPixmap(self.backImg))
        self.C1= QtGui.QPushButton()
        self.C1.setIcon(QtGui.QIcon(self.RockImg))
        self.C1.setIconSize(QtCore.QSize(100,100))
        self.C2= QtGui.QPushButton()
        self.C2.setIcon(QtGui.QIcon(self.ScImg))
        self.C2.setIconSize(QtCore.QSize(100,100))
        self.C3= QtGui.QPushButton()
        self.C3.setIcon(QtGui.QIcon(self.PpImg))
        self.C3.setIconSize(QtCore.QSize(100,100))
        self.heroHp = QtGui.QProgressBar()
        self.heroHp.setTextVisible(0)
        self.heroHp.setRange(0,10)
        self.MonsHp = QtGui.QProgressBar()
        self.MonsHp.setInvertedAppearance(True)
        self.MonsHp.setTextVisible(0)
        self.MonsHp.setRange(0,10)
        self.heroHp.setValue(a.HeroHp)
        self.MonsHp.setValue(a.MonsHp)
        self.wid= QtGui.QWidget()
    def Layout(self):
        mainLayout = QtGui.QVBoxLayout()
        topLayout = QtGui.QHBoxLayout()
        statLayout = QtGui.QHBoxLayout()
        charLayout = QtGui.QHBoxLayout()
        nameLayout = QtGui.QHBoxLayout()
        cardLayout = QtGui.QHBoxLayout()
        self.bar.addMenu(self.mass)        
        self.mass.addAction(self.reset)
        self.mass.addSeparator()
        self.mass.addAction(self.exit)
        topLayout.addWidget(self.gameName)
        topLayout.setAlignment(QtCore.Qt.AlignCenter)
        statLayout.addWidget(self.hp1)
        statLayout.addWidget(self.heroHp)
        self.heroHp.setAlignment(QtCore.Qt.AlignCenter)
        statLayout.addWidget(self.turn)
        statLayout.addWidget(self.MonsHp)
        statLayout.addWidget(self.hp2)
        statLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.MonsHp.setAlignment(QtCore.Qt.AlignCenter)
        charLayout.addWidget(self.heroPic)
        charLayout.addWidget(self.blank)
        charLayout.addWidget(QtGui.QLabel('VS'))
        charLayout.addWidget(self.MonsC)
        charLayout.addWidget(self.MonsPic)
        nameLayout.addWidget(self.heroN)
        nameLayout.addWidget(self.MonsN)
        nameLayout.setAlignment(self.heroN,QtCore.Qt.AlignLeft)
        nameLayout.setAlignment(self.MonsN,QtCore.Qt.AlignRight)
        cardLayout.addWidget(self.C1)
        cardLayout.addWidget(self.C2)
        cardLayout.addWidget(self.C3)
        cardLayout.setAlignment(QtCore.Qt.AlignCenter)
        mainLayout.setMenuBar(self.bar)
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(statLayout)
        mainLayout.addLayout(charLayout)
        mainLayout.addLayout(nameLayout)
        mainLayout.addLayout(cardLayout)
        self.setLayout(mainLayout)
        self.setWindowTitle('Hello Bubble')

    def Connect(self):
        self.exit.triggered.connect(self.close)
        self.reset.triggered.connect(self.resetGame)
        self.btn1.clicked.connect(self.widClose)
        self.C1.clicked.connect(self.Rock)
        self.C2.clicked.connect(self.Scissor)
        self.C3.clicked.connect(self.Paper)
    def Rock(self):
    	self.blank.setPixmap(QtGui.QPixmap('D:/Icon_jkp/Rk.png'))
    	self.Hpick = 'rock'
        self.turn.setText('%02d'%a.turnC)
        a.HeroCard =0
        self.monUCard()
        
    def Scissor(self):
        self.blank.setPixmap(QtGui.QPixmap('D:/Icon_jkp/Sc.png'))
        self.Hpick = 'Scissor'
        self.turn.setText('%02d'%a.turnC)
        a.HeroCard =1
        self.monUCard()
       
        
    def Paper(self):
        self.blank.setPixmap(QtGui.QPixmap('D:/Icon_jkp/Pp.png'))
        self.Hpick = 'paper'
        self.turn.setText('%02d'%a.turnC)
        a.HeroCard =2
        self.monUCard()
        
    def monUCard(self):
        a.MonRan()
        if a.MonsCard ==0:
            self.MonsC.setPixmap(QtGui.QPixmap('D:/Icon_jkp/Rk.png'))
        elif a.MonsCard ==1:
            self.MonsC.setPixmap(QtGui.QPixmap('D:/Icon_jkp/Sc.png'))
        elif a.MonsCard ==2:
            self.MonsC.setPixmap(QtGui.QPixmap('D:/Icon_jkp/Pp.png'))
        a.checkCard()
        self.heroHp.setValue(a.HeroHp)
        self.MonsHp.setValue(a.MonsHp)
        self.checkHP()
    def resetGame(self):
        a.reset()
        self.heroHp.setValue(a.HeroHp)
        self.MonsHp.setValue(a.MonsHp)
        self.turn.setText('%02d'%a.turnC)
        self.blank.setPixmap(QtGui.QPixmap(self.backImg))
        self.MonsC.setPixmap(QtGui.QPixmap(self.backImg))
    def checkHP(self):
        if a.HeroHp>0 and a.MonsHp<=0:
            self.winlog()
        elif a.HeroHp<=0 and a.MonsHp >0:
            self.winlog()

    def winlog(self):
    	self.wid.setGeometry(550,250,200,200)
        mLayout = QtGui.QVBoxLayout()
        logLayout1 = QtGui.QHBoxLayout()
        logLayout2 = QtGui.QHBoxLayout()
        self.txt1= QtGui.QLabel('You Win')
        self.txt2 =QtGui.QLabel('You Lose')
        if a.HeroHp>0 and a.MonsHp<=0:
            logLayout1.addWidget(self.heroPic)
            logLayout1.addWidget(self.txt1)
        elif a.HeroHp<=0 and a.MonsHp>0:
            logLayout1.addWidget(self.MonsPic)
            logLayout1.addWidget(self.txt2)
        logLayout2.addWidget(self.btn1)
        mLayout.addLayout(logLayout1)
        mLayout.addLayout(logLayout2)
        self.wid.setLayout(mLayout)
        self.wid.show()
        app1 = QtGui.QApplication(sys.argv)
        app1.exec_()
    def widClose(self):
        self.wid.close()

try:
    window.close()
except:
    pass
app = QtGui.QApplication(sys.argv)
window=Main()
window.show()
app.exec_()