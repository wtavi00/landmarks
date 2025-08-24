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
