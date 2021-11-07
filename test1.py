# Philip Johnson
# Assignment 1
# COP2034C

# shebang statement
#!/usr/bin/env python3

# prompt for data on IT majors and non IT majors
_totalITMajors = int(input("Please enter the total number of IT majors in the course: "))
_totalNonITMajors = int(input("Please enter the total number of non-IT majors in the course: "))


# this function will take in the two integer values and calculate the percentage for both
def CalculatePercentage(_iTMajors, _nonITMajors):
    # adding the two integer values for the total of majors in the class
    _totalMajors = _iTMajors + _nonITMajors

    # calculating the percentage for both majors
    _calculatedPercentageIT = float(_iTMajors / _totalMajors) * 100
    _calculatedPercentageNonIT = float(_nonITMajors / _totalMajors) * 100

    # rounding our calculated percentages to 1 number past the decimal point
    _percentageIT = round(_calculatedPercentageIT,1)
    _percentageNonIT = round(_calculatedPercentageNonIT,1)

    # creating our output message by formatting our calculated values into readable strings
    _outputMessage = "The percentage of IT majors is {}%\n" \
                     "The percentage of non IT majors is {}%"\
        .format(_percentageIT, _percentageNonIT)

    print(_outputMessage)


# Calling the CalculatePercentage function and we pass in the two inputs as parameters
CalculatePercentage(_totalITMajors, _totalNonITMajors)

