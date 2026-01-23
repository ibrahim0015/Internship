import json
import time
import requests
from pathlib import Path

CACHE_FILE = Path("cache.json")


def load_cache():
    if not CACHE_FILE.exists():
        return {}

    try:
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Cache file is corrupted. Rebuilding cache.")
        return {}


def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)


def is_cache_valid(timestamp, max_age_minutes):
    return (time.time() - timestamp) < (max_age_minutes * 60)


def fetch_github_repos(username, cache_minutes=10, token=None):
    cache = load_cache()
    cache_key = f"github_repos:{username}"

    # Check cache
    if cache_key in cache:
        cached = cache[cache_key]
        if is_cache_valid(cached["timestamp"], cache_minutes):
            return cached["data"], True

    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"

    all_repos = []
    page = 1
    per_page = 100

    while True:
        url = f"https://api.github.com/users/{username}/repos"
        params = {"page": page, "per_page": per_page}

        try:
            response = requests.get(
                url,
                headers=headers,
                params=params,
                timeout=10
            )
        except requests.exceptions.RequestException:
            raise Exception("Network error while contacting GitHub API.")

        if response.status_code == 403:
            raise Exception(
                "GitHub API rate limit exceeded. "
                "Use a personal access token."
            )

        if response.status_code == 404:
            raise Exception("GitHub user not found.")

        if response.status_code != 200:
            raise Exception(f"GitHub API error: {response.status_code}")

        page_data = response.json()
        if not page_data:
            break

        all_repos.extend(page_data)
        page += 1

    cache[cache_key] = {
        "timestamp": time.time(),
        "data": all_repos
    }
    save_cache(cache)

    return all_repos, False
