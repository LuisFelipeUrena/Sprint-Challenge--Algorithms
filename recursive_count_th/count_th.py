'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # we have to check if the given string contains th or not, and
    # the amount of times it occurss
    # recursion only
    # base case, the word does not contain th at all, or it is empty
    if word == "":
        return 0
    substring  = 'th'
    count = word.count(substring)    
    
    return count
    # runtime complexity O(n)