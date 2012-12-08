#!/usr/bin/env/python

import sys

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
	sys.exit()


class front_end:
	""" This is front handler for appsearch feature"""
	def __init__(self):
	
		#Set glade file
		self.gladefile = "UI_GTK.glade"
		self.wTree = gtk.glade.XML(self.gladefile)
	
		# Get main window and connect "destroy" event
		self.window = self.wTree.get_widget("MainWindow")
		if (self.window):
			self.window.connect("destroy", gtk.main_quit)


if __name__=="__main__" :
	front_obj=front_end()
	gtk.main()
  
