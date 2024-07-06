import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, \
    QFileDialog, QTextEdit
from PyQt5.QtGui import QPalette, QColor, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from API.Animal import AnimalAPI


class AnimalRecognitionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('动物识别')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # 横向布局，左侧用于显示监控画面，右侧用于显示识别信息
        hLayout = QHBoxLayout()

        # 监控画面区域
        self.monitorLabel = QLabel(self)
        self.monitorLabel.setFixedSize(QSize(530, 400))
        self.monitorLabel.setStyleSheet("background-color: gray")
        hLayout.addWidget(self.monitorLabel, 2)

        # 识别信息区域
        vLayout = QVBoxLayout()

        self.animalNameLabel = QLabel('动物名称', self)
        self.animalNameLabel.setAlignment(Qt.AlignCenter)
        self.animalNameLabel.setFont(QFont("Arial", 18, QFont.Bold))
        vLayout.addWidget(self.animalNameLabel)

        self.animalNameTextEdit = QTextEdit(self)
        vLayout.addWidget(self.animalNameTextEdit)

        self.animalInfoLabel = QLabel('动物信息', self)
        self.animalInfoLabel.setAlignment(Qt.AlignCenter)
        self.animalInfoLabel.setFont(QFont("Arial", 18, QFont.Bold))
        vLayout.addWidget(self.animalInfoLabel)

        self.animalInfoTextEdit = QTextEdit(self)
        vLayout.addWidget(self.animalInfoTextEdit)

        hLayout.addLayout(vLayout, 1)

        layout.addLayout(hLayout)

        # 导入监控按钮
        self.importButton = QPushButton('导入监控', self)
        self.importButton.setFont(QFont("Arial", 14, QFont.Bold))
        self.importButton.setStyleSheet("background-color: green; color: white;")
        self.importButton.clicked.connect(self.importVideo)
        layout.addWidget(self.importButton)

        self.setLayout(layout)
        self.videoPath = None
        self.cap = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateFrame)

    def importVideo(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "选择视频文件", "", "视频文件 (*.mp4 *.avi *.mkv)")
        if fileName:
            self.videoPath = fileName
            self.cap = cv2.VideoCapture(fileName)
            if not self.cap.isOpened():
                print("Error: 无法打开文件.")
                return
            print("Video opened successfully:", fileName)
            self.timer.start(30)
        else:
            print("No file selected.")

    def updateFrame(self):
        if self.cap is not None:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                self.monitorLabel.setPixmap(QPixmap.fromImage(image))

                # 调用AnimalAPI并更新UI
                self.recognizeAnimal(frame)
            else:
                print("Failed to read frame or end of video.")
                self.cap.release()
                self.cap = None
                self.timer.stop()
        else:
            print("No video capture available.")

    def recognizeAnimal(self, frame):
        # 保存当前帧为临时文件
        temp_image_path = 'temp_frame.jpg'
        cv2.imwrite(temp_image_path, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

        try:
            result = AnimalAPI(temp_image_path)
            if result and 'result' in result and len(result['result']) > 0:
                animal_info = result['result'][0]
                self.animalNameTextEdit.setText(animal_info.get('name', '未知'))
                baike_info = animal_info.get('baike_info', {})
                description = baike_info.get('description', '无详细信息')
                self.animalInfoTextEdit.setText(description)
            else:
                self.animalNameTextEdit.setText('识别失败')
                self.animalInfoTextEdit.setText('无详细信息')
        except Exception as e:
            print("Error during recognition:", e)
            self.animalNameTextEdit.setText('识别错误')
            self.animalInfoTextEdit.setText(str(e))

