
import subprocess as sp
import os

def app_search(keyword):
	""" This function is used to query dpkg and return single relevant answer; In: single string, Out: Error Number or string of relevant search """
	# Check for blank keywords
	if keyword=="":
		print "blank keyword"
		
		# error code 0		
		return 0
	
	# Will run only if keyword is not null, case insensitive search
	p1=sp.Popen(["dpkg" , "--get-selections"], stdout=sp.PIPE)
	p2=sp.Popen(["awk", "{print $1}"], stdin=p1.stdout, stdout=sp.PIPE)
	p3=sp.Popen(["grep","-i","-m","1", keyword], stdin=p2.stdout, stdout=sp.PIPE)
	output=p3.communicate()[0]

	# Kill earlier process pipes
	p1.kill()
	p2.kill()

	if output=="":
		# "No application by such name"
		#error code 1
		return 1
	else:
		#save this into .recent_searches file
		# We are saving output instead of keyword, since keyword==>result is many to one mapping 
		#recent_search_w(output)

		# problem is output from app_search is list with a delimiter \n; so 'app_name' becomes 'app_name\n', hence we use below function that removes delimiter
		delim_number=output.find("\n")
		output=output[:delim_number]
		
		# Write this keyword to .data.xml
		recent_search_w(keyword,1)
		return output	
		


# On Double clicking app from search, this should be called:
def open_app(program_name):
	
	''' Function used to open app when tapping of relevant keyword; In: single string, Out: Success Number '''
	
	sp.Popen([str(program_name)])
		
	# success code 100
	return 100

def search_file(keyword):
	'''Search function used to locate single file, In: String keyword, Out: list of all relevant path of keyword'''	
	if keyword=="":
		print "keyword cannot be null/blank"
		#error code 2
		return 2
	else:
		result = search_filesystem(keyword)

		if result=="":
			print "no such file found"
		else:
			recent_search_w(keyword,2)
			return result

def search_filesystem(keyword) :
	
	raw_home = os.walk('/home/')
	raw_media = os.walk('/media/aakash/')

	fin_list = []
	'''
		This block of code will remove all hidden files and folders
		to remove the unncessary '/.' files and folders to be searched.
	'''

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

	return fin_list
	
# path_full = one element from output of search_file
def open_path(path_full):
	""" Tapping relevant search result invokes file explorer to open folder containing relevant file, In: Single string of full_path Out: Error/Success number """
	try:
		# remove file_name
		print 'pranav is curious \n' + str(path_full.rpartition("/")[0])
		path=(str(path_full.rpartition("/")[0]))

		### REPLACE thunar with pcmanfm for lxde
		p1=sp.Popen(["pcmanfm", path])

		# success code 101
		return 101
	except: 
		#error code 3
		return 3


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
		tree = et.parse('.data.xml')
	except:
		print "data.xml not found, exiting"
		exit()
	
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
	
		# Code Retriving
		try:
			tree = et.parse('.data.xml')
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
		
		tree.write('.data.xml')	

	# If mode is 1, update apps_list, else update files_list
	if mode == 1:
		apps_output=update_list(apps_output)
		write(apps_output, mode)
		
	else :
		files_output=update_list(files_output)
		write(files_output, mode)	
	
	print "written to xml"
