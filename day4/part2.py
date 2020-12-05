import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "data.txt"
abs_file_path = os.path.join(script_dir, rel_path)
with open(abs_file_path) as f:
    lines = f.readlines()

data = []
temp = []
goodPassports = []
numPassports = 0

for i in range(len(lines)):
    if lines[i] == '\n':
        data.append(temp)
        temp = []
    else:
        temp += lines[i].split()

data.append(temp)

for i in range(len(data)):
    tempString = ''.join(map(str, data[i]))
    if tempString.find('byr') != -1 \
    and tempString.find('iyr') != -1 \
    and tempString.find('eyr') != -1 \
    and tempString.find('hgt') != -1 \
    and tempString.find('hcl') != -1 \
    and tempString.find('ecl') != -1 \
    and tempString.find('pid') != -1 :
        goodPassports.append(data[i])

print(len(data))
print(len(goodPassports))

for i in range(len(goodPassports)):
    tempValid = True
    for j in range(len(goodPassports[i])):
        info = goodPassports[i][j].split(':')
        
        if info[0] == "byr":
            num = int(info[1])
            if not(num >= 1920 and num <= 2002):
                tempValid = False
                break
        elif info[0] == "iyr":
            num = int(info[1])
            if not(num >= 2010 and num <= 2020):
                tempValid = False
                break
        elif info[0] == "eyr":
            num = int(info[1])
            if not(num >= 2020 and num <= 2030):
                tempValid = False
                break
        elif info[0] == "hgt":
            if "cm" in info[1]:
                num = int(info[1].replace("cm", ""))
                if not(num >= 150 and num <= 193):
                    tempValid = False
                    break
            elif "in" in info[1]:
                num = int(info[1].replace("in", ""))
                if not(num >= 59 and num <= 76):
                    tempValid = False
                    break
            else:
                tempValid = False
                break
        elif info[0] == "hcl":
            if info[1][0] != '#':
                tempValid = False
                break
            if len(info[1]) != 7:
                tempValid = False
                break

            for k in info[1]:
                if not(k == '#' or k == '1' or k == '2' or k == '3' or k == '4' or k == '5' or k == '6' or k == '7' or k == '8' or k == '9' or k == '0' or k == 'a' or k == 'b' or k == 'c' or k == 'd' or k == 'e' or k == 'f'):
                    tempValid == False
                    break
            if not(tempValid):
                break
        elif info[0] == "ecl":
            if not(info[1] == "amb" or info[1] == "blu" or info[1] == "brn" or info[1] == "gry" or info[1] == "grn" or info[1] == "hzl" or info[1] == "oth"):
                tempValid == False
                break
        elif info[0] == "pid":
            if len(info[1]) != 9:
                tempValid == False
                break
        
            
    

    if tempValid:
        numPassports += 1

print(numPassports)