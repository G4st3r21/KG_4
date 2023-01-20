from datetime import datetime

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QThread
from PySide6.QtGui import QPainter, QPaintEvent, QColor, QBrush
from PySide6.QtOpenGL import QOpenGLPaintDevice
from PySide6.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsRectItem
from Math.Vector3F import Vector3F
from ObjReader.ObjReader import read
from RenderEngine.Camera import Camera
from RenderEngine.RenderEngine import render_draw, render_new
from .interface import Ui_MainWindow
from Model.Model import Model


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.is_model_read = None
        self.renderer = None
        self.painter = None
        self.is_rendered = False
        self.antialiasing = True
        self.full_polygons = True

        self.setupUi(self)
        self.setWindowTitle("'^-^'")

        self.main_model: [Model, None] = None

        self.setMinimumWidth(1280)
        self.setMinimumHeight(720)
        self.camera: Camera = Camera(
            Vector3F(0.0, 0.0, 100.0),
            Vector3F(0.0, 0.0, 0.0),
            1.0, self.width() / self.height(), 0.01, 100
        )

        self.TRANSLATION = 2
        self.result_points = []

        self.fps = []

        self.connect_buttons()
        self.show()

    def connect_buttons(self):
        self.openObjPB.clicked.connect(self.read_model)
        self.FOVdoubleSpinBox.valueChanged.connect(self.change_fov)
        self.FOVdoubleSpinBox.setValue(self.camera.fov)
        self.NearPlaneDoubleSpinBox.valueChanged.connect(self.change_near_plane)
        self.NearPlaneDoubleSpinBox.setValue(self.camera.near_plane)
        self.FarPlaneDoubleSpinBox.valueChanged.connect(self.change_near_plane)
        self.FarPlaneDoubleSpinBox.setValue(self.camera.far_plane)
        self.AntialiasingCheckBox.clicked.connect(self.set_antialiasing)
        self.AntialiasingCheckBox.setChecked(self.antialiasing)
        self.FullPolygonsCheckBox.clicked.connect(self.set_full_polygons)
        self.FullPolygonsCheckBox.setChecked(self.full_polygons)

    def set_full_polygons(self):
        self.full_polygons = self.FullPolygonsCheckBox.isChecked()
        self.fps.clear()
        self.repaint()

    def set_antialiasing(self):
        self.antialiasing = self.AntialiasingCheckBox.isChecked()
        self.repaint()

    def change_fov(self):
        try:
            self.camera.fov = float(self.FOVdoubleSpinBox.value())
            self.repaint()
        except:
            print("нимагу:(")

    def change_near_plane(self):
        try:
            self.camera.near_plane = float(self.NearPlaneDoubleSpinBox.value())
            self.repaint()
        except:
            print("нимагу:(")

    def change_far_plane(self):
        try:
            self.camera.far_plane = float(self.FarPlaneDoubleSpinBox.value())
            self.repaint()
        except:
            print("нимагу:(")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_D:
            self.camera.move_position(Vector3F(-self.TRANSLATION, 0, 0))
        elif event.key() == Qt.Key.Key_A:
            self.camera.move_position(Vector3F(self.TRANSLATION, 0, 0))
        elif event.key() == Qt.Key.Key_W:
            self.camera.move_position(Vector3F(0, self.TRANSLATION, 0))
        elif event.key() == Qt.Key.Key_S:
            self.camera.move_position(Vector3F(0, -self.TRANSLATION, 0))
        elif event.key() == Qt.Key.Key_Z:
            self.camera.move_position(Vector3F(0, 0, self.TRANSLATION))
        elif event.key() == Qt.Key.Key_X:
            self.camera.move_position(Vector3F(0, 0, -self.TRANSLATION))
        elif event.key() == Qt.Key.Key_C:
            self.camera.set_position(Vector3F(0.0, 0.0, 100.0))

        if self.is_model_read:
            self.repaint()

    def read_model(self):
        self.is_model_read = False
        model_path = QtWidgets.QFileDialog.getOpenFileName()[0]
        with open(model_path, "r") as model:
            obj_file_content = [string.strip() for string in model.readlines()]
        self.main_model = read(obj_file_content)
        self.is_model_read = True

        self.fps.clear()
        self.repaint()

    def paintEvent(self, event: QPaintEvent) -> None:
        if len(self.fps) > 100:
            self.fps = self.fps[-100:-1]
        if self.is_model_read:
            start = datetime.now()
            self.painter = QPainter(self)
            if self.antialiasing:
                self.painter.setRenderHint(QPainter.Antialiasing)

            self.painter.fillRect(0, 0, self.width(), self.height(), Qt.GlobalColor.white)

            render_draw(self.painter, self.full_polygons, self.camera, self.main_model, self.width(), self.height())
            end = datetime.now() - start

            font = self.painter.font()
            font.setPointSize(20)
            self.painter.setFont(font)
            self.painter.setPen(QColor(0, 0, 0))
            self.fps.append(int(1 / (end.microseconds / 1000000)))
            self.painter.drawText(0, 100, f"{int(sum(self.fps) / len(self.fps))} FPS")
            self.painter.drawText(0, 130, f"Target: {self.camera.target}")
            self.painter.drawText(0, 160, f"Camera: {self.camera.position}")

            self.painter.end()

# class RenderThread(QThread):
#     def __init__(self, parent):
#         super().__init__()
#         self.parent = parent
#
#     def run(self) -> None:
#         while True:
#             self.parent.result_points = render(
#                 self.parent.camera,
#                 self.parent.main_model,
#                 self.parent.width(),
#                 self.parent.height()
#             )
#             self.parent.is_rendered = True
