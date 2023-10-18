import re

def dms2dd(degrees, minutes, seconds):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    return dd

with open("07.Project Angles Input.txt", 'r') as f:
    with open('07.Project Angles Output.txt', 'w') as out:
        for line in f:
            parts = re.split('[°\'"]+', line)
            lat = dms2dd(parts[0], parts[1], parts[2])
            out.write(str(lat) + '\n')

            
