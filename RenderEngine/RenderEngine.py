from datetime import datetime

from PyQt6.QtGui import QPainter
from Math.Matrix import Matrix
from Model.Model import Model
from .GraphicConveyor import rotate_scale_translate, vertex_to_point, multiply_matrix4_by_vector3
from RenderEngine import Camera
from numpy import copy


def render(qp: QPainter, camera: Camera, mesh: Model, width, height):
    now = datetime.now()

    model_matrix = rotate_scale_translate()
    view_matrix = camera.get_view_matrix()
    projection_matrix = camera.get_projection_matrix()

    model_view_projection_matrix = copy(model_matrix)
    model_view_projection_matrix = Matrix.mul(model_view_projection_matrix, view_matrix)
    model_view_projection_matrix = Matrix.mul(model_view_projection_matrix, projection_matrix)

    for local_points in mesh.local_points:
        result_point = tuple(
            multiply_matrix4_by_vector3(
                model_view_projection_matrix,
                points,
                width, height
            ) for points in local_points)
        n_vertices_in_polygon = len(result_point)
        vertex_in_polygon_ind = 1
        while vertex_in_polygon_ind < n_vertices_in_polygon:
            qp.drawLine(
                int(abs(result_point[vertex_in_polygon_ind - 1][0] - width)),
                int(abs(-result_point[vertex_in_polygon_ind - 1][1] - height)),
                int(abs(result_point[vertex_in_polygon_ind][0] - width)),
                int(abs(-result_point[vertex_in_polygon_ind][1] - height))
            )
            vertex_in_polygon_ind += 1

        if n_vertices_in_polygon > 0:
            qp.drawLine(
                int(abs(result_point[n_vertices_in_polygon - 1][0] - width)),
                int(abs(-result_point[n_vertices_in_polygon - 1][1] - height)),
                int(abs(result_point[0][0] - width)),
                int(abs(-result_point[0][1] - height))
            )
    print(datetime.now() - now)
