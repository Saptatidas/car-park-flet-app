import math

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points on the Earth's surface
    using the Haversine formula. The distance is returned in kilometers.
    """
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert latitude and longitude from degrees to radians
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    
    # Difference in latitude and longitude
    d_phi = math.radians(lat2 - lat1)
    d_lambda = math.radians(lon2 - lon1)
    
    # Debugging: Print the intermediate values for verification
    #print(f"phi1: {phi1}, phi2: {phi2}, d_phi: {d_phi}, d_lambda: {d_lambda}")
    
    # Haversine formula
    a = math.sin(d_phi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Calculate distance in kilometers
    distance_km = R * c
    
    # Debugging: Print the calculated distance
    #print(f"Calculated distance (km): {distance_km}")
    
    return distance_km