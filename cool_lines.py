"""
Codes here aren't functions/program, but lines/hack that could be used in project
I wrote it here, so I can find it later
"""

# switching between 0 and 1
n = 0
while True:
  n ^= 1        # the ^ operation is the XOR operation
  # n = 0 | 0 ^ 1 = 1
  # n = 1 | 1 ^ 1 = 0
  print(n)
# Output[1]: 1
# Output[2]: 0
# Output[3]: 1
# Output[4]: 0
# Output[5]: 1
# ...

####################################################################################################

# ouput in same line
print("Hello World!")
print("Goodbye World!")
# Output: Hello World!
# ...     Goodbye World!

print("Hello World!", end="\r")   # adding "end='\r' place the cursor at the beginnig of the line
print("Goodbye World!")
# Output: Goodbye World!

# WARNING
# if the first ouput is longer than the next one, it will be seen
print("Hello World!", end="\r")
print("Bye Earth!")
# Output: Bye Earth!d!

####################################################################################################
