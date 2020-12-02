with open('input.txt') as f: lines = (f.readlines())
nums = set()
for i in range(len(lines)): nums.add(int(lines[i]))
for i in nums:
  for j in nums:
    if (2020 - i - j) in nums:
      print(i*j*(2020 - i - j))
      break