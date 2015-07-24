"""Main module to call WebCrawler"""
__author__ = "Fabien GAMEIN, Ismail NGUYEN, Bruno VACQUEREL"
import getopt, sys
from WebCrawler import WebCrawler

if __name__ == "__main__":
    try:
        OPTS, ARGS = getopt.getopt(sys.argv[2:], "d:o:u:", ["depth=", "outside", "output="])
    except getopt.GetoptError as err:
        print err
        sys.exit(2)

    GO_OUTSIDE = False
    DEPTH = 2
    OUTPUT = ""

    URL = str(sys.argv[1])
    if URL == '':
        URL = "http://www.nguyenismail.com/"

    for o, a in OPTS:
        if o in ("-d", "-depth"):
            DEPTH = int(a)
        elif o in ("-o", "-outside"):
            GO_OUTSIDE = True
        elif o in ("-u", "-output"):
            OUTPUT = a
            print("aaaaa : ", a)
        else:
            print "Error : -d for depth, -o for go_outside, -u for output"

    if GO_OUTSIDE == '':
        GO_OUTSIDE = False
    if DEPTH == '':
        DEPTH = 2
    if OUTPUT == '':
        OUTPUT = "results"

    CRAWLER = WebCrawler(URL, DEPTH, GO_OUTSIDE, OUTPUT)
    CRAWLER.crawl()

    #print("Dictionary : ", CRAWLER.dictionary)

    print "Save the crawling ? (y/[n]) : "
    if raw_input() == 'y':
        CRAWLER.save()

    print "Charge the crawling ? (y/[n]) : "
    if raw_input() == 'y':
        print("Dictionary: ", CRAWLER.load())
