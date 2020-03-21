'''
Given a string and dictionary of words determine if the string can be constructed
from the words given in the dictionary.

Time complexity : O(nW)
Space complexity: O(n)

'''

def wordBreak(dictionary, string):

    # store if string of length i can be broken only using given words
    T = [False] * len(string)

    for i in range(len(string)):
        for word in dictionary:
            if string[i+1-len(word):i+1]==word and (T[i-len(word)] or i-len(word)==-1):
                T[i] = True 

    return T[-1]

if __name__ == '__main__':
    dictionary = ['this', 'th', 'Word', 'break', 'problem', 'b', 'r', 'brea', 'prob', 'lem']
    string = "Wordbreakproblem"

    print("\nWord Breakable = %s\n" % wordBreak(dictionary, string))
