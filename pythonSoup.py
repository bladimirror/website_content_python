#!/usr/bin/python
'''
This script uses beautifulsoup to pull specific data from a 
saved webpage. 
'''

#Allows for script to change directory
import os, sys, re

# Calls beautifulsoup Module
from bs4 import BeautifulSoup

#This soup contains the main content
soup = BeautifulSoup(open("/Users/Bladmirror/Desktop/coding_dojo_test/test.html"), "lxml")
section = soup.find_all('section')

#This soup contains the track titles
soup = BeautifulSoup(open("/Users/Bladmirror/Desktop/coding_dojo_test/views/05_python.html"), "html5lib")
chapter_soup = soup.find_all("h3")
lesson_soup = soup.find_all("h4")
title_soup = soup.find_all("title")

title = title_soup[0].string
chapter_array = []
lesson_array = []

#This soup contains chapter titles
for i in range(0, len(chapter_soup)):
	print "Chapter Loop"
	try:
		if i < len(chapter_soup):
			chapter_temp_name = str(chapter_soup[i].span.string)
			chapter_array.append(chapter_temp_name)
		else:
			continue
	except AttributeError:
		continue

#This soup contains lesson titles
for i in range(0, len(lesson_soup)):
	print "Lesson Loop"
	try:
		if i < len(lesson_soup):
			lesson_temp_name = str(lesson_soup[i].string)
			lesson_array.append(lesson_temp_name)
		else:
			continue
	except AttributeError:
		continue