text = 'hello'

# slicing
print('slicing:', text[::-1])
# Output: slicing: olleh

# using function
reversed_text = "".join(reversed(text))
print('using func:', reversed_text)
# Output: using func: olleh

# using loop
reversed = ""
for char in text:
    reversed = char + reversed
print('using loop:', reversed)
# Output: using loop: olleh
