#!/usr/bin/env python3

# Assignment3.py
# P. Brauda
# 09/17/2020
# display and update lists of student info


# use single quotes around each list element
# creating our lists
studentNames = ['Jacqueline', 'Blake', 'Denise', 'Aaron', 'Timothy', 'Jessica', 'Cheryl', 'Geoffrey']
attendanceStatus = ['unk', 'unk', 'a', 'unk', 'p', 'p', 'unk', 'unk']
club = ['Future Leaders of America', 'Spanish', 'Chess', 'Glee', 'unk', 'Band', 'unk', 'Stars']

# flags
found = False

# ------------begin customer interaction here---------------
# format the string to fit the style of string in the list
studentsName = str(input("Please enter a student's name: ")).lower()
studentsName = str.title(studentsName)

# check if the entered name matches any item in the list
if studentsName not in studentNames:
    print("Sorry, {} is not in this class.".format(studentsName))
else:
    tempIndex = studentNames.index(studentsName)

# start looping through list of names
for targetStudent in studentNames:
    # if their is a match between the list item and the user input
    if studentsName in studentNames:
        # has this lettuce family been recalled?
        targetAttendanceIndex = tempIndex
        print("{}'s attendance status is {}\n".format(studentsName, attendanceStatus[targetAttendanceIndex]))
        # if the the students attendance status is unknown then we ask for an update by the user
        if attendanceStatus[targetAttendanceIndex] == 'unk':
            newAttendanceStatus = input("Please enter 'a' for absent or 'p' for present: ").lower()
            attendanceStatus[targetAttendanceIndex] = newAttendanceStatus
            alteredAttendanceIndex = attendanceStatus.index(attendanceStatus[targetAttendanceIndex])
            print("Thank you, the new attendance code is saved as: {}\n".format(
                attendanceStatus[alteredAttendanceIndex]))

        print("{}'s club membership is {}".format(studentsName, club[tempIndex]))
        # we treat the club list the same if the item is unk
        if club[tempIndex] == 'unk':
            newClubList = []
            newClubList = club
            newClubList.remove('unk')
            print("Valid club names are: \n")
            for item in newClubList:
                print(newClubList[newClubList.index(item)])

            print("\n")
            newClubStatus = input("Please enter a club name for this student: ").lower()
            newClubStatus = str.title(newClubStatus)
            club[tempIndex] = newClubStatus
            # alteredClubIndex = club.index(targetClubIndex)
            print("Thank you, {}'s new club membership is saved as: {}".format(studentsName
                                                                               ,club[club.index(newClubStatus)]))
            break









