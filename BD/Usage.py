# Example usage:
csv_file_path = "landmarks.csv"  # change path if needed
destination_bd = load_destinations_from_csv(csv_file_path)

# Now you can access it the same way as the old dictionary:
for division, places in destination_bd.items():
    print(f"{division}:")
    for place, coords in places.items():
        print(f"  - {place}: {coords}")

