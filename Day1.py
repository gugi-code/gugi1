# opening the list of elves and adding data to a list (split by lines)
with open('d1.txt') as file:
    data = [i for i in file.read().split("\n")]

high_cal = 0 # highest elf cal count
high_cal_2 = 0 # 2nd highest elf cal count
high_cal_3 = 0 # 3rd highest elf cal count
sum_cal = 0 # sum of the elf cal counts
current_cal = 0 # current iteration count

# loop to go through the list
for i in data:
    if i == '':
        current_cal = 0 # resetting current cal if blank
    else:
        num = int(i)
        current_cal += num # sum of current elves cal count
        # loops to update high counts if higher than previous high counts & updates 2nd/third highest
        if high_cal_3 < current_cal:
            if high_cal_2 < high_cal_3:
                if high_cal < high_cal_2:
                    high_cal = current_cal
                else:
                    high_cal_2 = current_cal
            else:
                high_cal_3 = current_cal


sum_cal = (high_cal + high_cal_2 + high_cal_3)
print("Part 1 answer: " + str(high_cal))
print("Part 2 answer: " + str(sum_cal))
