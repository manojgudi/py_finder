
import subprocess as sp
import os
import gtk

def app_search(keyword):
	""" This function is used to query dpkg and return single relevant answer; In: single string, Out: Error Number or list of relevant search results(output_name_list) """
	# Check for blank keywords
	if keyword=="":
		print "blank keyword"
		
		# error code 0		
		return 0
	
	# Dynamic Array output
	output = []			# contains path(.desktop file) of all relevent search results
	output_name_list = []		# contains name of relevent search results
	icon_list = []  	# contains path of icons for relevent search results
	
	# Will run only if keyword is not null, search is indenpendent of case.
	path = "ls /usr/share/applications/*.desktop"
	p1 = sp.Popen(path, shell=True, stdout=sp.PIPE)
	list_of_files = p1.communicate()[0]
	
	# make it a list
	list_of_files = str2list(list_of_files)	
	
	# Search .desktop files for keyword	
	for i in list_of_files:
		p1 = sp.Popen(["cat", i], stdout=sp.PIPE)
		p2 = sp.Popen(["grep", "-i", keyword], stdin=p1.stdout, stdout=sp.PIPE)
		result = p2.communicate()[0]
		if result != "":
			output.append(i)
	
	# Format output names
	for i in output:
		name_with_ext = i.rpartition("/")[2]
		temp = name_with_ext.find(".desktop")
		
		# Saving Name without extension
		output_name_list.append(name_with_ext[:temp])
	
	print output_name_list
						
	for App_Name in output_name_list :
		icon_list.append(getIconPath (App_Name))
		
	# Kill earlier process pipe
	p1.kill()

	if output==[]:
		# No such application found error
		#error code 1
		return 1,1,1
	else:
		# Write this keyword to .data.xml
		recent_search_w(keyword,1)
		return output_name_list, output, icon_list
		


# On Double clicking app from search, this should be called:
def open_app(program_file):
	
	print program_file
	''' Function used to open app when tapping of relevant keyword; In: single string, Out: Success Number '''
	try:
		p1 = sp.Popen(["cat", program_file], stdout=sp.PIPE)
		p2 = sp.Popen(["grep","-m", "1", "Exec"], stdin=p1.stdout, stdout=sp.PIPE)
		program_name = p2.communicate()[0]
		
		# Removing "Exec="  "\n"  " %U"  strings which is in program_name string
		program_name=program_name.replace("Exec=","")
		program_name=program_name.replace("\n","")
		program_name=program_name[:program_name.find(" ")]
		
		print program_name
		
		sp.Popen([str(program_name)], shell=True)
			
		# success code 100
		program_output=100
	
	# Cannot Open Application
	except OSError: 
		program_output=1001
		print "Cannot Open Application"
	finally:
		return program_output
		

def search_file(keyword):
	'''Search function used to locate single file, In: String keyword, Out: list of all relevant path of keyword'''	
	if keyword=="":
		print "keyword cannot be null/blank"
		#error code 2
		return 2
	else:
		result = search_filesystem(keyword)
		if result == [None] :
			print "no such file found"
		else:
			return result

def search_filesystem(keyword) :
	
	raw_home = os.walk('/home/')
	raw_media = os.walk('/media/aakash/')

	fin_list = []
	
	"""This block of code will remove all hidden files and folders
	to remove the unncessary '/.' files and folders to be searched."""
	

	#Search in home folder
	for i in raw_home :
		#Search for hidden folders - remove all hidden folders.
		if '/.' not in i[0] :
			for j in i[1] :
			#removes all hidden folders at the root
				if '.' not in j :
					if keyword.upper() in j.upper() :
						fin_list.append(i[0] + '/' +j + '/')
			for k in i[2] :
			#removes all the hidden files at the root
				if not k.startswith('.') :
					#If the keyword is present then append
					if keyword.upper() in k.upper() :
						fin_list.append(i[0]+'/'+k)
							
	# delete unwated variables
	del(raw_home)

	#Search in media folder

	for i in raw_media :
		#Search for hidden folders - remove all hidden folders.
		if '/.' not in i[0] :
			for j in i[1] :
			#removes all hidden folders at the root
				if '.' not in j :
					if keyword.upper() in j.upper() :
						fin_list.append(i[0] + '/' +j + '/')
			for k in i[2] :
			#removes all the hidden files at the root
				if not k.startswith('.') :
					#If the keyword is present then append
					if keyword.upper() in k.upper() :
						fin_list.append(i[0]+'/'+k)
								
							
	del(raw_media)
	#Make it into a single list 
	
	# If fin_list is not Null, only then write keyword in xml
	if fin_list != []:
		print 'file_search_list is not null'
		recent_search_w(keyword,2)	
	return fin_list
		

	
# path_full = one element from output of search_file
def open_path(path_full):
	""" Tapping relevant search result invokes file explorer to open folder containing relevant file, In: Single string of full_path Out: Error/Success number """
	try:
		# remove file_name

		path=(str(path_full.rpartition("/")[0]))

		### REPLACE thunar with pcmanfm for lxde
		p1=sp.Popen(["pcmanfm", path])
		
		# success code 101
		return 101
	except: 
		#error code 3
		return 3


