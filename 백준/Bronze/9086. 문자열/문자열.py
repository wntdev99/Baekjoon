import sys
sys.stdin.readline()
for readline in sys.stdin.readlines():
    tmpString = readline.strip()
    print(tmpString[0] + tmpString[-1])