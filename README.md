# Spotify Artist Analytics Dashboard

A Flask web application that uses the Spotify Web API to search for an artist and display their top tracks and album artwork.

## Overview

This project provides a simple interface for exploring artist data from Spotify. A user enters an artist name, and the application retrieves information through the Spotify API and presents the artist's top 10 tracks along with associated album artwork.

## Features

- Search for an artist by name
- Retrieve artist data using the Spotify Web API
- Display an artist's top 10 tracks
- Display album artwork associated with returned tracks
- Render results in a browser-based Flask interface

## Tech Stack

- Python
- Flask
- HTML/CSS
- Spotify Web API
- Spotipy

## Project Structure

```text
.
├── app.py              # Flask application and routes
├── spotify_api.py      # Spotify API integration logic
├── templates/          # HTML templates for the user interface
├── .env.example        # Example environment-variable configuration
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.9 or later
- A Spotify Developer account
- A Spotify application with a Client ID and Client Secret

### 1. Clone the repository

```bash
git clone [https://github.com/DillonDeGuzman/Python-Spotify-API-Project.git](https://github.com/DillonDeGuzman/Python-Spotify-API-Project.git)
cd Python-Spotify-API-Project
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask spotipy python-dotenv
```

### 4. Configure Spotify credentials

Create a file named `.env` in the project root. Use `.env.example` as a template:

```env
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
```

Never commit your real `.env` file or credentials to GitHub.

### 5. Run the application

```bash
python app.py
```

Open the local URL printed in the terminal, typically:

```text
http://127.0.0.1:5000
```

## How It Works

1. The user enters an artist name in the Flask web interface.
2. The application sends a request to the Spotify Web API.
3. The API returns artist and track information.
4. The application renders the artist's top tracks and album artwork in the browser.

## Future Improvements

- Add artist profile details, genres, and follower counts
- Include audio previews when available
- Add track popularity metrics and visualizations
- Add automated tests for API and route behavior
- Deploy the application for public access

## Security Notes

This project uses Spotify API credentials stored in environment variables. The `.env` file is excluded from version control to prevent accidental exposure of sensitive credentials.
