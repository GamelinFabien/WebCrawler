# -*- coding: utf_8 -*-
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
    input_dictionary = None
    keyword = None
    output = None

    def __init__(self, url, depth=2, go_outside=True, output="results"):
        """Initialisation des variables globales"""
        self.url = url
        self.go_outside = go_outside
        self.depth = depth
        self.output = output

    #def __init__(self, input_dictionary, keyword):
        #self.input_dictionary = input_dictionary
        #self.keyword = keyword

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
                print "Error: Bad url (Expected url format : http://site.com/)"
                return

        if self.go_outside:
            print "Check if local domain"
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

    def extract(self):
        """Extraction des données de l'url"""
        req = requests.get("http://" + self.url).text
        soup = BeautifulSoup(req)
        dictionary = {}

        dictionary["Title"] = soup.find("title")

        description = soup.findAll("meta", attrs={"name": "description"})
        if description == []:
            dictionary['Description'] = "No description"
        else:
            dictionary['Description'] = description[0]["content"].encode("utf-8")

        keywords = soup.findAll("meta", attrs={"name": "keywords"})
        if keywords == []:
            dictionary["Keywords"] = "No description"
        else:
            dictionary["Keywords"] = keywords[0]["content"].encode("utf-8")

        dictionary['Links'] = []

        for link in soup.findAll("a", attrs={"href":True}):
            if link["href"].find("http://") > 0 or link["href"].find("www.") > 0:
                dictionary['Links'].append(link["href"])

        return dictionary

    def save(self):
        """Sauvegarde des resultats"""
        for j in range(0, len(self.dictionary)):
            self.name = re.sub(r"([\/\.:#]*)", '', self.dictionary[j])
            file_object = open(self.output + "//" + self.name + ".json", "w")
            file_object.write(self.dictionary[j])
            file_object.close()

    def load(self):
        """Chargement des resultats"""
        #list_url = []
        file_object = open(self.input_dictionary)
        # lire le contenu de file_object
        # parser et comparer avec self.keyword
        # si self.keyboard apparait dans le title, description,
        #ou mots keywords du dictionaire de l'url
        # ajouter cet url à list_url => list_url.append(url_found)
        file_object.close()

