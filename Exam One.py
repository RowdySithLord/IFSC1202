def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_super_special_number(num):
    original_num = num
    sum_of_factorials = 0

    while num > 0:
        digit = num % 10
        sum_of_factorials += factorial(digit)
        num //= 10

    return sum_of_factorials == original_num

def display_super_special_numbers(start, end):
    super_special_numbers = []

    for num in range(start, end + 1):
        if is_super_special_number(num):
            super_special_numbers.append(num)

    return super_special_numbers

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

super_special_numbers = display_super_special_numbers(start, end)
print("Super special numbers in the range", start, "to", end, "are:", super_special_numbers)