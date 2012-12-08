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
	sys.exit()


class front_end:
	""" This is front handler for appsearch feature"""
	def __init__(self):
	
		#Set glade file
		self.gladefile = "/home/vm/scripts/py_finder/UI_GTK.glade"
		self.glade = gtk.Builder()
		self.glade.add_from_file(self.gladefile)
		

        	self.window=self.glade.get_object("window1")
                self.window.show_all()
                self.open_kybd()
                self.dic = {"on_apps_searchbox_insert_at_cursor" : self.on_apps_searchbox_activate, "on_MainWindow_destroy" : gtk.main_quit }
                self.glade.connect_signals(self.dic)


        def open_kybd(self):
                try:
                        sp.Popen("florence")
                        print "started florence onscreen keyboard"
                except:
                        print "florence not found"
                        
                
	def main(self):		
		print 'hello dick'

        
        def on_apps_searchbox_activate(self,widget):
       		print "its working biatch"
		

	

if __name__=="__main__" :
	front_obj=front_end()
	front_obj.main()
        gtk.main()
