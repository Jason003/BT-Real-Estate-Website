import unittest
import collections


class Solution(unittest.TestCase):
    def maxDistance(self, A):
        n = len(A)
        dq = collections.deque([(i, j) for i in range(n)
                                for j in range(n) if A[i][j]])
        if len(dq) == n * n:
            return -1
        step = 0
        while dq:
            sz = len(dq)
            for _ in range(sz):
                x, y = dq.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < n and 0 <= yy < n and not A[xx][yy]:
                        A[xx][yy] = 1
                        dq.append((xx, yy))
            step += 1
        return step - 1

    def test_maxDistance(self):
        self.assertEqual(self.maxDistance(
            [[1, 0, 0], [0, 0, 0], [0, 0, 0]]), 4)

if __name__ == '__main__':
    unittest.main()
