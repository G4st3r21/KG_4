from array import *
from typing import List
import numpy as np

from Model.Model import Model
from Model.Polygon import Polygon
from ObjReader.ObjReaderException import ObjReaderException


def read(file_content: List[str]):
    res_model = Model()
    for string in file_content:
        line_words = string.split()
        if line_words:
            token = line_words[0]
            if token == "v":
                res_model.vertices.append(parse_vertex(line_words))
            elif token == "vt":
                res_model.texture_vertices.append(parse_texture_vertex(line_words))
            elif token == "vn":
                res_model.normals.append(parse_normal(line_words))
            elif token == "f":
                res_model.polygons.append(parse_face(line_words))

    return res_model


def parse_vertex(line_words: List[str]):
    try:
        return np.array([float(line_words[1]), float(line_words[2]), float(line_words[3])])
    except IndexError:
        raise ObjReaderException(f"Неподходящее кол-во координат(нужно 3)")
    except ValueError:
        raise ObjReaderException(f"Невозможно прочитать файл")


def parse_texture_vertex(line_words: List[str]):
    try:
        return np.array([float(line_words[1]), float(line_words[2])])
    except IndexError:
        raise ObjReaderException(f"Неподходящее кол-во координат(нужно 3)")
    except ValueError:
        raise ObjReaderException(f"Невозможно прочитать файл")


def parse_normal(line_words: List[str]):
    try:
        return np.array([float(line_words[1]), float(line_words[2]), float(line_words[3])])
    except IndexError:
        raise ObjReaderException(f"Неподходящее кол-во координат(нужно 3)")
    except ValueError:
        raise ObjReaderException(f"Невозможно прочитать файл")


def parse_face(line_words):
    one_polygon_vertex_indices: array = array('i')
    one_polygon_texture_vertex_indices: array = array('i')
    one_polygon_normal_indices: array = array('i')

    for word in line_words[1:]:
        parse_face_word(
            word,
            one_polygon_vertex_indices,
            one_polygon_texture_vertex_indices,
            one_polygon_normal_indices
        )

    polygon = Polygon()
    polygon.set_vertex_indices(one_polygon_vertex_indices)
    polygon.texture_vertex_indices = one_polygon_texture_vertex_indices
    polygon.normal_indices = one_polygon_normal_indices

    return polygon


def parse_face_word(
        word: str,
        one_polygon_vertex_indices,
        one_polygon_texture_vertex_indices,
        one_polygon_normal_indices
):
    try:
        word_indices = word.split("/")

        if len(word_indices) == 1:
            one_polygon_vertex_indices.append(int(word_indices[0]) - 1)
        elif len(word_indices) == 2:
            one_polygon_vertex_indices.append(int(word_indices[0]) - 1)
            one_polygon_texture_vertex_indices.append(int(word_indices[1]) - 1)
        elif len(word_indices) == 3:
            one_polygon_vertex_indices.append(int(word_indices[0]) - 1)
            if word_indices[1] == "":
                one_polygon_texture_vertex_indices.append(int(word_indices[1]) - 1)
            one_polygon_normal_indices.append(int(word_indices[2]) - 1)
        else:
            raise ObjReaderException(f"Неверное кол-во аргументов")

    except IndexError:
        raise ObjReaderException(f"Неподходящее кол-во координат")
    except ValueError:
        raise ObjReaderException(f"Невозможно прочитать файл")
