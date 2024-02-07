fin = open("random-file", "rb")

while True:
    b = fin.read(4)
    if (not b):
        break
    n = int.from_bytes(b, "big")
    print(n)