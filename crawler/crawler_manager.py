# coding=utf-8
import url_manager
import url_downloader
import html_parser
import data_outputer


class Crawler_Main:
    def __init__(self):
        self.urls = url_manager.Url_Mananger()
        self.downloader = url_downloader.Url_Downloader()
        self.parser = html_parser.Html_Parser()
        self.outputer = data_outputer.Data_Outputer()

    def craw(self, root_html, max_pages):
        self.urls.add_new_url(root_html)
        count = 0
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html_doc = self.downloader.download(new_url)
                new_urls, data = self.parser.parse(new_url, html_doc)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(data)
                print 'craw OK [%d]: %s' % (count, new_url)
                if count >= max_pages:
                    break
                count = count + 1
            except Exception:
                print "craw exception: %s" % new_url
            self.outputer.output_html()


if __name__ == '__main__':
    root_html = "http://baike.baidu.com/view/21087.htm"
    crawler = Crawler_Main()
    crawler.craw(root_html, 5)
