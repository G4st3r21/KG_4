from math import e, sqrt, cos, sin


class Vector3F:
    def __init__(self, x=0, y=0, z=0):
        self.x: float = x
        self.y: float = y
        self.z: float = z

    def __str__(self):
        return f"{self.x}, {self.y}. {self.z}"

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z

    def rotate(self, angle, axis):
        self.x = self.x * cos(angle) + sin(angle) * (axis.x * self.x) + (1 - cos(angle)) * (axis.x * self.x) * axis.x
        self.y = self.y * cos(angle) + sin(angle) * (axis.y * self.y) + (1 - cos(angle)) * (axis.y * self.y) * axis.y
        self.z = self.z * cos(angle) + sin(angle) * (axis.z * self.z) + (1 - cos(angle)) * (axis.z * self.z) * axis.z

    def cross(self, var1, var2):
        var3 = var1.y * var2.z - var1.z * var2.y
        var4 = var2.x * var1.z - var2.z * var1.x
        var5 = var1.x * var2.y - var1.y * var2.x
        self.x, self.y, self.z = var3, var4, var5

    def sub(self, var1, var2):
        self.x = var1.x - var2.x
        self.y = var1.y - var2.y
        self.z = var1.z - var2.z

    def normalise(self):
        var1 = 1.0 / sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        self.x *= var1
        self.y *= var1
        self.z *= var1

    def dot(self, var1):
        return self.x * var1.x + self.y * var1.y + self.z * var1.z

    def __eq__(self, other):
        return abs(self.x - other.x) < e and \
            abs(self.y - other.y) < e and \
            abs(self.z - other.z) < e
