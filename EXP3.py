import PyQt5
import PyQt5.QtCore
from PyQt5.QtCore import *
import PyQt5.QtGui
from PyQt5.QtGui import *
import PyQt5.QtWidgets
from PyQt5.QtWidgets import *
import random
import sys
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

class Exp3_class(QWidget):
    def __init__(self):
        super().__init__()
        self.tabs3 = QTabWidget()
        self.tab13 = QWidget()
        self.tab23 = QWidget()
        self.tab33 = QWidget()
        self.tab43 = QWidget()

        self.tabs3.addTab(self.tab13,"Theory")
        self.tabs3.addTab(self.tab23,"Perform")
        self.tabs3.addTab(self.tab33, "Video")
        self.tabs3.addTab(self.tab43, "Question Bank")

        self.templab3 = QLabel("Mark Room Temp(C):")
        self.tempLine3 = QDial()
        self.tempLine3.setNotchesVisible(True)
        self.tempLine3.setRange(10, 80)
        self.tempLine3.valueChanged.connect(self.changedValue_temp3)
        self.tempLineDisplay3 = QLabel(":~NA~:")
        self.tempLineDisplay3.setAlignment(Qt.AlignCenter)
        
        self.tempBox3 = QGroupBox()
        self.tempLay3 = QFormLayout()
        
        self.tempLay3.addRow(self.templab3)
        self.tempLay3.addRow(self.tempLineDisplay3, self.tempLine3)

        self.tempBox3.setLayout(self.tempLay3)

        self.SolLab = QLabel("Vol and Conc of Given Soln:")
        self.rowTit_13 = QLabel("Soln")
        self.rowTit_23 = QLabel("Conc")
        self.rowTit_33 = QLabel("Volm")

        self.HclLab = QLabel("HCl:")
        self.C2h5Lab = QLabel("C2H5OH:")
        self.Ch3Lab = QLabel("CH3COOH:")

        self.Hcl_spin_n = QDoubleSpinBox()
        self.Hcl_spin_v = QDoubleSpinBox()
        self.C2h5_spin_n = QDoubleSpinBox()
        self.C2h5_spin_v = QDoubleSpinBox()
        self.Ch3_spin_n = QDoubleSpinBox()
        self.Ch3_spin_v = QDoubleSpinBox()
        
        self.next13 = QPushButton("Validate")
        self.next13.setEnabled(True)
        self.next13.clicked.connect(self.ValidateEqui)

        self.tempBox23 = QGroupBox()
        
        self.tempLay23 = QFormLayout()
        self.tempLay23.addRow(self.SolLab)

        self.tempBox23b = QWidget()
        self.tempLay23g = QGridLayout()        
        self.tempLay23g.addWidget(self.rowTit_13, 0, 0)
        self.tempLay23g.addWidget(self.rowTit_23, 0, 1)
        self.tempLay23g.addWidget(self.rowTit_33, 0, 2)
        
        self.tempLay23g.addWidget(self.HclLab, 1, 0)
        self.tempLay23g.addWidget(self.Hcl_spin_n, 1, 1)
        self.tempLay23g.addWidget(self.Hcl_spin_v, 1, 2)
        
        self.tempLay23g.addWidget(self.C2h5Lab, 2, 0)
        self.tempLay23g.addWidget(self.C2h5_spin_n, 2, 1)
        self.tempLay23g.addWidget(self.C2h5_spin_v, 2, 2)
        
        self.tempLay23g.addWidget(self.Ch3Lab, 3, 0)
        self.tempLay23g.addWidget(self.Ch3_spin_n, 3, 1)
        self.tempLay23g.addWidget(self.Ch3_spin_v, 3, 2)

        self.tempBox23b.setLayout(self.tempLay23g)
        
        self.tempLay23.addRow(self.tempBox23b)
        self.tempLay23.addRow(self.next13)

        self.StandLab3 = QLabel("Standarizing NaOH:")
        #self.useOxa3 = QLabel("(Using Oxalic Acid)")

        self.OxaStren3 = QLabel("Strength Oxa.Acid")
        self.OxaStrenLine3 = QDoubleSpinBox()
        self.OxaUsed3 = QLabel("Vol of Oxa.Acid :")
        self.OxaUsedLine3 = QDoubleSpinBox()
        
        self.NaUsed3 = QLabel("Vol of NaOH :")
        self.NaUsedLine3 = QLabel("~NA~")
        #self.NaUsedLine3.setReadOnly(True)
        self.tit_13 = QGroupBox()
        self.tempLay23_tit_13 = QFormLayout()

        self.tempLay23_tit_13.addRow(self.StandLab3)
        #self.tempLay23_tit_13.addRow(self.useOxa3)
        self.tempLay23_tit_13.addRow(self.OxaStren3, self.OxaStrenLine3)
        self.tempLay23_tit_13.addRow(self.OxaUsed3, self.OxaUsedLine3)
        self.tempLay23_tit_13.addRow(self.NaUsed3, self.NaUsedLine3)
        self.tit_13.setLayout(self.tempLay23_tit_13)
        self.next_NaSt = QPushButton("Generate")
        self.next_NaSt.setEnabled(False)
        self.temp_naoh3 = QLineEdit()
        self.temp_naoh3.setReadOnly(True)
        self.next_NaSt.clicked.connect(self.getGenerateNaOh)################
        #print("second box")
        self.tempLay23.addRow(self.tit_13)
        self.tempLay23.addRow(self.next_NaSt)
        self.tempBox23.setLayout(self.tempLay23)

        self.labe23 = QLabel("Standarizing HCl:")
        self.NaohUsded_3 = QLabel("Vol of NaOH taken:")
        self.NaohUsded_spin_3 = QDoubleSpinBox()
        self.VolLab23 = QLabel("Vol of HCl :")
        self.volLabHcl3 = QLabel("~NA~")
        self.temp_hcl3 = QLineEdit()
        self.temp_hcl3.setReadOnly(True)
        self.next23 = QPushButton("Generate")
        self.next23.setEnabled(False)
        self.next23.clicked.connect(self.getGenerateHCL)

        self.tempBox33 = QGroupBox()
        self.tempLay33 = QFormLayout()
        
        self.tempLay33.addRow(self.labe23)
        self.tempLay33.addRow(self.NaohUsded_3, self.NaohUsded_spin_3)
        self.tempLay33.addRow(self.VolLab23, self.volLabHcl3)
        self.tempLay33.addRow(self.next23)
        
        self.tempBox33.setLayout(self.tempLay33)
        #print("HCl done")
        
        self.labe33 = QLabel("Equilibrium state:")
        self.labe43= QLabel("Titrate the whole contents\nof the bottle")
        self.Indicator3 = QLabel("Indicator :")
        self.IndicatorDrop3 = QComboBox()
        self.IndicatorDrop3.addItems(["Phenolpthalein", "Indicator 2",
                                      "Indicator 3"])
        self.VolLast3 = QLabel("Vol of NaOH :")
        self.VolLine3 = QLabel("~NA~")
        #self.VolLine3.setReadOnly(True)
        self.LastBut3 = QPushButton("Generate")
        self.LastBut3.setEnabled(False)
        self.LastBut3.clicked.connect(self.getEquiHcl)
        self.NLast3 = QLineEdit()

        self.tempBox43 = QGroupBox()
        self.tempLay43 = QFormLayout()
        
        self.tempLay43.addRow(self.labe33)
        self.tempLay43.addRow(self.labe43)
        self.tempLay43.addRow(self.Indicator3, self.IndicatorDrop3)
        self.tempLay43.addRow(self.VolLast3, self.VolLine3)
        self.tempLay43.addRow(self.LastBut3)
        self.tempBox43.setLayout(self.tempLay43)
        
        self.HomeLay3 = QVBoxLayout()
        
        
        for i in[self.tempBox3, self.tempBox23, self.tempBox33, self.tempBox43]:
            self.HomeLay3.addWidget(i)
            
        #print("widgets added")
        
        self.Title3 = QLabel("DETERMINING THE EQUILIBRIUM CONSTANT")
        self.Title3.setAlignment(Qt.AlignCenter)
        self.movie23 = QMovie("test_tube.gif")
        
        self.movie3 = QLabel()
        
        self.movie3.setMovie(self.movie23)
        self.movie23.start()
        ##print("insideClass2")
        
        ##print("insideClassMid")
        self.movieBox3 = QVBoxLayout()
        self.movieBox3.addWidget(self.Title3)
        self.movieBox3.addWidget(self.movie3)
        self.group13 = QGroupBox()
        self.group13.setLayout(self.movieBox3)
        self.group23 = QGroupBox()
        self.group23.setLayout(self.HomeLay3)

        self.pageBox3 = QHBoxLayout()
        self.pageBox3.addWidget(self.group23)
        self.pageBox3.addWidget(self.group13)
        
        self.tab23.setLayout(self.pageBox3)

        #print("tab2 done")
        #self.tab1text = QPlainTextEdit()
        
        self.l13 = QLabel()
        self.l13.setPixmap(QPixmap("equi-1.jpg"))
        #self.l1.setAlignment(Qt.AlignCenter)
        self.l13.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l13.setAlignment(Qt.AlignCenter)
        
        self.l23 = QLabel()
        self.l23.setPixmap(QPixmap("equi-2.jpg"))
        self.l23.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l23.setAlignment(Qt.AlignCenter)

        
        self.tab1Lay3 = QVBoxLayout()
        self.tab1Lay3.addWidget(self.l13)
        self.tab1Lay3.addWidget(self.l23)


        self.scrollWidget3 = QWidget()
        self.scrollWidget3.setLayout(self.tab1Lay3)
        
        self.scrollAr3 = QScrollArea()
        self.scrollAr3.setWidget(self.scrollWidget3)
        
        self.tab1Lay23 = QVBoxLayout()
        self.tab1Lay23.addWidget(self.scrollAr3)
        
        self.tab13.setLayout(self.tab1Lay23)
        #print("tab1 done")        

        self.tab3text3 = QPlainTextEdit()
        self.tab4text3 = QPlainTextEdit()

        self.mediaPlayer3 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.playButton3 = QPushButton()
        self.playButton3.setText("Play")
        self.playButton3.setEnabled(True) #default is on False, will not play video
        #self.playButton3.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay)) #How the button looks
        self.playButton3.clicked.connect(self.play3)  #when clicked, should play
 
        self.positionSlider3 = QSlider(Qt.Horizontal) #the video slider
        self.positionSlider3.setRange(0, 0) #setting the range of the slider
        self.positionSlider3.sliderMoved.connect(self.setPosition3)
 
        self.errorLabel3 = QLabel()
        self.errorLabel3.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
 
        # Create a widget for window contents
 
        # Create layouts to place inside widget
        self.videoWidget3 = QVideoWidget()
        self.controlLayout3 = QHBoxLayout()
        self.controlLayout3.setContentsMargins(0, 0, 0, 0)
        self.controlLayout3.addWidget(self.playButton3)
        self.controlLayout3.addWidget(self.positionSlider3)
 
        self.layout3 = QVBoxLayout()
        self.layout3.addWidget(self.videoWidget3)
        self.layout3.addLayout(self.controlLayout3)
        self.layout3.addWidget(self.errorLabel3)
 
        # Set widget to contain window contents
        self.Video_widget3 = QWidget()
        self.Video_widget3.setLayout(self.layout3)
 
        self.mediaPlayer3.setVideoOutput(self.videoWidget3)
        self.mediaPlayer3.stateChanged.connect(self.mediaStateChanged3)
        self.mediaPlayer3.positionChanged.connect(self.positionChanged3)
        self.mediaPlayer3.durationChanged.connect(self.durationChanged3)
        self.mediaPlayer3.error.connect(self.handleError3)
        self.loaded3 = 0

        self.tab3Lay3 = QVBoxLayout()
        self.tab3Lay3.addWidget(self.Video_widget3)
        self.tab33.setLayout(self.tab3Lay3)
        
        self.tab4Lay3 = QVBoxLayout()
        self.tab4Lay3.addWidget(self.tab4text3)
        
        self.tab43.setLayout(self.tab4Lay3)

        #self.backHome3 = QPushButton("Back")
        #self.backHome3.clicked.connect(self.goBackToDef)
        self.HomePage_lay3 = QHBoxLayout()
        self.HomePage_lay3.addWidget(self.tabs3)
        #self.HomePage_lay3.addWidget(self.backHome3)
        #print("back button added")
       
        self.Exp3_widget = QWidget()
        self.setLayout(self.HomePage_lay3)
        self.setGeometry(100,100,200,200)
        self.Exp3_widget.setWindowTitle("Experiment 3")

        ##print("insideClassend")
    def changedValue_temp3(self):
        self.tempLineDisplay3.setText(":"+str(self.tempLine3.value())+" Deg C:")
        #self.next3.setEnabled(True)
    def ValidateEqui(self):

        for i, j in zip([self.Hcl_spin_v, self.C2h5_spin_v, self.Ch3_spin_v],
                     [self.Hcl_spin_n, self.C2h5_spin_n, self.Ch3_spin_n]):
            if(i.value() <= 0.00 or j.value() <= 0.00):
                self.errorMessage()
                return
            else :
                continue
        
        self.next_NaSt.setEnabled(True)
    def getGenerateNaOh(self):

        for i in [self.OxaStrenLine3, self.OxaUsedLine3]:
            if(i.value()<= 0.00):
                self.errorMessage()
                return
        n1 = self.OxaStrenLine3.value() + (((float(random.randint(-200, 200)))/10000)*self.OxaStrenLine3.value())
        n2 = (float(random.randint(80, 200))/100)+ ((float(random.randint(-1000, 9999)))/10000)
        v1 = self.OxaUsedLine3.value() + (((float(random.randint(-200, 200)))/10000)*self.OxaUsedLine3.value())
        #self.OxaUsed3 = QLabel("Vol of Oxa.Acid :")
        v2 ="%.3f" % ((n1*v1)/n2)
        
        self.NaUsedLine3.setText(str(v2)+" ml")
        self.temp_naoh3.setText(str(n2))
        self.next23.setEnabled(True)

    def getGenerateHCL(self):
        for i in [self.NaohUsded_spin_3]:
            if(i.value()<= 0.00):
                self.errorMessage()
                return
        #print("Oka")
        n1 = float(self.temp_naoh3.text())
        #print("Okay")
        n2 = self.Hcl_spin_n.value() + (((float(random.randint(-1000, 1000)))/10000)*self.Hcl_spin_n.value())
        v1 = self.NaohUsded_spin_3.value() + (((float(random.randint(-500, 500)))/10000)*self.NaohUsded_spin_3.value())
        v2 = "%.3f" % ((n1*v1)/n2)
        self.volLabHcl3.setText(str(v2)+" ml")
        self.temp_hcl3.setText(str(n2))
        self.LastBut3.setEnabled(True)

    def getEquiHcl(self):
        
        c_c2h5 = self.C2h5_spin_n.value()
        v_c2h5 = self.C2h5_spin_v.value()
        c_ch3 = self.C2h5_spin_n.value()
        v_ch3 = self.Ch3_spin_v.value()

        #print("okaty")
        volume_tot = self.Hcl_spin_v.value()+ self.C2h5_spin_v.value()+self.Ch3_spin_v.value()
        #print("okay2")

        n1 = float(self.temp_hcl3.text())
        #print("Okay")
        n1 = n1 + c_ch3*v_ch3*0.5
        v1 = volume_tot
        n2 = float(self.temp_naoh3.text())
        #print("Okay")
        v2 = (n1*v1)/n2
        self.VolLine3.setText(str(v2))
        
        
    
        
    def play3(self):
        
        fileName = "exp3.mp4"
        if self.loaded3 == 0:
            self.mediaPlayer3.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton3.setEnabled(True)
            self.playButton3.setText("Pause")
            self.loaded3 = 1
            
        if self.mediaPlayer3.state() == QMediaPlayer.PlayingState:
            self.playButton3.setText("Play")
            self.mediaPlayer3.pause()
        else:
            self.mediaPlayer3.play()
            self.playButton3.setText("Pause")
 
    def mediaStateChanged3(self, state):
        if self.mediaPlayer3.state() == QMediaPlayer.PlayingState:
            self.playButton3.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton3.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
 
    def positionChanged3(self, position):
        self.positionSlider3.setValue(position)
 
    def durationChanged3(self, duration):
        self.positionSlider3.setRange(0, duration)
 
    def setPosition3(self, position):
        self.mediaPlayer3.setPosition(position)
 
    def handleError3(self):
        self.playButton3.setEnabled(False)
        self.errorLabel3.setText("Error: " + self.mediaPlayer3.errorString())

    def errorMessage(self):
        self.w = QMessageBox()
        self.w.resize(150, 150)
        self.w.setIcon(QMessageBox.Warning)
        self.w.setInformativeText("Invalid entry !")
        self.w.setWindowTitle("Warning")
        self.w.exec()


def main_exp3():
    obj = Exp3_class()
    return obj
