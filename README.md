#WebCrawler

##Authors
- Fabien GAMELIN
- Ismail NGUYEN
- Bruno VACQUEREL


##Description
Le WebCrawler permet d'indexer automatiquement les pages Web à partir d'un URL donné.
Il va parcourir tous les liens présents sur chaque page et les parcourir un à un.
Ces liens seront ensuite stockés sous format JSON.


##Modules
- re
- request
- bs4


##Functions
##extract
extract all web links with depth searching from a specific url given in parameters

###crawl
create a dictionary with all links

###save
save the dictionary of crawled links

###load
load a saved dictionary of crawled links
