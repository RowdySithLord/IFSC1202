import re

def dms2dd(degrees, minutes, seconds):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    return dd

with open('07.Project Angles Input.txt', 'r') as file:
    lines = file.readlines(6)

output = []
for line in lines:
    parts = re.split('[°\'"]+', line)
    dd = dms2dd(parts[0], parts[1], parts[2])
    output.append(dd)

with open('07.Project Angles Output.txt', 'w') as file:
    for item in output:
        file.write("%s\n" % item)

