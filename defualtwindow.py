import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#다른 윈도우에서도 사용할 메뉴, 툴바, 배경등을 가지고있는 defaultwindow 
class defualtwindow(QMainWindow):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):


      self.setWindowTitle('강아지 사전')
      self.setWindowIcon(QIcon('dogprofile.png'))


      exitAction = QAction(QIcon('exit.png'), 'Exit', self)
      exitAction.setShortcut('Ctrl+Q')
      exitAction.setStatusTip('Exit Application')
      exitAction.triggered.connect(qApp.quit)

      helpAction = QAction(QIcon('help.png'),'사전 사용법', self)
      helpAction.triggered.connect(self.dialog_open)
      helpAction.setShortcut('Ctrl+H')
      helpAction.setStatusTip('Help Application')

      menubar = self.menuBar()
      filemenu = menubar.addMenu('&File')
      filemenu.addAction(exitAction)
      helpmenu = menubar.addMenu('&Help')
      helpmenu.addAction(helpAction)

      self.toolbar = self.addToolBar('Exit')
      self.toolbar.addAction(exitAction)
      self.toolbar = self.addToolBar('Help')
      self.toolbar.addAction(helpAction)

      self.resize(600, 600)

      self.center()
      self.date = QDate.currentDate() #현재시간값 불러오기

      self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate)) # 날짜,시간  default 위치에 표시
      
      self.defualt_widget = defualtwidget()
      self.setCentralWidget(self.defualt_widget)

  def dialog_open(self):
     # Help dialog 세팅
      self.dialog = QDialog()

      self.dialog.setWindowTitle('사전 사용법')
      self.dialog.setWindowModality(Qt.ApplicationModal)
      self.helpLabel = QLabel(self.dialog)
      self.helpLabel.setText("강아지에 대한 다양한 정보를 얻을 수 있는 사전입니다.\n\n\n\n\n 역사  -  강아지가 사람과 가장 친근한 동물이 된 배경을 알 수 있습니다. \n\n\n 다양한품종 과 특징  -  강아지의 다양한 품종과 각각의 특징에 대해 알 수 있습니다. \n\n\n 먹으면 안되는것  -  강아지가 먹었을때 위험한 음식을 알 수 있습니다. \n\n\n 미니게임  -  미니게임을 플레이 하실 수 있습니다.")
      font = self.helpLabel.font()
      font.setPointSize(10)
      font.setBold(True)
      self.helpLabel.setFont(font)
    
      # Help dialog 버튼 추가
      self.btnDialog = QPushButton('닫기', self.dialog)
      self.btnDialog.clicked.connect(self.dialog_close)
      self.btnDialog.move(270,470)

      diaVbox = QVBoxLayout()

      diaVbox.addStretch(1)
      diaVbox.addWidget(self.helpLabel)
      diaVbox.addStretch(2)

      diaHbox = QHBoxLayout()

      diaHbox.addStretch(1)
      diaHbox.addLayout(diaVbox)
      diaHbox.addStretch(1)

      self.dialog.setLayout(diaHbox)

      self.dialog.resize(500,500)
      self.dialog.show()

  def dialog_close(self):
      self.dialog.close()

      #창을 화면의 가운데로 띄우기
  def center(self):
      qr = self.frameGeometry()
      cp = QDesktopWidget().availableGeometry().center()
      qr.moveCenter(cp)
      self.move(qr.topLeft())

class defualtwidget(QWidget):

  def __init__(self):
      super().__init__()

      # 배경

      self.background = QLabel(self)
      self.background.setPixmap(QPixmap("background.jpg"))
      self.background.show()

     #자주쓰이는 Back 버튼 
class defualtwidget2(defualtwidget):

  def __init__(self):
      super().__init__()

      self.backButton = QPushButton(self)
      self.backButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
      self.backButton.setText('Back')
      self.backButton.resize(100,35)
      self.backButton.move(460,460)  

     #자주쓰이는 Back,Home 버튼
class defualtwidget3(defualtwidget2):

  def __init__(self):
      super().__init__()

      self.homeButton = QPushButton(self)
      self.homeButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
      self.homeButton.setText('Home')
      self.homeButton.resize(100,35)
      self.homeButton.move(350,460) 

      
if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = defualtwindow()
  sys.exit(app.exec_()) 