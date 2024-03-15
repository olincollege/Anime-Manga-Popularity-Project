import requests
import pandas as pd
from bs4 import BeautifulSoup


site_url = "https://myanimelist.net"
response = requests.get(site_url)
response.status_code
len(response.text)

doc = BeautifulSoup(response.text)
type(doc)  # should return bs4.BeautifulSoup

most_pop_url = site_url + "/topanime.php?type=bypopularity"
response = requests.get(most_pop_url)
response.status_code
doc = BeautifulSoup(response.text)

row_content = doc.find_all("tr", {"class": "ranking-list"})
len(row_content)


# list(map(lambda x:x.strip(),var[:2]))
def parse_episodes(listt):
    """ """
    result = []
    for i in listt[:2]:
        r = i.strip()
        result.append(r)
    return result


var = (
    row_content[5]
    .find("div", class_="information di-ib mt4")
    .text.strip()
    .split("\n")
)
parse_episodes(var)

popular_anime = []
for row in row_content:
    episode = parse_episodes(
        row.find("div", class_="information di-ib mt4").text.strip().split("\n")
    )
    ranking = {
        "Rank": row.find("td", class_="rank ac").find("span").text,
        "Title": row.find("div", class_="di-ib clearfix").find("a").text,
        "Rating": row.find("td", class_="score ac fs14").find("span").text,
        "Image_URL": row.find("td", class_="title al va-t word-break").find(
            "img"
        )["data-src"],
        "Episodes": episode[0],
        "Dates": episode[1],
    }
    popular_anime.append(ranking)

popular_anime[:5]


def write_csv(items, path):
    """ """
    # Open the file in write mode
    with open(path, "w") as f:
        # Return if there's nothing to write
        if len(items) == 0:
            return

        # Write the headers in the first line
        headers = list(items[0].keys())
        f.write(",".join(headers) + "\n")

        # Write one item per line
        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            f.write(",".join(values) + "\n")


write_csv(popular_anime, "popular_anime.csv")
