# -*- coding: utf-8 -*-
"""
Guess a Number between 1 and 100

Setup: The computer generates a random number between 1 and 100. The human's
goal is to guess that number in 5 or fewer guesses.


"""

import random
import time

# human number guess
hum_num = 0

# 5 trys to guess the right number
guesses = 5

# num_check =1 if guess right; =0 if guess wrong
num_check = 0

# variables to keep track of score
comp_wins = 0
comp_loss = 0


# function to check if guess is above, below, or equal to my number 
def number_check(hum_num, comp_num, guess_left):
    
    # if input is valid, then see if number is below, above, or same
    if hum_num < comp_num:
        print('My number is above %d.' % hum_num)
        number_right = 0
        
    elif hum_num > comp_num:
        print('My number is below %d.' % hum_num)        
        number_right = 0
         
    elif hum_num == comp_num:
        number_right = 1
        
    return number_right



# BEGIN GAME ##################################################################
print('Guess my number! Enter q to quit.' )
print("I'm thinking of a number between 1 and 100.")
print("Guess what number I picked with 5 or fewer guesses and you win (nothing)")

# continue playing until player wants to quit
while hum_num != 'q':
    
    # print score
    print('Score:')
    print('Human', 'Computer', sep='\t')
    print(' %s \t %s' % (comp_loss, comp_wins))
    
    guess_left = guesses
    
    # draw a number between 1 and 100
    draw = random.randrange(0, 101)
    
    while guess_left > 0:
        
        # get input from huuman
        print()
        hum_num = input('Enter number between 1 and 100: ')
        
        
        # end if user wants to quit
        if hum_num == 'q':
            print('Final Score:')
            print('Human', 'Computer', sep='\t')
            print(' %s \t %s' % (comp_loss, comp_wins))
            break
        
        # if input is invalid, report error
        hum_num = int(hum_num)
        if hum_num > 100 or hum_num < 1:
            print('Invalid entry. Enter a number between 1 and 100')
        
        else: 

            # check if human's guess it below, above, or equal to number   
            num_check = number_check(hum_num=hum_num, comp_num=draw, 
                         guess_left=guess_left)
            
            # if guess it correct, report human win and go to next game
            if num_check==1:
                print('My number is %i. You won this round!' % draw)
                comp_loss += 1
                break
        
            guess_left -= 1
            if guess_left > 1:
                print('You have %i guesses left' % guess_left)
            else:
                print('You have %i guess left' % guess_left)
        
    # if human is not able to guess correct in 5 tries, they lose
    if num_check==0 and hum_num != 'q':        
        print('My number is %i. You lost this round.' % draw)
        comp_wins += 1
        
    # short break so slow human can read and then report score
    time.sleep(2)

