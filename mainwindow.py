import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from defualtwindow import *


class mainwindow(defualtwindow):

  def __init__(self):
      super().__init__()

      self.main_widget = mainwidget()
      self.setCentralWidget(self.main_widget)

      self.show()

class mainwidget(defualtwidget):

  def __init__(self):
      super().__init__()

      #제목 생성, 폰트조정
      self.titlelabel = QLabel('강아지 사전',self)
      font1 = self.titlelabel.font()
      font1.setPointSize(45)
      font1.setBold(True)

      self.titlelabel.setFont(font1)
      self.titlelabel.setStyleSheet("Color : brown")

      #4개의 메뉴버튼
      self.historyButton = QPushButton('역사')
      self.speciesButton = QPushButton('다양한 품종과 특징')
      self.foodButton = QPushButton('먹으면 안되는것')
      self.minigameButton = QPushButton('미니게임')

      self.historyButton.setStyleSheet('color:blue; background:white; font:bold')
      self.speciesButton.setStyleSheet('color:blue; background:white; font:bold')
      self.foodButton.setStyleSheet('color:blue; background:white; font:bold')
      self.minigameButton.setStyleSheet('color:blue; background:white; font:bold')
      
      self.historyButton.setMaximumHeight(40)
      self.speciesButton.setMaximumHeight(40)
      self.foodButton.setMaximumHeight(40)
      self.minigameButton.setMaximumHeight(40)
  
      #메뉴정리
      vbox = QVBoxLayout()

      vbox.addWidget(self.titlelabel)
      vbox.addWidget(self.historyButton)
      vbox.addWidget(self.speciesButton)
      vbox.addWidget(self.foodButton)
      vbox.addWidget(self.minigameButton)
      
      hbox = QHBoxLayout()

      hbox.addStretch(1)
      hbox.addLayout(vbox)
      hbox.addStretch(1)

      self.setLayout(hbox)
      #메뉴버튼 이벤트
      self.historyButton.clicked.connect(self.historyButton_onClick)
      self.speciesButton.clicked.connect(self.speciesButton_onClick)
      self.foodButton.clicked.connect(self.foodButton_onClick)
      self.minigameButton.clicked.connect(self.minigameButton_onClick)

  def historyButton_onClick(self):

      history_window.show()
      ex.close()

  def speciesButton_onClick(self):

      species_window.show()
      ex.close()

  def foodButton_onClick(self):

      food_window.show()
      ex.close()

  def minigameButton_onClick(self):

      minigame_window.show()
      ex.close()


class historywindow(defualtwindow):

  def __init__(self):
      super().__init__()

      self.history_widget = historywidget()
      self.setCentralWidget(self.history_widget)

class historywidget(defualtwidget2):

  def __init__(self):
      super().__init__()
      #제목생성, 폰트조정
      self.histitlelabel = QLabel("강아지의 역사와 기원")
      font = self.histitlelabel.font()
      font.setPointSize(18)
      font.setBold(True)
      self.histitlelabel.setFont(font)
      #내용생성, 폰트조정
      self.hislabel = QLabel("개는 중형 동물이자 가장 널리 분포하며 개체 수가 가장 많은 지상 동물 중 하나이며 가축화한 회색늑대이다. 개의 진화 경로나 가축화의 과정에 대해서는 여러 이견이 있으나 확실하지는 않다. 어떤 학자는 야생 늑대가 인간의 무리와 함께 살면서 개로 종분화가 되었다고 보기도 하고, 다른 경우엔 늑대에서 생물학적으로 갈라져 나온 개의 조상 개체군이 인간에 의해 길러지기 시작한 것으로 보기도 한다. 유전자 연구에 따르면 개는 늑대로부터 약 10만 년 전 이전에 분리된 것으로 추측되며, 2013년 개의 화석을 이용한 분석에서는 33,000 - 36,000년 전 사이에 분화가 이루어졌을 것으로 보고 있다. 개가 인간에 길들여진 시기는 약 1만 5천 년 전 이후 또는 1만 4천 년 ~ 1만 2천 년 전으로 추정되며, 최소한 9천 년 전에는 가축으로 기르고 있었다. 인간이 개를 기른 것을 증명하는 유적 가운데 가장 오래된 것은 이라크의 팔레가우라 동굴에서 발견된 개 뼈이다. 마지막 빙하기인 만 2천 년 전 해수면이 낮아져 베링 해협이 육지가 되었을 때 아메리카 원주민의 선조들이 아메리카 대륙으로 건너가면서 개도 함께 데려갔을 것으로 보기도 한다.")
      self.hislabel.setWordWrap(True) # 정의된 gridlayout 내에서 자동 줄바꿈
      font1 = self.hislabel.font()
      font1.setPointSize(13)
      font1.setBold(True)

      self.hislabel.setFont(font1)
      self.hislabel.setStyleSheet("Color : gray29")
      self.hislabel.setStyleSheet("background-color: white")

      #gridLayout
      self.layout = QGridLayout()
      self.layout.addWidget(self.histitlelabel,0,0)
      self.layout.addWidget(self.hislabel,1,0)
      self.layout.addWidget(self.backButton,4,4)
      self.setLayout(self.layout)

      #defaultwidget에 정의된 back버튼 이벤트
      self.backButton.clicked.connect(self.goMainWindow)

  def goMainWindow(self):

      history_window.close()
      ex.show()

