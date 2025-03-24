from flask import Flask, jsonify, render_template
from spotify_api import get_token, search_for_artist, get_songs_by_artist

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/top-tracks/<artist_name>')
def top_tracks(artist_name):
    try:
        token = get_token()
        artist = search_for_artist(token, artist_name)
        
        if not artist:
            return jsonify({"error": "Artist not found"}), 404
            
        tracks = get_songs_by_artist(token, artist["id"])
        return jsonify({
            "artist": artist["name"],
            "tracks": [track["name"] for track in tracks]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)