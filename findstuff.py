from bs4 import BeautifulSoup, SoupStrainer
from time import time

import threading
import requests
import lxml




BASIC_URL = "https://replit.com/@"

class User():
	def __init__(self, cycles, bio, name, hacker):
		self.cycles = cycles
		self.bio = bio
		self.name = name
		self.hacker = hacker
	def display_data(self):
		green = '\033[92m'
		clear = '\033[0m'
		print(f"Name: {green}{self.name}{clear}")
		print(f"Cycles: {green}{self.cycles}{clear}")
		print(f"Bio: {green}{self.bio}{clear}")
		print(f"Hacker: {green}{self.hacker}{clear}")


class LeaderBoard():
	def __init__(self, leaderboard):
		self.leaderboard = leaderboard
	
	def placing(self, user):
		if user not in self.leaderboard:
			return None
		else:
			return self.leaderboard.index(user)+1

def find_user(username):
	try:
		page = requests.get(BASIC_URL+username)


		## This is the stuff that is slow


		soup = BeautifulSoup(page.text, 'lxml', parse_only=SoupStrainer(['span', 'h1']))

		## The other stuff takes just a fraction of a second



		userdata = User(None, None, None, None)

		def findCycles():
			try:
				userdata.cycles = soup.find(title='cycles').text.strip().replace("(", "").replace(")", "")
			except:
				pass
		
		def findBio():
			try:
				userdata.bio = soup.find(class_="Linkify").text.strip()
			except:
				pass

		def findName():
			try:
				userdata.name = soup.find("h1", class_="heading").text.strip()
			except:
				pass

		def findHacker():
			try:
				hacker = soup.find(class_="hacker").text.strip()
				if hacker == 'hacker':
					userdata.hacker = True
				else:
					userdata.hacker = False
			except:
				userdata.hacker = False


		threading.Thread(target=findCycles).start()
		threading.Thread(target=findBio).start()
		threading.Thread(target=findName).start()
		threading.Thread(target=findHacker).start()

		return userdata
	except:
		return False


def leaderboard(since):
	url = "https://replit.com/leaders?since="+since

	page = requests.get(url)

	soup = BeautifulSoup(page.text, 'lxml', parse_only=SoupStrainer(['a']))

	leaders = soup.find_all(class_="jsx-2250455014")
	leaders2 = soup.find_all(class_="jsx-801033477")

	data = []

	# terrible way to quick sort this stuff

	for i in leaders:
		if i.text in data:
			pass
		else:
			data.append(i.text)

	
	for i in leaders2:
		if i.text in data:
			pass
		else:
			data.append(i.text)

	bob = []


	for i in data:
		i = i.lower()
		for t in [char for char in i]:
			if t in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
				bob.append(i)
				break
	
	zed = []
	for i in bob:
		data = i.split("(")
		d = data[0]
		d = d.replace(' ', '')
		zed.append(d)
	return LeaderBoard(zed)
