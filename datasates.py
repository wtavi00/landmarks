import csv
from collections import defaultdict

def load_states_from_csv(csv_path):
    """Load state boundary coordinates from a CSV file into a dict."""
    states_data = defaultdict(list)
    with open(csv_path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            state = row["state"]
            lat = float(row["lat"])
            lon = float(row["lon"])
            states_data[state].append((lat, lon))
    return dict(states_data)


# Load boundaries from CSV (place states.csv in same folder as this script)
states = load_states_from_csv("landmarks.csv")

def findstate(lat, lon):
    state = "not found"

    for key, coords in states.items():
        polysides = len(coords)
        j = polysides - 1
        oddnodes = False

        for i in range(polysides):
            if (coords[i][1] < lon and coords[j][1] >= lon) or (coords[j][1] < lon and coords[i][1] >= lon):
                if (coords[i][0] + (lon - coords[i][1]) / (coords[j][1] - coords[i][1]) * (coords[j][0] - coords[i][0])) < lat:
                    oddnodes = not oddnodes
            j = i

        if oddnodes:
            state = key
            break

    return state

