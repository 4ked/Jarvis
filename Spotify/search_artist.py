# shows artist info for a URN or URL

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import json
import os

with open('artists.json', 'r') as f:
    artists = json.load(f)

if len(sys.argv) > 1:
    arg_line = " ".join(sys.argv[1:])
    for name in artists:
        if name == arg_line:
            urn = artists[name]
else:
    urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'


sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
response = sp.artist_top_tracks(urn)

def artistTopTracks():
    topTracks =[]
    for track in response['tracks']:
        topTracks.append(track['name'])

    return "Top Tracks: \n - " + "\n - ".join(topTracks)
