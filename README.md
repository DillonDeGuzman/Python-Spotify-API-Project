# Spotify Artist Analytics Dashboard

A Flask web application that uses the Spotify API to search for an artist and display their top tracks and album artwork.

## Features

- Search for an artist by name
- Retrieve artist data through the Spotify API
- Display the artist's top 10 tracks
- Display album artwork for returned tracks

## Tech Stack

- Python
- Flask
- HTML/CSS
- Spotify API
- Spotipy

## Run Locally

1. Clone the repository:

```bash
git clone [https://github.com/DillonDeGuzman/Python-Spotify-API-Project.git](https://github.com/DillonDeGuzman/Python-Spotify-API-Project.git)
cd Python-Spotify-API-Project
```

2. Install dependencies:

```bash
pip install flask spotipy python-dotenv
```

3. Run the application:

```bash
python app.py
```

4. Open the local URL shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

## Project Structure

```text
app.py          # Flask application
spotify_api.py  # Spotify API logic
templates/      # HTML templates
```
