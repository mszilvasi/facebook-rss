import json
import requests
from feedgen.feed import FeedGenerator

# Replace this with your Facebook Graph API Access Token
ACCESS_TOKEN = 'EAAoZBbKyx7dwBO3mtTZBpjCA1vFCmnXzkJpqBC8I8YUTo3lAXRbiOXddkOO3TieaZCS12S24z9oiVlf9Nl9Y3YdIyyrePSS2HpJjJNjFJww1kGiZB7456H8lN5MZBxquZCvbEP5DPAYFRxZBdqjZBVQlghRn2il8b80BuhnJZBhgsYsHWSLvqygfPRZAfsyZCF2l9HIgnAokkE5DXUMSG1KucIZD'

# Load pages from pages.json
with open('pages.json', 'r') as file:
    pages = json.load(file)['pages']

# Initialize the RSS feed
feed = FeedGenerator()
feed.title("Facebook RSS Feed")
feed.link(href="http://example.com", rel="alternate")
feed.description("RSS feed generated from Facebook posts")

# Fetch posts from each page and add them to the RSS feed
for page in pages:
    url = f"https://graph.facebook.com/{page}/posts?access_token={ACCESS_TOKEN}"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json().get('data', [])
        for post in posts:
            entry = feed.add_entry()
            entry.title(post.get('message', 'No Title'))
            entry.link(href=f"https://facebook.com/{post['id']}")
            entry.description(post.get('message', 'No Description'))
    else:
        print(f"Failed to fetch posts for {page}: {response.status_code}")

# Save the RSS feed to an XML file
feed.rss_file('facebook_feed.xml')