import UI_GTK.py

try:
	import elementtree.Elementtree
except:
	print 'Install the depencences in dep_install, Refer readme for more details'

	'''
		This should invoke the UI_GTK.py python program which contains the Front End written in python.
	'''
if __name__=="__main__" :
	front_obj=front_end()
	front_obj.main()
    gtk.main()
	
	'''
		Need to add the constraints
			1). TO check if keyborad is already open...
	'''