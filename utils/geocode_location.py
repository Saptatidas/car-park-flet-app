from geopy.geocoders import Nominatim

def get_coordinates_from_place(location_name, city="Kolkata", country="India"):
    geolocator = Nominatim(user_agent="kolkata_parking_locator")

    # List of districts to consider in the query
    districts = ["Kolkata", "North 24 Parganas", "South 24 Parganas"]
    
    # Build the full query dynamically
    full_location = location_name
    if city and city not in districts:  # Check if city is not already part of districts
        full_location += f", {city}"
    if country:
        full_location += f", {country}"

    try:
        location = geolocator.geocode(full_location, exactly_one=True, timeout=10)
        if location:
            return (location.latitude, location.longitude)
        else:
            print(f"No coordinates found for: {full_location}")
            
            # Try searching in each district if the first query fails
            for district in districts:
                if district not in full_location:  # Avoid searching the same district twice
                    district_location = f"{location_name}, {district}, {country}"
                    print(f"Trying district search: {district_location}")
                    location = geolocator.geocode(district_location, exactly_one=True, timeout=10)
                    if location:
                        return (location.latitude, location.longitude)
            
            return None
    except Exception as e:
        print(f"Geocoding error for '{full_location}': {e}")
        return None
