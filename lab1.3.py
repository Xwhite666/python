n = 5

for i in range(1, n + 1):
    line = ""
    num = 5
    for j in range(i):
        line = f"{num} " + line
        num -= 1
    print(line.strip())