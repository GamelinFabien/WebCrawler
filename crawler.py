__author__ = 'Fabien GAMEIN, Ismail NGUYEN, Bruno VACQUEREL'
from WebCrawler import WebCrawler

if __name__ == "__main__":

    print "URL : "
    url = raw_input()

    print "Depth : "
    depth = raw_input()

    print "Go outside ? ([o]/n)"

    crawler = WebCrawler(url, depth, False if raw_input() == 'n' else True)
    crawler.crawl()

    print("Dictionary : ", crawler.dictionary)

    print "Save the crawling ? (o/[n]) : "
    if raw_input() == 'o':
        print "Folder : "
    crawler.save(raw_input())

    print "Charge the crawling ? (o/[n]) : "
    if raw_input() == 'o':
        print "Folder : "
    crawler.load(raw_input())
