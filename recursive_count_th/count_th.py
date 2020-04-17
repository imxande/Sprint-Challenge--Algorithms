'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # Base Case
    if  len(word) < 2: 
        return 0

    # Need a way to reduce all cases back to the base case so I need a counter    
    count = 0

    # checkin if word has the "th" if so add on to the count
    if word[0] == 't' and word[1] == 'h':
        count = 1 # if this is true I need to set count to 1 

    # Recursion is hapening here, if base case is not reach yet call count_th again and repeat
    count += count_th(word[1:])

    return count
    


  