class specieswindow(defualtwindow):

  def __init__(self):
      super().__init__()

      self.species_widget = specieswidget()
      self.setCentralWidget(self.species_widget)

class specieswidget(defualtwidget2):

  def __init__(self):
      super().__init__()
      #제목설정
      self.selectlabel = QLabel('정보를 알고싶은 품종을 선택해주세요:',self)
      font1 = self.selectlabel.font()
      font1.setPointSize(16)
      font1.setBold(True)
      self.selectlabel.setFont(font1)
      self.selectlabel.setStyleSheet("Color : brown")

      self.combo = QComboBox(self)
      self.current_text = None 
      self.combo.addItems(["Select one...", "골든리트리버", "비글", "비숑", "사모예드", "포메라니안", "푸들" ])
      self.combo.currentTextChanged.connect(self.on_combobox_func)  #  
   

      
      self.selectbutton = QPushButton(self)
      self.selectbutton.setText('Select')
      self.selectbutton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')

      self.selectbutton.clicked.connect(self.gogoldenwindow)
      self.backButton.clicked.connect(self.goMainWindow)

            #메뉴정리
      hbox = QHBoxLayout()


      hbox.addStretch(1)
      hbox.addWidget(self.selectlabel)
      hbox.addWidget(self.combo)
      hbox.addWidget(self.selectbutton)
      hbox.addStretch(1)
      
      vbox = QVBoxLayout()

      vbox.addStretch(1)
      vbox.addLayout(hbox)
      vbox.addStretch(3)

      self.setLayout(vbox)


  def on_combobox_func(self, text):                                                   
       self.current_text  = text 

  def gogoldenwindow(self):                                                             
      if self.current_text == "골든리트리버":
          golden_window.show() 
          species_window.close()
      elif self.current_text == "비글":
          beagle_window.show() 
          species_window.close()
      elif self.current_text == "비숑":
          bichon_window.show() 
          species_window.close()
      elif self.current_text == "사모예드":
          samo_window.show() 
          species_window.close()
      elif self.current_text == "포메라니안":
          pome_window.show() 
          species_window.close()
      elif self.current_text == "푸들":
          poodle_window.show() 
          species_window.close()

      else: QMessageBox.warning(self, "경고", "선택된 품종이 없습니다.")

  def goMainWindow(self):

      species_window.close()
      ex.show()

class foodwindow(defualtwindow):

  def __init__(self):
      super().__init__()

      self.food_widget = foodwidget()
      self.setCentralWidget(self.food_widget)

