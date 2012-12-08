#!/usr/bin/env python


#Example base.py

import pygtk
pygtk.require('2.0')
import gtk


class HelloWorld:
	
	# Callback function
	def hello(self, widget, data=None):
		print "duck"
		
	def delete_event(self, widget, event, data=None):
		print "delete event occured"
		return False
	# return true and and the window wont be destroyed on calling of this function
		
	def destroy(self, widget, data=None):
		gtk.main_quit()
		
	def __init__(self):
		#Create a new window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
	
		# 
		self.window.connect("delete_event")

		#connecting gtk_widget_destroy signal handler to delete_event
