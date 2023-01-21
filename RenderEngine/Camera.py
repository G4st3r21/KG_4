import math

from Math.Vector2F import Vector2F
from Math.Vector3F import Vector3F
from .GraphicConveyor import look_at, perspective


class Camera:
    def __init__(
            self, position: Vector3F, target: Vector3F,
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

    def screen_projection(self, target: Vector3F, width, height):
        scale = width / (2 * self.screen_dist * math.tan(self.observe_range / 2))
        delta = self.screen_dist / target.z * scale
        projection = Vector2F(target.x * delta, target.y * delta)
        in_screen_basis = projection + Vector2F(width / 2, -height / 2)
        return in_screen_basis.x, -in_screen_basis.y

    def move_position(self, translation: Vector3F):
        self.position + translation

    # TODO: Афинные сюда!

    def set_position(self, position: Vector3F):
        self.position = position

    def rotate(self, angle, axis: Vector3F):
        self.target.rotate(angle, axis)

    def get_view_matrix(self):
        return look_at(self.position, self.target)

    def get_projection_matrix(self):
        return perspective(self.fov, self.aspect_ratio, self.near_plane, self.far_plane)
