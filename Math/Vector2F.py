class Vector2F:
    def __init__(self, x, y):
        self.x: float = x
        self.y: float = y

    def __add__(self, other):
        return Vector2F(self.x + other.x, self.y + other.y)

