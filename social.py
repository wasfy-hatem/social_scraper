import sys
import jsonpickle
#import json
import simplejson as json

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


base_url            = "https://github.com/search?q="
ending_url          = "+in:email&type=Users"
email = sys.argv[1] #input from outside
#email               = "ha_wasfy@yahoo.com"
result_start_url    = "https://github.com"
site_url =  base_url + email + ending_url

#info_by_user_name = "https://api.github.com/users/hatemwasfy"
#https://api.github.com/search/users?q=ha_wasfy@yahoo.com


print("-------------------------------------------------------")
print("email is: ", email)
print("site URL is: ", site_url)
print("-------------------------------------------------------")

try:
	read = urlopen(site_url).read()
	#print (" Title Of the Site Is : " + title)
	soup = BeautifulSoup(read, 'html.parser')
	####print (soup.title.get_text()) ## Example For Title
	# <p class="count">12</p>
	mydivs_class_is_count       =  soup.find_all("div", class_="user-list-item f5 py-4 d-flex")
	a_tags                      =  mydivs_class_is_count[0].find_all("a")

	results                     =  a_tags[0].text  #each page takes 20 result as fixed system

	github_user_name = a_tags[0]["href"] # result example is: /hatemwasfy

	user_github_account = result_start_url + github_user_name
except:
	user_github_account = "Not found"
#print("Results are: ", results)
print("Github account is: ", user_github_account)

