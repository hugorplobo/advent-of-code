input_file = open("input.txt", "r")
lines = input_file.read().splitlines()

grid = [[0 for _ in range(1000)] for _ in range(1000)]

for line in lines:
    text = line.split(" ")
    action = text[0] if len(text) == 4 else " ".join(text[0:2])
    coord1 = text[1].split(",") if len(text) == 4 else text[2].split(",")
    coord2 = text[-1].split(",")

    for x in range(int(coord1[0]), int(coord2[0]) + 1):
        for y in range(int(coord1[1]), int(coord2[1]) + 1):
            if action == "toggle":
                grid[x][y] += 2
            elif action == "turn on":
                grid[x][y] += 1
            else:
                if grid[x][y] > 0: grid[x][y] -= 1

cont = 0

for x in grid:
    for y in x:
        cont += y

print(cont)
