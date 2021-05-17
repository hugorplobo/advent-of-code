input_file = open("input.txt", "r")
presents = input_file.read().splitlines()
res = 0

for present in presents:
    l, w, h = present.split("x")
    l, w, h = int(l), int(w), int(h)
    perimeter1 = l*2 + h*2
    perimeter2 = l*2 + w*2
    perimeter3 = w*2 + h*2
    minor = min(perimeter1, perimeter2, perimeter3)
    bow = l*w*h
    res += minor + bow

input_file.close()
print(res)
