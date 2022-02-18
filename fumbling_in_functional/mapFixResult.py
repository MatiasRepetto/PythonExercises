def solution(result):
    def fix(x):
        return x // 10
		
    return list(map(fix, result))	

"""
Example

For result = [42, 239, 365, 50], the output should be
solution(result) = [4, 23, 36, 5].
"""