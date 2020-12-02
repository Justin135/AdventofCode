with open('data.txt') as f: lines = (f.readlines())
nums = set()
for i in range(len(lines)): nums.add(int(lines[i]))
for i in nums:
    if (2020 - i) in nums:
        print(i * (2020 - i))
        break