class Matrix:
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
