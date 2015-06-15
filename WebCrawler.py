__author__ = 'Ismaïl NGUYEN'
import re
import requests
from bs4 import BeautifulSoup

class WebCrawler:
	nodes = []
	name = {}
	dictionary = {}
	url = ""
	goOutside = False
	depth = 0
	
	def __init__(self, url, goOutside=True, depth=2):
		self.url = url
		self.goOutside = goOutside
		self.depth = depth
		

	def extract():
		_soup = BeautifulSoup(requests.get(self.url).text)
		_match = "http"
		_dictionary = {}
		
		for _title in _soup.find_all("title"):
			_dictionary["Titre"] = _title

		for _metaDescriptionMin in _soup.find_all('meta', attrs={"name": "description"}):
			_dictionary['Description'] = _metaDescriptionMin.get('content')

		for _metaDescriptionMaj in _soup.find_all('meta', attrs={"name": "Description"}):
			_dictionary['Description'] = _metaDescriptionMaj.get('content')

		for _metaKeywords in _soup.find_all('meta', attrs={"name": "keywords"}):
			_dictionary['Keyword'] = _metaKeywords.get('content')

		for _metaKeyword in _soup.find_all('meta', attrs={"name": "keyword"}):
			_dictionary['Keyword'] = _metaKeyword.get('content')

		_dictionary['Links'] = []

		for a in _soup.find_all('a', href=True):
			if _match in a.get('href'):
				_dictionary['Links'].append(a.get('href'))

		return _dictionary


	def start(depth=0):
		_compteur = 0

		if not self.url:
			print("Computing base domain ...")
			_domainRegex = re.findall("//([^/]*)", self.url)
			if _domainRegex:
				print("Base domain : %s" % _domainRegex[0])
				self.url = _domainRegex[0]
			else:
				print("[Error] Url Format : http://site.com/")
				return

		if not self.goOutside:
			print("Checking base domain...")
			_domainRegex = re.findall("//([^/]*)", self.url)
			if domainRegex:
				if _domainRegex[0] != self.url:
					print("Different domain ! Skipping.")
					return

		if self.url in self.nodes:
			print("Node : %s already crawled." % self.url)
			return

		print("Crawling : %s" % self.url)
		_urlData = self.extract()
		self.nodes.append(self.url)

		if _urlData and "Links" in _urlData:
			for k in _urlData["Links"]:
				print("Found link : %s" % k)
				if self.depth >= depth:
					self.url = k
					self.start(depth + 1)
				else:
					print("Max depth.")

		for k in self.nodes:
			self.dictionary[_compteur] = k
			_compteur += 1

	def save(path):
		for j in range(0, len(self.dictionary)):
			self.name = re.sub("([\/\.:#]*)", '',  self.dictionary[j])
			file = open(path + "//" + self.name + ".json", "w")
			file.write(self.dictionary[j])
			file.close()

	def load(path):
		print(path)