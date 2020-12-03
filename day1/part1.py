import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "data.txt"
abs_file_path = os.path.join(script_dir, rel_path)
with open(abs_file_path) as f:
    lines = f.readlines()

nums = set()
for i in range(len(lines)): nums.add(int(lines[i]))
for i in nums:
    if (2020 - i) in nums:
        print(i * (2020 - i))
        break