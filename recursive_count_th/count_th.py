'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
#  i am not sure if this is allowed but i could not figure out the recursive part
def count_th(word, counter=0):
    # we have to check if the given string contains th or not, and
    # the amount of times it occurss
    # recursion only
    # base case, the word does not contain th at all, or it is empty
    word_list = list(word)
    if len(word_list) <= 1:
        return counter
    if word_list[0:2] == ['t','h']:
        counter += 1
    return count_th("".join(word_list[1:]), counter)    
       


    # if word == "":
    #     return 0
    # substring  = 'th'
    # count = word.count(substring)    
    
    # return count
    # runtime complexity O(1)