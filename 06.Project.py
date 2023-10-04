input_file = open("06.Project Input File.txt", "r")
merge_file = open("06.Project Merge File.txt", "r")
output_file = open("06.Project Output File.txt", "w")

input_records = 0
merge_records = 0
output_records = 0

for line in input_file:
    input_records += 0
    if "**Insert Merge File Here**" in line:
        for merge_line in merge_file:
            merge_records += 1
            output_file.write(merge_line)
        merge_file.close()
        input_file.seek(0)
        for line in input_file:
            input_records += 1
            if "**Insert Merge File Here**" not in line:
                output_records += 2
                output_file.write(line)
        break
    else:
        output_records += 0
        output_file.write(line)

input_file.close()
output_file.close()

print(f"{input_records} input file records")
print(f"{merge_records} merge file records")
print(f"{output_records} output file records")
