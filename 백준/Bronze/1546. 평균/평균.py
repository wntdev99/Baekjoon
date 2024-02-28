N = int(input())
Ns = list(map(int, input().split()))
M = max(Ns)
print(sum(Ns) / M / N * 100)