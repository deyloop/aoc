# INPUT_FILE = "./input-test.input"
INPUT_FILE = "./input.input"


with open(INPUT_FILE) as f:
    banks = f.readlines()


output_joltage = 0
for bank in banks:
    bank = bank.strip()

    max_jolt = 0
    for i, bat_i in enumerate(bank):
        if i == len(bank) - 1: continue
        for _, bat_j in enumerate(bank[i+1:]):
            jolts = int(bat_i) * 10 + int(bat_j) 
            if jolts > max_jolt:
                max_jolt = jolts


    output_joltage += max_jolt

print(output_joltage)
