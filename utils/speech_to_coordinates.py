import openrouteservice

ORS_API_KEY = "5b3ce3597851110001cf62485c7aca9aadb24e8c8a33178cce00f631"  # Replace with your actual OpenRouteService API key

client = openrouteservice.Client(key=ORS_API_KEY)

def speech_to_coordinates(location_name):
    try:
        # Bound this to a rectangle around Kolkata to avoid wrong matches
        geocode = client.pelias_search(
            text=location_name,
            boundary_rect=[88.30, 22.45, 88.50, 22.65],  # Kolkata bounding box
            size=1
        )
        features = geocode.get('features', [])
        if features:
            coords = features[0]['geometry']['coordinates']  # [lon, lat]
            return coords[1], coords[0]  # Return as lat, lon
    except Exception as e:
        print(f"[Geocoding Error] {e}")
    return None, None
