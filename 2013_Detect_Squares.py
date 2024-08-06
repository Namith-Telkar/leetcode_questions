from collections import defaultdict

class DetectSquares:
    def __init__(self):
        self.ptsCounts = defaultdict(int)
        self.pts = []
        
    def add(self, point: list[int]) -> None:
        self.ptsCounts[tuple(point)] += 1
        self.pts.append(point)
        
    def count(self, point: list[int]) -> int:
        res = 0
        qx, qy = point
        for x, y in self.pts:
            if (abs(x - qx) != abs(y - qy)) or x == qx or y == qy:
                continue
            res += self.ptsCounts[(qx, y)] * self.ptsCounts[(x, qy)]
        return res
        
