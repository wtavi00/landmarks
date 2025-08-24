import csv
import states.csv

states = load_states_from_csv("states.csv")

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


def search(lat, lon, states):
    """Return which state a point belongs to."""
    for state, coords in states.items():
        if point_in_polygon(lat, lon, coords):
            return f"Found in {state}"
    return "Found None"



# --------- Example Usage ----------
def main():
    # Load landmarks
    landmarks = load_destinations_from_csv("states.csv")
    for division, places in landmarks.items():
        print(f"{division}:")
        for place, coords in places.items():
            print(f"  - {place}: {coords}")

    print("\n--- State Boundary Test ---")
    
    states = load_states_from_csv("states.csv")

    # Example coordinate tests
    print(search(32.154106, -85.330811, states))
    print(search(32.904956, -104.106445, states))
    print(search(33.406942, -111.906281, states))
    print(search(44.018046, -92.467569, states))
    print(search(40.2282, -89.1234, states))

    for state, coords in states.items():
        print(f"{state}: {len(coords)} boundary points")


if __name__ == "__main__":
    main()
