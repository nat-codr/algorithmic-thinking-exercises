from random import randint
countPos = 0
countZero = 0
countNegative = 0

minimum = -100
maximum = 100

for n in range(1000):
    chosen_number = randint(minimum, maximum)
    if chosen_number > 0:
        countPos = countPos + 1
    if chosen_number < 0:
        countNegative = countNegative + 1
    if chosen_number == 0:
        countZero = countZero + 1

print("# of positive numbers " + str(countPos))
print("# of zeros " + str(countZero))
print("# of negative numbers " + str(countNegative))




