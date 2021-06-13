class triangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculation(self):
        area = .5 * self.width * self.height
        print(area)

t = triangle(5,7)
t.calculation()