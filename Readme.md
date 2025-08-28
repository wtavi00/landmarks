# 🗺️ Landmarks Boundary

This project loads U.S. (or any region’s) state/region polygon boundaries from a CSV file and allows you to determine which state a given latitude/longitude point belongs to using the ray-casting point-in-polygon algorithm.

## 📂 Project Structure
```bash
├── states.csv             
├── datasets.py
├── searching.py         
├── README.md
```

## 📊 CSV Format
states.csv

This file should contain polygon boundary points for each state/region.
Headers required:
```bash
state	lat	lon
AL	32.154106	-85.330811
AL	33.000000	-85.500000
NM	32.904956	-104.106445
...	...	...
```

Each row is a coordinate (latitude, longitude).
Rows belonging to the same state form the polygon boundary for that state.
The polygon should be closed (first and last points are the same) for accuracy.

## ⚙️ Installation

Clone the repo and install Python 3.8+.
```bash
git clone https://github.com/wtavi00/landmarks/tree/main
cd boundary-landmarks
```

No external dependencies are required (only Python standard library).

## 🚀 Usage

Run the script:
```bash
python datasets.py
```

Example code inside main.py:
```bash
print(search(32.154106, -85.330811, states))
print(search(32.904956, -104.106445, states))
print(search(33.406942, -111.906281, states))
print(search(44.018046, -92.467569, states))
print(search(40.2282, -89.1234, states))
```

Expected output:
```bash
Found in AL
Found in NM
Found in AZ
Found in MN
Found in IL
```

## 🧠 How It Works

The program loads polygon boundaries from states.csv.
Uses the ray-casting algorithm to determine if a point (lat, lon) lies inside a polygon.
Returns the state name if found, otherwise "Found None".

## 📌 Features
Works with any region’s polygon boundaries, not just U.S. states.
Easy to extend with landmark search (landmarks.csv).
Pure Python (no external dependencies).

