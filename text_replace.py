#!/usr/bin/python
'''
This script takes a newly created text file which contains
the HTML code and removes all content extra content except
for the programming material.

NOTE:  Need to clean up and add to Promordial HTML Soup Script.
'''

test_arr = []
new_file = ""

with open('/Users/Bladmirror/Desktop/Coding/coding_dojo_test/completed-test-files/test.txt', 'r') as f:
	content = f.read()
	startrange_01 = content.index('<!-- Modal Inactivity Notice Modal -->')
	endrange_01 = content.index('<!-- end of My Account Modal  -->')
	startrange_02 = content.index('<a class="unload_link" href="http://learn.codingdojo.com/dashboard">\n<span class="glyphicon glyphicon-th-large"></span><span>Home</span>\n</a>')
	endrange_02 = startrange_02 + 141
f.close()
print "File read..."
print "Ranges set..."

for line in content:
	test_arr.append(line)	

for i in range(startrange_01, endrange_01):
	test_arr[i] = ""
print "Inactivity module deleted..."

for y in range(startrange_02, endrange_02):
	test_arr[y] = ""
print "Home button deleted..."

arraylength = len(test_arr)-(endrange_01 - startrange_01)

for x in range(0, arraylength):
	new_file += test_arr[x]
print "HTML array complete..."

txt = open("/Users/Bladmirror/Desktop/Coding/coding_dojo_test/completed-test-files/new_file.txt", "wb+")
txt.write(new_file)
txt.close()
print "HTML file complete..."

