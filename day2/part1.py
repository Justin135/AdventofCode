import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "data.txt"
abs_file_path = os.path.join(script_dir, rel_path)
with open(abs_file_path) as f:
    lines = f.readlines()


num1 = []
num2 = []
specialChars = []
passwords = []
count = 0
value = 0
tempString = '\0'
tempString2 = '\0'

for i in range(len(lines)):
  tempString = lines[i].split('-')
  num1.append(tempString[0])
  tempString2 = tempString[1].split()
  num2.append(tempString2[0])

  tempString = tempString2[1].split(':')
  specialChars.append(tempString[0])

  tempString = lines[i].split(": ")
  passwords.append(tempString[1])
  if passwords[i].count(specialChars[i]) >= int(num1[i]) and passwords[i].count(specialChars[i]) <= int(num2[i]):
    value += 1
print(value)