#!/usr/bin/python
'''
This script walks through an HTML file and 
searches and changes specific HTML links.
Original purpose was to change html links
to different links of my choosing.  The link
paths were too variable so this approach did not work.
'''

import re, os

file_string = ""
fileLink_sub = ""
dashboard_sub = ""
new_filename = ""
asset_filenames = []
html_files = []

#Opens html file(s) to be modified
#images = ['*.png', '*.gif', '*.js', '*.css', '*.html']
asset_folders = ['images', 'javascripts', 'stylesheets']
html_folder = 'views'
subfolder_count = 0
parentFile = ""

#Walks through data_folder array
for data in asset_folders:
	## FILES ##
	#Walks into each parent folder to move files
	for root, dirnames, filenames in os.walk("/Users/Bladmirror/Desktop/coding_dojo_test/%s" %data):
		asset_filenames = filenames
	for root, dirnames, filenames in os.walk("/Users/Bladmirror/Desktop/coding_dojo_test/%s" %html_folder):
		html_files = filenames
	for html_file in html_files: #filenames is an Array of all files in the folder
		with open(html_file, "wb+") as filename:
			## FILES ##
			#Walks into each parent folder to move files
			#for root, dirnames, filenames in os.walk("/Users/Bladmirror/Desktop/coding_dojo_test/%s" %data):
			for asset_file in asset_filenames:
				#Counts number of directories in data_folder element
				subfolder_count += len(dirnames)
				#Concatenates subfolder filename
				parentFile = data.split("_", 1)
				for i in range(0, subfolder_count):
					if i < 10:
						new_filename = "0%s_%s_files" %(i, parentFile[1])
					else:
						new_filename = "%s_%s_files" %(i, parentFile[1])

				fileLink_sub = re.sub('https?:[;\/?\\@&=+$,\[\]A-Za-z0-9\-_\.\!\~\*\'\(\)%][\;\/\?\:\@\&\=\+\$\,\[\]A-Za-z0-9\-_\.\!\~\*\'\(\)%#]*|[KZ]:\\*.*\w+', new_filename, filename)
				dashboard_sub = re.sub('https?:[;\/?\\@&=+$,\[\]A-Za-z0-9\-_\.\!\~\*\'\(\)%][\;\/\?\:\@\&\=\+\$\,\[\]A-Za-z0-9\-_\.\!\~\*\'\(\)%#]*|[KZ]:\\*.*\w+', """student_dashboard.html""", filename)
				
				#link_search = re.findall('https?:[;\/?\\@&=+$,\[\]A-Za-z0-9\-_\.\!\~\*\'\(\)%][\;\/\?\:\@\&\=\+\$\,\[\]A-Za-z0-9\-_\.\!\~\*\'\(\)%#]*|[KZ]:\\*.*\w+', file_string)	
				#filename.write(file_sub)	
				#print file_sub

			filename.close()

'''
Need to go into view folder and then walk through
each sub-folder modifying the html links based on the lesson 
name

Need to also change html links to images, js, css.  Currently linking to different folder.

1st pass: Search of HTML file for filename.  Replace filename with link to images
'''