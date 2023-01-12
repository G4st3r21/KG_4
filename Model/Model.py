from typing import List
from Math import Vector2F, Vector3F


class Model:
    def __init__(self):
        self.vertices: List[Vector3F] = []
        self.texture_vertices: List[Vector2F] = []
        self.normals: List[Vector3F] = []
        self.polygons: set = set()

        self.local_points = []

    def recalculate_points(self):
        for polygon in self.polygons:
            local_points = tuple(
                self.vertices[vertex_in_polygon]
                for vertex_in_polygon in polygon.get_vertex_indices()
            )
            self.local_points.append(local_points)


def __str__(self):
    return "\n".join([" ".join(polygon.get_vertex_indices(True)) for polygon in self.polygons])
