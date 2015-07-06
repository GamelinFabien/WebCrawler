"""Module for search by keywords"""
__author__ = "Fabien GAMEIN, Ismail NGUYEN, Bruno VACQUEREL"
import getopt, sys
from WebCrawler import WebCrawler

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:k:", ["input=", "keyword="])
    except getopt.GetoptError as err:
        print err
        sys.exit(2)

    for o, a in opts:
        if o in ("-i", "-input"):
            INPUT = a
        elif o in ("-k", "-keyword"):
            KEYWORD = a
        else:
            print "Error : -i for input, -k for keyword"
     
    CRAWLER = WebCrawler(URL, DEPTH, GO_OUTSIDE)
    CRAWLER.load()

    print("Dictionary : ", CRAWLER.dictionary)

    print "Save the crawling ? (o/[n]) : "
    if raw_input() == 'o':
        print "Folder : "
    CRAWLER.save(raw_input())

    print "Charge the crawling ? (o/[n]) : "
    if raw_input() == 'o':
        print "Folder : "
    CRAWLER.load(raw_input())
