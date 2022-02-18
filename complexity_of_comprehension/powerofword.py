def solution(word):
    num = {o: ord(o)-96 for o in word} //['a': 1, 'b': 2, 'c': 3......]
    return sum([num[ch] for ch in word])    