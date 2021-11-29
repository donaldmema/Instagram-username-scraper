import os

import json
from bs4 import BeautifulSoup

from collections import Counter


def run():
    
    with open("./raw_pagesource.html", "r", encoding="utf-8") as file:
        raw_html = file.read()

    soup = BeautifulSoup(raw_html, features="lxml")

    # findings = soup.find(text="email")
    findings = raw_html.find("@")

    print(findings)


def _extract_url(raw_html):
    
    soup = BeautifulSoup(raw_html, features="lxml")

    anchors = soup.find_all(name="a", attrs={"class": "sqdOP yWX7d _8A5w5 ZIAjV"})

    return anchors[0]['href']

def extract_all_urls(filenames):

    extracted_urls = []

    for filename in filenames:

        with open(filename, 'r', encoding='utf-8') as file:
            raw_html = file.read()

        extracted_urls.append(_extract_url(raw_html))

    return extracted_urls



def is_post(anchor):
    return '/p/' in anchor['href']


def get_links(filename):
    with open("./instamoments/" + filename, "r", encoding="utf-8") as file:
        raw_html = file.read()

    soup = BeautifulSoup(raw_html, features="lxml")

    anchors = soup.find_all("a")

    post_links = []

    for anchor in anchors:
        if is_post(anchor):
            post_links.append(anchor['href'])

    return post_links


def scrape_links():

    filenames = os.listdir("instamoments")

    all_post_links = []

    for filename in filenames:
        all_post_links += get_links(filename)

    link_counter = Counter(all_post_links)

    unique_links = list(link_counter.keys())

    print(unique_links)

    with open("instamoments_post_links.json", 'w') as file:
        unique_links_dict = {"links": unique_links}
        json.dump(unique_links_dict, file)


if __name__ == "__main__":
    # run()

    # scrape_post()

    # scrape_links()

    filenames = os.listdir('post_sources')

    filenames = ["post_sources/" + filename for filename in filenames]

    urls = extract_all_urls(filenames)

    url_counter = Counter(urls)

    unique_user_urls = list(url_counter.keys())

    print(unique_user_urls)

    print(f"Original: {len(urls)}")
    print(f"Uniques: {len(unique_user_urls)}")
