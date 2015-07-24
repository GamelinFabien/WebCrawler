"""Module for search by keywords"""
__author__ = "Fabien GAMEIN, Ismail NGUYEN, Bruno VACQUEREL"
import getopt, sys
from WebCrawler import WebCrawler

if __name__ == "__main__":
    try:
        OPTS, ARGS = getopt.getopt(sys.argv[1:], "i:k:", ["input=", "keyword="])
    except getopt.GetoptError as err:
        print err
        sys.exit(2)

    for o, a in OPTS:
        if o in ("-i", "-input"):
            INPUT = a
        elif o in ("-k", "-keyword"):
            KEYWORD = a
        else:
            print "Error : -i for input, -k for keyword"

    CRAWLER = WebCrawler(URL, null, null, null, INPUT, KEYWORD)
    CRAWLER.load()

    print("Dictionary : ", CRAWLER.dictionary)

    print "Save the crawling ? (o/[n]) : "
    if raw_input() == 'o':
        print "Folder : "
    CRAWLER.save()

    print "Charge the crawling ? (o/[n]) : "
    if raw_input() == 'o':
        print "Folder : "
    CRAWLER.load()
