file1 = open('data.txt', 'r')
calories = file1.readlines()

maximum = 0

currentTotal = 0

for calorie in calories:

    if calorie.strip() == '':
        maximum = currentTotal if currentTotal > maximum else maximum
        currentTotal = 0
    else:
        currentTotal += int(calorie.strip())

print(maximum)

