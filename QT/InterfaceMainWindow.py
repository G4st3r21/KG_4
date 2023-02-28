from datetime import datetime
from typing import List

from PySide6 import QtWidgets
from PySide6.QtGui import QPainter, QPaintEvent, QColor, Qt
from PySide6.QtWidgets import QMainWindow

from Math.Vector3F import Vector3F
from ObjReader.ObjReader import read
from RenderEngine.Camera import Camera
from RenderEngine.RenderEngine import render
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
        self.polygon_quality = 4

        self.setupUi(self)
        self.setWindowTitle("'^-^'")

        self.models: List[Model] = []
        self.actual_model: [Model, None] = None
        self.cameras: List[Camera] = []
        self.actual_camera: [Camera, None] = None

        self.setMinimumWidth(1280)
        self.setMinimumHeight(720)

        self.translation = 0.5
        self.result_points = []

        self.fps = []

        self.connect_buttons()
        self.show()

    def connect_buttons(self):
        self.openObjPB.clicked.connect(self.read_model)

        self.ActualModelComboBox.currentIndexChanged.connect(self.change_actual_model)
        if self.actual_camera:
            self.FOVhorizontalSlider.setValue(self.actual_camera.fov)
        self.FOVhorizontalSlider.valueChanged.connect(self.change_fov)

        self.TranslationDoubleSpinBox.valueChanged.connect(self.change_translation)
        self.TranslationDoubleSpinBox.setValue(self.translation)

        self.AntialiasingCheckBox.clicked.connect(self.set_antialiasing)
        self.AntialiasingCheckBox.setChecked(self.antialiasing)

        self.MaksimalRadioButton.clicked.connect(self.setMaksPolyQuality)
        self.MediumRadioButton.clicked.connect(self.setMedPolyQuality)
        self.MinimalRadioButton.clicked.connect(self.setMinPolyQuality)
        self.MaksimalRadioButton.setChecked(True)

    def setMaksPolyQuality(self):
        self.polygon_quality = 4
        self.fps.clear()
        self.repaint()

    def setMedPolyQuality(self):
        self.polygon_quality = 2
        self.fps.clear()
        self.repaint()

    def setMinPolyQuality(self):
        self.polygon_quality = 1
        self.fps.clear()
        self.repaint()

    def change_translation(self):
        self.translation = self.TranslationDoubleSpinBox.value()

    def change_actual_model(self):
        model_index = self.ActualModelComboBox.currentIndex()
        self.actual_model = self.models[model_index]
        self.actual_camera = self.cameras[model_index]
        self.fps.clear()
        self.repaint()

    def generate_new_camera(self):
        return Camera(
            Vector3F(0.0, 0.0, 100.0),
            Vector3F(0.0, 0.0, 0.0),
            1.0, self.width() / self.height(), 0.01, 100
        )

    def update_FPS(self):
        if len(self.fps) > 100:
            self.fps = self.fps[-100:-1]
        self.FPSLabel.setText(f"{int(sum(self.fps) / len(self.fps))}")

    def update_positions(self):
        self.CameraPosLabel.setText(
            f"x: {self.actual_camera.position.x}"
            f" y: {self.actual_camera.position.y} "
            f" z: {self.actual_camera.position.z}"
        )
        self.TargetPosLabel.setText(
            f"x: {self.actual_camera.target.x}"
            f" y: {self.actual_camera.target.y} "
            f" z: {self.actual_camera.target.z}"
        )
        self.CameraPosLabel.setAlignment(Qt.AlignCenter)
        self.TargetPosLabel.setAlignment(Qt.AlignCenter)

    def set_antialiasing(self):
        self.antialiasing = self.AntialiasingCheckBox.isChecked()
        self.repaint()

    def change_fov(self):
        value = self.FOVhorizontalSlider.value()
        if value != 0:
            self.actual_camera.fov = float(self.FOVhorizontalSlider.value() / 100)
        else:
            self.actual_camera.fov = 1
        self.repaint()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_D:
            self.actual_camera.move_position(Vector3F(-self.translation, 0, 0))
        elif event.key() == Qt.Key.Key_A:
            self.actual_camera.move_position(Vector3F(self.translation, 0, 0))
        elif event.key() == Qt.Key.Key_W:
            self.actual_camera.move_position(Vector3F(0, self.translation, 0))
        elif event.key() == Qt.Key.Key_S:
            self.actual_camera.move_position(Vector3F(0, -self.translation, 0))
        elif event.key() == Qt.Key.Key_Z:
            self.actual_camera.move_position(Vector3F(0, 0, self.translation))
        elif event.key() == Qt.Key.Key_X:
            self.actual_camera.move_position(Vector3F(0, 0, -self.translation))
        elif event.key() == Qt.Key.Key_C:
            self.actual_camera.set_position(Vector3F(0.0, 0.0, 100.0))

        if self.is_model_read:
            self.repaint()

    def read_model(self):
        self.is_model_read = False
        model_path = QtWidgets.QFileDialog.getOpenFileName()[0]
        if model_path:
            with open(model_path, "r") as model:
                obj_file_content = [string.strip() for string in model.readlines()]
            model = read(obj_file_content)
            if model not in self.models:
                self.models.append(model)
                self.actual_model = self.models[-1]
                self.cameras.append(self.generate_new_camera())
                self.actual_camera = self.cameras[-1]
                current_model_name = model_path.split("/")[-1].split(".")[0]
                self.ActualModelComboBox.addItem(current_model_name)
                self.ActualModelComboBox.setCurrentText(current_model_name)
                self.is_model_read = True

        self.fps.clear()
        self.repaint()

    def paintEvent(self, event: QPaintEvent) -> None:
        if self.is_model_read:
            start = datetime.now()
            self.painter = QPainter(self)

            # if self.antialiasing:
            #     self.painter.setRenderHint(QPainter.Antialiasing)
            self.painter.fillRect(0, 0, self.width(), self.height(), Qt.GlobalColor.white)
            self.painter.setPen(QColor(0, 0, 0))
            render(
                self.painter, self.polygon_quality,
                self.actual_camera, self.actual_model,
                self.width(), self.height()
            )

            end = datetime.now() - start
            self.fps.append(int(1 / (end.microseconds / 1000000)))

            self.update_FPS()
            self.update_positions()

            self.painter.end()
