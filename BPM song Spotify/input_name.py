import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'your_client_id'
client_secret = 'your_client_secret'

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_bpm(song_name, artist_name):

    results = sp.search(q=f'track:{song_name} artist:{artist_name}', type='track')
    if not results['tracks']['items']:
        print(f'No results found for "{song_name}" by {artist_name}')
        return None

    track = results['tracks']['items'][0]
    audio_features = sp.audio_features(track['id'])[0]
    if not audio_features:
        print(f'No audio features found for "{song_name}" by {artist_name}')
        return None

    return audio_features['tempo']

# Main function to handle user input 
def main():
    while True:
        song_name = input("Enter the song name: ")
        artist_name = input("Enter the artist name: ")

        bpm = get_bpm(song_name, artist_name)
        if bpm is not None:
            print(f'The BPM of "{song_name}" by {artist_name} is {bpm}')
        else:
            print("Could not find the song or its audio features.")

        if input("Do you want to search for another song? (y/n): ").lower() != 'y':
            break

if __name__ == '__main__':
    main()