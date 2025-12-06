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

    # grug mode
    while(clicks > 0):
        clicks -= 1

        cur = cur + 1 if direction == "R" else cur - 1

        if cur == -1: cur = 99
        if cur == 100 :
            cur = 0

        if cur == 0:
            counts_zero += 1

    print(f"d:{direction}, c:{clicks} -> cur:{cur}, z:{counts_zero}")

print(f"counts_zero: {counts_zero}")
