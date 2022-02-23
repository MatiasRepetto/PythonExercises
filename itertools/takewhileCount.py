from itertools import takewhile, count

def solution(start, stop, step):
    gen = takewhile(lambda x: x < stop, count(start, step))
    return list(gen)
	
'''
Example

For start = -0.9, stop = 0.45, and step = 0.2,
the output should be
solution(start, stop, step) = [-0.9, -0.7, -0.5, -0.3, -0.1, 0.1, 0.3].
'''