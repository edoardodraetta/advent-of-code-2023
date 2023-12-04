import re

# with open("./1/input.txt") as input:
#     lines = input.readlines()

# # Part 1
# sum = 0 
# for line in lines:
#     # print(line)
#     digits = re.findall("\d", line)
#     # print(digits, digits[0], digits[-1]) 
#     sum += int(str(digits[0]) + str(digits[-1]))
#     # print()

# print(sum)

# Part 2

# Open the file
with open("./1/input.txt") as input:
    lines = input.readlines()

# Define a regex pattern to match
pattern = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"

# Dictionary to decode strings
word_to_number = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

sum = 0
# Loop through lines in the file
for line in lines:
    digits = re.findall(pattern, line)
    print(line)
    a = None
    
    try:
        a = int(digits[0])
    except ValueError:
        if digits[0] in word_to_number:
            a = word_to_number[digits[0]]
            print(digits[0], a)


    b = None
    try:
        b = int(digits[-1])
    except ValueError:
        if digits[-1] in word_to_number:
            b = word_to_number[digits[-1]]
            print(digits[-1], b)

    sum += int(str(a) + str(b))
    print(sum, a, b, int(str(a) + str(b)))
    print()

    
print(sum)