def solution(ids, k):
    digitSum = lambda i: sum(int(x) for x in str(i))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0