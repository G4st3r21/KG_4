from math import tan

from PySide6.QtCore import QPoint

from Math.Matrix import Matrix
from Math.Vector2F import Vector2F
from Math.Vector3F import Vector3F
from Math.Vector4F import Vector4F


def rotate_scale_translate():
    return [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]


def look_at(eye: Vector3F, target: Vector3F, up: [Vector3F, None] = None):
    if not up:
        up = Vector3F(0.0, 1.0, 0.0)

    resX, resY, resZ = Vector3F(), Vector3F(), Vector3F()

    resZ.sub(target, eye)
    resX.cross(up, resZ)
    resY.cross(resZ, resX)

    resX.normalise()
    resY.normalise()
    resZ.normalise()

    return [
        [resX.x, resY.x, resZ.x, 0],
        [resX.y, resY.y, resZ.y, 0],
        [resX.z, resY.z, resZ.z, 0],
        [-resX.dot(eye), -resY.dot(eye), -resZ.dot(eye), 1]
    ]


def perspective(fov: float, aspect_ratio: float, near_plane: float, far_plane: float):
    result = [
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
    ]

    tangent_minus_on_degree = float(1.0 / tan(fov * 0.5))
    result[0][0] = tangent_minus_on_degree / aspect_ratio
    result[1][1] = tangent_minus_on_degree
    result[2][2] = (far_plane + near_plane) / (far_plane - near_plane)
    result[2][3] = 1.0
    result[3][2] = 2 * (near_plane * far_plane) / (near_plane - far_plane)

    return result


def multiply_matrix4_by_vector3(matrix, vertex, width, height):
    return vertex_to_point(Matrix.multiply_by_vector(matrix, Vector4F(vertex.x, vertex.y, vertex.z)), width, height)


def vertex_to_point(vector: Vector2F, width: int, height: int):
    return vector.x * width + width / 2, vector.y * height - height / 2
