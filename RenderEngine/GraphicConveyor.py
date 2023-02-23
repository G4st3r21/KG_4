from math import tan
import numpy as np


def rotate_scale_translate():
    return [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]


def look_at(eye, target, up=None):
    if not up:
        up = np.array([0.0, 1.0, 0.0])

    # resX, resY, resZ = np.array('f'), np.array('f'), np.array('f')

    resZ = target - eye
    # resZ.sub(target, eye)
    resX = np.cross(up, resZ)
    resY = np.cross(resZ, resX)

    resX = resX / np.linalg.norm(resX)
    resY = resY / np.linalg.norm(resY)
    resZ = resZ / np.linalg.norm(resZ)

    return [
        [resX[0], resY[0], resZ[0], 0],
        [resX[1], resY[1], resZ[1], 0],
        [resX[2], resY[2], resZ[2], 0],
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
    return vertex_to_point(np.matmul(matrix, np.array([vertex[0], vertex[1], vertex[2], 0])), width, height)


def vertex_to_point(vector, width: int, height: int):
    return vector[0] * width + width / 2, vector[1] * height - height / 2
