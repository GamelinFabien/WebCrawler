"""Main module to call WebCrawler"""
__author__ = "Fabien GAMEIN, Ismail NGUYEN, Bruno VACQUEREL"
import getopt, sys
from WebCrawler import WebCrawler

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[2:], "d:o", ["depth=", "outside"])
    except getopt.GetoptError as err:
        print err
        sys.exit(2)

    GO_OUTSIDE = False
    DEPTH = 2
    
    URL = str(sys.argv[1])
    if URL == '':
        URL = "http://www.nguyenismail.com/"
    
    for o, a in opts:
        if o in ("-d", "-depth"):
            DEPTH = int(a)
        elif o in ("-o", "-outside"):
            GO_OUTSIDE = True
        else:
            print "Error : -d for depth, -o for go_outside"
     
    CRAWLER = WebCrawler(URL, DEPTH, GO_OUTSIDE)
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
