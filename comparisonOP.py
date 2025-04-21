'''# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the two numbers
if num1 == num2:
    print("✅ The numbers are equal.")
else:
    print("❌ The numbers are not equal.")'''


"""# Ask the user to enter a number
number = float(input("Enter a number: "))

# Check if the number is less than 0
if number < 0:
    print("❗ The number is negative.")
else:
    print("✅ The number is not negative.")"""

# Ask for the user's age
age = int(input("Enter your age: "))

# Determine age category
if age < 18:
    print("🧒 You are a minor.")
elif age <= 60:
    print("🧑 You are an adult.")
else:
    print("👴 You are a senior.")
