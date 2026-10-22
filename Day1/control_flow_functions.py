
# Python Day 1 - Control Flow and Functions

# 1. Check even or odd
def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

print("1.", check_even_odd(10))

# 2. Find the largest of three numbers
def largest(a, b, c):
    return max(a, b, c)

print("2. Largest:", largest(10, 25, 15))

# 3. Check positive, negative or zero
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    return "Zero"

print("3.", check_number(-5))

# 4. Print numbers using a loop
print("4. Numbers:", end=" ")
for number in range(1, 6):
    print(number, end=" ")
print()

# 5. Sum of first N natural numbers
def sum_n(n):
    return sum(range(1, n + 1))

print("5. Sum:", sum_n(5))

# 6. Factorial using a loop
def factorial(n):
    result = 1
    for number in range(1, n + 1):
        result *= number
    return result

print("6. Factorial:", factorial(5))

# 7. Multiplication table
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

print("7. Multiplication table of 3:")
multiplication_table(3)

# 8. Check whether a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("8. Is 7 prime?", is_prime(7))
