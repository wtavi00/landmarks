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
  
