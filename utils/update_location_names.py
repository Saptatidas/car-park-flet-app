import sqlite3
from reverse_geocode import get_place_name_from_coordinates

ORS_API_KEY = "5b3ce3597851110001cf62485c7aca9aadb24e8c8a33178cce00f631"  # 🔁 Replace with your OpenRouteService API key

# Coordinates for parking locations A–J
parking_locations = {
    "A": (22.5734, 88.4337),
    "B": (22.5761, 88.4292),
    "C": (22.5799, 88.4345),
    "D": (22.5701, 88.4352),
    "E": (22.5670, 88.4320),
    "F": (22.5745, 88.4305),
    "G": (22.5755, 88.4370),
    "H": (22.5712, 88.4400),
    "I": (22.5780, 88.4385),
    "J": (22.5699, 88.4275),
}

# Connect to SQLite DB
conn = sqlite3.connect("database/parking.db")
cursor = conn.cursor()

for code, (lat, lon) in parking_locations.items():
    place_name = get_place_name_from_coordinates(lat, lon, ORS_API_KEY)
    print(f"{code}: {place_name}")
    
    # Update name in database where name = 'A', 'B', etc.
    cursor.execute("UPDATE parking_locations SET name = ? WHERE name = ?", (place_name, code))

conn.commit()
conn.close()
