# -*- coding: cp1252 -*-
"""WebCrawler - ESGI 3A AL 2014/2015"""
__author__ = 'Fabien GAMELIN, Ismail NGUYEN, Bruno VACQUEREL'
import re
import requests
from bs4 import BeautifulSoup

class WebCrawler(object):
    """Classe permettant de crawler une URL fournie"""
    nodes = []
    name = {}
    dictionary = {}
    url = ''
    go_outside = False
    depth = 0

    def __init__(self, url='http://www.nguyenismail.com/', go_outside=True, depth=2):
        """Initialisation des variables globales"""
        self.url = url
        self.go_outside = go_outside
        self.depth = depth
        print "l'url donne est %d" % self.depth


    def extract(self):
        """Extraction des données de l'url"""
        print "l'url prsente est %s" % self.url
        req = requests.get("http://" + self.url).text
        soup = BeautifulSoup(req)
        match = "http"
        dictionary = {}

        for title in soup.find_all("title"):
            dictionary["Titre"] = title

        for meta_description_min in soup.find_all('meta', attrs={"name": "description"}):
            dictionary['Description'] = meta_description_min.get('content')

        for meta_description_maj in soup.find_all('meta', attrs={"name": "Description"}):
            dictionary['Description'] = meta_description_maj.get('content')

        for meta_keywords in soup.find_all('meta', attrs={"name": "keywords"}):
            dictionary['Keyword'] = meta_keywords.get('content')

        for meta_keyword in soup.find_all('meta', attrs={"name": "keyword"}):
            dictionary['Keyword'] = meta_keyword.get('content')

        dictionary['Links'] = []

        for link in soup.find_all('a', href=True):
            if match in link.get('href'):
                dictionary['Links'].append(link.get('href'))

        return dictionary

    def crawl(self, depth=2):
        """Parcours des urls"""
        compteur = 0

        if self.url:
            print "Computing base domain ..."
            domain_regex = re.findall("//([^/]*)", self.url)
            if domain_regex:
                print "Base domain : %s" % domain_regex[0]
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
            print "Node : %s already crawled." % self.url
            return

        print "Crawling : %s" % self.url
        url_data = self.extract()
        self.nodes.append(self.url)

        if url_data and "Links" in url_data:
            for k in url_data["Links"]:
                print "Found link : %s" % k
                if self.depth >= depth:
                    self.url = k
                    self.crawl(depth + 1)
                else:
                    print "Max depth."

        for k in self.nodes:
            self.dictionary[compteur] = k
            compteur += 1

    def save(self, path="results"):
        """Sauvegarde des resultats"""
        for j in range(0, len(self.dictionary)):
            self.name = re.sub(r"([\/\.:#]*)", '', self.dictionary[j])
            file_object = open(path + "//" + self.name + ".json", "w")
            file_object.write(self.dictionary[j])
            file_object.close()

    def load(self, path):
        """Chargement des resultats"""
        print path
        print self.url

