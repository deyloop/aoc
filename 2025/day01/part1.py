# INPUT_FILE = "./part1-test.input"
INPUT_FILE = "./part1.input"

with open(INPUT_FILE) as f:
    lines = f.readlines()

cur = 50
counts_zero = 0
for line in lines:
    line = line.strip()

    direction = line[0]
    clicks = int(line[1:])

    cur = cur + clicks if direction == "R" else cur - clicks
    while cur < 0 or cur > 99:
        if cur < 0:
            cur = 100 + cur
        if cur > 99:
            cur = cur - 100

    if cur == 0:
        counts_zero += 1

    print(f"d:{direction}, c:{clicks} -> cur:{cur}")

print(f"counts_zero: {counts_zero}")
