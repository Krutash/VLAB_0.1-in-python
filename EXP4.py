from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
import sys
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
import math
class DragLabel(QLabel):
    def __init__(self, label, parent):
        super().__init__(label, parent)
        self.value = 0.001
        self.name = label
    def name_(self):
        return self.name
    def setName(self, name):
        self.name = name
        
    def value_(self):
        return self.value
    def setValue(self, value):
        self.value = value
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()
 
    def mouseMoveEvent(self, event):
        if not(event.buttons() & Qt.LeftButton):
            return
        else:
            drag = QDrag(self)
            mimedata = QMimeData()
            mimedata.setText(str(self.value_()))
            mimedata.setHtml(str(self.name_()))
            drag.setMimeData(mimedata)
            # createing the dragging effect
            pixmap = QPixmap(self.size()) # label size
 
            painter = QPainter(pixmap)
            painter.drawPixmap(self.rect(), self.grab())
            painter.end()
 
            drag.setPixmap(pixmap)
            drag.setHotSpot(event.pos())
            drag.exec_(Qt.CopyAction | Qt.MoveAction)
 
class DropLabel(QLineEdit):
    def __init__(self, label, parent):
        super().__init__(label, parent)
        self.nameDropped = label
        self.setAcceptDrops(True)

    def name_(self):
        return self.nameDropped
    def setName(self, name):
        self.nameDropped = name
 
    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()
 
    def dropEvent(self, event):
        pos = event.pos()
        text = event.mimeData().text()
        name = event.mimeData().html()
        self.setText(text)
        self.setName(name)
        event.acceptProposedAction()
        
