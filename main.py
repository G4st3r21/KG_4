import os
import sys
from PyQt6.QtWidgets import QApplication
from QT.InterfaceMainWindow import MainWindow

# os.system("python -m PyQt5.uic.pyuic -x QT/interface.ui -o QT/interface.py")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWindow()
    sys.exit(app.exec())
