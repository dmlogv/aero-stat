import urllib.parse as urlparse


class Link:
    @staticmethod
    def toabsolute(baseurl, link):
        parsed_link = urlparse.urlparse(link)
        parsed_baseurl = urlparse.urlparse(baseurl)
        return urlparse.urljoin(
            parsed_baseurl.scheme + '://' + parsed_baseurl.netloc,
            parsed_link.path)
