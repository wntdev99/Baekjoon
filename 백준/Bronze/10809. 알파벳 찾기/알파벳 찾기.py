positions = [-1] * 26
S = input()

for i in range(len(S)):
    idx = ord(S[i]) - ord('a')
    if positions[idx] == -1:
        positions[idx] = i

for pos in positions:
    print(pos, end=' ')