
line_length = 20

line = ""

for i in range(1, line_length + 1):
    if i % 3 == 0:
        line += "<<"
    else:
        line += "*"

print(line)
