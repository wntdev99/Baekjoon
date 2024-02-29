for _ in range(int(input())):
    outputString = ''
    repeatNum, repeatString = input().split()
    for tmpString in repeatString:
        outputString += tmpString * int(repeatNum)
    print(outputString)