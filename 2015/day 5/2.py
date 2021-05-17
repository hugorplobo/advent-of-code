import re

input_file = open("input.txt", "r")
lines = input_file.read().splitlines()


rgx1 = "([a-z][a-z]).*\\1"
rgx2 = "([a-z])[a-z]\\1"

res = 0

for line in lines:
    match1 = re.search(rgx1, line)
    match2 = re.search(rgx2, line)

    if (match1 != None and match2 != None):
        res += 1

print(res)