class foodwidget(defualtwidget2):

  def __init__(self):
      super().__init__()

      self.backButton.clicked.connect(self.goMainWindow)

      self.foodtitlelabel = QLabel('강아지가 먹으면 위험한 음식들',self)
      font = self.foodtitlelabel.font()
      font.setPointSize(20)
      font.setBold(True)
      self.foodtitlelabel.setFont(font)

      self.fruitButton = QPushButton('과일씨, 잎, 줄기')
      self.xylitolButton = QPushButton('자일리톨 성분')
      self.caffeineButton = QPushButton('카페인')
      self.alcoholButton = QPushButton('알코올')
      self.grapeButton = QPushButton('포도')
      self.milkButton = QPushButton('우유')  

      self.noteatimage = QLabel(self)
      self.noteatlabel = QLabel(self)
      self.noteatlabel.setWordWrap(True)
      font1 = self.noteatlabel.font()
      font1.setPointSize(13)
      font1.setBold(True)
      self.noteatlabel.setFont(font1)

 #과일.....
      self.pixmap1 = QPixmap("fruit.jpg")
      self.pixmapscaled1 = self.pixmap1.scaledToHeight(230)
 #자일리톨.....
      self.pixmap2 = QPixmap("xylitol.jpg")
      self.pixmapscaled2 = self.pixmap2.scaledToHeight(230)
 #카페인.....
      self.pixmap3 = QPixmap("caffeine.jpg")
      self.pixmapscaled3 = self.pixmap3.scaledToHeight(230)
 #알코올.....
      self.pixmap4 = QPixmap("alcohol.jpg")
      self.pixmapscaled4 = self.pixmap4.scaledToHeight(230)
 #포도.....
      self.pixmap5 = QPixmap("grape.jpg")
      self.pixmapscaled5 = self.pixmap5.scaledToHeight(230)
 #우유.....
      self.pixmap6 = QPixmap("milk.jpg")
      self.pixmapscaled6 = self.pixmap6.scaledToHeight(230)

           #   Layout
      self.layout = QGridLayout()
      self.layout.addWidget(self.foodtitlelabel,0,3,1,5)
      self.layout.addWidget(self.noteatimage,1,3,1,5)
      self.layout.addWidget(self.noteatlabel,2,3,5,5)

      self.layout.addWidget(self.fruitButton,2,0,1,1)
      self.layout.addWidget(self.xylitolButton,3,0,1,1)
      self.layout.addWidget(self.caffeineButton,4,0,1,1)
      self.layout.addWidget(self.alcoholButton ,5,0,1,1)
      self.layout.addWidget(self.grapeButton,6,0,1,1)
      self.layout.addWidget(self.milkButton,7,0,1,1)
      self.layout.addWidget(self.backButton,7,7,1,1)
   
      self.setLayout(self.layout)

      self.fruitButton.clicked.connect(self.showfruit)
      self.xylitolButton.clicked.connect(self.showxylitol)
      self.caffeineButton.clicked.connect(self.showcaffeine)
      self.alcoholButton.clicked.connect(self.showalcohol)
      self.grapeButton.clicked.connect(self.showgrape)
      self.milkButton.clicked.connect(self.showmilk)


  def showfruit(self):
      self.noteatimage.setPixmap(self.pixmapscaled1)
      self.noteatlabel.setText("기본적으로 과일씨, 잎, 줄기는 강아지에게 중독증세, 소화불량을 일으킬 수 있습니다. 예를 들어, 사과, 체리의 경우에는 씨에 시안화물이라는 물질이 있어 중독증세를 일으키고, 채소 중에서는 감자줄기, 잎에 솔라닌이라는 독성물질이 있습니다.초록색으로 변한 감자 자체도 마찬가지 입니다.")
      self.noteatlabel.setStyleSheet("background-color: white")

  def showxylitol(self):
      self.noteatimage.setPixmap(self.pixmapscaled2)
      self.noteatlabel.setText("과도한 양이 체내에 쌓이면 저혈당증, 간경변증 등과 같은 질환을 야기하기 때문입니다. 자이리톨은 산딸기, 사탕, 치약, 껌 등에 함유되어 있는데요. 소량을 먹었다고 중독증세가 일어나지는 않지만 강아지가 몰래 사탕 등을 먹는 상황이나 산에서 떨어진 산딸기를 주워먹는 등 다량을 섭취할 수 있는 상황이 생기지 않도록 신경을 써야 합니다.")
      self.noteatlabel.setStyleSheet("background-color: white")

  def showcaffeine(self):
      self.noteatimage.setPixmap(self.pixmapscaled3)
      self.noteatlabel.setText("강아지는 메틸크산틴이라는 화학물질에 중독증세를 보이는데요. 카페인은 메틸크산틴 성분을 함유하고 있어 섭취 시 구토, 설사, 경련, 심박수 이상 등을 야기할 수 있습니다. 우리가 잘 알고 있는 초콜렛 뿐만 아니라 콜라, 에너지 음료, 커피 (원두 포함), 차, 감기약, 진통제 등에도 카페인이 함유되어 있으니 이러한 음식을 섭취할 때는 강아지가 모르고 먹지 않도록 조심해야 합니다.")
      self.noteatlabel.setStyleSheet("background-color: white")
      
  def showalcohol(self):
      self.noteatimage.setPixmap(self.pixmapscaled4)
      self.noteatlabel.setText("알콜 중독증세는 사람의 증세와 비슷하지만 강아지가 더욱 심각한데요. 알코올은 강아직에게 구토, 호흡곤란, 뇌사 및 심한 경우 죽음에까지 이를 수 있습니다. 꼭 맥주, 소주와 같은 주류 뿐만 아닌 일반식품이어도 알콜이 함유되어 있는 경우가 있기 때문에 이를 인지할 필요가 있습니다.")
      self.noteatlabel.setStyleSheet("background-color: white")

  def showgrape(self):
      self.noteatimage.setPixmap(self.pixmapscaled5)
      self.noteatlabel.setText("아직 정확하게 원인이 밝혀지지는 않았지만 강아지에게 포도는 치명적인 음식입니다. 구토 및 설사는 물론, 급성 신부전까지 야기할 수 있기 때문이니 주의해주세요! 포토 과일 자체 뿐만 아니라 샐러드, 시리얼, 그레놀라바, 건포도 쿠기 등도 신경써야 합니다.")
      self.noteatlabel.setStyleSheet("background-color: white")

  def showmilk(self):
      self.noteatimage.setPixmap(self.pixmapscaled6)
      self.noteatlabel.setText("강아지는 락타아제라고 불리는 유당 분해 효소가 부족합니다. 따라서 우유나 우유로 만든 유제품을 개에게 준다면  설사와 같은 소화기계 문제를 야기시킬 수 있고 음식 알러지를 일으킬 수 있습니다. 그러니 유당-free인 제품이나 반려동물 전용 우유를 주어야 합니다.")
      self.noteatlabel.setStyleSheet("background-color: white")


  def goMainWindow(self):

      food_window.close()
      ex.show()

