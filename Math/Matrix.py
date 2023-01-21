from Math.Vector2F import Vector2F
from Math.Vector4F import Vector4F


class Matrix:
    @staticmethod
    def multiply(matrix1, matrix2):
        return [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*matrix2)] for X_row in matrix1]

    @staticmethod
    def multiply_by_vector(matrix, vector: Vector4F):
        w = matrix[0][3] * vector.x + matrix[1][3] * vector.y + matrix[2][3] * vector.z + matrix[3][3]
        return Vector2F(
            (
                    matrix[0][0] * vector.x +
                    matrix[1][0] * vector.y +
                    matrix[2][0] * vector.z +
                    matrix[3][1]
            ) / w,
            (
                    matrix[0][1] * vector.x +
                    matrix[1][1] * vector.y +
                    matrix[2][1] * vector.z +
                    matrix[3][1]
            ) / w,
        )

    @staticmethod
    def mul(var0, var1):
        var0.itemset((0, 0), var0.item((0, 0)) * var1.item((0, 0)) + var0.item((0, 1)) * var1.item((1, 0)) + var0.item(
            (0, 2)) * var1.item((2, 0)) + var0.item((0, 3)) * var1.item((3, 0)))
        var0.itemset((0, 1), var0.item((0, 0)) * var1.item((0, 1)) + var0.item((0, 1)) * var1.item((1, 1)) + var0.item(
            (0, 2)) * var1.item((2, 1)) + var0.item((0, 3)) * var1.item((3, 1)))
        var0.itemset((0, 2), var0.item((0, 0)) * var1.item((0, 2)) + var0.item((0, 1)) * var1.item((1, 2)) + var0.item(
            (0, 2)) * var1.item((2, 2)) + var0.item((0, 3)) * var1.item((3, 2)))
        var0.itemset((0, 3), var0.item((0, 0)) * var1.item((0, 3)) + var0.item((0, 1)) * var1.item((1, 3)) + var0.item(
            (0, 2)) * var1.item((2, 3)) + var0.item((0, 3)) * var1.item((3, 3)))
        var0.itemset((1, 0), var0.item((1, 0)) * var1.item((0, 0)) + var0.item((1, 1)) * var1.item((1, 0)) + var0.item(
            (1, 2)) * var1.item((2, 0)) + var0.item((1, 3)) * var1.item((3, 0)))
        var0.itemset((1, 1), var0.item((1, 0)) * var1.item((0, 1)) + var0.item((1, 1)) * var1.item((1, 1)) + var0.item(
            (1, 2)) * var1.item((2, 1)) + var0.item((1, 3)) * var1.item((3, 1)))
        var0.itemset((1, 2), var0.item((1, 0)) * var1.item((0, 2)) + var0.item((1, 1)) * var1.item((1, 2)) + var0.item(
            (1, 2)) * var1.item((2, 2)) + var0.item((1, 3)) * var1.item((3, 2)))
        var0.itemset((1, 3), var0.item((1, 0)) * var1.item((0, 3)) + var0.item((1, 1)) * var1.item((1, 3)) + var0.item(
            (1, 2)) * var1.item((2, 3)) + var0.item((1, 3)) * var1.item((3, 3)))
        var0.itemset((2, 0), var0.item((2, 0)) * var1.item((0, 0)) + var0.item((2, 1)) * var1.item((1, 0)) + var0.item(
            (2, 2)) * var1.item((2, 0)) + var0.item((2, 3)) * var1.item((3, 0)))
        var0.itemset((2, 1), var0.item((2, 0)) * var1.item((0, 1)) + var0.item((2, 1)) * var1.item((1, 1)) + var0.item(
            (2, 2)) * var1.item((2, 1)) + var0.item((2, 3)) * var1.item((3, 1)))
        var0.itemset((2, 2), var0.item((2, 0)) * var1.item((0, 2)) + var0.item((2, 1)) * var1.item((1, 2)) + var0.item(
            (2, 2)) * var1.item((2, 2)) + var0.item((2, 3)) * var1.item((3, 2)))
        var0.itemset((2, 3), var0.item((2, 0)) * var1.item((0, 3)) + var0.item((2, 1)) * var1.item((1, 3)) + var0.item(
            (2, 2)) * var1.item((2, 3)) + var0.item((2, 3)) * var1.item((3, 3)))
        var0.itemset((3, 0), var0.item((3, 0)) * var1.item((0, 0)) + var0.item((3, 1)) * var1.item((1, 0)) + var0.item(
            (3, 2)) * var1.item((2, 0)) + var0.item((3, 3)) * var1.item((3, 0)))
        var0.itemset((3, 1), var0.item((3, 0)) * var1.item((0, 1)) + var0.item((3, 1)) * var1.item((1, 1)) + var0.item(
            (3, 2)) * var1.item((2, 1)) + var0.item((3, 3)) * var1.item((3, 1)))
        var0.itemset((3, 2), var0.item((3, 0)) * var1.item((0, 2)) + var0.item((3, 1)) * var1.item((1, 2)) + var0.item(
            (3, 2)) * var1.item((2, 2)) + var0.item((3, 3)) * var1.item((3, 2)))
        var0.itemset((3, 3), var0.item((3, 0)) * var1.item((0, 3)) + var0.item((3, 1)) * var1.item((1, 3)) + var0.item(
            (3, 2)) * var1.item((2, 3)) + var0.item((3, 3)) * var1.item((3, 3)))

        return var0
