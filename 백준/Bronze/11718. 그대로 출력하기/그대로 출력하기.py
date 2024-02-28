lines = []
for _ in range(100):
    try:
        line = input()
        if line:
            lines.append(line)
    except EOFError:
        break

for line in lines:
    print(line)
