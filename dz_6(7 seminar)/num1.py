class Vector:
    def __init__(self, x, y, z):
        assert isinstance(x, (int, float)) and not isinstance(x, bool)
        assert isinstance(y, (int, float)) and not isinstance(y, bool)
        assert isinstance(z, (int, float)) and not isinstance(z, bool)
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __add__(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, (int, float)) and not isinstance(other, bool):
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError("Unsupported operand type for multiplication")
 
    def __str__(self):
        return f"x = {self.x}, y = {self.y}, z = {self.z}"

    def __truediv__(self, other):
        if isinstance(other, (int, float)) and not isinstance(other, bool):
            return Vector(self.x / other, self.y / other, self.z / other)
        else:
            raise TypeError("Unsupported operand type for division")

    def vector_mul(self, other):
        assert isinstance(other, Vector)
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def mass_center(l):
        res = Vector(0, 0, 0)
        for i in l:
            res += i
        return res/len(l)

    def area(x, y, z):
        return (abs((y - x).vector_mul(z - x)))/2

    def max_area(l):
        cur_max = 0
        res = ()

        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                for k in range(j + 1, len(l)):
                    t = Vector.area(l[i], l[j], l[k])
                    if t > cur_max:
                        cur_max = t
                        res = (l[i], l[j], l[k])
        return cur_max, res

