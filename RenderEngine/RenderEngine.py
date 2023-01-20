from PySide6.QtGui import QPainter
from Math.Matrix import Matrix
from Model.Model import Model
from .GraphicConveyor import rotate_scale_translate, multiply_matrix4_by_vector3
from RenderEngine import Camera


def render_draw(qp: QPainter, full_polygons: bool, camera: Camera, mesh: Model, width, height):
    model_matrix = rotate_scale_translate()
    view_matrix = camera.get_view_matrix()
    projection_matrix = camera.get_projection_matrix()

    model_view_projection_matrix = model_matrix
    model_view_projection_matrix = Matrix.multiply(model_view_projection_matrix, view_matrix)
    model_view_projection_matrix = Matrix.multiply(model_view_projection_matrix, projection_matrix)
    result_points = [
        tuple(
            multiply_matrix4_by_vector3(
                model_view_projection_matrix,
                points,
                width, height
            ) for points in local_points)
        for local_points in mesh.local_points
    ]

    for result_point in result_points:
        n_vertices_in_polygon = len(list(result_point))
        if full_polygons:
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


def render_new(qp, camera: Camera, mesh: Model, width, height):
    for local_point in mesh.local_points:
        lines = [[line for line in camera.screen_projection(vector, width, height)] for vector in local_point]

        for i in range(0, len(lines) - 1):
            qp.drawLine(
                int(abs(lines[i][0])),
                int(abs(lines[i][1])),
                int(abs(lines[i + 1][0])),
                int(abs(lines[i + 1][1]))
            )
