# 🗺️ landmarks Bd

This project loads some of Bangladesh landmarks in polygon boundaries from a CSV file and allows you to determine which state a given latitude/longitude point belongs to using the ray-casting point-in-polygon algorithm.

## 📂 Project Structure
```bash
├── destination.csv
├── Usage.py
├── display.py
├── README.md
├── Landmarks_dictionary.py (Optional)
```

## 📊 CSV Format
destination.csv

This file should contain polygon boundary points for each state/region.
Headers required:
```bash
Division	Landmark	    Lat     Lon
Dhaka       Lalbagh Fort	23.719	90.3881
Dhaka   	Star Mosque	    23.7162	90.3948
Dhaka 	    Curzon Hall	    23.7319	90.3938
...	...	...
```

Each row is a coordinate (latitude, longitude).
Rows belonging to the same state form the polygon boundary for that state.
The polygon should be closed (first and last points are the same) for accuracy.

## ⚙️ Installation

Clone the repo and install Python 3.8+.
```bash
git clone https://github.com/wtavi00/landmarks/tree/main/BD
cd landmarks-BD
```

No external dependencies are required (only Python standard library).

## 🚀 Usage

Run the script:
```bash
python display.py
```


## 🧠 How It Works

The program loads polygon boundaries from states.csv.
Uses the ray-casting algorithm to determine if a point lies inside a polygon.
Returns the state name if found, otherwise "Found None".

## 📌 Features
Works with any region’s polygon boundaries.
Easy to extend with landmark search (destination.csv).
Pure Python (no external dependencies).

