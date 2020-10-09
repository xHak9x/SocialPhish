#!/bin/python3
#Contact me on Github - github.com/Vickyarts
import sys
import os
try:
	from selenium import webdriver
	from bs4 import BeautifulSoup
except ModuleNotFoundError:
	print('(Visit http://127.0.0.1:4040/status to get your link manually)')
	os.system('apt install pip > /dev/null 2>&1 ')
	os.system('pip install selenium bs4 > /dev/null 2>&1')
	sys.exit()

ngrok = 'http://127.0.0.1:4040/status'

def remove_scripts(soup):
  [s.extract() for s in soup('script')]

def getlink(page):
	try:
		site = BeautifulSoup(page,'lxml')
		remove_scripts(site)
		links = site.find('tr')
		link = links.text
	except Exception:
		print('Visit http://127.0.0.1:4040/status to get your link manually')
	else:
		return link[3:]

def getpage(url):
	try:
		try:
			driver = webdriver.Chrome()
		except Exception:
			try:
				driver = webdriver.Firefox()
			except Exception:
				pass
		driver.get(ngrok)
	except Exception:
		print('(Visit http://127.0.0.1:4040/status to get your link manually) or install webdriver)')
	else:
		htmlpage = driver.page_source
		driver.close()
		link = getlink(htmlpage)
		return link
	
def run():
	if __name__ == "__main__":
		link = getpage("http://127.0.0.1:4040/status")
		if link != None:
			print(link)

run()
