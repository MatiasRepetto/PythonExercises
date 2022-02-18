def solution(bestStudents, scholarships, allStudents):
    return len(scholarships) < len(allStudents) and sum([x in allStudents for x in scholarships]) == len(scholarships) and sum([x in scholarships for x in bestStudents]) == min(len(bestStudents), len(scholarships))
	
"""
Example

For bestStudents = [3, 5], scholarships = [3, 5, 7], and
allStudents = [1, 2, 3, 4, 5, 6, 7], the output should be
solution(bestStudents, scholarships, allStudents) = true;

For bestStudents = [3, 5], scholarships = [3, 5], and
allStudents = [3, 5], the output should be
solution(bestStudents, scholarships, allStudents) = false.

All students get a scholarship, which is not correct.

For bestStudents = [3], scholarships = [1, 3, 5], and
allStudents = [1, 2, 3], the output should be
solution(bestStudents, scholarships, allStudents) = false.

There's no student with id 5, yet somehow he managed to get a scholarship.
"""