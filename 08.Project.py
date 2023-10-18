import requests

response = requests.get("https://www.usconstitution.net/const.txt")
constitution = response.text

constitution_lines = constitution.split("\n")

search_term = input("Enter a search term: ")

while search_term != "":
    found = False
    for i, line in enumerate(constitution_lines):
        
        if search_term.lower() in line.lower():
            found = True
            
            j = i - 1
            while j >= 0 and constitution_lines[j].strip() != "":
                j -= 1

            k = i + 1
            while k < len(constitution_lines) and constitution_lines[k].strip() != "":
                k += 1

            print(f"Section {j+2} to {k}:\n")
            for l in range(j+1, k):
                print(f"{l+1:>3} {constitution_lines[l]}")
            print("\n")

            i = k

    if not found:
        print(f"No results found for '{search_term}'\n")

    search_term = input("Enter a search term: ")

