#!/usr/bin/env python3

# Assignment 4
# Philip Johnson
# 09/25/2021
# Manipulating Dictionary data structures

# define the glossary using a python dictionary data structure
shoppingList = []

exitOption = 'x'
currentIndex = 0
inMenu = True

while inMenu:
    userAnswer = input("Please enter a sandwich type, or x to exit: ")
    print("Adding {} to the order list".format(userAnswer))
    if userAnswer == exitOption:
        inMenu = False
    else:
        shoppingList.insert(currentIndex,userAnswer)
        currentIndex += 1
else:
    for sandwich in shoppingList:
        print("I made your {} sandwich".format(sandwich))

    print("The following sandwiches were made: ")
    for order in shoppingList:
        print(order)

