# coding:utf8
import cookielib
import urllib2


def load1(url):
    response1 = urllib2.urlopen(url)
    return response1.read()


def load2(url):
    request = urllib2.Request(url)
    request.add_header('user-agent', 'Mozilla/5.0')
    response2 = urllib2.urlopen(request)
    return response2.read()


def load3(url):
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    response3 = urllib2.urlopen(url)
    return response3.read()


class Url_Downloader:
    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
