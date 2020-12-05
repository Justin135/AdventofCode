import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "data.txt"
abs_file_path = os.path.join(script_dir, rel_path)
with open(abs_file_path) as f:
    lines = f.readlines()

data = []
temp = ""
numPassports = 0

for i in range(len(lines)):
    if lines[i] == '\n':
        data.append(temp)
        temp = ""
    else:
        temp += lines[i]

data.append(temp)

for i in range(len(data)):
    tempString = ''.join(map(str, data[i]))
    if data[i].find('byr') != -1 \
    and data[i].find('iyr') != -1 \
    and data[i].find('eyr') != -1 \
    and data[i].find('hgt') != -1 \
    and data[i].find('hcl') != -1 \
    and data[i].find('ecl') != -1 \
    and data[i].find('pid') != -1 :
        numPassports += 1

print("{} {}".format(len(data), numPassports))