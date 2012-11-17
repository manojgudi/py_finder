import subprocess as sp

def app_search(keyword):
	
	# Check for blank keywords
	if keyword=="":
		print "blank keyword"
		output="blank keyword"
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
		print "No application by such name"
	else:
		print output

		# check for repetition of keyword
		
		#save this into .recent_searches file
		recent_search_w(keyword)

		return output	
		


# On Double clicking app from search, this should be called:
def open_app(program_name):
	sp.Popen([program_name])	



def search_file(keyword):
	
	if keyword=="":
		print "keyword cannot be null"
		main()
	else:
		p1=sp.Popen(["locate","-b",keyword], stdout=sp.PIPE)
		result=p1.communicate()[0]

		if result=="":
			print "no file found"
		else:
			print result
			return result
	
def open_path(path):
	p1=sp.Popen(["thunar", path])

# Called when 
def recent_search_r():
	try:
		file_obj=open(".recent_searches","r")
	except IOError:
		output="no recent searches"
		return output
	# This blocks runs only if there is NO IOError
	recent_search_list=file_obj.read()
	print recent_search_list # is a string@@@@@
	return str2list(recent_search_list)
	

def recent_search_w(keyword):
	file_ob=open(".recent_searches",'a')
	file_ob.write(keyword)
	file_ob.write("\n")
	file_ob.close()
	
	#checking for 11th term and deleting it
	file_ob=open(".recent_searches",'r')
	content=file_ob.read()
	limit=10
	if limit>10:
		pass
		#del
	else:
		pass
	
# Formatted String to list
def str2list(str_var):
	number_lines=str_var.count("\n")
	list_var=[None]*(number_lines)
	temp2=str_var
	for i in range(number_lines):
		temp=str(temp2.partition("\n")[0])
		list_var[i]=temp
		temp2=str(temp2.partition("\n")[2])
	return list_var				


# For testing purposes
def main():
	var=raw_input("Enter package name: ")
	app_search(var)
	#search_file(var)
	#open_path(var)
	recent_search_r()

main()

