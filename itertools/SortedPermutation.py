from itertools import permutations

def solution(players):
    return sorted(list(permutations(players, 2)))
	
'''
Example

For players = ["trainee", "warrior", "ninja"], the output should be

solution(players) = [["ninja", "trainee"], ["ninja", "warrior"], 
                              ["trainee", "ninja"], ["trainee", "warrior"], 
                              ["warrior", "ninja"], ["warrior", "trainee"]]
'''