def solution(companies):
    cmp1 = set(companies[0])
    cmp2 = set(companies[1])
    cmp3 = set(companies[2])
    res = (((cmp1 & cmp2) | (cmp1 & cmp3) | (cmp2 & cmp3)) - (cmp1 & cmp2 & cmp3))
    return list(sorted(list(res)))
	
"""
Example

For companies = ["coolcompany", "nicecompany", "legendarycompany"],
the output should be
solution(companies) = ['e', 'l'].

Here's how the answer can be obtained:

these letters appear in all three company names and are thus mainstream: 'a', 'c', 'm', 'n', 'o', 'p', 'y';
these letters appear only in one of the company names and are thus not popular: 'd', 'g', 'i', 'r';
the remaining letters are popular and not mainstream: 'e', 'l'.
"""