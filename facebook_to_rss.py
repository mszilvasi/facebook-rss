import requests
from feedgen.feed import FeedGenerator
from datetime import datetime

# Facebook page IDs or usernames
PAGES = [
    "share/1Av6mRa981",  # Example: Modify with your actual page names
    "dmagyarmuzsa",
    "vastagbor",
    "avakmajom",
    "kancz.geopolitika",
    "balazs.csire",
    "kardblog",
    "Kartonkocsma",
    "istvan.szentivanyi.56",
    "valasztasi.kalauz",
    "torokgaborelemez",
    "tamas.gomperz",
    "feledy",
    "Tiborublog",
    "szeletommy",
    "andras.racz.526",
]

ACCESS_TOKEN = "EAAoZBbKyx7dwBO3mtTZBpjCA1vFCmnXzkJpqBC8I8YUTo3lAXRbiOXddkOO3TieaZCS12S24z9oiVlf9Nl9Y3YdIyyrePSS2HpJjJNjFJww1kGiZB7456H8lN5MZBxquZCvbEP5DPAYFRxZBdqjZBVQlghRn2il8b80BuhnJZBhgsYsHWSLvqygfPRZAfsyZCF2l9HIgnAokkE5DXUMSG1KucIZD"

def fetch_facebook_posts(page_id, token):
    url = f"https://graph.facebook.com/v16.0/{page_id}/posts?access_token={token}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print(f"Error fetching posts from {page_id}: {response.status_code}")
        return []

def generate_rss_feed(posts):
    fg = FeedGenerator()
    fg.title("Facebook RSS Feed")
    fg.link(href="https://www.facebook.com", rel="alternate")
    fg.description("RSS feed for Facebook posts")

    for post in posts:
        entry = fg.add_entry()
        entry.title(post.get("message", "No title available"))
        entry.link(href=f"https://www.facebook.com/{post.get('id')}")
        entry.description(post.get("message", "No description available"))
        entry.pubDate(datetime.strptime(post["created_time"], "%Y-%m-%dT%H:%M:%S%z"))

    fg.rss_file("facebook_feed.xml")

def main():
    all_posts = []
    for page in PAGES:
        posts = fetch_facebook_posts(page, ACCESS_TOKEN)
        all_posts.extend(posts)

    generate_rss_feed(all_posts)

if __name__ == "__main__":
    main()