#!/usr/bin/env python3

# lottery.py
# Philip Johnson
# 09/10/2021
# generate a sequence of lottery tickets and print their stats

from random import randint


# constants
LIMIT = 50
NUM_DIGITS = 6


# function to get average of a list
def find_mean(_list):
    _res = sum(_list) / len(_list)
    return _res


# function to get the median value of a list
def find_median(_list):
    _list.sort()
    # this operator returns a floor div so if the length of a list is odd
    # then we will return an integer instead of a float
    mid = len(_list) // 2
    _res = (_list[mid] + _list[~mid]) / 2
    return _res


# returns min value from list
def find_min(_list):
    return min(_list)


# returns max value from list
def find_max(_list):
    return max(_list)


# prompt user for number of lottery number lists
num = int(input("How many lottery tickets would you like? "))
print()

# for each ticket requested
for ticket in range(1, num+1):
    _number_list = []

    # append NUM_DIGITS random integers between 1 and LIMIT to list
    for _count in range(1, NUM_DIGITS+1):
        _number_list.append(randint(1, LIMIT))

    # show this ticket
    print(str(ticket) + ": " + str(_number_list))

    # generate the stats we need based off of the values from _number_list
    # converting to string values to fill each index of a list we will create
    _mean = "Mean = " + str(round(find_mean(_number_list)))
    _median = "Median = " + str(round(find_median(_number_list)))
    _min = "Min = " + str(find_min(_number_list))
    _max = "Max = " + str(find_max(_number_list))

    # creating a new list to store the values of our newly generated stats
    _stat_list = [_mean, _median, _min, _max]

    print("Ticket summary: ")
    # loop through our newly created list
    for _count in range(0, len(_stat_list)):
        # print the value at each index
        print(_stat_list[_count])
