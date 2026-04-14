class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in list(self.points.keys()):
            if (abs(py - y) == abs(px - x) and x != px and y != py):
                res += (
                self.points[(x, y)] *
                self.points[(px, y)] *
                self.points[(x, py)]
            )

        
        return res