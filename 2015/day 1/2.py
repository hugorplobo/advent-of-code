input_file = open("input.txt", "r")
text = input_file.read()
floor = 0
position = 0

for i, char in enumerate(text):
    if char == "(":
        floor += 1
    else:
        floor -= 1

    if floor == -1:
        position = i + 1
        break

input_file.close()
print(position)
