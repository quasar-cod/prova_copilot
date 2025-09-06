import requests
from bs4 import BeautifulSoup

def search_youtube(query):
    url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.find_all("a"):
        href = link.get("href")
        title = link.get("title")
        if href and "/watch?v=" in href and title:
            return f"https://www.youtube.com{href}", title
    return None, None

if __name__ == "__main__":
    song = input("Enter the song name: ")
    video_url, video_title = search_youtube(song)
    if video_url:
        print(f"Top result: {video_title}\n{video_url}")
    else:
        print("No results found.")