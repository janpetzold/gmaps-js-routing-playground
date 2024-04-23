import re
import base64
import json
import requests
from dotenv import load_dotenv
import googlemaps
import os
from datetime import datetime

load_dotenv()

def extract_route_details(directions_result):
    route_details = []
    # Assuming directions_result is a list and we take the first route
    for leg in directions_result[0]["legs"]:
        for step in leg["steps"]:
            detail = {
                "start_location": step["start_location"],  # Get from step
                "end_location": step["end_location"],      # Get from step
                "html_instructions": step["html_instructions"]  # Get from step
            }
            route_details.append(detail)
    return route_details

# Link from Google Maps for given route with four waypoints
gmaps_url = 'https://maps.app.goo.gl/5t2vbyiqKXTZQoM69'
decoded_url = requests.get(gmaps_url)

#print(f"Decoded URL is {decoded_url.url}")

# Get all Geopositions in an Array
regex_pattern = r"!1d([-\d.]+)!2d([-\d.]+)"

# Find all matches of the regex pattern in the URL
matches = re.findall(regex_pattern, decoded_url.url)

# Convert matches to a list of tuples, where each tuple represents a pair of GPS coordinates (longitude, latitude)
# Be aware that logitude is first here for whatever reason.
gps_coordinates = [(float(lon), float(lat)) for lon, lat in matches]
gps_coordinates_reversed = [(float(lat), float(lon)) for lon, lat in matches]

gmaps = googlemaps.Client(os.getenv("GMAPS_API_KEY"))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions(str(gps_coordinates_reversed[0]).replace("(", "").replace(")", ""),
                                     str(gps_coordinates_reversed[3]).replace("(", "").replace(")", ""),
                                     mode="driving",
                                     departure_time=now,
                                     units="metric",
                                     waypoints=[
                                        str(gps_coordinates_reversed[1]).replace("(", "").replace(")", ""),
                                        str(gps_coordinates_reversed[2]).replace("(", "").replace(")", "")
                                     ])

#print("Polyline of route is as follows. Verify it e.g. via https://valhalla.github.io/demos/polyline/.")
#print(directions_result[0]["overview_polyline"]["points"])

route_details = extract_route_details(directions_result)
#print(route_details)

json_string = json.dumps(route_details)
base64_bytes_route = base64.b64encode(json_string.encode('utf-8'))

print("+++++")
print("Route details as Base64:")
print(base64_bytes_route)

message_bytes = directions_result[0]["overview_polyline"]["points"].encode('ascii')
base64_bytes_polyline = base64.b64encode(message_bytes)

print("+++++")
print("Polyline as Base64:")
print(base64_bytes_polyline)