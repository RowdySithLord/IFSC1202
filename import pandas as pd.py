import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('09.Project Distances.csv')

# Prompt for From City and To City
from_city = input("Enter From City: ")
to_city = input("Enter To City: ")

# Search the table for the distance between the cities
distance = df.loc[(df['From City'] == from_city) & (df['To City'] == to_city), 'Distance'].iloc[0]

# Print the distance between the cities
print(f"The distance between {from_city} and {to_city} is {distance} miles.")
