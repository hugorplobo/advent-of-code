input_file = open("input.txt", "r")
presents = file_input.read().splitlines()
res = 0

for present in presents:
    l, w, h = present.split("x")
    l, w, h = int(l), int(w), int(h)
    side1 = l*w
    side2 = l*h
    side3 = w*h
    minor = min(side1, side2, side3)
    res += 2*l*w + 2*w*h + 2*h*l + minor

input_file.close()
print(res)