class minigamewindow(defualtwindow):

  def __init__(self):
      super().__init__()

      self.minigame_widget = minigamewidget()
      self.setCentralWidget(self.minigame_widget)

class minigamewidget(defualtwidget2):

  def __init__(self):
      super().__init__()

      self.backButton.clicked.connect(self.goMainWindow)

  def goMainWindow(self):

      minigame_window.close()
      ex.show()
 
#리트리버@@@@@@
class goldenwindow(defualtwindow):

  def __init__(self):
      super().__init__()

      self.golden_widget = goldenwidget()
      self.setCentralWidget(self.golden_widget)

class goldenwidget(defualtwidget3):

  def __init__(self):
      super().__init__()

      self.homeButton.clicked.connect(self.goMainWindow)
      self.backButton.clicked.connect(self.gospecieswindow)

      self.pixmap = QPixmap("golden.png")
      self.pixmap1 = self.pixmap.scaledToWidth(200)

      self.goldenimage = QLabel(self)
      self.goldenimage.setPixmap(self.pixmap1)

      self.goldentitlelabel = QLabel('골든리트리버',self)
      font = self.goldentitlelabel.font()
      font.setPointSize(20)
      font.setBold(True)
      self.goldentitlelabel.setFont(font)

      self.goldenlabel = QLabel("골든 리트리버는 방수가 되고 물결모양에 납작하고 금색이나 크림색이 도는 털을 가지고 있다. 이 견종이 가장 사랑 받는 점은 목과, 다리, 허벅지와 꼬리 밑쪽으로 난 수북한 털이다. 이 견종의 머리는 튼튼하고 넓다. 귀는 많이 크지 않지만 머리 높은 쪽에 위치해 있으며 턱선까지 내려와 있다. 가슴은 깊고, 몸의 균형이 잘 맞아 있다. 골든 리트리버는 10년에서 13년정도 살 수 있다. 골든 리트리버는 매우 차분하고 지능적이며 애정 어린 견종이다. 골든 리트리버는 장난스럽고 아이들과 친하게 지내며 다른 반려동물이나 낯선 사람들과 잘 어울리는 경향이 있습니다. 이 견종들은 매순간 열심히 노력하기 때문에 복종훈련에 잘 적응하며 인기 있는 서비스견이다. 그들은 조렵 활동을 돕거나 주인의 슬리퍼를 가져 오는 등 일하는 것을 좋아한다. 골든 리트리버는 자주 짖지 않으며 경비 본능 부족하므로 좋은 감시견은 아니다. 그러나 몇몇 골든 리트리버는 낯선 사람이 다가오면 주인에게 알려주기도 한다.")
      self.goldenlabel.setWordWrap(True)
       
       # type
      font1 = self.goldenlabel.font()
      font1.setPointSize(13)
      font1.setBold(True)

      self.goldenlabel.setFont(font1)
      self.goldenlabel.setStyleSheet("background-color: white")

          #   Layout
      self.layout = QGridLayout()
      self.layout.addWidget(self.goldenimage,1,0,1,1)
      self.layout.addWidget(self.goldentitlelabel,0,2,1,4)
      self.layout.addWidget(self.goldenlabel,1,2,1,4)
      self.layout.addWidget(self.backButton,4,5)
      self.layout.addWidget(self.homeButton,4,4)
      self.setLayout(self.layout)

  def gospecieswindow(self):

      golden_window.close()
      species_window.show()

  def goMainWindow(self):

      golden_window.close()
      ex.show()