def get_xml_path():
	import os
	
	# Current Home Working directory
	home=os.getenv('HOME')
	path = home+'/.local/.data.xml'
	
	# If .data.xml exists in ~/.local then simply return path
	if os.path.exists(path) == True:
		print path
		return path
	else:
		print "First Run, copying .data.xml"
		first_run()
		return path
	
def first_run():
	# copy the .data.xml 
	import os
	import shutil
	
	home = os.getenv('HOME')
	dest_path = home+'/.local/.data.xml'
	src_path=os.getcwd()+'/.data.xml'
	print src_path
	
	shutil.copy(src_path,dest_path)
	print 'done'

# Called when 
def recent_search_r(mode):
	""" Reading the .data.xml file.
	If mode is 1, then it outputs apps_list else it outputs files_list	
	 In: Mode, Out: List of all values present in .recent_searches file"""
	try:
		import elementtree.ElementTree as et
	except:
		print "Please Run dep_install first"
	
	# Code Retriving
	try:	
		path = get_xml_path()
		print path
		tree = et.parse(path)
		print ".data.xml found"
	except:
		# User Process
		print ".data.xml not found..."
		print "First Run of User"

	# Defining variables
	apps_output = [None] * 5
	files_output = [None] * 5
	
	# global iterator
	global i
	i=0
	
	# Get root
	root = tree.getroot()
	
	# If mode passed to function is 1, then output_apps_list, else output_files_list
	if mode == 1:
		# Output apps list
		for apps in root:
			if apps.tag == 'apps':
				for gen in apps:
					if i<5 :
						apps_output[i]=gen.text
						i = i+1
		return apps_output

	else:	
		# Output file list
		# Reuse i global variable
		i=0
		for files in root:
			if files.tag == 'files':
				for gen in files:
					if i<5 :
						files_output[i]=gen.text
						i = i+1
		return files_output
				
	

	

def recent_search_w(result, mode):
	""" Called by other functions to write a successful result to .recent_searches.file; 
	result is the successful keyword, mode is to specify the keyword belongs to files section or apps section
	If mode = 1 => write for apps section, else write in file section
	In: Successful String Result from app_search()/file_search() and mode; Out: None  """
	
	apps_output=recent_search_r(1)
	files_output=recent_search_r(2)
	
	def update_list(any_list):
		# temp variable = any_list; NOTE we cannot directly copy list variable by temp_var=any_list, temp_var will act as reference
		temp_list=[None]*len(any_list)
		for j in range(len(any_list)):
			temp_list[j]=any_list[j]
		
		# If temp_list[0]!=result, only then update, else we will get repeated writing of values
		if temp_list[0]!= result:
			temp_list[0] = result
			for j in range(4):
				temp_list[j+1]=any_list[j]
			return temp_list				
		else: 
			return any_list 
		

	# Writing updated list to 
	def write(any_list, mode):
		try:
			import elementtree.ElementTree as et
		except:
			print "Please Run dep_install first"
		# XML path variable
		path = get_xml_path()

		# Code Retriving
		try:
			tree = et.parse(path)
			root = tree.getroot()
		except:
			print ".data.xml not found, exiting"
			exit()
		
		# Writing it to xml again according to mode
		if mode == 1:
			# Write it in <apps></apps>
			for apps in root:
				if apps.tag == 'apps':
					for i in range(len(any_list)):  # I Am assuming that length of any_list and <gen></gen> is same  = 5
						apps[i].text=any_list[i]
		else:
			# Write it in <files></files>
			for files in root:
				if files.tag == 'files':
					for i in range(len(any_list)):
						files[i].text=any_list[i]

		tree.write(path)	

	# If mode is 1, update apps_list, else update files_list
	if mode == 1:
		apps_output=update_list(apps_output)
		write(apps_output, mode)
		
	else :
		files_output=update_list(files_output)
		write(files_output, mode)	
	print "written to xml"

def str2list(str_var):
	""" Function to convert long formatted string of delimited (/n) to a list; In: Long Formatted List Out: List of elements """
	number_lines=str_var.count("\n")
	list_var=[None]*(number_lines)
	temp2=str_var
	for i in range(number_lines):
		temp=str(temp2.partition("\n")[0])
		list_var[i]=temp
		temp2=str(temp2.partition("\n")[2])
	return list_var	

def getIconPath (App_Name) :
	''' This function is for searching the path of the icon listed in the .desktop File 
		Input: filename
		Output: Icon-Path.
	'''
	# 1. Search Icons for Default icons - using relative path.
	# 2. Search Icons for Other/Custom Icons - using absolute path in case there is some issue displaying the icon provided by GTK+ theme.
	# Get the icon theme first.
	Icon_Theme = gtk.icon_theme_get_default()
	# Get the icon path from the Icon Theme.
	try :
		# 1. Get Icons from the relative path.
		Icon_Path = Icon_Theme.lookup_icon(App_Name , 48 , 0)
		#if(Icon_Path
		Icon_Path = Icon_Path.get_filename()
	except :
		# To be implemented - Rite now it sends an error message and sends null string.
		# 2. Get icons from absolute path. 
		Icon_Path = 'NoIconFound'
		print "Icon Not Found"
		
	return Icon_Path
