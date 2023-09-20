def is_special_number(n):
    # Calculate the number of digits
    number_digits = 0
    temp = n
    while temp > 0:
        temp //= 10
        number_digits += 1

    # Calculate the sum of digits raised to the power of the number of digits
    temp = n
    sum_of_digits = 0
    while temp > 0:
        digit = temp % 10
        sum_of_digits += digit ** number_digits
        temp //= 10

    # Check if the calculated value is equal to the original number
    return sum_of_digits == n

def display_special_numbers(start, end):
    special_numbers = []

    for num in range(start, end + 1):
        if is_special_number(num):
            special_numbers.append(num)
   
    return special_numbers

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

special_numbers = display_special_numbers(start, end)
print("Special numbers between", start, "and", end, "are:", special_numbers)
