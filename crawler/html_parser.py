# coding=utf-8
import re
import urlparse
from bs4 import BeautifulSoup


class Html_Parser:
    def parse(self, page_url, page_doc):
        if page_url is None or page_doc is None:
            return
        soup = BeautifulSoup(page_doc, 'html.parser', from_encoding='utf-8')
        new_urls = self._parse_new_urls(page_url, soup)
        new_data = self._parse_new_data(page_url, soup)
        return new_urls, new_data

    def _parse_new_urls(self, page_url, soup):
        new_urls = set()
        # url = '/view/123.htm'
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            half_url = link['href']
            full_url = urlparse.urljoin(page_url, half_url)
            new_urls.add(full_url)
        return new_urls

    def _parse_new_data(self, page_url, soup):
        new_data = {}
        new_data['url'] = page_url
        # title: <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        new_data['title'] = title_node.get_text()
        # summary: <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        new_data['summary'] = summary_node.get_text()
        return new_data
