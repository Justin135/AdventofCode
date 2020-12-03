import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "data.txt"
abs_file_path = os.path.join(script_dir, rel_path)
with open(abs_file_path) as f:
    lines = f.readlines()

index = 0
index2 = 0
index3 = 0
index4 = 0
index5 = 0
numTrees = 0
numTrees2 = 0
numTrees3 = 0
numTrees4 = 0
numTrees5 = 0

for i in range(1, len(lines)):
    index += 1
    index2 += 3
    index3 += 5
    index4 += 7
    if i % 2 == 0:
        index5 += 1
    
    if index >= 31:
        index -= 31
    if index2 >= 31:
        index2 -= 31
    if index3 >= 31:
        index3 -= 31
    if index4 >= 31:
        index4 -= 31
    if index5 >= 31:
        index5 -= 31

    if lines[i][index] == '#':
        numTrees += 1
    if lines[i][index2] == '#':
        numTrees2 += 1
    if lines[i][index3] == '#':
        numTrees3 += 1
    if lines[i][index4] == '#':
        numTrees4 += 1
    if lines[i][index5] == '#' and i % 2 == 0:
        numTrees5 += 1

print({numTrees}, {numTrees2}, {numTrees3}, {numTrees4}, {numTrees5})
print(numTrees * numTrees2 * numTrees3 * numTrees4 * numTrees5)