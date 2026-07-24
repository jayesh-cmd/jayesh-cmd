import json, requests
from bs4 import BeautifulSoup

def fetch_contributions():
    username = "jayesh-cmd"
    url = f"https://github.com/users/{username}/contributions"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200: raise Exception(f"Failed: {response.status_code}")
    soup = BeautifulSoup(response.text, "html.parser")
    days = [{"date": tool.get("data-date"), "level": int(tool.get("data-level", "0"))} 
            for tool in soup.find_all("td", class_="ContributionCalendar-day") if tool.get("data-date")]
    with open("data/contributions.json", "w") as f:
        json.dump({"days": days}, f, indent=2)

if __name__ == "__main__":
    fetch_contributions()
