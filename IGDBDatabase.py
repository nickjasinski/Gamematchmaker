# currently just finds random games from the database, will expand to retrieve desired games later
# yr9ttfd7f5s3xyncki7zvzvetlajwa - client id
# bdi9rpdoyqp4lo1qel82f7b6ng2ple - access token

import requests
import datetime  # Required for converting Unix timestamps to human-readable dates

# Twitch Client ID and Access Token
client_id = 'yr9ttfd7f5s3xyncki7zvzvetlajwa'
access_token = 'bdi9rpdoyqp4lo1qel82f7b6ng2ple'

# Set the endpoint URL for the IGDB API (v4)
url = 'https://api.igdb.com/v4/games'

# Headers for authentication and API request
headers = {
    'Client-ID': client_id,
    'Authorization': f'Bearer {access_token}'
}

# Define the query to fetch game data
query = """
fields name, genres.name, platforms.name, release_dates.date, rating;
limit 5;
"""

# Make the POST request to the IGDB API
response = requests.post(url, headers=headers, data=query)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response data
    games_data = response.json()
    
    for game in games_data:
        # Safely get the game name
        game_name = game.get('name', 'No name available')
        
        # Safely get the genres
        genres = game.get('genres', [])
        genres_list = ', '.join([genre['name'] for genre in genres]) if genres else 'No genres available'
        
        # Safely get the platforms
        platforms = game.get('platforms', [])
        platforms_list = ', '.join([platform['name'] for platform in platforms]) if platforms else 'No platforms available'
        
        # Safely get the release date (Unix timestamp)
        release_dates = game.get('release_dates', [])
        
        if release_dates:
            release_date = release_dates[0].get('date', None)
            if release_date:
                release_date = datetime.datetime.utcfromtimestamp(release_date).strftime('%Y-%m-%d')
            else:
                release_date = 'No release date available'
        else:
            release_date = 'No release date available'
        
        # Safely get the rating
        rating = game.get('rating', None)
        rating = rating if rating is not None else 'No rating available'
        
        # Print the game data
        print(f"Game Name: {game_name}")
        print(f"Genres: {genres_list}")
        print(f"Platforms: {platforms_list}")
        print(f"Release Date: {release_date}")
        print(f"Rating: {rating}")
        print('-' * 30)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")