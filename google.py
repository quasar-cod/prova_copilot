import webbrowser

import urllib.parse

def open_google_maps(country, town):
    query = f"{town}, {country}"
    url = f"https://www.google.com/maps/search/{urllib.parse.quote(query)}"
    webbrowser.open(url)

# Ask user for a string and store it in a variable
user_input = input("Enter a location (e.g., Rome, Italy): ")

# Split the input into town and country (assuming format "Town, Country")
try:
    town, country = [x.strip() for x in user_input.split(",", 1)]
    open_google_maps(country, town)
except ValueError:
    print("Please enter the location in the format 'Town, Country'")
