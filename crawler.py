"""Main module to call WebCrawler"""
__author__ = 'Fabien GAMEIN, Ismail NGUYEN, Bruno VACQUEREL'
from WebCrawler import WebCrawler

if __name__ == "__main__":
    print "URL : "
    URL = raw_input()
    if URL == '':
        URL = "http://www.nguyenismail.com/"

    print "Depth : ([2])"
    DEPTH = raw_input()
    if DEPTH == '' or not DEPTH.isdigit():
        DEPTH = 2
    else:
        DEPTH = int(DEPTH)

    print "Go outside ? ([o]/n)"

    CRAWLER = WebCrawler(URL, DEPTH, False if raw_input() == 'n' else True)
    CRAWLER.crawl()

    print("Dictionary : ", CRAWLER.dictionary)

    print "Save the crawling ? (o/[n]) : "
    if raw_input() == 'o':
        print "Folder : "
    CRAWLER.save(raw_input())

    print "Charge the crawling ? (o/[n]) : "
    if raw_input() == 'o':
        print "Folder : "
    CRAWLER.load(raw_input())