#비글@@@@@@
class beaglewindow(defualtwindow):

  def __init__(self):
      super().__init__()

      self.beagle_widget = beaglewidget()
      self.setCentralWidget(self.beagle_widget)

class beaglewidget(defualtwidget3):

  def __init__(self):
      super().__init__()

      self.homeButton.clicked.connect(self.goMainWindow)
      self.backButton.clicked.connect(self.gospecieswindow)

      self.pixmap = QPixmap("beagle.jpg")
      self.pixmap1 = self.pixmap.scaledToWidth(200)

      self.beagleimage = QLabel(self)
      self.beagleimage.setPixmap(self.pixmap1)

      self.beagletitlelabel = QLabel('비글',self)
      font = self.beagletitlelabel.font()
      font.setPointSize(20)
      font.setBold(True)
      self.beagletitlelabel.setFont(font)

      self.beaglelabel = QLabel("몇몇 종은 어깨에서부터 13인치 정도 크고 몸무게는 18파운드 (8킬로그램)정도 나간다; 두번째 크기는 13에서 15인치 크고 몸무게는 20파운드 (9킬로그램)정도 나간다. 비글은 근육진 탄탄한 체형을 가지고 있으며, 돔 모양의 머리를 가지고 있다. 주둥이는 각이 졌으며 넓은 코를 가지고 있다. 귀는 길면서 축 쳐져 있고, 가슴은 깊고 등은 곧으면서 높게 솟은 중간길이의 꼬리를 가지고 있다. 이 견종은 부드러우면서 빽빽한 검은색이나 갈색, 이나 흰색의 털을 가지고 있다. 비글은 다른 반려동물이나 어린이들과 잘 어울리는 견종으로 널리 알려져 있다. 애착이 많은 활발하고 낙천적인 견종이다. 같이 있는 것을 좋아하고 혼자 남겨졌을 시 늑대처럼 울부짖고 파괴적일 수 있다. 한 소비자의 개에 관한 지침서에 따르면, 비글은 과도하게 짖거나 배변훈련 및 순종훈련을 시키기 어려운 상위 견종으로 분류되어있다. ")
      self.beaglelabel.setWordWrap(True)
       
       # type
      font1 = self.beaglelabel.font()
      font1.setPointSize(13)
      font1.setBold(True)

      self.beaglelabel.setFont(font1)
      self.beaglelabel.setStyleSheet("background-color: white")

  #   Layout
      self.layout = QGridLayout()
      self.layout.addWidget(self.beagleimage,1,0,1,1)
      self.layout.addWidget(self.beagletitlelabel,0,2,1,4)
      self.layout.addWidget(self.beaglelabel,1,2,1,4)
      self.layout.addWidget(self.backButton,4,5)
      self.layout.addWidget(self.homeButton,4,4)
      self.setLayout(self.layout)      

  def gospecieswindow(self):

      beagle_window.close()
      species_window.show()

  def goMainWindow(self):

      beagle_window.close()
      ex.show()
