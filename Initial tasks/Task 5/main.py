import argparse
from client import fetch_github_repos


def summarize_repos(repos):
    total = len(repos)

    sorted_repos = sorted(
        repos,
        key=lambda r: r.get("stargazers_count", 0),
        reverse=True
    )

    return total, sorted_repos[:5]


def main():
    parser = argparse.ArgumentParser(description="GitHub Repo Stats Tool")
    parser.add_argument("username", help="GitHub username")
    parser.add_argument("--cache-minutes", type=int, default=10)
    parser.add_argument(
        "--token",
        help="GitHub Personal Access Token (optional)"
    )

    args = parser.parse_args()

    try:
        repos, from_cache = fetch_github_repos(
            args.username,
            cache_minutes=args.cache_minutes,
            token=args.token
        )
    except Exception as e:
        print("Error:", e)
        return

    total, top_repos = summarize_repos(repos)

    print("\nGitHub User:", args.username)
    print("Source:", "CACHE" if from_cache else "API")
    print("Total Public Repositories:", total)

    print("\nTop 5 Repositories by Stars:")
    for repo in top_repos:
        print(
            f"- {repo['name']} | ⭐ {repo['stargazers_count']} | "
            f"{repo['html_url']}"
        )


if __name__ == "__main__":
    main()
