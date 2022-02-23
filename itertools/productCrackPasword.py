from itertools import product

def solution(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted([createNumber(x) for x in product(digits, repeat=k) if int(createNumber(x)) % d == 0])
	
'''
Example

For digits = [1, 5, 2], k = 2, and d = 3,
the output should be
solution(digits, k, d) = ["12", "15", "21", "51"].

Here are all the numbers of length 2: 11, 15, 12, 51, 55, 52, 21, 25 and 22. Only four of them are divisible by 3, and they comprise the answer.
'''