#비숑@@@@@@
class bichonwindow(defualtwindow):

  def __init__(self):
      super().__init__()

      self.bichon_widget = bichonwidget()
      self.setCentralWidget(self.bichon_widget)

class bichonwidget(defualtwidget3):

  def __init__(self):
      super().__init__()

      self.homeButton.clicked.connect(self.goMainWindow)
      self.backButton.clicked.connect(self.gospecieswindow)

      self.pixmap = QPixmap("bichon.png")
      self.pixmap1 = self.pixmap.scaledToWidth(200)

      self.bichonimage = QLabel(self)
      self.bichonimage.setPixmap(self.pixmap1)

      self.bichontitlelabel = QLabel('비숑 프리제',self)
      font = self.bichontitlelabel.font()
      font.setPointSize(20)
      font.setBold(True)
      self.bichontitlelabel.setFont(font)

      self.bichonlabel = QLabel("비숑의 털은 푸들과 비슷한 털을 가졌다. 이 털은 비단과 같지만 겉은 곱슬 하고 안은 부드럽다. 그들은 하얀색, 하얀색과 담황색, 크림색, 살구색 혹은 회색이다. 비숑의 길이는 높이 보다 더 길다. 깃털로 장식한 듯한 꼬리는 등위로 올라간다. 비숑은 몸과 비율이 알맞은 머리를 가졌으며 귀가 늘어져있다. 코는 단호하며 검정색이다. 비숑 프리제는 전체적으로 좋은 반려동물이라는 의견이 많으며 온화하면서도 장난 끼가 많다. 비숑은 다른 반려동물들과도 잘 지낸다. 아이들과도 보통 잘 지낸다고 보여진다. 하나의 설문 조사에서 아이들에게 짖는 것에 높은 등수가 나오긴 했지만 개와 아이가 만나면 항상 주의를 기울여야 한다. 같은 설문 조사에서 집에서 물건을 잘 부수고 훈련하기 힘들다고 나오긴 했지만 어떤 주인들은 물건을 자주 부서뜨린다고 동의 하지는 않는다. ")
      self.bichonlabel.setWordWrap(True)
       
       # type
      font1 = self.bichonlabel.font()
      font1.setPointSize(13)
      font1.setBold(True)

      self.bichonlabel.setFont(font1)
      self.bichonlabel.setStyleSheet("background-color: white")

  #   Layout
      self.layout = QGridLayout()
      self.layout.addWidget(self.bichonimage,1,0,1,1)
      self.layout.addWidget(self.bichontitlelabel,0,2,1,4)
      self.layout.addWidget(self.bichonlabel,1,2,1,4)
      self.layout.addWidget(self.backButton,4,5)
      self.layout.addWidget(self.homeButton,4,4)
      self.setLayout(self.layout)         

  def gospecieswindow(self):

      bichon_window.close()
      species_window.show()

  def goMainWindow(self):

      bichon_window.close()
      ex.show()
#사모@@@@@@
class samowindow(defualtwindow):

  def __init__(self):
      super().__init__()

      self.samo_widget = samowidget()
      self.setCentralWidget(self.samo_widget)

