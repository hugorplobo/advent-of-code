import hashlib

input_file = open("input.txt", "r")
n = 0
key = input_file.read()

while True:
    hash = hashlib.md5((key + str(n)).encode())
    if hash.hexdigest().startswith("000000"):
        break
    n += 1

print(n)
