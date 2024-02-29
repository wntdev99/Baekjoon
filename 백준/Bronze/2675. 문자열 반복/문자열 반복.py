import sys

for readline in sys.stdin.readlines()[1:]:
    R, S = readline.split()
    P = ''.join([char * int(R) for char in S])
    print(P)