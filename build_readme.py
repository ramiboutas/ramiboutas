from pathlib import Path

import feedparser
import requests
from bs4 import BeautifulSoup


def main():
    chunks = []
    chunks.extend(get_bio())
    chunks.append("")
    chunks.append("## Latest blog posts\n")
    chunks.extend(get_latest_posts())
    chunks.append("")
    chunks.append("## On social media\n")
    chunks.extend(on_social_media())
    chunks.append("")

    readme = Path(__file__).parent / "README.md"
    readme.write_text("\n".join(chunks))


def get_bio():
    # Get bio from my website to avoid duplication
    response = requests.get("https://www.ramiboutas.com/me/")
    if response.status_code != 200:
        raise ValueError("Unexpected response status code {response.status_code}")
    soup = BeautifulSoup(response.content.decode(), "html.parser")
    heading = soup.body.find("h1")
    for elem in heading.next_siblings:
        if elem.name != "img" and str(elem).strip():
            yield str(elem).replace("welcome to my site", "welcome to my GitHub bio")


def on_social_media():
    response = requests.get("https://www.ramiboutas.com/")
    if response.status_code != 200:
        raise ValueError("Unexpected response status code {response.status_code}")
    soup = BeautifulSoup(response.content.decode(), "html.parser")
    heading = soup.body.find("h2")
    for elem in heading.next_siblings:
        if elem.name != "img" and str(elem).strip():
            yield str(elem)


def get_latest_posts():
    chunks = []
    posts = feedparser.parse("https://www.ramiboutas.com/feeds/all.atom.xml")[
        "entries"
    ][:10]
    chunks.extend(
        [
            f'* [{post["title"]}]({post["link"]}) ({post["updated"].split("T")[0]})'
            for post in posts
        ]
    )
    return chunks


if __name__ == "__main__":
    main()
