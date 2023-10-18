import requests

# Read the US Constitution from the internet
response = requests.get("https://www.usconstitution.net/const.txt")
constitution = response.text

# Split the string into a list of strings, each line being an item in the list
constitution_lines = constitution.split("\n")

# Prompt for a search term (exit the program when the search term is blank)
search_term = input("Enter a search term: ")

while search_term != "":
    found = False
    for i, line in enumerate(constitution_lines):
        # Search for the search term in each line. When the search term is found:
        if search_term.lower() in line.lower():
            found = True
            # Loop backwards from the current line to find the beginning of the section. Look for a blank line.
            j = i - 1
            while j >= 0 and constitution_lines[j].strip() != "":
                j -= 1

            # Loop forwards from the current lint to find the end of the section. Look for a blank line.
            k = i + 1
            while k < len(constitution_lines) and constitution_lines[k].strip() != "":
                k += 1

            # Print the section of text that contains the serach term along with the line number.
            print(f"Section {j+2} to {k}:\n")
            for l in range(j+1, k):
                print(f"{l+1:>3} {constitution_lines[l]}")
            print("\n")

            # Skip to the end of the section. Don't print the section twice if the search term is found twice.
            i = k

    if not found:
        print(f"No results found for '{search_term}'\n")

    # Prompt for another search term
    search_term = input("Enter a search term: ")

