input_file = open("input.txt", "r")
text = input_file.read()
houses = {"0,0"}
santa_coord = [0, 0]
robot_coord = [0, 0]

def get_move(char, coord):
    if char == "^":
        coord[1] += 1
    elif char == ">":
        coord[0] += 1
    elif char == "v":
        coord[1] -= 1
    else:
        coord[0] -= 1

    houses.add("{},{}".format(coord[0], coord[1]))

for i, char in enumerate(text):
    if i % 2 == 0:
        get_move(char, santa_coord)
    else:
        get_move(char, robot_coord)

input_file.close()
print(len(houses))
