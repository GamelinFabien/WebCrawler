__author__ = 'Fabien GAMELIN, Ismail NGUYEN, Bruno VACQUEREL'
import re
import requests
from bs4 import BeautifulSoup

class WebCrawler:
    nodes = []
    name = {}
    dictionary = {}
    url = ""
    go_outside = False
    depth = 0

    def __init__(self, url, go_outside=True, depth=2):
        self.url = url
        self.go_outside = go_outside
        self.depth = depth


    def extract(self):
        soup = BeautifulSoup(requests.get(self.url).text)
        match = "http"
        dictionary = {}

        for title in soup.find_all("title"):
            dictionary["Titre"] = title

        for meta_description_min in soup.find_all('meta', attrs={"name": "description"}):
            dictionary['Description'] = meta_description_min.get('content')

        for _meta_description_maj in soup.find_all('meta', attrs={"name": "Description"}):
            dictionary['Description'] = meta_description_maj.get('content')

        for meta_keywords in soup.find_all('meta', attrs={"name": "keywords"}):
            dictionary['Keyword'] = meta_keywords.get('content')

        for meta_keyword in soup.find_all('meta', attrs={"name": "keyword"}):
            dictionary['Keyword'] = meta_keyword.get('content')

        dictionary['Links'] = []

        for a in soup.find_all('a', href=True):
            if match in a.get('href'):
                dictionary['Links'].append(a.get('href'))

        return _dictionary

    def crawl(self, depth=2):
        compteur = 0

        if self.url:
            print "Computing base domain ..."
            domain_regex = re.findall("//([^/]*)", self.url)
            if domain_regex:
                print("Base domain : %s" % domain_regex[0])
                self.url = domain_regex[0]
            else:
                print "[Error] Url Format : http://site.com/"
                return

        if self.go_outside:
            print "Checking base domain..."
            domain_regex = re.findall("//([^/]*)", self.url)
            if domain_regex:
                if domain_regex[0] != self.url:
                    print "Different domain ! Skipping."
                    return

        if self.url in self.nodes:
            print("Node : %s already crawled." % self.url)
            return

        print("Crawling : %s" % self.url)
        url_data = self.extract()
        self.nodes.append(self.url)

        if url_data and "Links" in url_data:
            for k in url_data["Links"]:
                print("Found link : %s" % k)
                if self.depth >= depth:
                    self.url = k
                    self.crawl(depth + 1)
                else:
                    print "Max depth."

        for k in self.nodes:
            self.dictionary[compteur] = k
            compteur += 1

    def save(self, path="results"):
        for j in range(0, len(self.dictionary)):
            self.name = re.sub("([\/\.:#]*)", '',  self.dictionary[j])
            file = open(path + "//" + self.name + ".json", "w")
            file.write(self.dictionary[j])
            file.close()

    def load(self, path):
        print path

