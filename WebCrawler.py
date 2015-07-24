# -*- coding: utf_8 -*-
"""WebCrawler - ESGI 3A AL 2014/2015"""
__author__ = 'Fabien GAMELIN, Ismail NGUYEN, Bruno VACQUEREL'
import re
import json
import os
import requests
from bs4 import BeautifulSoup

class WebCrawler(object):
    """Classe permettant de crawler une URL fournie"""
    nodes = []
    dictionary = {}
    url = ''
    go_outside = False
    depth = 0
    input_dictionary = None
    keyword = None
    output = None

    def __init__(self, url, depth=2, go_outside=True, output="resutlts"):
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
            domain_regex = re.findall("//([^/]*)", self.url)
            if domain_regex:
                self.url = domain_regex[0]
            else:
                print "Error: Bad url (Expected url format : http://site.com/)"
                return

        if self.go_outside:
            domain_regex = re.findall("//([^/]*)", self.url)
            if domain_regex:
                if domain_regex[0] != self.url:
                    return

        if self.url in self.nodes:
            return

        print "Crawling : %s" % self.url
        url_data = self.extract()
        self.nodes.append(url_data)

        if url_data and "Links" in url_data:
            for k in url_data["Links"]:
                #print "Found link : %s" % k
                if self.depth >= depth:
                    self.url = k
                    self.crawl(depth + 1)

        for k in self.nodes:
            self.dictionary[compteur] = k
            compteur += 1

    def extract(self):
        """Extraction des données de l'url"""
        req = requests.get("http://" + self.url).text

        soup = BeautifulSoup(req)
        dictionary = {}

        dictionary["Url"] = self.url
        dictionary["Title"] = soup.find("title").text

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
        if not os.path.isdir(self.output):
            os.makedirs(self.output)

        for j in range(0, len(self.nodes)):
            name = re.sub(r"([\/\.:#]*)", '', self.dictionary[j]["Url"])
            file_object = open(self.output + '/' + name + ".json", "w")
            json.dump(self.nodes[j], file_object, indent=4)
            file_object.close()

    def load(self):
        """Chargement des resultats"""
        matches = []
        for item in os.listdir(self.output):
            if os.path.isfile(os.path.join(self.output, item)):
                matches.append(json.load(open(self.output + '/' + item)))
        return matches

