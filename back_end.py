import subprocess as sp

def app_search(keyword):
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
	


# For testing purposes
def main():
	var=raw_input("Enter package name: ")
	#app_search(var)
	search_file(var)
	#open_path(var)
	pass

main()

