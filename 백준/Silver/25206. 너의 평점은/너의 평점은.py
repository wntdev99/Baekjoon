import sys

totalClass = 0.0
totalGrade = 0.0

readLines = sys.stdin.readlines()
for readLine in readLines:
    className, classRate, classGrade = readLine.split()
    if classGrade == 'P': 
        continue
    elif classGrade == 'F':
        totalClass += float(classRate)
    else:
        totalClass += float(classRate)
        totalGrade += (69.0 - ord(classGrade[0]) + (48.0 - ord(classGrade[1])) / 10.0) * float(classRate)
print(totalGrade / totalClass)