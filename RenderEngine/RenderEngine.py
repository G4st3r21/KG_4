from PySide6.QtGui import QPainter

from Math.Matrix import Matrix
from Math.Vector3F import Vector3F
from Model.Model import Model
from .GraphicConveyor import rotate_scale_translate, multiply_matrix4_by_vector3
from RenderEngine import Camera


def render(qp: QPainter, polygon_quality: int, camera: Camera, mesh: Model, width, height):
    model_matrix = rotate_scale_translate()
    view_matrix = camera.get_view_matrix()
    projection_matrix = camera.get_projection_matrix()

    model_view_projection_matrix = model_matrix
    model_view_projection_matrix = Matrix.multiply(model_view_projection_matrix, view_matrix)
    model_view_projection_matrix = Matrix.multiply(model_view_projection_matrix, projection_matrix)
    # mesh.recalculate_poly_avg_dz(cam_pos=camera.position)

    all_res_points = []
    for polygon in mesh.polygons:
        n_vertices_in_polygon = len(polygon.get_vertex_indices())
        result_points = []
        for vertex_in_polygon_ind in range(n_vertices_in_polygon):
            vertex = mesh.vertices[polygon.get_vertex_indices()[vertex_in_polygon_ind]]
            vertex_vecmath = Vector3F(vertex.x, vertex.y, vertex.z)
            result_point = multiply_matrix4_by_vector3(model_view_projection_matrix, vertex_vecmath, width, height)
            result_points.append(result_point)
        all_res_points.append(result_points)

    for result_points in all_res_points:
        for line_count in range(polygon_quality):
            qp.drawLine(
                int(result_points[line_count - 1][0]),
                int(-result_points[line_count - 1][1]),
                int(result_points[line_count][0]),
                int(-result_points[line_count][1]),
            )