import math
from .GraphicConveyor import look_at, perspective
import numpy as np


class Camera:
    def __init__(
            self, position, target,
            fov: float, aspect_ratio: float, near_plane: float, far_plane: float,
            observe_range: float = math.pi / 2, screen_dist: float = 100
    ):
        self.position = position
        self.target = target
        self.fov = fov
        self.aspect_ratio = aspect_ratio
        self.near_plane = near_plane
        self.far_plane = far_plane
        self.screen_dist = screen_dist
        self.observe_range = observe_range

    def screen_projection(self, target, width, height):
        scale = width / (2 * self.screen_dist * math.tan(self.observe_range / 2))
        delta = self.screen_dist / target.z * scale
        projection = np.array([target.x * delta, target.y * delta])
        in_screen_basis = projection + np.array([width / 2, -height / 2])
        return in_screen_basis.x, -in_screen_basis.y

    def move_position(self, translation):
        self.position += translation

    def set_position(self, position):
        self.position = position

    def rotate(self, angle, axis):
        self.target.rotate(angle, axis)

    def get_view_matrix(self):
        return look_at(self.position, self.target)

    def get_projection_matrix(self):
        return perspective(self.fov, self.aspect_ratio, self.near_plane, self.far_plane)
