import numpy as np
from numpy import ndarray
from Math.Vector3F import Vector3F


class Pivot:
    def __init__(self, center: Vector3F, x_axis: Vector3F, y_axis: Vector3F, z_axis: Vector3F):
        self.center: Vector3F = center
        self.x_axis: Vector3F = x_axis
        self.y_axis: Vector3F = y_axis
        self.z_axis: Vector3F = z_axis

        self.local_matrix3: ndarray = np.array([
            [self.x_axis.x, self.y_axis.x, self.z_axis.x],
            [self.x_axis.y, self.y_axis.y, self.z_axis.y],
            [self.x_axis.z, self.y_axis.z, self.z_axis.z]
        ])
        self.global_matrix3: ndarray = np.array([
            [self.x_axis.x, self.x_axis.y, self.x_axis.z],
            [self.y_axis.x, self.y_axis.y, self.y_axis.z],
            [self.z_axis.x, self.z_axis.y, self.z_axis.z]
        ])

    def to_local_coords(self, v_global: Vector3F):
        return self.local_matrix3 * (v_global - self.center)

    def to_global_coords(self, v_local: Vector3F):
        return (self.local_matrix3 * v_local) + self.center

    def move(self, v: Vector3F):
        self.center + v

    def rotate(self, angle: float, axis: Vector3F):
        self.x_axis.rotate(angle, axis)
        self.y_axis.rotate(angle, axis)
        self.z_axis.rotate(angle, axis)
