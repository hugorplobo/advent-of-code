import re

input_file = open("input.txt", "r")
lines = input_file.read().splitlines()


rgx1 = "[aeiou].*[aeiou].*[aeiou]"
rgx2 = "(.)\\1{1}"
rgx3 = "ab|cd|pq|xy"

res = 0

for line in lines:
    match1 = re.search(rgx1, line)
    match2 = re.search(rgx2, line)
    match3 = re.search(rgx3, line)

    if (match1 != None and match2 != None and match3 == None):
        res += 1

print(res)
