#!/usr/bin/python
'''
This is a "whiteboard" script where I tested certain
functions.  This script may or may not work.
'''

import os, sys, fnmatch, re

images = ['*.js', '*.css', '*.png', '*.html']
matches = []
file_string = ""
file_sub = ""
dash_sub = ""

# Finds path for HTML file to be modified
for root, dirnames, filenames in os.walk("/Users/Bladmirror/Desktop/coding_dojo_test/css"):
	for extensions in images:
		for filename in fnmatch.filter(filenames, extensions):
			matches.append(os.path.join(root, filename))

#print matches

# Opens and reads HTML
with open('test.html', "r+") as filename:
	#for line in filename:
	file_string = filename.read()
	filename.close()

#Sort of works now.  Need to refine it
with open('test.html', "wb+") as filename:
	file_sub = re.sub('https?:[;\/?\\@&=+$,\[\]A-Za-z0-9\-_\.\!\~\*\'\(\)%][\;\/\?\:\@\&\=\+\$\,\[\]A-Za-z0-9\-_\.\!\~\*\'\(\)%#]*|[KZ]:\\*.*\w+', """01_intro_to_swift.html""", file_string)
	dash_sub = re.sub('https?:[;\/?\\@&=+$,\[\]A-Za-z0-9\-_\.\!\~\*\'\(\)%][\;\/\?\:\@\&\=\+\$\,\[\]A-Za-z0-9\-_\.\!\~\*\'\(\)%#]*|[KZ]:\\*.*\w+', """student_dashboard.html""", file_string)
	
	#link_search = re.findall('https?:[;\/?\\@&=+$,\[\]A-Za-z0-9\-_\.\!\~\*\'\(\)%][\;\/\?\:\@\&\=\+\$\,\[\]A-Za-z0-9\-_\.\!\~\*\'\(\)%#]*|[KZ]:\\*.*\w+', file_string)	
	#filename.write(file_sub)	
	#print file_sub
	filename.close()

'''
<form class="form-horizontal" action='/logout'>
	<input name="authenticity_token" value="<%= form_authenticity_token %>" type="hidden">
	<input class="btn btn-primary" type='submit' value='Log Out' />
</form>

#Next Button
<a href="http://learn.codingdojo.com.*$" class="btn btn-primary next_button_link unload_link">
	Next
	<span class="glyphicon glyphicon-chevron-right"></span>
</a>

#Previous Button
<a href="http://learn.codingdojo.com.*$" class="btn btn-primary previous_button_link unload_link">
	<span class="glyphicon glyphicon-chevron-left"></span>
	Previous
</a>

#Sidebar menu links
<a class="tab_title unload_link" href="http://learn.codingdojo.com.*$">
	<div class="tab_label"><span class="tab_icon"></span></div>
	
	#Sidebar Title
	<span class="tab_details" id="quiz_id_17214">
		<h4>Overview</h4> <!-- % if contents["type"] == QUIZ_MODULE % -->
	</span>
</a>

#Some HTML files have already been modified
<a href="02_html.html" class="btn btn-primary next_button_link unload_link">
	<span class="glyphicon glyphicon-chevron-right"></span>
</a>
'''