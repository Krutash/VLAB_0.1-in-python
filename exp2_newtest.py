from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
import sys
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
import math
class MimeData(QMimeData):
    data1 = "name"
    data2 = 0
    def __init__(self):
        super().__init__()
        
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
            mimedata = MimeData()
            mimedata.data1 = self.value_()
            mimedata.data2 = str(self.name_())
            drag.setMimeData(mimedata)
            
            pixmap = QPixmap(self.size()) # label size
 
            painter = QPainter(pixmap)
            painter.drawPixmap(self.rect(), self.grab())
            painter.end()
 
            drag.setPixmap(pixmap)
            drag.setHotSpot(event.pos())
            drag.exec_(Qt.CopyAction | Qt.MoveAction)
 
class DropLabel(QLineEdit):
    value_data = "hello"
    def __init__(self, label, parent):
        super().__init__(label, parent)
        self.nameDropped = label
        self.setAcceptDrops(True)

    def name_(self):
        return self.nameDropped
    def setName(self, name):
        self.nameDropped = name
 
    def dragEnterEvent(self, event):
        event.acceptProposedAction()
 
    def dropEvent(self, event):
        pos = event.pos()
        text = event.mimeData().data1
        name = event.mimeData().data2
        DropLabel.value_data = text
        self.setName(name)
        self.setText(name)
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
        
        #Tab2 defs :
        self.Label1 = QLabel("A) CALIBRATION CURVE:")
        self.stockSol = QLabel("Stock Soln Conc.(M):")
        self.stockSol_val = QLineEdit()
        self.stockSol_val.setText("0.00")
        self.stockSol_val.editingFinished.connect(self.validateStock)
        self.stockSol_val.setMaximumWidth(100)
        self.stock_Box = QWidget()
        self.stock_Box.setMaximumWidth(300)
        self.stock_Lay = QHBoxLayout()
        self.stock_Lay.addWidget(self.stockSol)
        self.stock_Lay.addWidget(self.stockSol_val)
        self.stock_Box.setLayout(self.stock_Lay)
        self.Label2 = QLabel("Prepare Iodine Solutions:")
        self.Label3 = QLabel("(Enter Volm in ml, Flask: 10ml)")

        self.IodineTable = QTableWidget(4, 4)
        ver = self.IodineTable.horizontalHeader()
        ver.setVisible(False)
        ver2 = self.IodineTable.verticalHeader()
        ver2.setVisible(False)
        

        for i in [0, 1, 2, 3]:

            self.IodineTable.setCellWidget(0, i, QLabel("Iodine-"+str(i+1)))
            self.IodineTable.cellWidget(0, i).setAlignment(Qt.AlignCenter)
            self.IodineTable.setCellWidget(1, i, DragLabel("Iodine-"+str(i+1), self))
            self.IodineTable.cellWidget(1, i).setAlignment(Qt.AlignCenter)
            self.IodineTable.cellWidget(1, i).setPixmap(QPixmap("media/emptyflask.jpg"))
            self.IodineTable.setCellWidget(2, i, QDoubleSpinBox())
            self.IodineTable.setCellWidget(3, i, QPushButton("Get"))
            self.IodineTable.cellWidget(3,i).clicked.connect(self.cal_Iodine)
            

        self.IodineTable.setMaximumHeight(205)
        self.IodineTable.setMinimumHeight(205)
        self.IodineTable.setMaximumWidth(310)
        self.IodineTable.setMinimumWidth(310)
        
        header = self.IodineTable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        header = self.IodineTable.verticalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.Label4 = QLabel("B) RATE MEASUREMENT:")
        self.Label5 = QLabel("Prepare Trial Solutions:\n(Vol in ml, flask : 10ml)")
        self.SolsTab = QTableWidget(8, 4)

        for k in [0, 1, 2, 3]:
            
            self.SolsTab.setCellWidget(6, k, QLabel("Trial-"+str(k+1)))
            self.SolsTab.cellWidget(6, k).setAlignment(Qt.AlignCenter)
            self.SolsTab.setCellWidget(5, k, DragLabel("Trial-"+str(k+1), self))
            self.SolsTab.cellWidget(5, k).setAlignment(Qt.AlignCenter)
            self.SolsTab.cellWidget(5, k).setPixmap(QPixmap("media/emptyflask.jpg"))
            self.SolsTab.setCellWidget(7, k, QPushButton("Get"))

        
        header = self.SolsTab.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        header = self.SolsTab.verticalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        
        self.SolsTab.setMaximumHeight(305)
        self.SolsTab.setMinimumHeight(305)
        self.SolsTab.setMaximumWidth(310)
        self.SolsTab.setMinimumWidth(310)

        ver = self.SolsTab.horizontalHeader()
        ver.setVisible(False)
        ver2 = self.SolsTab.verticalHeader()
        ver2.setVisible(False)
            
        self.SolsTab.setCellWidget(0, 1, QLabel("Acetone"))
        self.SolsTab.setCellWidget(0, 2, QLabel("HCl"))
        self.SolsTab.setCellWidget(0, 3, QLabel("Iodine"))

        for i in [1, 2, 3]:
            self.SolsTab.cellWidget(0, i).setAlignment(Qt.AlignCenter)
            
        for i in range(1, 5):
            self.SolsTab.setCellWidget(i, 0, QLabel("  Trial-"+str(i)+"  "))
            self.SolsTab.cellWidget(i, 0).setAlignment(Qt.AlignCenter)
            
        for i in [1, 2, 3, 4]:
            for j in [1, 2, 3]:
                self.SolsTab.setCellWidget(i, j, QDoubleSpinBox())

        self.wid_2lay = QVBoxLayout()
        for i in [self.Label1, self.stock_Box, self.Label2, self.Label3, self.IodineTable, self.Label4,
                  self.Label5, self.SolsTab]:
              self.wid_2lay.addWidget(i)

        self.wid_2 = QWidget()
        self.wid_2.setLayout(self.wid_2lay)

        self.meterLabel = DropLabel("Drop_here", self)
        self.meterLabel.textChanged.connect(self.update)
        self.meterLabel.setReadOnly(True)
        self.meterLabel.setStyleSheet("QLineEdit {color: white; background-image : url(media/photometer_open.jpg)}") 
        self.meterLabel.setMinimumWidth(750)
        self.meterLabel.setMaximumWidth(750)
        self.meterLabel.setMinimumHeight(413)
        self.meterLabel.setMaximumHeight(413)
        self.meterLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.wave = QDial()
        self.wave.setRange(200, 700)
        self.wave.setValue(250)
        self.wave.setNotchesVisible(True)
        self.wave.valueChanged.connect(self.changedWave)

        self.waveLab = QLabel("-WAVELENGTH-\n(in nm)")
        self.waveLab.setAlignment(Qt.AlignCenter)
        
        self.waveLCD = QLCDNumber()
        self.waveLCD.setStyleSheet("QLCDNumber { background-color: blue }")
        self.waveLCD.display(250)

        self.waveLay = QVBoxLayout()
        self.waveLay.addWidget(self.waveLCD)
        self.waveLay.addWidget(self.waveLab)
        self.waveLay.addWidget(self.wave)

        self.waveBox = QGroupBox()
        self.waveBox.setLayout(self.waveLay)

        self.absorb = QLCDNumber()
        self.absorb.setMaximumWidth(70)
        self.absorb.setStyleSheet("QLCDNumber { background-color: blue }")
        self.absorb.setSmallDecimalPoint(True)
        self.absorb.setDigitCount(5)
        self.absorb.display("-E-")
        
        self.absorbLab = QLabel("-ASORBANCE-\n(in fraction)")
        self.absorbLab.setAlignment(Qt.AlignCenter)
        
        self.tempLcd = QLCDNumber()
        self.tempLcd.setStyleSheet("QLCDNumber { background-color: blue }")
        self.tempLcd.setMaximumWidth(70)
        self.tempLab = QLabel("-TEMPERATURE-\n(in Degree C)")
        self.tempLab.setAlignment(Qt.AlignCenter)
        self.tempLcd.display(25)

        self.temp = QDial()
        self.temp.setRange(10, 100)
        self.temp.setValue(25)
        self.temp.setNotchesVisible(True)
        self.temp.valueChanged.connect(self.changedTemp)

        self.loadBut = QPushButton("-LOAD-")
        self.loadBut.setEnabled(False)
        self.loadBut.clicked.connect(self.loading)
        self.resetBut = QPushButton("-RESET-")
        self.startBut = QPushButton("-START-")
        self.startBut.clicked.connect(self.starting)

        self.displayLoad = QLineEdit()
        self.displayLoad.setText("--NONE--")
        self.displayLoad.setReadOnly(True)
        self.displayLab = QLabel("Loaded Sample")
        self.displayLab.setAlignment(Qt.AlignRight)

        self.loaded = False

        self.loLay = QVBoxLayout()
        self.loLay.addWidget(self.startBut)
        self.loLay.addWidget(self.loadBut)
        self.loLay.addWidget(self.resetBut)

        self.loWid = QWidget()
        self.loWid.setLayout(self.loLay)
        self.loWid.setMaximumWidth(70)
        self.temporary = QLabel("\n")
        self.miscLay = QFormLayout()
        self.miscLay.addRow(self.absorbLab,self.absorb)
        self.miscLay.addRow(self.tempLab,self.tempLcd)
        self.miscLay.addRow(self.temporary)
        self.miscLay.addRow(self.temp, self.loWid)
        self.miscWid = QGroupBox()
        self.miscWid.setLayout(self.miscLay)
        
        self.InfoLabel = QLabel("//UNLOADED//\n\n-LID OPEN-")
        self.InfoLabel.setAlignment(Qt.AlignCenter)
        self.InfoLabel.setFont(QFont('Times', 20)) 
        self.InfoLabel.setStyleSheet("QLabel {color : white ; border : 3px solid black; background-color: blue}")

        self.sideBelowLay = QHBoxLayout()
        self.sideLay2 = QVBoxLayout()
        self.sideBelowWid = QWidget()
        
        for i, j in zip([self.waveBox, self.miscWid, self.InfoLabel],
                        [self.meterLabel, self.displayLoad, self.sideBelowWid]):
            self.sideBelowLay.addWidget(i)
            self.sideLay2.addWidget(j)

        self.sideBelowWid.setLayout(self.sideBelowLay)

        self.sideWid2 = QGroupBox()
        self.sideWid2.setLayout(self.sideLay2)
        

        self.Page4lay = QHBoxLayout()
        self.Page4lay.addWidget(self.wid_2)
        self.Page4lay.addWidget(self.sideWid2)

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
        self.l24 = QLabel()
        self.l34 = QLabel()
        self.l44 = QLabel()
        self.tab1Lay4 = QVBoxLayout()
        
        for i, j in zip([1, 2, 3, 4], [self.l14, self.l24, self.l34, self.l44]):
            j.setPixmap(QPixmap("media/Iodination-"+str(i)+".jpg"))
            j.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            j.setAlignment(Qt.AlignCenter)
            self.tab1Lay4.addWidget(j)

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
        self.errorFlag = 0
        self.count = 0
        self.timerIodine = QTimer()
        self.timerIodine.timeout.connect(self.showTime)
        self.start = False
        self.timerIodine.start(100)
        self.valueToDisplay = 0

    def starting(self):
        try:
            if(self.loaded == True):
                if(self.wave.value() != 565):
                    self.errorFlag = 3
                    self.errorMessage()
                    return
                
                self.count = 100
                self.start =  True
        except:
            self.errorFlag = 2
            self.errorMessage()
            return
        
    def showTime(self):
        if(self.start):
            self.count -= 1
            if self.count == 0:
                self.start = False
                self.InfoLabel.setText("//COMPLETE//")
                self.absorb.display(self.valueToDisplay)
        if(self.start):
            if(self.count %16 == 0):
                self.InfoLabel.setText("WARMING UP\nPlease Wait\n.   ")
            if(self.count %16 == 2):
                self.InfoLabel.setText("WARMING UP\nPlease Wait\n..  ")
            if(self.count %16 == 4):
                self.InfoLabel.setText("WARMING UP\nPlease Wait\n... ")
            if(self.count %16 == 6):
                self.InfoLabel.setText("WARMING UP\nPlease Wait\n....")
            if(self.count %16 == 8):
                self.InfoLabel.setText("WARMING UP\nPlease Wait\n....")
            if(self.count %16 == 10):
                self.InfoLabel.setText("WARMING UP\nPlease Wait\n... ")
            if(self.count %16 == 12):
                self.InfoLabel.setText("WARMING UP\nPlease Wait\n..  ")
            if(self.count %16 == 14):
                self.InfoLabel.setText("WARMING UP\nPlease Wait\n.   ")
                            
    def loading(self):
        try:
            
            if(self.loaded == False):
                self.meterLabel.setStyleSheet("QLineEdit {color: white; background-image : url(media/photometer.jpg)}")
                self.InfoLabel.setText("//LOADED//\n\n-LID CLOSE-\nPress START")
                self.loadBut.setText("-UNLOAD-")
                self.valueToDisplay = self.meterLabel.value_data
                self.loaded = True
                return

            elif(self.loaded == True):
                self.loadBut.setText("-LOAD-")
                self.meterLabel.setStyleSheet("QLineEdit {color: white; background-image : url(media/photometer_open.jpg)}")
                self.absorb.display("-E-")
                self.InfoLabel.setText("//UNLOADED//\n\n-LID OPEN-")
                self.displayLoad.setText("-NONE-")
                self.loadBut.setEnabled(False)
                self.valueToDisplay = 0
                self.meterLabel.setText("-1")
                self.loaded = False
                return
        except:
            self.errorFlag = 2
            self.errorMessage()
            
    def update(self):
   
        if(self.loaded):
            self.errorFlag = 4
            self.errorMessage()
            return
        
        try :
            val = float(self.meterLabel.value_data)
        except:
            val = 0
        self.absorb.display("-E-")
        self.displayLoad.setText(str(self.meterLabel.text()))
        self.InfoLabel.setText("//UNLOADED//\n\n-LID OPEN-\nPress LOAD")
        self.loadBut.setEnabled(True)

    def cal_Iodine(self):
        try:
            st = float(self.stockSol_val.text())
        except:
            self.errorFlag = 1
            self.errorMessage()
            return

        column = self.IodineTable.currentColumn()
        row = 2

        val_wid = self.IodineTable.cellWidget(row,column)
        val = val_wid.value()
        if(val == 0 or val >= 10):
            self.errorMessage()
            return
        elif(float(self.stockSol_val.text()) == 0):
            self.errorFlag = 1
            self.errorMessage()
            return
        else:

            absorbance = val/10 + (((float(random.randint(-500, 500)))/10000)*val)
            if(absorbance > 1):
                absorbance = 1
            elif(absorbance< 0):
                absorbance = 0
                
            flask = self.IodineTable.cellWidget(row-1,column)
            flask.setPixmap(QPixmap("media/iodine.jpg"))
            flask.setValue(absorbance)

    def validateStock(self):
        try:
            val = float(self.stockSol_val.text())
        except:
            self.errorFlag = 0
            self.errorMessage()
            return
        
    def errorMessage(self):
        self.w = QMessageBox()
        self.w.resize(150, 150)
        title = "Warning"
        text = "Invalid entry !\nPlease Check Entered Values."
        if(self.errorFlag == 1):
            text = "Calibration Error!\nStock Solution Invalid!"
            title = "Stock Error!"
        elif(self.errorFlag == 2):
            title  = "Unknown Error"
            text = "Instrument Error!\nReport a bug?"
        elif(self.errorFlag == 3):
            title = "Wavelength error"
            text = "Warning!\nReset Wavelenght Appropriate for Iodine Calibration."
        elif(self.errorFlag == 4):
            text = "Warning!\nSample Already Loaded. Unload the sample first."
            
        self.w.setIcon(QMessageBox.Warning)
        self.w.setInformativeText(text)
        self.w.setWindowTitle(title)
        self.w.exec()
        self.errorFlag = 0
            

    def play4(self):
        
        fileName = "media/exp2.mp4"
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

    def changedWave(self):
        self.waveLCD.display(self.wave.value())

    def changedTemp(self):
        self.tempLcd.display(self.temp.value())
        
def main_exp4():
    obj = Exp4_class()
    return obj

Vlab = QApplication(sys.argv)
obj = main_exp4()
#obj.show()
obj.showMaximized()
Vlab.exec_()
