INPUT_FILE = "./input-test.txt"
INPUT_FILE = "./input.txt"

import re

with open(INPUT_FILE) as f:
    lines = f.readlines()

ranges = lines[0].split(",")
ranges = [r.split("-") for r in ranges]
ranges = [(int(r[0]), int(r[1])) for r in ranges]

sum_all = 0
for start, end in ranges:
    print(f"{start}, {end}")
    for i in range(start, end+1):
        print(f">> {i}")
        number = str(i)
        m = re.search(r"^(\d+)\1+$", number)
        if m:
            sum_all += i
            print(f">>> matched")

print(sum_all)

