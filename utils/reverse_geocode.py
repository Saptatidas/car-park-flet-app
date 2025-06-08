import requests

def get_place_name_from_coordinates(lat, lon, api_key):
    try:
        url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={api_key}"
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'OK':
            return data['results'][0]['formatted_address']
        else:
            print("Reverse geocoding error:", data['status'])
            return "Unknown Location"
    except Exception as e:
        print("Error during reverse geocoding:", e)
        return "Error"