class samowidget(defualtwidget3):

  def __init__(self):
      super().__init__()

      self.homeButton.clicked.connect(self.goMainWindow)
      self.backButton.clicked.connect(self.gospecieswindow)

      self.pixmap = QPixmap("samo.jpg")
      self.pixmap1 = self.pixmap.scaledToWidth(200)

      self.samoimage = QLabel(self)
      self.samoimage.setPixmap(self.pixmap1)

      self.samotitlelabel = QLabel('사모예드',self)
      font = self.samotitlelabel.font()
      font.setPointSize(20)
      font.setBold(True)
      self.samotitlelabel.setFont(font)

      self.samolabel = QLabel("사모예드의 머리는 넓고 날렵한 귀를 가지고 있다. 입 주변은 살짝 올라가 있다. 사모예드는 몸 전체의 하얀색 털과 달리 눈과 코, 입 주위에는 어두운 색의 털을 가지고 있다. 사모예드에게는 번쩍이는 하얀색 털이 제일 큰 특징이다. 북쪽에서 발견된 견종답게, 털이 두껍고, 거칠고 꼿꼿하면서 속털은 많은 잔털로 이루어져있다. 보통 흰색인 경우가 많으나, 간혹 비스킷이나 크림색깔을 가지고 있는 경우도 있다. 사모예드의 풍성한 털은 사람들로 하여금 푹신한 이미지를 심어준다. 사모예드는 친근하고 개성 있는 견종이다. 매우 영리하고, 독립적인 성향을 가지고 있다. 가족들과 가까운 곳에 있는 천막에서 생활할 수 있으며 사람들의 반려견으로 인기 있다. 사모예드는 위협을 느낄 경우 짖는다, 오랜 기간 동안 혼자 남겨져 있는 경우, 성가시게 많이 짖게 되는 성향으로 바뀔 수도 있다. 시원한 휴식장소를 찾기 위해서 땅을 파는 성향이 문제점이 될 수도 있다. ")
      self.samolabel.setWordWrap(True)
       
       # type
      font1 = self.samolabel.font()
      font1.setPointSize(13)
      font1.setBold(True)

      self.samolabel.setFont(font1)
      self.samolabel.setStyleSheet("background-color: white")

  #   Layout
      self.layout = QGridLayout()
      self.layout.addWidget(self.samoimage,1,0,1,1)
      self.layout.addWidget(self.samotitlelabel,0,2,1,4)
      self.layout.addWidget(self.samolabel,1,2,1,4)
      self.layout.addWidget(self.backButton,4,5)
      self.layout.addWidget(self.homeButton,4,4)
      self.setLayout(self.layout) 

  def gospecieswindow(self):

      samo_window.close()
      species_window.show()

  def goMainWindow(self):

      samo_window.close()
      ex.show()
#포메@@@@@@
class pomewindow(defualtwindow):

  def __init__(self):
      super().__init__()

      self.pome_widget = pomewidget()
      self.setCentralWidget(self.pome_widget)

class pomewidget(defualtwidget3):

  def __init__(self):
      super().__init__()

      self.homeButton.clicked.connect(self.goMainWindow)
      self.backButton.clicked.connect(self.gospecieswindow)

      self.pixmap = QPixmap("pome.jpg")
      self.pixmap1 = self.pixmap.scaledToWidth(200)

      self.pomeimage = QLabel(self)
      self.pomeimage.setPixmap(self.pixmap1)

      self.pometitlelabel = QLabel('포메라니안',self)
      font = self.pometitlelabel.font()
      font.setPointSize(20)
      font.setBold(True)
      self.pometitlelabel.setFont(font)

      self.pomelabel = QLabel("포메라니안은 풍성하고 솜털 같은 이중 털과 여우 같은 얼굴, 뾰족하고 경계하는 듯한 귀로 쉽게 알아 볼 수 있다. 몸은 네모난 편이며 솜털 같은 꼬리는 위로 향해서 등 위로 올라간다. 목 부위에 두꺼운 스카프 같은 털이 북 독일에서 쇼에 출현할 법한 이미지를 완성시킨다. 머리는 둥글면서 코와 주둥이는 뚜렷하다. 포메라니안은 다양한 색으로 있다. 포메라니안은 보통 활기차고 친밀한 작은 개다. 자기자신이 작은 체구라는 점을 인지하지 못하는 듯하며 간혹 큰 개를 공격하거나 최소한 짖을 수 도 있다. 포메라니안은 작고 매일 운동이 필요로 하다, 최소한 동네 한 바퀴라도 좋다. 매우 영리하며 독립적인 구석에도 불구하고 순종 대회에서도 좋은 모습을 보인다. 나이를 먹으며 사람 말을 더 잘 듣게 되는 반려견이다.")
      self.pomelabel.setWordWrap(True)
       
       # type
      font1 = self.pomelabel.font()
      font1.setPointSize(13)
      font1.setBold(True)

      self.pomelabel.setFont(font1)
      self.pomelabel.setStyleSheet("background-color: white")

  #   Layout
      self.layout = QGridLayout()
      self.layout.addWidget(self.pomeimage,1,0,1,1)
      self.layout.addWidget(self.pometitlelabel,0,2,1,4)
      self.layout.addWidget(self.pomelabel,1,2,1,4)
      self.layout.addWidget(self.backButton,4,5)
      self.layout.addWidget(self.homeButton,4,4)
      self.setLayout(self.layout)     

  def gospecieswindow(self):

      pome_window.close()
      species_window.show()

  def goMainWindow(self):

      pome_window.close()
      ex.show()
