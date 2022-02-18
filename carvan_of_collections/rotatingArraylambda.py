from collections import deque

def solution(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda x: x[1].rotate(-x[0]), enumerate(res)), 0)
    return [list(d) for d in res]
	
"""
Example

For digits = [1, 2, 3, 4, 5], the output should be

solution(digits) = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2],
                           [4, 5, 1, 2, 3], [5, 1, 2, 3, 4]]
"""