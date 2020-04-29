# shows artist info for a URN or URL

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys

if len(sys.argv) > 1:
    urn = sys.argv[1]
else:
    urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
response = sp.artist_top_tracks(urn)

def artistTopTracks():
    topTracks =[]
    for track in response['tracks']:
        topTracks.append(track['name'])

    return "Top Tracks: \n - " + "\n - ".join(topTracks)