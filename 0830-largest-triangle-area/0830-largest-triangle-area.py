class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        m = len(points)
        ans = 0.0
        for i in range(m):
            x1, y1 = points[i]
            for j in range(i+1, m):
                x2, y2 = points[j]
                for k in range(j+1, m):
                    x3, y3 = points[k]
                    area = abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)) * 0.5
                    if area > ans: ans = area
        return ans
