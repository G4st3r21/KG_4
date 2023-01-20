import os
import sys
from PySide6.QtWidgets import QApplication
from QT.InterfaceMainWindow import MainWindow

# os.system("python -m PyQt5.uic.pyuic -x QT/interface.ui -o QT/interface.py")

if __name__ == '__main__':
    os.system("export QT_QPA_PLATFORM=wayland")
    app = QApplication(sys.argv)
    widget = MainWindow()
    sys.exit(app.exec())
