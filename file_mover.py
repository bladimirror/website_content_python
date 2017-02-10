#!/usr/bin/python
'''
This script moves the saved webpage data files (see images variable) based
on file type to specific folders (see asset_folders).  The 
folders (see asset_folders) are based on a Ruby Webapp structure.
'''

import fnmatch
import os

images = ['*.png', '*.gif', '*.js', '*.css', '*.html']
asset_folders = ['images', 'images', 'javascripts', 'stylesheets', 'views']
data_folders = ["01_web_fundamentals", "02_python", "03_ruby_on_rails", "04_mean", "05_ios"]
count = 0

#Walks through data_folder array
for data in data_folders:
	## FILES ##
	#Walks into each parent folder to move files
	for root, dirnames, filenames in os.walk("/Users/Bladmirror/Desktop/webscrapped_data/raw-html-data/%s" %data):
			root_head, root_tail = os.path.split(root)
			sub_head, sub_tail = os.path.split(root_head)

			for i in range(0,5):
				for filename in fnmatch.filter(filenames, images[i]):
					docfile = os.path.join(root, filename)
					path, filename = os.path.split(docfile)
					os.rename(docfile, "/Users/Bladmirror/Desktop/webscrapped_data/separated-html-files/%s/%s" %(asset_folders[i],filename))
					count += 1
			print "%s File(s) moved..." %count

'''
## SUBFOLDERS ##
#Counts number of directories in data_folder element
for root, dirs, files in os.walk("/Users/Bladmirror/Desktop/webscrapped_data/%s" %data):
	subfolder_count += len(dirs)
#Concatenates subfolder filename
parentFile = data.split("_", 1)
for i in range(0, subfolder_count+1):
	if i < 10:
		subfolder = "0%s_%s_files" %(i, parentFile[1])
	else:
		subfolder = "%s_%s_files" %(i, parentFile[1])
	#Walks into each sub_folder to move files
	for root, dirnames, filenames in os.walk("/Users/Bladmirror/Desktop/webscrapped_data/%s/%s" %(data, subfolder)):
		for i in range(0,5):
			for filename in fnmatch.filter(filenames, images[i]):
				docfile = os.path.join(root, filename)
				path, filename = os.path.split(docfile)
				os.rename(docfile, "/Users/Bladmirror/Desktop/webscrapped_data/%s/%s" %(asset_folders[i],filename))	
print "%s file(s) moved" %data

Files can be moved to specific folders.

Next step is to create sub-folders within each asset_folder 
for each track and then for each lesson.  This is needed because each track will have
it's own controller and routing file.

You should move two lessons and play around on how to properly link the files.
Once you get that working it will give you a better idea as to how to write the remaing script

Consider making the routes in Ruby variables example XX + filename 

'''	
