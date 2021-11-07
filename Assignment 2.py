#!/usr/bin/env python3

# Assignment3.py
# P. Brauda
# 09/17/2020
# display and update lists of student info


# use single quotes around each list element
studentNames = ['Jacqueline', 'Blake', 'Denise', 'Aaron', 'Timothy', 'Jessica', 'Cheryl', 'Geoffrey']
attendanceStatus = ['unk', 'unk', 'a', 'unk', 'p', 'p', 'unk', 'unk']
club = ['Future Leaders of America', 'Spanish', 'Chess', 'Glee', 'unk', 'Band', 'unk', 'Stars']

# flags
found = False

# ------------begin customer interaction here---------------
studentsName = str(input("Please enter a student's name: ")).lower()
studentsName = str.title(studentsName)
tempIndex = studentNames.index(studentsName)

# look in the full inventory for the lettuce family
for targetStudent in studentNames:
    # is the customer's choice one of the families we sell?
    if studentsName in targetStudent:

        found = True
        # has this lettuce family been recalled?
        targetAttendanceIndex = tempIndex
        print("{}'s attendance status is {}\n".format(studentsName, attendanceStatus[targetAttendanceIndex]))
        if attendanceStatus[targetAttendanceIndex] == 'unk':
            newAttendanceStatus = input("Please enter 'a' for absent or 'p' for present: ").lower()
            attendanceStatus[targetAttendanceIndex] = newAttendanceStatus
            alteredAttendanceIndex = attendanceStatus.index(attendanceStatus[targetAttendanceIndex])
            print("Thank you, the new attendance code is saved as: {}\n".format(
                attendanceStatus[alteredAttendanceIndex]))

        print("{}'s club membership is {}".format(studentsName, club[tempIndex]))
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







