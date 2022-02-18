def solution(word1, word2):
    def getIdentifier(w1, w2):
        return "".join(sorted(set(w1)-set(w2)))

    return [getIdentifier(word1, word2), getIdentifier(word2, word1)]
	
"""
Example

For word1 = "program" and word2 = "develop",
the output should be
solution(word1, word2) = ["agmr", "delv"].

Letters 'o' and 'p' are present in both words, and other letters identify them uniquely.
"""