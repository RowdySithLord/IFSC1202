import csv

with open('Exam Two Properties.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    properties = [list(map(str, row)) for row in reader]

for i in range(len(properties)):
    properties[i][4] = float(properties[i][4])


zipcodes = []


for property in properties:
    
    found = False
    for zipcode in zipcodes:
        
        if property[3] == zipcode[0]:
            
            zipcode[1] += 1
            
            zipcode[2] += property[4]
            found = True
            break
    if not found:
        zipcodes.append([property[3], 1, property[4]])

print("Zipcode\tCount of Properties\tAverage Property Price")

for zipcode in zipcodes:
    print(f"{zipcode[0]}\t{zipcode[1]}\t\t\t{zipcode[2]/zipcode[1]:.2f}")
