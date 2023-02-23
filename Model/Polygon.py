from array import *


class Polygon:
    def __init__(self):
        self.__vertex_indices = array('f')
        self.texture_vertex_indices = array('f')
        self.normal_indices = array('f')
        self.avg_dz = -1

    def set_vertex_indices(self, vertex_indices: array):
        assert len(vertex_indices) >= 3

        self.__vertex_indices = vertex_indices

    def get_vertex_indices(self, need_str=False):
        return self.__vertex_indices if not need_str else [str(vi) for vi in self.__vertex_indices]
