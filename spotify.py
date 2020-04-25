import sys
import spotipy
import spotipy.util as util

# plz don't use my keys I'm just testing :D
util.prompt_for_user_token('max.goeke',
                           'user-library-read',
                           client_id='6ef7562983d84fd0a99093701c2dade1',
                           client_secret='a5ea54deba2c49f2bb50382ba19c4d05',
                           redirect_uri='http://maxgoeke.me/jarvis')

# A few notes...
# As of now you have to use environment variables, I'm still figuring this out
# python3 spotify.py username \\ to run this script that prints all songs in every playlist of user username

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name']))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need your username!")
        print("usage: python user_playlists.py [username]")
        sys.exit()

    token = util.prompt_for_user_token(username)

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print()
                print(playlist['name'])
                print ('  total tracks', playlist['tracks']['total'])
                results = sp.playlist(playlist['id'],
                    fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks)
    else:
        print("Can't get token for", username)