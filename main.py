"""
Main program
"""
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from icecream import ic
import json

MAX_TRACKS_RETURNED = 10000
DEFAULT_LIMIT = 100

# Load the environment variables on .env
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret
)

spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Iterate every forward offset
for i in range(0, MAX_TRACKS_RETURNED, DEFAULT_LIMIT):
    # Return only items key
    playlist = spotify.playlist_tracks(
        playlist_id="https://open.spotify.com/playlist/37i9dQZF1DX08mhnhv6g9b?si=d4807825a7864fdb",
        fields="items",
        offset=i,
    )

    # If the items doesn't contain anything then break the loop
    if len(playlist["items"]) == 0:
        break

    ic(len(playlist["items"]))

    # Save to json file
    with open(os.path.join("dump", f"playlist_{i}.json"), "w", encoding="utf-8") as f:
        json.dump(playlist, f, indent=4)
