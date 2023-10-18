import re

def dms2dd(degrees, minutes, seconds):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    return dd

with open('07.Project Angles Input.txt', 'r') as f:
    lines = f.readlines()

output = []
for line in lines:
    parts = re.split('[°\'"]', line)
    dd = dms2dd(parts[0], parts[1], parts[2])
    output.append(dd)

with open('07.Project Angles Output.txt', 'w') as f:
    for item in output:
        f.write("%s\n" % item)
