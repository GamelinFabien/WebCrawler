__author__ = 'Fabien GAMELIN, Ismaïl NGUYEN, Bruno VACQUEREL'
import WebCrawler

if __name__ == "__main__":
	
	print("URL : ")
	urlInput = input()
	
	print("Depth : ")
	depthInput = input()
	
	print("Go outside ? ([o]/n)")
	outsideInput = input()
	
	crawler = WebCrawler(urlInput, False if input() == 'n' else True, depthInput)
	crawler.start()

	print("Dictionary : ", crawler.dictionary)
	
	print("Save the crawling ? (o/[n]) : ")
	if input() == 'o':
		print("Folder : ")
		crawler.save(input())

	print("Charge the crawling ? (o/[n]) : ")
	if input() == 'o':
		print("Folder : ")
		crawler.load(input())