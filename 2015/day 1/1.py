input_file = open("input.txt", "r")
text = input_file.read()
floor = 0

for char in text:
    if char == "(":
        floor += 1
    else:
        floor -= 1

input_file.close()
print(floor)
