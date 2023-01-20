import sys

import dearpygui.dearpygui as dpg
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt6.uic.properties import QtWidgets

from Math.Vector3F import Vector3F
from ObjReader.ObjReader import read
from RenderEngine.Camera import Camera
from RenderEngine.RenderEngine import render_new


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


app = QApplication(sys.argv)
widget = MainWindow()


def draw_object(all_lines, width, height):
    with dpg.window(label="3D Object"):
        with dpg.drawlist(width=width, height=height):
            dpg.draw_polygon([0, 0, width, height], color=(255, 255, 255))
            for result_point in all_lines:
                n_vertices_in_polygon = len(result_point)
                vertex_in_polygon_ind = 1
                while vertex_in_polygon_ind < n_vertices_in_polygon:
                    dpg.draw_line(
                        (int(abs(result_point[vertex_in_polygon_ind - 1][0] - width)),
                         int(abs(-result_point[vertex_in_polygon_ind - 1][1] - height))),
                        (int(abs(result_point[vertex_in_polygon_ind][0] - width)),
                         int(abs(-result_point[vertex_in_polygon_ind][1] - height)))
                    )
                    vertex_in_polygon_ind += 1

                if n_vertices_in_polygon > 0:
                    dpg.draw_line(
                        (int(abs(result_point[n_vertices_in_polygon - 1][0] - width)),
                         int(abs(-result_point[n_vertices_in_polygon - 1][1] - height))),
                        (int(abs(result_point[0][0] - width)),
                         int(abs(-result_point[0][1] - height)))
                    )
    print("drew")


model = None
rendered = False
width, height = 1080, 720
camera: Camera = Camera(
    Vector3F(0.0, 0.0, 100.0),
    Vector3F(0.0, 0.0, 0.0),
    1.0, width / height, 0.01, 100
)
dpg.create_context()
dpg.create_viewport(title="'^_^'", width=width, height=height)
dpg.setup_dearpygui()

dpg.show_viewport()
# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():
    if model:
        draw_object(render_new(camera, model, width, height), width, height)
    elif not model and not rendered:
        model_path = QFileDialog.getOpenFileName()[0]
        with open(model_path, "r") as model:
            obj_file_content = [string.strip() for string in model.readlines()]
        model = read(obj_file_content)
        rendered = True
    print("this will run every frame")
    dpg.render_dearpygui_frame()

dpg.destroy_context()
