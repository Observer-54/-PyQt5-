from PyQt5.QtWidgets import QApplication
from UI.MainWindowUI import MainWindow
import sys


class MonitorApp(QApplication):
    def __init__(self):
        super(MonitorApp, self).__init__(sys.argv)
        self.window = MainWindow()
        self.window.show()