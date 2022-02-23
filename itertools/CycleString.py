from itertools import cycle

def solution(name, n):
    gen = cycle(name)
    res = [next(gen) for _ in range(n)]
    return ''.join(res)
	
'''
Example

For name = "nicecoder" and n = 15, the output should be
solution(name, n) = "nicecoderniceco".
'''