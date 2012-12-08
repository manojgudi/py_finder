#!/usr/bin/env python


#Example base.py

import pygtk
pygtk.require('2.0')

import gtk

class Base:
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.show()
		
	def main(self):
		
		#### Anything from here is called
		print "hello dick"

		gtk.main()
		
print __name__

if __name__ == "__main__":
	base = Base()
	base.main()
