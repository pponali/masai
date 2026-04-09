import requests
import time
import json
import os
from datetime import datetime
from urllib3.util.retry import Retry


def get_session():
    session = requests.Session()
    session.headers.update({"User-Agent": "TrendPulse/1.0"})
    retry = Retry(total=5, backoff_factor=1, status_forcelist=[429,502, 503, 504], allowed_methods=["HEAD", "GET", "OPTIONS"])
    adapter = requests.adapters.HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session      
    

try:
    response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching top stories: {e}")
    response = None

if response is not None:
    ids = response.json()[:500]
    print(ids)
else:
    ids = []

technology_category_stories = []
worldnews_category_stories = []
sports_category_stories = []
science_category_stories = []
entertainment_category_stories = []


technology_keywords = ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"]
worldnews_keywords = ["war", "government", "country", "president", "election", "climate", "attack", "global"]
sport_keywords = ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"]
science_keywords = ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"]
entertainment_keywords = ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]

headers = {"User-Agent": "TrendPulse/1.0"}

session = get_session()
for story_id in ids:
    details_response = session.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json", headers=headers)
    story = details_response.json()

    if story is None or "title" not in story:
        continue

    title = story.get('title', '').lower()
    post_id = story.get('id', '')
    score = story.get('score', 0)
    num_comments = story.get('descendants', 0)
    author = story.get('by', '')
    collected_at = datetime.now().isoformat()

    # Step 1: Figure out which category this story belongs to
    category = None


    ''' It is bit complex logic for myself. To ensure that we only collect 25 stories per category, we check the length of 
    the respective category list before assigning the category to the story.'''

    if any(keyword.lower() in title for keyword in technology_keywords) and len(technology_category_stories) < 25:
        category = "technology"
    elif any(keyword.lower() in title for keyword in worldnews_keywords) and len(worldnews_category_stories) < 25:
        category = "worldnews"
    elif any(keyword.lower() in title for keyword in sport_keywords) and len(sports_category_stories) < 25:
        category = "sports"
    elif any(keyword.lower() in title for keyword in science_keywords) and len(science_category_stories) < 25:
        category = "science"
    elif any(keyword.lower() in title for keyword in entertainment_keywords) and len(entertainment_category_stories) < 25:
        category = "entertainment"

    # Step 2: If the story matched a category, build story_data and add it to the right list
    if category is not None:
        story_data = {
            "post_id": post_id,
            "title": story.get('title', ''),
            "score": score,
            "num_comments": num_comments,
            "author": author,
            "collected_at": collected_at,
            "category": category
        }

        #adding store the respecitve category list and print the story category and title.
        if category == "technology":
            technology_category_stories.append(story_data)
        elif category == "worldnews":
            worldnews_category_stories.append(story_data)
        elif category == "sports":
            sports_category_stories.append(story_data)
        elif category == "science":
            science_category_stories.append(story_data)
        elif category == "entertainment":
            entertainment_category_stories.append(story_data)

        print(f"[{category}] {story_data['title']}")

    
    # If we have collected 25 stories for each category, we can stop early instead of waiting to loop through all 500 story ids. which is waste of resource and time.
    if len(technology_category_stories) == 25 and len(worldnews_category_stories) == 25 and len(sports_category_stories) == 25 and len(science_category_stories) == 25 and len(entertainment_category_stories) == 25:
        break

    time.sleep(1)
# Step 3: Save to file after each story
all_stories = {
        "technology": technology_category_stories,
        "worldnews": worldnews_category_stories,
        "sports": sports_category_stories,
        "science": science_category_stories,
        "entertainment": entertainment_category_stories
    }
os.makedirs("data", exist_ok=True)
with open("data/trends_20240115.json", "w") as f:
    json.dump(all_stories, f, indent=4)

print(f"Collected {len(technology_category_stories) + len(worldnews_category_stories) + len(sports_category_stories) + len(science_category_stories) + len(entertainment_category_stories)} stories. Saved to data/trends_20240115.json")