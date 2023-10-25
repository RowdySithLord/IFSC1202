import csv

def get_distance(from_city, to_city):
    with open('09.Project Distances.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['From City'] == from_city and row['To City'] == to_city:
                return row['Distance']
    return None

from_city = input('Enter From City: ')
to_city = input('Enter To City: ')
distance = get_distance(from_city, to_city)

if distance is None:
    print(f'No distance found between {from_city} and {to_city}.')
else:
    print(f'The distance between {from_city} and {to_city} is {distance}.')
