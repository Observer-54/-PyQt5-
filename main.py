import sys
from UI.monitorApp import MonitorApp
if __name__ == '__main__':
    app = MonitorApp()
    sys.exit(app.exec())