import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "data.txt"
abs_file_path = os.path.join(script_dir, rel_path)
with open(abs_file_path) as f:
    lines = f.readlines()

index = 0
numTrees = 0

for i in range(1, len(lines)):
    index += 3
    
    if index >= 31:
        index -= 31

    if lines[i][index] == '#':
        numTrees += 1

print(numTrees)