class Exp4_class(QWidget):

    def __init__(self):
        super().__init__()
        self.tabs4 = QTabWidget()
        self.tab14 = QWidget()
        self.tab24 = QWidget()
        self.tab34 = QWidget()
        self.tab44 = QWidget()
        self.tabs4.addTab(self.tab14,"Theory")
        self.tabs4.addTab(self.tab24,"Perform")
        self.tabs4.addTab(self.tab34, "Video")
        self.tabs4.addTab(self.tab44, "Question Bank")

        self.GiveLab = QLabel("Given Kcl Solution")
        self.spin_b = QDoubleSpinBox()
        self.spin_b.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.spin_b.valueChanged.connect(self.NoteValue)
        self.AdjustLabel = QLabel("1. Adjust the Conductance\n and Calibrate")
        self.labTemp = QLabel("")
        
        self.formLay1 = QFormLayout()
        self.formLay1.addRow(self.GiveLab, self.spin_b)
        self.formLay1.addRow(self.AdjustLabel)
        self.widgetCond = QWidget()
        self.widgetCond.setLayout(self.formLay1)
        
        self.nextBut4 = QPushButton("Next")
        self.nextBut4.clicked.connect(self.setNext4)
        self.grpbox14 = QGroupBox()
        self.grpbox1lay4 = QVBoxLayout()
        self.grpbox1lay4.addWidget(self.widgetCond)
        self.grpbox14.setLayout(self.grpbox1lay4)

        self.PipLabel = QLabel("")
        self.makLab = QLabel("")
        self.UseLab2 = QLabel("")
        self.UseLab = QLabel("")
        self.TheCon = QLabel("Concentration of stock:")
        self.ConLine = QLineEdit()
        self.ConLine.setMaximumWidth(50)
        self.nextBut24 = QPushButton("Generate Stock")
        self.nextBut24.setEnabled(False)
        self.nextBut24.clicked.connect(self.validate)
        
        self.grpbo2lay4 = QFormLayout()
        self.grpbo2lay4.addRow(self.PipLabel)
        self.grpbo2lay4.addRow(self.makLab)
        self.grpbo2lay4.addRow(self.UseLab2)
        self.grpbo2lay4.addRow(self.TheCon, self.ConLine)
        self.grpbo2lay4.addRow(self.UseLab)
        self.grpbo2lay4.addRow(self.nextBut24)

        self.grpbo24 = QGroupBox()
        self.grpbo24.setLayout(self.grpbo2lay4)
        self.maklab = QLabel("Make up the Volm to 100ml using Stock:")
        self.rowTit_1 = QLabel("Conc")
        self.rowTit_3 = QLabel("Stock")

        self.n4 = QLabel("N/4")
        self.n8 = QLabel("N/8")
        self.n16 = QLabel("N/16")
        self.n32 = QLabel("N/32")
        self.n64 = QLabel("N/64")
        self.n128 = QLabel("N/128")
        self.spin_n4n = QDoubleSpinBox()
        self.spin_n8n = QDoubleSpinBox()
        self.spin_n16n = QDoubleSpinBox()
        self.spin_n32n = QDoubleSpinBox()
        self.spin_n64n = QDoubleSpinBox()
        self.spin_n128n = QDoubleSpinBox()
        self.validateBut = QPushButton("Generate Solns")
        self.validateBut.setEnabled(False)
        self.validateBut.clicked.connect(self.validate2)
        
        self.grpbo3lay4 = QGridLayout()
        self.grpbo3lay4.addWidget(self.rowTit_1, 1, 0)
        self.grpbo3lay4.addWidget(self.rowTit_3, 1, 1)
        
        self.grpbo3lay4.addWidget(self.n4, 2, 0)
        self.grpbo3lay4.addWidget(self.spin_n4n, 2, 1)

        self.grpbo3lay4.addWidget(self.n8, 3, 0)
        self.grpbo3lay4.addWidget(self.spin_n8n, 3, 1)
        self.grpbo3lay4.addWidget(self.n16, 4, 0)
        self.grpbo3lay4.addWidget(self.spin_n16n, 4, 1)
        self.grpbo3lay4.addWidget(self.n32, 5, 0)
        self.grpbo3lay4.addWidget(self.spin_n32n, 5, 1)
        self.grpbo3lay4.addWidget(self.n64, 6, 0)
        self.grpbo3lay4.addWidget(self.spin_n64n, 6, 1)
        self.grpbo3lay4.addWidget(self.n128, 7, 0)
        self.grpbo3lay4.addWidget(self.spin_n128n, 7, 1)
        

        self.grpbo34 = QGroupBox()
        self.temp1 = QGroupBox()
        self.temp1.setLayout(self.grpbo3lay4)
        
        self.grms34 = QVBoxLayout()
        self.grms34.addWidget(self.maklab)
        self.grms34.addWidget(self.temp1)
        self.grms34.addWidget(self.validateBut)
        
        self.grpbo34.setLayout(self.grms34)
        self.marklab = QLabel("Note Down Conductance below (in mS):")

        self.markn4 = QLabel("N/4")
        self.markn8 = QLabel("N/8")
        self.markn16 = QLabel("N/16")
        self.markn32 = QLabel("N/32")
        self.markn64 = QLabel("N/64")
        self.markn128 = QLabel("N/128")

        self.note_n4n = QLineEdit()
        self.note_n8n = QLineEdit()
        self.note_n16n = QLineEdit()
        self.note_n32n = QLineEdit()
        self.note_n64n = QLineEdit()
        self.note_n128n = QLineEdit()
        
        self.grpbo4lay = QFormLayout()
        self.grpbo4lay.addRow(self.marklab)

        self.grpbo4grid = QGridLayout()
        self.grpbo4grid.addWidget(self.markn4, 0, 0)
        self.grpbo4grid.addWidget(self.note_n4n, 0, 1)
        self.grpbo4grid.addWidget(self.markn8, 0, 2)
        self.grpbo4grid.addWidget(self.note_n8n, 0, 3)
        self.grpbo4grid.addWidget(self.markn16, 1, 0)
        self.grpbo4grid.addWidget(self.note_n16n, 1, 1)
        self.grpbo4grid.addWidget(self.markn32, 1, 2)
        self.grpbo4grid.addWidget(self.note_n32n, 1, 3)
        self.grpbo4grid.addWidget(self.markn64, 2, 0)
        self.grpbo4grid.addWidget(self.note_n64n, 2, 1)
        self.grpbo4grid.addWidget(self.markn128, 2, 2)
        self.grpbo4grid.addWidget(self.note_n128n, 2, 3)

        self.grpbo4gridBox = QWidget()
        self.grpbo4gridBox.setLayout(self.grpbo4grid)

        self.grpbo4lay.addRow(self.grpbo4gridBox)

        self.grpbo44 = QGroupBox()
        self.grpbo44.setLayout(self.grpbo4lay)
        
        self.side1box4 = QGroupBox()
        self.side1lay4 = QVBoxLayout()

        self.side1lay4.addWidget(self.grpbox14)
        self.side1lay4.addWidget(self.grpbo24)
        self.side1lay4.addWidget(self.grpbo34)
        self.side1lay4.addWidget(self.grpbo44)
        
        self.side1box4.setLayout(self.side1lay4)
        self.Titlelab4 = QLabel("DISSOCIATION CONSTANT")
        self.Titlelab4.setAlignment(Qt.AlignCenter)

        self.SolutionsAvaliabel = QLabel("Avalable Solutions :")

        self.StockSol = DragLabel("stock", self)
        self.StockSol.setPixmap(QPixmap("media/emptyflask.jpg"))
        self.StockSolLab = QLabel("Stock")
        self.StockSolLab.setAlignment(Qt.AlignCenter)

        self.KCLSol = DragLabel("KCl", self)
        self.KCLSol.setPixmap(QPixmap("media/smallflask.jpg"))
        self.KCLSol.setValue("%.3f" %(12.01 + (((float(random.randint(-200, 200)))/10000)*12.01)))
        self.KCLSolLab = QLabel("KCl")
        self.KCLSolLab.setAlignment(Qt.AlignCenter)
        
        self.N4Sol = DragLabel("N/4", self)
        self.N4Sol.setPixmap(QPixmap("media/emptyflask.jpg"))
        self.N4SolLab = QLabel("N/4")
        self.N4SolLab.setAlignment(Qt.AlignCenter)

        self.N8Sol = DragLabel("N/8", self)
        self.N8Sol.setPixmap(QPixmap("media/emptyflask.jpg"))
        self.N8SolLab = QLabel("N/8")
        self.N8SolLab.setAlignment(Qt.AlignCenter)

        self.N16Sol = DragLabel("N/16", self)
        self.N16Sol.setPixmap(QPixmap("media/emptyflask.jpg"))
        self.N16SolLab = QLabel("N/16")
        self.N16SolLab.setAlignment(Qt.AlignCenter)

        self.N32Sol = DragLabel("N/32", self)
        self.N32Sol.setPixmap(QPixmap("media/emptyflask.jpg"))
        self.N32SolLab = QLabel("N/32")
        self.N32SolLab.setAlignment(Qt.AlignCenter)

        self.N64Sol = DragLabel("N/64", self)
        self.N64Sol.setPixmap(QPixmap("media/emptyflask.jpg"))
        self.N64SolLab = QLabel("N/64")
        self.N64SolLab.setAlignment(Qt.AlignCenter)

        self.N128Sol = DragLabel("N/128", self)
        self.N128Sol.setPixmap(QPixmap("media/emptyflask.jpg"))
        self.N128SolLab = QLabel("N/128")
        self.N128SolLab.setAlignment(Qt.AlignCenter)

        self.SolRack1 = QVBoxLayout()
        self.SolRack1.addWidget(self.StockSol)
        self.SolRack1.addWidget(self.StockSolLab)
        self.SolRack1.addWidget(self.N4Sol)
        self.SolRack1.addWidget(self.N4SolLab)
        self.SolRack1.addWidget(self.N16Sol)
        self.SolRack1.addWidget(self.N16SolLab)
        self.SolRack1.addWidget(self.N64Sol)
        self.SolRack1.addWidget(self.N64SolLab)
        self.SolRack1_wid = QWidget()
        self.SolRack1_wid.setLayout(self.SolRack1)

        self.SolRack2 = QVBoxLayout()
        self.SolRack2.addWidget(self.KCLSol)
        self.SolRack2.addWidget(self.KCLSolLab)
        self.SolRack2.addWidget(self.N8Sol)
        self.SolRack2.addWidget(self.N8SolLab)
        self.SolRack2.addWidget(self.N32Sol)
        self.SolRack2.addWidget(self.N32SolLab)
        self.SolRack2.addWidget(self.N128Sol)
        self.SolRack2.addWidget(self.N128SolLab)
        self.SolRack2_wid = QWidget()
        self.SolRack2_wid.setLayout(self.SolRack2)

        self.SolRack = QHBoxLayout()
        self.SolRack.addWidget(self.SolRack1_wid)
        self.SolRack.addWidget(self.SolRack2_wid)
        self.solRackWid = QGroupBox()
        self.solRackWid.setLayout(self.SolRack)

        self.SolRackBoxLay = QVBoxLayout()
        #self.SolRackBoxLay.addWidget(self.SolutionsAvaliabel)
        self.SolRackBoxLay.addWidget(self.solRackWid)

        self.SolRackBox = QGroupBox()
        self.SolRackBox.setLayout(self.SolRackBoxLay)
        
        self.meterLabel = DropLabel("Drop_here", self)
        self.meterLabel.setReadOnly(True)
        self.meterLabel.setStyleSheet("QLineEdit {color: white; background-image : url(media/con_meter.jpg)}") 
        self.meterLabel.setMinimumWidth(500)
        self.meterLabel.setMaximumWidth(500)
        self.meterLabel.setMinimumHeight(470)
        self.meterLabel.textChanged.connect(self.update)
        self.meterLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.DialTemp = QDial()
        self.DialTemp.setRange(1, 80)
        self.DialTemp.setValue(25)
        self.DialTemp.setNotchesVisible(True)
        self.DialTemp.valueChanged.connect(self.changedTemp)
        
        self.tempLCD = QLCDNumber()
        self.tempLCD.setStyleSheet("QLCDNumber { background-color: blue }")
        self.tempLCD.display(25)

        self.tempLab = QLabel("TEMPERATURE")
        self.tempLab.setAlignment(Qt.AlignCenter)
        self.conLab = QLabel("CONDUCTANCE")
        self.conLab.setAlignment(Qt.AlignCenter)
        
        self.conLCD = QLCDNumber()
        self.conLCD.setStyleSheet("QLCDNumber { background-color: blue }")

        self.conLCD.setSmallDecimalPoint(True)
        self.conLCD.setDigitCount(5)
        self.conLCD.display(1.01)
        self.DialCon = QDial()
        self.DialCon.setRange(0, 3000)
        self.DialCon.setNotchesVisible(False)
        self.DialCon.valueChanged.connect(self.changedValue)

        self.calBut = QPushButton("Calibrate")
        self.calButlab = QLabel("Calibrate")
        self.calBut.clicked.connect(self.setNext4)
        
        self.ResetBut = QPushButton("RESET")
        self.calBut.resize(10, 10)
        self.ResetBut.resize(10, 10)
        self.ResetButlab = QLabel("RESET")
        self.Unit = QLabel("Units")
        self.UnitLCD = QLCDNumber()
        self.UnitLCD.setStyleSheet("QLCDNumber { background-color: blue }")
        self.UnitLCD.display("E-3 S")

        self.SideButBox = QGroupBox()
        self.SideButBoxlay = QFormLayout()
        self.SideButBoxlay.addRow(self.calBut)
        self.SideButBoxlay.addRow(self.ResetBut)
        self.SideButBoxlay.addRow(self.Unit, self.UnitLCD)
        
        self.SideButBox.setLayout(self.SideButBoxlay)
        

        self.GroupBOX = QGroupBox()
        self.GroupTEMP = QGroupBox()
        self.GroupTEMPLay = QVBoxLayout()
        self.GroupTEMPLay.addWidget(self.DialTemp)
        self.GroupTEMPLay.addWidget(self.tempLab)
        self.GroupTEMPLay.addWidget(self.tempLCD)
        self.GroupTEMP.setLayout(self.GroupTEMPLay)
        self.GroupTEMP.setAlignment(Qt.AlignCenter)
        
        self.GroupCON = QGroupBox()
        self.GroupCONLay = QVBoxLayout()
        self.GroupCONLay.addWidget(self.DialCon)
        self.GroupCONLay.addWidget(self.conLab)
        self.GroupCONLay.addWidget(self.conLCD)
        self.GroupCON.setLayout(self.GroupCONLay)

        self.GROUPDOWNlay = QHBoxLayout()
        self.GROUPDOWNlay.addWidget(self.GroupTEMP)
        self.GROUPDOWNlay.addWidget(self.GroupCON)
        self.GROUPDOWNlay.addWidget(self.SideButBox)
        self.GroupBOX.setLayout(self.GROUPDOWNlay)

        self.side2lay4 = QVBoxLayout()
        self.side2lay4.addWidget(self.Titlelab4)
        self.side2lay4.addWidget(self.meterLabel)
        self.side2lay4.addWidget(self.GroupBOX)

        self.side2wid4 = QWidget()
        self.side2wid4.setLayout(self.side2lay4)
        self.side1box4.setMaximumWidth(300)
        self.Page4lay = QHBoxLayout()
        self.Page4lay.addWidget(self.side1box4)
        self.Page4lay.addWidget(self.solRackWid)
        self.Page4lay.addWidget(self.side2wid4)

        self.tab24.setLayout(self.Page4lay)
        self.mediaPlayer4 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.playButton4 = QPushButton("Play")
        self.playButton4.setEnabled(True)
        #default is on False, will not play video
        #How the button looks
        self.playButton4.clicked.connect(self.play4)  #when clicked, should play
        self.positionSlider4 = QSlider(Qt.Horizontal) #the video slider
        self.positionSlider4.setRange(0, 0) #setting the range of the slider
        self.positionSlider4.sliderMoved.connect(self.setPosition4)
        
        self.errorLabel4 = QLabel()
        self.errorLabel4.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        # Create a widget for window contents
        # Create layouts to place inside widget
        self.videoWidget4 = QVideoWidget()
        self.controlLayout4 = QHBoxLayout()
        self.controlLayout4.setContentsMargins(0, 0, 0, 0)
        self.controlLayout4.addWidget(self.playButton4)
        self.controlLayout4.addWidget(self.positionSlider4)
 
        self.layout4 = QVBoxLayout()
        self.layout4.addWidget(self.videoWidget4)
        self.layout4.addLayout(self.controlLayout4)
        self.layout4.addWidget(self.errorLabel4)
        # Set widget to contain window contents
        self.Video_widget4 = QWidget()
        self.Video_widget4.setLayout(self.layout4)
 
        self.mediaPlayer4.setVideoOutput(self.videoWidget4)
        self.mediaPlayer4.stateChanged.connect(self.mediaStateChanged4)
        self.mediaPlayer4.positionChanged.connect(self.positionChanged4)
        self.mediaPlayer4.durationChanged.connect(self.durationChanged4)
        self.mediaPlayer4.error.connect(self.handleError4)
        self.loaded4 = 0
        
        self.l14 = QLabel()
        self.l14.setPixmap(QPixmap("media/discon-1.jpg"))
        self.l14.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l14.setAlignment(Qt.AlignCenter)
        
        self.l24 = QLabel()
        self.l24.setPixmap(QPixmap("media/discon-2.jpg"))
        self.l24.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l24.setAlignment(Qt.AlignCenter)
    
        self.l34 = QLabel()
        self.l34.setPixmap(QPixmap("media/discon-3.jpg"))
        self.l34.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l34.setAlignment(Qt.AlignCenter)
  
        self.l44 = QLabel()
        self.l44.setPixmap(QPixmap("media/discon-4.jpg"))
        self.l44.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l44.setAlignment(Qt.AlignCenter)

        self.tab1Lay4 = QVBoxLayout()
        self.tab1Lay4.addWidget(self.l14)
        self.tab1Lay4.addWidget(self.l24)
        self.tab1Lay4.addWidget(self.l34)
        self.tab1Lay4.addWidget(self.l44)

        self.scrollWidget4 = QWidget()
        self.scrollWidget4.setLayout(self.tab1Lay4)
        
        self.scrollAr4 = QScrollArea()
        self.scrollAr4.setWidget(self.scrollWidget4)
        
        self.tab1Lay24 = QVBoxLayout()
        self.tab1Lay24.addWidget(self.scrollAr4)
        
        self.tab14.setLayout(self.tab1Lay24)
        
        
        self.tab3Lay4 = QVBoxLayout()
        self.tab3Lay4.addWidget(self.Video_widget4)
        self.tab34.setLayout(self.tab3Lay4)

        self.HomePage_lay4 = QHBoxLayout()
        self.HomePage_lay4.addWidget(self.tabs4)       
        self.Exp4_widget = QWidget()
        self.setLayout(self.HomePage_lay4)
        self.setWindowTitle("ChemVlab-1.0.0")
        self.errorAccu = 0
        self.errorFlag = 0
        self.flag = 0
        self.Ka = 0
        
    def update(self):
        try :
            val = float(self.meterLabel.text())
        except:
            val = 0
        self.conLCD.display(val)
        self.DialCon.setValue(val*100)
        
        
    def setNext4(self):
        name = self.meterLabel.name_()
        if(name != "KCl"):
            self.errorFlag = 1
            self.errorMessage()
            return
        val = float(self.DialCon.value())/100
        if(val != 12.88):
            self.errorAccu = ((val-12.88)/12.88)
            if(self.errorAccu > 0.3 or self.errorAccu < -0.3):
                self.errorFlag = 3
                self.errorMessage()
                return
        if(val !=  self.KCLSol.value_()):
            self.flag = 0
        self.KCLSol.setValue(val)
        self.PipLabel.setText("2.Pipette out 50 ml 1N Acetic Acid")
        self.makLab.setText("3.Make up the volm to 100 ml")
        self.UseLab2.setText("(Use Conductivity Water !!)")
        self.TheCon.setText("Concentration of stock:")
        self.nextBut24.setEnabled(True)

    def play4(self):
        
        fileName = "media/exp4.mp4"
        if self.loaded4 == 0:
            self.mediaPlayer4.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton4.setEnabled(True)
            self.playButton4.setText("Pause")
            self.loaded4 = 1
            
        if self.mediaPlayer4.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer4.pause()
            self.playButton4.setText("Play")
        else:
            self.mediaPlayer4.play()
            self.playButton4.setText("Pause")
 
    def mediaStateChanged4(self, state):
        if self.mediaPlayer4.state() == QMediaPlayer.PlayingState:
            self.playButton4.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton4.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
 
    def positionChanged4(self, position):
        self.positionSlider4.setValue(position)
 
    def durationChanged4(self, duration):
        self.positionSlider4.setRange(0, duration)
 
    def setPosition4(self, position):
        self.mediaPlayer4.setPosition(position)
 
    def handleError4(self):
        self.playButton4.setEnabled(False)
        self.errorLabel4.setText("Error: " + self.mediaPlayer4.errorString())

    def NoteValue(self):

        condval = self.spin_b.value()

    def changedValue(self):
        val = float(self.DialCon.value())/100
        self.conLCD.display(val)

    def changedTemp(self):
        self.tempLCD.display(self.DialTemp.value())
    def validate(self):

        try:
            k = float(self.ConLine.text())
            if(k<0.45 or k>0.55):
               self.UseLab.setText("Wrong ! it's 0.5. Anyways continue")
            else :
                self.UseLab.setText("Correct ! it's 0.5.")

            self.StockSol.setPixmap(QPixmap("media/smallflask.jpg"))
            Ka = 1.75
            k = float(random.randint(100, 9999))
            error = k/10000
            Ka = Ka + error
            Ka = Ka/100000
            
            c1 = (float(self.ConLine.text())*100)/(100)
            c1 = c1 + (((float(random.randint(-200, 200)))/10000)*c1)
            alpha1 = (math.sqrt((Ka**2) + (4*c1*Ka))-Ka)/(2*c1)
            kappa1 = "%.3f" %(390.8*alpha1)
            
            self.StockSol.setValue(kappa1)
            self.validateBut.setEnabled(True)
        except:
            self.errorFlag = 2
            self.validateBut.setEnabled(False)
            self.errorMessage()
    def validate2(self):
        for i in[self.spin_n4n, self.spin_n8n, self.spin_n16n, self.spin_n32n, self.spin_n64n, self.spin_n128n]:
            try:
                temp = float(i.value())
                
                if temp >= 100 or temp == 0:
                    self.errorFlag = 4
                    self.errorMessage()
                    return
            except:
                self.errorMessage()
                return
        self.CalculateConductivity()

    def CalculateConductivity(self):

        Ka = 1.75
        k = float(random.randint(100, 9999))
        error = k/10000
        Ka = Ka + error
        Ka = Ka/100000
        
        if(self.flag == 0) :
            self.Ka = Ka
            c1 = (float(self.ConLine.text())*self.spin_n4n.value())/(100)
            c2 = (float(self.ConLine.text())*self.spin_n8n.value())/(100)
            c3 = (float(self.ConLine.text())*self.spin_n16n.value())/(100)
            c4 = (float(self.ConLine.text())*self.spin_n32n.value())/(100)
            c5 = (float(self.ConLine.text())*self.spin_n64n.value())/(100)
            c6 = (float(self.ConLine.text())*self.spin_n128n.value())/(100)
            #print("values extracted")
            c1 = c1 + (((float(random.randint(-200, 200)))/10000)*c1)+ self.errorAccu*c1
            c2 = c2 + (((float(random.randint(-200, 200)))/10000)*c2)+ self.errorAccu*c2
            c3 = c3 + (((float(random.randint(-200, 200)))/10000)*c3)+ self.errorAccu*c3
            c4 = c4 + (((float(random.randint(-200, 200)))/10000)*c4)+ self.errorAccu*c4
            c5 = c5 + (((float(random.randint(-200, 200)))/10000)*c5)+ self.errorAccu*c5
            c6 = c6 + (((float(random.randint(-200, 200)))/10000)*c6)+ self.errorAccu*c6
            #print("error added")
            alpha1 = (math.sqrt((Ka**2) + (4*c1*Ka))-Ka)/(2*c1)
            alpha2 = (math.sqrt((Ka**2) + (4*c2*Ka))-Ka)/(2*c2)
            alpha3 = (math.sqrt((Ka**2) + (4*c3*Ka))-Ka)/(2*c3)
            alpha4 = (math.sqrt((Ka**2) + (4*c4*Ka))-Ka)/(2*c4)
            alpha5 = (math.sqrt((Ka**2) + (4*c5*Ka))-Ka)/(2*c5)
            alpha6 = (math.sqrt((Ka**2) + (4*c6*Ka))-Ka)/(2*c6)
            #print("alpha calculated")
            kappa1 = "%.3f" %(390.8*alpha1)
            kappa2 = "%.3f" %(390.8*alpha2)
            kappa3 = "%.3f" %(390.8*alpha3)
            kappa4 = "%.3f" %(390.8*alpha4)
            kappa5 = "%.3f" %(390.8*alpha5)
            kappa6 = "%.3f" %(390.8*alpha6)
            #print("kappa calculated")
            self.flag = 1
            self.N4Sol.setValue(kappa1)
            self.N8Sol.setValue(kappa2)
            self.N16Sol.setValue(kappa3)
            self.N32Sol.setValue(kappa4)
            self.N64Sol.setValue(kappa5)
            self.N128Sol.setValue(kappa6)
            #print("Done calculated")
        if(self.flag == 1):
            self.N4Sol.setPixmap(QPixmap("media/smallflask.jpg"))
            self.N8Sol.setPixmap(QPixmap("media/smallflask.jpg"))
            self.N16Sol.setPixmap(QPixmap("media/smallflask.jpg"))
            self.N32Sol.setPixmap(QPixmap("media/smallflask.jpg"))
            self.N64Sol.setPixmap(QPixmap("media/smallflask.jpg"))
            self.N128Sol.setPixmap(QPixmap("media/smallflask.jpg"))
            
    def errorMessage(self):
        self.w = QMessageBox()
        self.w.resize(150, 150)
        title = "Warning"
        text = "Invalid entry !\nPlease Check Entered Values."
        if(self.errorFlag == 1):
            text = "Calibration Error!\nCalibration Data Available for KCl Only."
            title = "Error!"
        elif(self.errorFlag == 2):
            text = "Invalid Entry !\nPlease Enter a valid concentration for Stock Solution."
        elif(self.errorFlag == 3):
            text = "Warning!\nInaccurate Calibration for KCl.\nRecalibration Recommended.\n(Tip : Use Keyboard arrow keys)"
        elif(self.errorFlag == 4):
            text = "Warning!\nInaccurate Solution preparation.\nReverification Recommended."
        self.w.setIcon(QMessageBox.Warning)
        self.w.setInformativeText(text)
        self.w.setWindowTitle(title)
        self.w.exec()
        self.errorFlag = 0
        
def main_exp4():
    obj = Exp4_class()
    return obj

Vlab = QApplication(sys.argv)
obj = main_exp4()
#obj.show()
obj.showMaximized()
Vlab.exec_()
