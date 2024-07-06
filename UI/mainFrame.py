from PyQt5 import QtWidgets, QtGui, QtCore
from UI.MainWindowUI import MainWindow
from UI.PlantUI import AnimalRecognitionWindow
from UI.AnimalUI import PlantRecognitionWindow

class MainDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel(self)
        self.setCentralWidget(self.label)
        self.pixmap = QtGui.QPixmap(":/welcome.jpg")
        # 设置QLabel的尺寸
        self.label.resize(self.width(), self.height())
        self.label.setScaledContents(True)
        # 将背景图片设置为QLabel的内容
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))
        # 监听窗口大小变化事件
        self.resizeEvent = self.on_resize
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)



    def on_resize(self, event):
        self.label.resize(self.width(), self.height())
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))


