#主窗口的UI设计
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QPalette, QColor, QFont, QPixmap
from PyQt5.QtCore import Qt
from UI.AnimalUI import AnimalRecognitionWindow
from UI.PlantUI import PlantRecognitionWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("mainWindow { border-image: url('./welcome.jpg'); }")
        self.setWindowTitle('草原生态监测系统')
        self.setGeometry(100, 100, 800, 600)

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        mainLayout = QVBoxLayout()

        welcomeLabel = QLabel('欢迎使用草原生态监测系统', self)
        #welcomeLabel.setAlignment(Qt.AlignCenter)
        welcomeLabel.setFont(QFont("Arial", 36, QFont.Bold))
        label_width = 500
        label_height = 50
        y_position = 50
        # 设置标签的位置和大小
        welcomeLabel.setGeometry(100, y_position, label_width, label_height)

        palette = QPalette()
        palette.setColor(QPalette.WindowText, QColor('#006400'))  # 深绿色
        welcomeLabel.setPalette(palette)

        buttonLayout = QHBoxLayout()

        self.animalButton = QPushButton('动物识别', self)
        self.animalButton.setFont(QFont("Arial", 14, QFont.Bold))
        self.animalButton.setStyleSheet("background-color: green; color: white;")
        button_width = 200
        button_height = 50
        window_width = self.frameGeometry().width()
        button_x_position = (window_width - button_width) // 2
        button_y_position = y_position + 100  # 下移100个像素
        self.animalButton.setGeometry(button_x_position, button_y_position, button_width, button_height)
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

    def showAnimalRecognition(self):
        self.animalWindow = AnimalRecognitionWindow()
        self.animalWindow.show()

    def showPlantRecognition(self):
        self.plantWindow = PlantRecognitionWindow()
        self.plantWindow.show()

