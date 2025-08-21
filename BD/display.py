import csv

def load_destinations_from_csv(csv_path):
    destinations = {}
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            region = row["Division/Region"]
            place_name = row["Place Name"]
            latitude = float(row["Latitude"])
            longitude = float(row["Longitude"])
            
            if region not in destinations:
                destinations[region] = {}
            destinations[region][place_name] = (latitude, longitude)
    return destinations
#---------------
# Example usage:
#---------------
csv_file_path = "landmarks.csv"  # change path if needed
destination_bd = load_destinations_from_csv(csv_file_path)

# Now you can access it the same way as the old dictionary:
for division, places in destination_bd.items():
    print(f"{division}:")
    for place, coords in places.items():
        print(f"  - {place}: {coords}")


