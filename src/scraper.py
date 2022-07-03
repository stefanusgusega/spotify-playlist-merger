"""
Module to scrape the playlist data
"""

import json
import spotipy
from icecream import ic


MAX_TRACKS_RETURNED = 10000
DEFAULT_LIMIT = 100


class Scraper:
    """
    Scrape playlist with this class
    """

    def __init__(self, spotify_client: spotipy.Spotify) -> None:
        self.spotify_client = spotify_client

    def scrape(self, playlist_url: str, json_to_save: str = None):
        # Scraped playlist
        playlist = []

        # Iterate every forward offset
        for i in range(0, MAX_TRACKS_RETURNED, DEFAULT_LIMIT):
            # Return only items key
            temp_playlist = self.spotify_client.playlist_tracks(
                playlist_id=playlist_url,
                fields="items",
                offset=i,
            )

            # If the items doesn't contain anything then break the loop
            if len(temp_playlist["items"]) == 0:
                break

            ic(len(temp_playlist["items"]))

            # Extend the array with the items at this offset
            playlist.extend(temp_playlist["items"])

        # Save json if json_to_save defined
        if json_to_save is not None:
            print(f"Saving scraped data into json file: {json_to_save}")
            with open(json_to_save, "w", encoding="utf-8") as f:
                json.dump(playlist, f, indent=4)

        return playlist
