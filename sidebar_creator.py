#!/usr/bin/python
'''
This script uses beautifulsoup to pull specific data from a 
saved webpage and puts all the lesson names for a module from 1 html file and creates
a text file with the data, which can then be used to create the sidebar in
the primordial_html_soup.py (creates html page) file.
'''

import fnmatch
import os

# Calls beautifulsoup Module
from bs4 import BeautifulSoup

images = ['*.html']
data_folders = ["01_web_fundamentals", "02_python", "03_ruby_on_rails", "04_mean", "05_ios", "06_post_bootcamp"]
lesson_soup = ""
lesson_array = []

#Walks through data_folder array
for data in data_folders:
	## FILES ##
	#Walks into each parent folder to move files
	for root, dirnames, filenames in os.walk("/Users/Bladmirror/Desktop/coding_dojo_test/raw-html-data/%s" %data):
		root_head, root_tail = os.path.split(root)
		sub_head, sub_tail = os.path.split(root_head)

		#Only searches for 1 html file for the module
		for filename in fnmatch.filter(filenames, images[0]):
			if filename.lower().endswith(".html") and filename.split("_", 1)[0] == "01":
				soup = BeautifulSoup(open("%s/%s" %(root, filename)), "html5lib")
				lesson_soup = soup.find_all("h4")

				#This soup contains lesson titles
				for i in range(0, len(lesson_soup)):
				  try:
				    if i < len(lesson_soup):
				      lesson_temp_name = str(lesson_soup[i].string)
				      lesson_array.append(lesson_temp_name)
				    else:
				      continue
				  except AttributeError:
				    continue
				print "Lesson soup is done..."

				#Writing to file
				os.chdir("/Users/Bladmirror/Desktop/coding_dojo_test/sidebar/")
				txt = open("/Users/Bladmirror/Desktop/coding_dojo_test/sidebar/%s - %s.txt" %(data, filename.split(".", 1)[0]), "wb+")
				for i in lesson_array:
					txt.seek(0,2)
					txt.write("%s\n" %i)
				txt.close()
				lesson_array = []

	print "Title Text File created..."

