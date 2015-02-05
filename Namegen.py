# -*- coding: utf-8 -*-
"""
Created on Wed Feb 04 22:54:58 2015

@author: Edward
"""

from random import randint

def roll(a=1,b=6,c=0):
    """The syntax for this function is "roll(adb +c)", where a, b, and c are 
    integers. Default values are listed above, and will roll an unmodified d6.
    Please don't break my function by putting floats, strings, lists, dicts, 
    etc in a, b, or c, as I haven't put in any exceptions yet :)"""
    d = 0
    for x in range(0, a):
        d = d + randint(1,b)
        print d
    return(d + c)
    
def make_word(a=-1):
    """This is probably very buggy, not gonna lie. "make_word(a)", where a is 
    the optional length of the word you want to make. There's no particular 
    special rules in here. You can only have the same letter twice in a row, 
    and you can only have two vowels or consonants in a row. If it breaks, well, 
    I rewrote this at 00:00, so I don't care :)"""
    length = a
    if(a<=0):
        length = roll(1,12,3)
    print "Length = %s" % length
    thisletter = 0
    currentletter = 0
    lastletter = 0
    currentlength = 0
    vowels = ["A","E","I","O","U"]
    word = ""
    while currentlength < length:
        thisletter = chr(roll(1,26,64))
        if currentlength > 1 and (currentletter == lastletter == thisletter):
            print "Identical previous and current letter"
        elif currentlength > 1 and (thisletter in vowels) and (currentletter in vowels) and (lastletter in vowels):
            #currentlength -= 1
            print "Three vowels in a row"
        elif currentlength > 1 and (thisletter not in vowels) and (currentletter not in vowels) and (lastletter not in vowels):
            #currentlength -= 1
            print "Three consonants in a row"
        else:
            lastletter = currentletter
            currentletter = thisletter
            print currentletter
            word += thisletter
            currentlength += 1
            print "Successfully added a letter"
    return word