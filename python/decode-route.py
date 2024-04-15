import re
import base64
import requests
from dotenv import load_dotenv
import googlemaps
import os
from datetime import datetime

load_dotenv()

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
                                     mode="walking",
                                     departure_time=now,
                                     waypoints=[
                                        str(gps_coordinates_reversed[1]).replace("(", "").replace(")", ""),
                                        str(gps_coordinates_reversed[2]).replace("(", "").replace(")", "")
                                     ])

print("Polyline of route is as follows. Verify it e.g. via https://valhalla.github.io/demos/polyline/.")
print(directions_result[0]["overview_polyline"]["points"])

print("Base64 encoding")
message_bytes = directions_result[0]["overview_polyline"]["points"].encode('ascii')
base64_bytes = base64.b64encode(message_bytes)

print(base64_bytes)