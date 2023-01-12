from math import tan
from numpy import array, dot, eye as matrix_eye
from Math.Vector3F import Vector3F


def rotate_scale_translate():
    return matrix_eye(4, dtype=float)


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

    return array([
        [resX.x, resY.x, resZ.x, 0],
        [resX.y, resY.y, resZ.y, 0],
        [resX.z, resY.z, resZ.z, 0],
        [-resX.dot(eye), -resY.dot(eye), -resZ.dot(eye), 1]
    ])


def perspective(fov: float, aspect_ratio: float, near_plane: float, far_plane: float):
    result = array([
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
    ])

    tangent_minus_on_degree = float(1.0 / tan(fov * 0.5))
    result.itemset((0, 0), tangent_minus_on_degree / aspect_ratio)
    result.itemset((1, 1), tangent_minus_on_degree)
    result.itemset((2, 2), (far_plane + near_plane) / (far_plane - near_plane))
    result.itemset((2, 3), 1.0)
    result.itemset((3, 2), 2 * (near_plane * far_plane) / (near_plane - far_plane))

    return result


def multiply_matrix4_by_vector3(matrix: array, vertex: Vector3F, width, height):
    return vertex_to_point(dot(array([vertex.x, vertex.y, vertex.z, 0]), matrix) / 100, width, height)


def multiply_matrix4_by_vector3_old(matrix: array, vertex: Vector3F):
    x = (vertex.x * matrix.item((0, 0))) + (vertex.z * matrix.item((1, 0))) + \
        (vertex.z * matrix.item((2, 0))) + matrix.item((3, 0))
    y = (vertex.x * matrix.item((0, 1))) + (vertex.z * matrix.item((1, 1))) + \
        (vertex.z * matrix.item((2, 1))) + matrix.item((3, 1))
    w = (vertex.x * matrix.item((0, 3))) + (vertex.z * matrix.item((1, 3))) + \
        (vertex.z * matrix.item((2, 3))) + matrix.item((3, 3))

    return x / w, y / w


def vertex_to_point(arr, width: int, height: int):
    return arr[0] * width + width / 2, -arr[1] * height - height / 2
