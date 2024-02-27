SUBTRACT_MINUTE = 45
inputHour, inputMinute = map(int,input().split())
if inputMinute - SUBTRACT_MINUTE >= 0: print(f"{inputHour} {inputMinute - 45}")
else:
    if inputHour - 1 >= 0: print(f"{inputHour - 1} {60 + inputMinute - 45}")
    elif inputHour - 1 < 0: print(f"23 {60 + inputMinute - 45}")