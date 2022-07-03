"""
Main program
"""
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

from src.scraper import Scraper

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

# Scraped playlist
playlist = Scraper(spotify_client=spotify).scrape(
    playlist_url="https://open.spotify.com/playlist/37i9dQZF1DX08mhnhv6g9b",
    json_to_save=os.path.join("dump", "playlist_full.json"),
)
