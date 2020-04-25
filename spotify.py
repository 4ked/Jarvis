import sys
import spotipy
import spotipy.util as util

# plz don't use my keys I'm just testing :D
util.prompt_for_user_token('max.goeke',
                           'user-library-read',
                           client_id='6ef7562983d84fd0a99093701c2dade1',
                           client_secret='a5ea54deba2c49f2bb50382ba19c4d05',
                           redirect_uri='http://maxgoeke.me/jarvis')

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)