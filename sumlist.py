numbers=[1,"chandan", true]
print(sum(numbers))# Let's try modifying the second element (index 1)
my_tuple[1] = 99  # This will raise an error
TypeError: 'tuple' object does not support item assignment
sliced_tuple = my_tuple[1:3]  # Index 1 and 2 (3 is not included)
print("Sliced Tuple (2nd and 3rd elements):", sliced_tuple)
