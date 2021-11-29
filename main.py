from InstagramScraper import InstagramSpider
import json


def save_page_source(page_source, filename, append=False):
    with open(filename, "w" if not append else "a", encoding="utf-8") as file:
        file.write(page_source)


def get_post_links():
    url = "https://www.instagram.com/explore/tags/instamoments/"

    bot = InstagramSpider()

    bot.goto(url)
    
    for i in range(20):
        bot.mousewheel_vscroll(5)

        page_source = bot._browser.page_source

        postfix = str(i) + ".html"
        filename = "instamoments/instamoments" + postfix

        save_page_source(page_source, filename, append=True)


    bot._browser.close()


def get_user_link():
    bot = InstagramSpider()

    urls = [
        "https://www.instagram.com/p/CHfqIVrFOsA/",
        "https://www.instagram.com/p/CHfX3K5lsUk/"
    ]

    for i, url in enumerate(urls):
        bot.goto(url)
        page_source = bot._browser.page_source
        save_page_source(page_source,  filename=str(i) + ".html")

    bot._browser.close()
    


def get_all_post_pagesources(links):

    bot = InstagramSpider()
    prefix = "https://instagram.com"

    for link in links:
        bot.goto(prefix + link)

        page_source = bot._browser.page_source

        filename = "post_sources/" + link.split('/')[-2] + ".html"

        save_page_source(page_source, filename)

    bot._browser.close()



if __name__ == "__main__":
    # get_user_link()

    with open("./instamoments_post_links.json", "r") as file:
        links = json.load(file)

    get_all_post_pagesources(links['links'])
