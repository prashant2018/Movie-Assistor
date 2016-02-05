# Movie Assistor - This script scans the directory for movies and returns the ratings and riviews in a spreadsheet.

import os
import guessit
import threading
import pyperclip
import sys

# List of all possible video formats 
name_list = ["webm","mkv","flv","vob","ogv","ogg","drc","gif","gifv","mng","avi","moc","qt","wmv","yuv","rm","rmvb","asf",
			 "mp4","m4p","m4v","mpg","mp2","mpe","mpeg","m2v","svi","3gp","3g2","mxf","roq","nsv","f4p","f4a","f4b"]

movie_names = []

# path of directory is stored here
dir_path = "hi"

# Input of directory path
def input_directory():
	
	if len(sys.argv) == 1:
		print("Copy folder's path and paste here : ")
		dir_path = input()
	else:
		dir_path = pyperclip.paste()

	if os.path.exists(dir_path):
		os.chdir(dir_path)
		#print(os.getcwd())
	else:
		print("Directory Does Not Exists")
		return 999

# movie name extracting
def movie_title(item):
	
	title = ""
	
	if "sample" in item.lower():
		return ""	
	try:
		data = guessit.guessit(item)
	except:
		return ""
		
	try:
		extension = data['container']
	except:
		return ""
		
	if extension in name_list:
		try:
			title = data['title']
		except:
			title = ""
	return title

# Walkthrough all movie folders
def walk_dir():
	title=""
	
	for	folderName,	subfolders,	filenames in os.walk(os.getcwd()):
		for	filename in	filenames:
			title = movie_title(filename)
			if title != "":
				movie_names.append(title)

#finally calling and displaying for testing purpose
def func_call():
	input_directory()
	#print(dir_path)
	walk_dir()	
	
	for name in movie_names:
		print(name)

func_call()