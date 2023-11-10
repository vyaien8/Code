class DetectSquares:
    def __init__(self) -> None:
        self.count = {}
    def add(self, point: [int]):
        self.count[tuple(point)] = self.count.get(tuple(point), 0) + 1
    def count(self, point: [int]):
        res = 0
        px, py = point
        for x, y in list(self.count.keys()):
            if x == px or y == py or (abs(py - y) != abs(px - x)):
                continue
            res += self.count.get((x, py), 0) * self.count.get((y, px), 0)
        return res