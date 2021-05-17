input_file = open("input.txt", "r")
text = input_file.read()
houses = {"0,0"}
coord = [0, 0]

for char in text:
    if char == "^":
        coord[0] += 1
    elif char == ">":
        coord[1] += 1
    elif char == "v":
        coord[0] -= 1
    else:
        coord[1] -= 1

    houses.add("{},{}".format(coord[0], coord[1]))

input_file.close()
print(len(houses))

