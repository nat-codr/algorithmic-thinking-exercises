
def multiplyLargestTwoNumbers(number1, number2, number3):
    if number3 > number2:
        largest = number3
        secondlargest = number2
    else:
        largest = number2
        secondlargest = number3

    if number1 > largest:
        secondlargest = largest
        largest = number1

    elif number1 > secondlargest:
        secondlargest = number1

    return largest * secondlargest;