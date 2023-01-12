from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QThread
from PyQt6.QtGui import QPainter, QPixmap
from PyQt6.QtWidgets import QMainWindow
from Math.Vector3F import Vector3F
from ObjReader.ObjReader import read
from RenderEngine.Camera import Camera
from RenderEngine.RenderEngine import render
from .interface import Ui_MainWindow
from Model.Model import Model


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.is_updated = None
        self.is_model_read = None
        self.setupUi(self)
        self.setWindowTitle("'^-^'")

        self.main_model: [Model, None] = None
        self.openObjPB.clicked.connect(self.read_model)
        self.camera: Camera = Camera(
            Vector3F(0.0, 0.0, 100.0),
            Vector3F(0.0, 0.0, 0.0),
            1.0, self.width() / self.height(), 0.01, 100
        )
        self.TRANSLATION = 0.5
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_D:
            self.camera.move_position(Vector3F(-self.TRANSLATION, 0, 0))
        elif event.key() == Qt.Key.Key_A:
            self.camera.move_position(Vector3F(self.TRANSLATION, 0, 0))
        elif event.key() == Qt.Key.Key_W:
            self.camera.move_position(Vector3F(0, self.TRANSLATION, 0))
        elif event.key() == Qt.Key.Key_S:
            self.camera.move_position(Vector3F(0, -self.TRANSLATION, 0))
        elif event.key() == Qt.Key.Key_Up:
            self.camera.move_position(Vector3F(0, 0, self.TRANSLATION))
        elif event.key() == Qt.Key.Key_Down:
            self.camera.move_position(Vector3F(0, 0, -self.TRANSLATION))

        if self.is_model_read:
            self.render_model()

    def read_model(self):
        self.is_model_read = False
        model_path = QtWidgets.QFileDialog.getOpenFileName()[0]
        with open(model_path, "r") as model:
            obj_file_content = [string.strip() for string in model.readlines()]
        self.main_model = read(obj_file_content)
        self.is_model_read = True

        self.render_model()

    def render_model(self):
        pixmap = QPixmap(1080, 720)
        self.label.setPixmap(pixmap)
        painter = QPainter(pixmap)
        painter.fillRect(0, 0, 1080, 720, Qt.GlobalColor.white)
        render(painter, self.camera, self.main_model, 1080, 720)
        del painter


class ThreadDrawing(QThread):
    def __init__(self, root):
        super().__init__()
        self.qp = None
        self.root = root

    def run(self) -> None:
        while True:
            if self.root.is_updated:
                print("painting")
                self.qp = QPainter(self.root)
                self.qp.fillRect(0, 0, self.root.width(), self.root.height(), Qt.GlobalColor.white)
                self.qp.setPen(Qt.GlobalColor.black)

                self.render()
                self.root.is_updated = False

    def render(self) -> None:
        print("rendering")
        render(self.qp, self.root.camera, self.root.main_model, self.root.width(), self.root.height())
