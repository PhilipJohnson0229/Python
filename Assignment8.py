#!/usr/bin/env python3
# Philip Johnson
#10/30/2021
# read number pairs and divide them

import csv

CSV = "numberpairs.csv"

myList = []
#reads the csv file and creates a list of number pairs based on data in the file
def readfile(list):

    with open(CSV) as fileToOpen:
        csvReader = csv.reader(fileToOpen)
        for row in csvReader:
            myList.append(row)
    return myList



    
# divides two numbers and returns result
# raises ZeroDivisionError exception if denominator is 0
def divideNums(value1, value2):
    if (value2 == 0):
        raise ZeroDivisionError("denominator is zero!")

    return value1 / value2

def calculateDataFromList(pairList):
    for numRows in pairList:
        numX = float(numRows[0])
        numY = float(numRows[1])
        try:
            print(numX, "divided by", numY, "is", str(divideNums(numX, numY)))
        except ZeroDivisionError as divieByZero:
            print(numX, "divided by", numY, "error: " + str(divieByZero))


def main():
    # read pairs of numbers
    listOfNumPairs = readfile(myList)

    calculateDataFromList(listOfNumPairs)

main()
