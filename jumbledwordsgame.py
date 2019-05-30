# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11  2019

@author: narayanatantry
"""

import random 
def choose():
    words=['eat','water','computer','love','python','GOD','discipline'] #random words given by the user 
    pick=random.choice(words)

def jumbleword(words):
    "".join(random.sample(word,len(word)))        #creating a new function to jumble the letter in the word
    return jumble

def play():
p1 = input('your name ')
p2 = input('your name')
pp1 = 0
pp2 = 0
t = 0
while(1):                                        #the loop runs if and only if the user wants to play  
    picked_word:choose()
    qn= jumble(picked_word)
    print qn
        
if t%2==0: 
    print(p1,"your turn.")
    ans = input("what is on your mind")
    if ans==picked_word:
        pp1+=
        print('your score is',pp1)
    else:
        print("better luck next time)
    c = input("press 1 to continue and to quit :")
    if c==0:
         break
              
else:
    print(p1,"your turn.")
    ans = input("what is on your mind")
    if ans==picked_word:
        pp1+=
        print('your score is',pp1)
    else:
        print("better luck next time)
    c = input("press 1 to continue and to quit :")
    if c==0:
          break
           
              
        
    

   
