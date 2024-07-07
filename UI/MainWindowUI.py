import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QPalette, QColor, QFont, QPixmap,QBrush
from PyQt5.QtCore import Qt
from UI.AnimalUI import AnimalRecognitionWindow
from UI.PlantUI import PlantRecognitionWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(800, 600)

        # 创建 QLabel 并设置背景图片
        self.label = QLabel(self)
        self.set_background_image()

        # 连接窗口调整大小事件到 resizeEvent 方法
        self.resizeEvent = self.on_resize

        self.setWindowTitle('草原生态监测系统')
        self.setGeometry(100, 100, 800, 600)

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        mainLayout = QVBoxLayout()

        welcomeLabel = QLabel('欢迎使用草原生态监测系统', self)
        welcomeLabel.setAlignment(Qt.AlignCenter)
        welcomeLabel.setFont(QFont("Arial", 36, QFont.Bold))
        welcomeLabel.setGeometry(0, 20, self.width(), 50)

        palette = QPalette()
        palette.setColor(QPalette.WindowText, QColor('#006400'))  # 深绿色
        welcomeLabel.setPalette(palette)

        buttonLayout = QHBoxLayout()

        self.animalButton = QPushButton('动物识别', self)
        self.animalButton.setFont(QFont("Arial", 14, QFont.Bold))
        self.animalButton.setStyleSheet("background-color: green; color: white;")
        button_width = 200
        button_height = 200
        window_width = self.frameGeometry().width()
        button_x_position = (window_width - button_width) // 2
        # button_y_position = y_position + 100  # 下移100个像素
        # self.animalButton.setGeometry(button_x_position, button_y_position, button_width, button_height)
        self.animalButton.clicked.connect(self.showAnimalRecognition)

        self.plantButton = QPushButton('植物识别', self)
        self.plantButton.setFont(QFont("Arial", 14, QFont.Bold))
        self.plantButton.setStyleSheet("background-color: green; color: white;")
        self.plantButton.clicked.connect(self.showPlantRecognition)

        buttonLayout.addWidget(self.animalButton)
        buttonLayout.addWidget(self.plantButton)

        mainLayout.addStretch()
        mainLayout.addWidget(welcomeLabel)
        mainLayout.addLayout(buttonLayout)
        mainLayout.addStretch()

        centralWidget.setLayout(mainLayout)

        # self.resizeEvent = self.on_resize

    def set_background_image(self):
        # 获取图片路径，假设图片在与此脚本相同的目录下的 UI 文件夹中
        image_path = 'UI/welcome.jpg'

        # 加载图片
        pixmap = QPixmap(image_path)

        # 设置 QLabel 的图片
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.label.setGeometry(0, 0, self.width(), self.height())

    def on_resize(self, event):
        # 窗口调整大小时更新 QLabel 大小
        self.label.setGeometry(0, 0, self.width(), self.height())
        event.accept()

    def showAnimalRecognition(self):
        self.animalWindow = AnimalRecognitionWindow()
        self.animalWindow.show()

    def showPlantRecognition(self):
        self.plantWindow = PlantRecognitionWindow()
        self.plantWindow.show()

