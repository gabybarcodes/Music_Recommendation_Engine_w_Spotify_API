import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '2a57e99a627e4443b20a0ac81d92120e'
client_secret = '77cbceff91cb46c6b6e60077a1e15906'

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_bpm(song_name, artist_name):
    results = sp.search(q=f'track:{song_name} artist:{artist_name}', type='track')
    track = results['tracks']['items'][0]

    audio_features = sp.audio_features(track['id'])[0]


    return audio_features['tempo']

# Example usage
song_name = 'Blinding Lights'
artist_name = 'The Weeknd'
bpm = get_bpm(song_name, artist_name)
print(f'The BPM of "{song_name}" by {artist_name} is {bpm}')
