import subprocess as sp

def app_search(keyword):
	""" This function is used to query dpkg and return single relevant answer; In: single string, Out: Error Number or string of relevant search """
	# Check for blank keywords
	if keyword=="":
		print "blank keyword"
		
		# error code 0		
		return 0
	
	# Will run only if keyword is not null
	p1=sp.Popen(["dpkg" , "--get-selections"], stdout=sp.PIPE)
	p2=sp.Popen(["awk", "{print $1}"], stdin=p1.stdout, stdout=sp.PIPE)
	p3=sp.Popen(["grep","-m","1", keyword], stdin=p2.stdout, stdout=sp.PIPE)
	output=p3.communicate()[0]

	# Kill earlier process pipes
	p1.kill()
	p2.kill()

	if output=="":
		#print "No application by such name"
		# error code 1
		return 1
	else:
		#print output

		#save this into .recent_searches file
		# We are saving output instead of keyword, since keyword==>result is many to one mapping 
		#recent_search_w(output)
		return output	
		


# On Double clicking app from search, this should be called:
def open_app(program_name):
	
	''' Function used to open app when tapping of relevant keyword; In: single string, Out: Success Number '''
	
	# Additional functionality reserved for future for program whose installation package name different than execution name
	# for i in special_program_name:
		#if program_name==i:
			#program_name=y #(mapped from special_program_name list)

	sp.Popen([program_name])
	
	# success code 100
	return 100

def search_file(keyword):
	'''Search function used to locate single file, In: String keyword, Out: list of all relevant path of keyword'''	
	if keyword=="":
		print "keyword cannot be null"
		#error code 2
		return 2
	else:
		p1=sp.Popen(["locate","-b",keyword], stdout=sp.PIPE)
		result=p1.communicate()[0]

		if result=="":
			print "no file found"
		else:
			output=str2list(result)
			print output
			#open_path(output[3])
			return output

# path_full = one element from output of search_file
def open_path(path_full):
	""" Tapping relevant search result invokes file explorer to open folder containing relevant file, In: Single string of full_path Out: Error/Success number """
	try:
		# remove file_name
		path=(str(path_full.rpartition("/")[0]))
		
		### REPLACE thunar with pcmanfm for lxde
		p1=sp.Popen(["thunar", path])
		
		# success code 101
		return 101
	except: 
		#error code 3
		return 3


# Called when 
def recent_search_r():
	""" Reading the .recent_searches file In: None, Out: List of all values present in .recent_searches file"""
	try:
		file_obj=open(".recent_searches","r")
	except IOError:
		# error code 4
		return 4
		
	# This blocks runs only if there is NO IOError
	recent_search_list=file_obj.read()
	print recent_search_list # is a string@@@@@
	output=str2list(recent_search_list)
	return output
	

def recent_search_w(result):
	""" Called by other functions to write a successful result to .recent_searches.file; In: Successful String Result from app_search(); Out: None  """
	file_read=recent_search_r()

	def write(result):
		file_ob=open(".recent_searches",'a')
		file_ob.write(result)
		file_ob.write("\n")
		file_ob.close()

	# if .recent_searches is empty then... 4 is return of recent_search_r()			
	if file_read==4:
		write(result)	
	else:		
		# Result has a \n removing that:
		result=result[:result.find("\n")]
		# if result is new, write only then
		if file_read.count(result)>=1:
			pass
		else:
			write(result)
	
	#checking for 11th term and deleting it; so that .recent_searches contain only last 10 results
	#content=recent_search_r()
	#if len(content)>11:
	#	content.pop(len(content)-1)
	#	print content
	#	file_ob=open(".recent_searches",'w')
	#	file_ob.write(content)
	#else: pass
	
# Formatted String to list
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


