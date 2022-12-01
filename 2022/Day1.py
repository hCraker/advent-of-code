# Part 1
file = open('input.txt')
max = 0
total = 0
for line in file:
    if line == '\n':
        total = 0
    else:
        total += int(line)

    if total > max:
        max = total

print(max)
file.close()

# Part 2
file = open('input.txt')
max1 = 0
max2 = 0
max3 = 0
total = 0
for line in file:
    if line == '\n':
        total = 0
    else:
        total += int(line)

    if total > max1:
        max3 = max2
        max2 = max1
        max1 = total
    elif total > max2:
        max3 = max2
        max2 = total
    elif total > max3:
        max3 = total


print(max1+max2+max3)