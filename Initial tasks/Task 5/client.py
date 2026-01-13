import json
import time
import requests
from pathlib import Path

CACHE_FILE = Path("cache.json")


def load_cache():
    if CACHE_FILE.exists():
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}


def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)


def is_cache_valid(timestamp, max_age_minutes):
    return (time.time() - timestamp) < (max_age_minutes * 60)


def fetch_github_repos(username, cache_minutes=10):
    cache = load_cache()
    cache_key = f"github_repos:{username}"

    # Check cache
    if cache_key in cache:
        cached_entry = cache[cache_key]
        if is_cache_valid(cached_entry["timestamp"], cache_minutes):
            return cached_entry["data"], True

    # Fetch from API
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.status_code}")

    data = response.json()

    # Save to cache
    cache[cache_key] = {
        "timestamp": time.time(),
        "data": data
    }
    save_cache(cache)

    return data, False
