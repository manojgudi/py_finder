import subprocess as sp

var=raw_input("Enter package name: ")

def search_input(var):
	p1=sp.Popen(["dpkg" , "--get-selections"], stdout=sp.PIPE)
	p2=sp.Popen(["awk", "{print $1}"], stdin=p1.stdout, stdout=sp.PIPE)
	p3=sp.Popen(["grep","-m","1", var], stdin=p2.stdout, stdout=sp.PIPE)
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

def main():
	search_input(var)

main()
