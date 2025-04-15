# Swapping using a third variable
def swap_with_temp(a, b):
    print("Before swap (with temp): a =", a, " b =", b)
    temp = a
    a = b
    b = temp
    print("After swap (with temp): a =", a, " b =", b)
    return a, b

# Swapping without using a third variable (using Python's tuple unpacking)
def swap_without_temp(a, b):
    print("Before swap (without temp): a =", a, ", b =", b)
    a, b = b, a
    print("After swap (without temp): a =", a, ", b =", b)
    return a, b

# Example usage
x = 6
y = 11

# Swap with a third variable
x, y = swap_with_temp(x, y)

# Swap back without a third variable
x, y = swap_without_temp(x, y)
