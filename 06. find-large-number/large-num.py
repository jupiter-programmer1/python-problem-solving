numbers = [10, 45, 2, 99, 67, 150, 23]

# Method 1: Using max()
largest_max = max(numbers)
print("Using max():", largest_max)

# Method 2: Using loop
largest_loop = numbers[0]
for num in numbers:
    if num > largest_loop:
        largest_loop = num
print("Using loop:", largest_loop)

# Method 3: Using sort()
sorted_nums = sorted(numbers)
largest_sort = sorted_nums[-1]
print("Using sort():", largest_sort)
