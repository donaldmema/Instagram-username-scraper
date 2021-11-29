from basic_web_scraper.BasicSpider import BasicSpider


class InstagramSpider(BasicSpider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



    def enter_username(self):

        field_name = "username"

        field = self._browser.find_element_by_name(field_name)
        
        self.slow_type()
