import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "data.txt"
abs_file_path = os.path.join(script_dir, rel_path)
with open(abs_file_path) as f:
    lines = f.readlines()

rows = [0] * len(lines)
columns = [0] * len(lines)
ids = [0] * len(lines)
low = 0
high = 127

for i in range(len(lines)):
    low = 0
    high = 127
    for j in range(7):
        diff = high - low + 1
        if lines[i][j] == 'F':
            high -= (diff / 2)
        elif lines[i][j] == 'B':
            low += (diff / 2)
    rows[i] = low

    low = 0
    high = 7
    for j in range(7, 10):
        diff = high - low + 1
        if lines[i][j] == 'L':
            high -= (diff / 2)
        elif lines[i][j] == 'R':
            low += (diff / 2)
    columns[i] = low
    ids[i] = (rows[i] * 8) + columns[i]

print(max(ids))