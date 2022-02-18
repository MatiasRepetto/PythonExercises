from collections import Counter

def solution(encryptedText):
    return Counter(encryptedText).most_common(1)[0][0]
	
"""
Example

For encryptedText = "$~NmiNmim$/NVeirp@dlzrCCCCfFfQQQ",
the output should be
solution(encryptedText) = 'C'.

Letter 'C' appears in the text more than any other character (4 times), which is why it is the answer.
"""