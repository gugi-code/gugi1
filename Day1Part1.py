# opening the list of elves and adding data to a list (split by lines)
with open('d1.txt') as file:
    data = [i for i in file.read().split("\n")]

# the current calorie count for the iteration + the high count (most calories)
high_cal = 0
current_cal = 0

# loop to go through the list
for i in data:
    if i == '':
        # resetting current cal if blank
        current_cal = 0
    else:
        num = int(i)
        # sum of current elves cal count
        current_cal += num
        # loop to update high count if higher than previous high count
        if high_cal < current_cal:
            high_cal = current_cal

print(high_cal)
