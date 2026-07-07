
#Snippet 1
x = 10
y = 0
if y != 0:
    result = x/y
    print("Result:", result)
else:
    print("Erros: cannot divide by zero")
#Snippet 2
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i])
#Snippet 3
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area
radius = 5
print(calculate_area(radius))
#Snippet 4
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(7))
#Snippet 5
for i in range(5):
    print(i)
#Snippet 6
def greet(name):
    return "Hello, " + name
print(greet("Alice"))
#Snippet 7
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print("Sum of numbers:", total)
#Snippet 8
def factorial(n):
    if n == 0:
      return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
#Snippet 9
name = input("Enter your name: ")
if name == "Alice" or "Bob":
    print("Hello, " + name)
else:
    print("Hello, stranger!")
#Snippet 10
def divide_numbers(x, y):
    if y == 0:
        return "Error: cannot divide by zero"
    result = x / y
    return result
num1 = 10
num2 = 0
print(divide_numbers(num1, num2))