#푸들@@@@@@
class poodlewindow(defualtwindow):

  def __init__(self):
      super().__init__()

      self.poodle_widget = poodlewidget()
      self.setCentralWidget(self.poodle_widget)

class poodlewidget(defualtwidget3):

  def __init__(self):
      super().__init__()

      self.homeButton.clicked.connect(self.goMainWindow)
      self.backButton.clicked.connect(self.gospecieswindow)

      self.pixmap = QPixmap("poodle.jpg")
      self.pixmap1 = self.pixmap.scaledToWidth(200)

      self.poodleimage = QLabel(self)
      self.poodleimage.setPixmap(self.pixmap1)

      self.poodletitlelabel = QLabel('푸들',self)
      font = self.poodletitlelabel.font()
      font.setPointSize(20)
      font.setBold(True)
      self.poodletitlelabel.setFont(font)

      self.poodlelabel = QLabel("모든 푸들은 체격이 네모나며 길고 우아한 목과 곧은 등을 가졌다. 꼬리는 잘린 것처럼 보이지만 짧지 않으며 기쁜 듯이 흔들 수 있다. 푸들은 다리가 매우 길어 보이는 인상을 주며 안면이 길고 귀는 늘어졌다. 그들은 탄력 있고 활력 있는 걸음걸이를 가졌다. 푸들은 그들의 지능과 훈련을 쉽게 받는 것 때문에 유명하다. 그들은 활발하고 활동량이 많으며 장난을 즐기고 웃기는 면이 있는 반려견이다. 푸들은 관심 받는 것을 좋아하며 혼자두거나 무시하면 짖는 행위 같은 안 좋은 습관이 생길 수 있다. 비교적 작은 푸들은 가족외의 사람이나 다른 개들한테 공격적일 수 도 있다. 그들은 타인과 반려동물들에 대한 초기 단계의 사회화가 필요하며 훈련에 있어서 확실하게 해두어야 한다. 푸들은 가정과 자기 집에 대해서 보호본능이 있다. ")
      self.poodlelabel.setWordWrap(True)
       
       # type
      font1 = self.poodlelabel.font()
      font1.setPointSize(13)
      font1.setBold(True)

      self.poodlelabel.setFont(font1)
      self.poodlelabel.setStyleSheet("background-color: white")

  #   Layout
      self.layout = QGridLayout()
      self.layout.addWidget(self.poodleimage,1,0,1,1)
      self.layout.addWidget(self.poodletitlelabel,0,2,1,4)
      self.layout.addWidget(self.poodlelabel,1,2,1,4)
      self.layout.addWidget(self.backButton,4,5)
      self.layout.addWidget(self.homeButton,4,4)
      self.setLayout(self.layout)     

  def gospecieswindow(self):

      poodle_window.close()
      species_window.show()

  def goMainWindow(self):

      poodle_window.close()
      ex.show()



if __name__ == '__main__':

  app = QApplication(sys.argv)

  history_window = historywindow()
  species_window = specieswindow()
  food_window = foodwindow() 
  minigame_window = minigamewindow()

  golden_window = goldenwindow()
  beagle_window = beaglewindow()
  bichon_window = bichonwindow()
  samo_window = samowindow()
  pome_window = pomewindow()
  poodle_window = poodlewindow()

  ex = mainwindow()
  #ex.show()
  sys.exit(app.exec_())  