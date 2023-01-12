from Math.Vector2F import Vector2F
from Math.Vector3F import Vector3F
from Model.Model import Model


class ObjWriter:
    def __init__(self, model: Model = None):
        self.model = model if model else Model()

    @staticmethod
    def get_content(model: Model):
        obj_writer = ObjWriter(model)

        return obj_writer

    @staticmethod
    def _get_vector2f_with_token_in_string(vector: Vector2F, token):
        return token + str(int(vector.x)) + " " + str(int(vector.y))

    @staticmethod
    def _get_vector3f_with_token_in_string(vector: Vector3F, token):
        return token + str(int(vector.x)) + " " + str(int(vector.y)) + " " + str(int(vector.z))

    def write_obj_file(self):
        lines = []
        self.__append_vertices_in_lines(lines)
        self.__append_textures_in_lines(lines)
        self.__append_normals_in_lines(lines)
        self.__append_faces_in_lines(lines)

        return "".join(lines)

    def __append_vertices_in_lines(self, lines: List[str]):
        if len(self.model.vertices) == 0:
            raise ValueError("Невозможно создать объект без вершин")
        else:
            for vertex in self.model.vertices:
                lines.append(self._get_vector3f_with_token_in_string(vertex, "v"))
                lines.append("\n")

    def __append_textures_in_lines(self, lines: List[str]):
        if self.model.texture_vertices:
            for vertex in self.model.texture_vertices:
                lines.append(self._get_vector3f_with_token_in_string(vertex, "vt"))
                lines.append("\n")

    def __append_normals_in_lines(self, lines: List[str]):
        if self.model.normals:
            for normal in self.model.normals:
                lines.append(self._get_vector3f_with_token_in_string(normal, "vn"))
                lines.append("\n")

    def __append_faces_in_lines(self, lines: List[str]):
        if self.model.polygons:
            raise ValueError("Невозможно создать объект без полигонов")
        else:
            for i in range(len(self.model.polygons)):
                polygon = self.model.polygons[i]
                lines.append("f")
                lines.append(" ")
                for index in range(len((polygon.get_vertex_indices()))):
                    lines.append(str(int(polygon.get_vertex_indices()[index]) + 1))

                    texture_index = None
                    if len(polygon.texture_vertex_indices) > 0:
                        texture_index = polygon.texture_vertex_indices[index] + 1
                        lines.append("/")
                        lines.append(str(texture_index))
                        lines.append(" ")

                    if len(polygon.normal_indices) > 0:
                        if not texture_index:
                            lines.append("/")

                        lines.append("/")
                        lines.append(str(int(polygon.normal_indices[index]) + 1))

                    if index < polygon.get_vertex_indices() - 1:
                        lines.append(" ")

                if i < len(polygon) - 1:
                    lines.append("\n")
