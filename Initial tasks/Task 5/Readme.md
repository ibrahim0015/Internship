# GitHub API Stats CLI Tool

A simple command-line tool that fetches public repository data from the GitHub API, caches results locally, and displays useful statistics for a given GitHub user.

## Features

- Fetches public repositories for a GitHub username
- Local file-based caching (`cache.json`) with time-based expiration
- Displays total public repositories
- Shows top 5 repositories by star count
- Simple CLI interface

## Project Structure

.
├── client.py
├── main.py
├── cache.json # auto-generated
└── README.md

markdown
Copy code

## Requirements

- Python 3.8+
- requests

Install dependency:
pip install requests

csharp
Copy code

## How to Run

Run the program by passing a GitHub username:

python main.py <github_username>

makefile
Copy code

Example:
python main.py torvalds

vbnet
Copy code

## Cache Duration

Default cache duration is 10 minutes.  
To change it:

python main.py torvalds --cache-minutes 30

csharp
Copy code

The output will indicate whether data was loaded from the API or cache.

## Notes

- `cache.json` is created automatically on first run
- GitHub API rate limits apply when cache is expired
- Intended for learning and CLI practice