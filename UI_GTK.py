#!/usr/bin/env/python

import sys
import subprocess as sp


try:
	import pygtk
	pygtk.require("2.0")
except:
	print "check pygtk deps"
	sys.exit()
	
try:
	import gtk
	import gtk.glade 
except:
	print "check gtk deps"
	sys.exit(1)

class front_end:
	""" This is front handler for appsearch feature"""
	def __init__(self):
	
		#Set glade file
		self.gladefile = "./UI_GTK.glade"
		self.glade = gtk.Builder()
		self.glade.add_from_file(self.gladefile)
		
		self.window=self.glade.get_object("window1")
		self.window.show_all()
		self.window.connect("destroy",self.gtk_main_quit)
		self.open_kybd()
		self.dic = {"on_apps_searchbox_activate" : self.on_apps_searchbox_activate, "destroy" : self.gtk_main_quit }
		self.glade.connect_signals(self.dic)
		
        def open_kybd(self):
                try:
                        sp.Popen("florence")
                        print "started florence onscreen keyboard"
                except:
                        print "florence not found"

	def gtk_main_quit(self,widget):
		"""
			Predefined callback.
			Equivalent to self.quit()
			I want my ram free of any infections after fucking with GTK....;)
		"""                    
		sp.Popen(["echo", "Killing florence"])
		sp.Popen(["pkill", "florence"])			
		gtk.main_quit()
                
	def main(self):		
	# Insert any code just before apps goes into gtk.main()
		print 'manoj is a dick'


        def on_apps_searchbox_activate(self,widget):
       		print "its working biatch"
       		self.apps_searchbox=self.glade.get_object("apps_searchbox")
       		self.keyword=self.apps_searchbox.get_text()
       		print self.keyword
		
		# Importing functions
		from back_end import app_search as app_search
		self.output=app_search(self.keyword)		

		# Displaying static text on label
		self.apps_display_result = self.glade.get_object("apps_display_result")
		if (self.output==0):
			# Error condition
			self.apps_display_result.set_text("cannot search blank keyword")
			self.apps_searchbox.set_text("")
		elif (self.output==1):
			# Error condition
			self.apps_display_result.set_text("no such application found")
			self.apps_searchbox.set_text("")

		else:
			# display result on app
			self.apps_display_result.set_text(self.output)
			self.apps_searchbox.set_text("")


if __name__=="__main__" :
	front_obj=front_end()
	front_obj.main()
    	gtk.main()
