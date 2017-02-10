#!/usr/bin/python
'''
This script uses beautifulsoup to pull specific data from a 
saved webpage.  The data is then repacked using a generic
html and CSS page I created.  This script also creates the Ruby
routes file, methods file, and links the generated htmls to each
other
'''

#Allows for script to change directory
import os, sys, re

#Calls beautifulsoup Module
from bs4 import BeautifulSoup

all_html_files = []
title = ""
chapter_array = []
lesson_array = []
lesson_tag = ""
sidebar_arr = []
sidebar_count = 0

#Opens html file
#have this read all-html-filenames.txt
with open("/Users/Bladmirror/Desktop/Coding/coding_dojo_test/sidebar/all-html-filenames.txt", "r+") as txt:
  for line in txt:
    all_html_files.append(line.strip(",,,,,\r\n"))

print "File list loaded..."

#This soup contains the main content

#Left off here.  creating opening files

for filelist in all_html_files:
  soup = BeautifulSoup(open("/Users/Bladmirror/Desktop/Coding/coding_dojo_test/separated-html-files/views/%s" %filelist), "lxml")
  section = soup.find_all('section')

  #This soup contains the track titles
  soup = BeautifulSoup(open("/Users/Bladmirror/Desktop/Coding/coding_dojo_test/separated-html-files/views/%s" %filelist), "html5lib")
  chapter_soup = soup.find_all("h3")
  lesson_soup = soup.find_all("h4")
  title_soup = soup.find_all("title")

  title = title_soup[0].string
  print "Soup prep complete..."

  #This soup contains chapter titles
  for i in range(0, len(chapter_soup)):
    try:
      if i < len(chapter_soup):
        chapter_temp_name = str(chapter_soup[i].span.string)
        chapter_array.append(chapter_temp_name)
      else:
        continue
    except AttributeError:
      continue
  print "Chapter soup is done..."


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

  #Creates sidebar
  #for text_file in text_array:
  if sidebar_count == 0:
    with open("/Users/Bladmirror/Desktop/Coding/coding_dojo_test/sidebar/02_python - 01_django.txt", "r+") as txt:
      for line in txt:
        sidebar_arr.append(line.strip("\r\n"))
    print sidebar_arr

    for i in sidebar_arr:
      lesson_string = """<li class="list-group-item">%s</li>""" %i
      lesson_tag = lesson_tag + lesson_string
      lesson_string = ""
    sidebar_count += 1
    print "Lesson sidebar is done...%s" % lesson_tag
  else:
    pass


  #[IN PROGRESS] This will link pages together to one another.
  #Need to create script that will pull all titles from all files by track
  #Need to create script that will create route file + method file
  '''
  Test converting finished file to a text file and searching for the "account modal" data
  then deleting it.  Then convert the file to HTML
  '''

  '''
  """<form class="form-horizontal" action='/%s'>
  <input name="authenticity_token" value="<%= form_authenticity_token %>" type="hidden">
  <input class="btn btn-primary" type='submit' value='%s' />
  </form>""" #% (title, title)
  '''

  #Creates HTML file
  html_file01 = """<!DOCTYPE html> <html lang="en" media="screen"> <head> <meta name="viewport" content="width=device-width, initial-scale=1.0" http-equiv="Content-Type"> <title>""" 
  html_file02 = str(chapter_array[1] + " - " + chapter_array[0])
  html_file03 = """</title><!-- Latest compiled and minified CSS --> <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous"> <!-- Optional theme --> <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous"> <!-- CSS File <link rel="stylesheet", href="/assets/test.css"> --> <link rel="stylesheet", href="test.css"> <!--GOOGLE FONTS CSS--> <link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet"> </head> <body> <div id="container"> <ul class="nav nav-tabs navbar-fixed-top"> <li role="presentation" class="active"><a href="#">Dashboard</a></li> <li role="presentation" class="disabled"><a href="#">Track Name: """
  html_file04 = str(chapter_array[1] + " - " + chapter_array[0])
  html_file05 = """</a></li></ul><div class="sidebar"><ul class="list-group">"""
  html_file06 = str(lesson_tag)
  html_file07 = """</ul></div><div class="soup_content">"""
  html_file08 = str(section[0])
  html_file09 = """</div></div> </body></html>"""

  html_file = html_file01 + html_file02 + html_file03 + html_file04 + html_file05 + html_file06 + html_file07 + html_file08 + html_file09
  print "HTML stew is done..."


  #Writing to file
  os.chdir("/Users/Bladmirror/Desktop/Coding/coding_dojo_test/completed-html/")
  txt = open("/Users/Bladmirror/Desktop/Coding/coding_dojo_test/completed-html/%s - %s.html" %(chapter_array[1], chapter_array[0]), "wb+")
  txt.seek(0,2)
  txt.write("%s" %html_file)
  txt.close()
  print "HTML File created..."



