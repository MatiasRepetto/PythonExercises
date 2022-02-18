def solution(document):
    return sorted([x for i, x in enumerate(document) if x not in document[0:i]])

"""
Example

For document = "Todd told Tom to trot to the timber",
the output should be
solution(document) = [' ', 'T', 'b', 'd', 'e', 'h', 'i', 'l', 'm', 'o', 'r', 't'].
"""