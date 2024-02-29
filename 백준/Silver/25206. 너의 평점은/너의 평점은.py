import sys

GRADEDICTIONARY = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

totalRate = 0.0
totalGrade = 0.0

readLines = sys.stdin.readlines()
for readline in readLines:
    className, classRate, classGrade = readline.split()
    if classGrade == 'P': continue
    totalRate += float(classRate)
    totalGrade += GRADEDICTIONARY[classGrade] * float(classRate)
print(totalGrade/totalRate)