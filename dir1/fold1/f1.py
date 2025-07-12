# This is a comment. Comments are ignored by the Python interpreter.

# 1. Printing output to the console
print("Hello, World!")

# 2. Variables and data types
name = "Alice"  # String
age = 30        # Integer
height = 1.75   # Float
is_student = True # Boolean

print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")

# 3. Basic arithmetic operations
num1 = 10
num2 = 5

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 # Returns a float
floor_division = num1 // num2 # Returns an integer (discards fractional part)

print(f"Addition: {addition}, Subtraction: {subtraction}, Multiplication: {multiplication}")
print(f"Division: {division}, Floor Division: {floor_division}")

# 4. Conditional statements (if-elif-else)
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# 5. Loops (for loop)
print("Counting from 1 to 5:")
for i in range(1, 6): # range(start, end) generates numbers up to (end-1)
    print(i)

# 6. Functions
def greet(person_name):
    """This function takes a name and prints a greeting."""
    print(f"Greetings, {person_name}!")

greet("Bob")
