from typing import List
from Model.Polygon import Polygon
from numpy import array


class Model:
    def __init__(self):
        self.vertices: List[array] = []
        self.texture_vertices: List[array] = []
        self.normals: List[array] = []
        self.polygons: List[Polygon] = []
        self.visible_polygons: List[Polygon] = []

    def recalculate_poly_avg_dz(self, cam_pos: array):
        x, y, z = cam_pos[0], cam_pos[1], cam_pos[2]
        for polygon in self.polygons:
            dz_list = []
            n_vertices_in_polygon = len(polygon.get_vertex_indices())
            for vertex_in_polygon_ind in range(n_vertices_in_polygon):
                vertex = self.vertices[polygon.get_vertex_indices()[vertex_in_polygon_ind]]
                dz_list.append(((vertex[0] - x) ** 2 + (vertex[1] - y) ** 2 + (vertex[2] - z) ** 2) ** 0.5)

            polygon.avg_dz = sum(dz_list) / len(dz_list)



    def __str__(self):
        return "\n".join([" ".join(polygon.get_vertex_indices(True)) for polygon in self.polygons])
