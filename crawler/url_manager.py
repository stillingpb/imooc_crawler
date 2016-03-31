# coding=utf-8
class Url_Mananger:
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url in self.new_urls or url in self.old_urls:
            return
        self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) > 0

    def get_new_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url
