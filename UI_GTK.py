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
		
		## dic start
		self.dic = {
		"on_apps_searchbox_activate" : self.on_apps_searchbox_activate,
		"destroy" : self.gtk_main_quit, 
		"on_apps_launch_button_clicked" : self.on_apps_launch_button_clicked, 
		"on_apps_search_button_clicked" : self.on_apps_searchbox_activate,
		"on_file_searchbox_activate" : self.on_file_searchbox_activate
		
		}
		## End of dic
		
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
       		print "apps_searchbox working"
       		self.apps_searchbox=self.glade.get_object("apps_searchbox")
       		self.keyword=self.apps_searchbox.get_text()
       		print self.keyword
		
		# Importing functions
		from back_end import app_search as app_search
		self.output=app_search(self.keyword)		

		# Displaying static text on label
		self.apps_display_result = self.glade.get_object("apps_display_result")
	
		# get application launch button object
       		self.apps_launch_button=self.glade.get_object("apps_launch_button")

		if (self.output==0):
			# Error condition
			self.apps_display_result.set_text("cannot search blank keyword")
			self.apps_searchbox.set_text("")

			# hide launch button
	       		self.apps_launch_button.hide()

		elif (self.output==1):
			# Error condition
			self.apps_display_result.set_text("no such application found")
			self.apps_searchbox.set_text("")

			# hide launch button
	       		self.apps_launch_button.hide()

		else:
			# display result on app
			self.apps_display_result.set_text(self.output)	
			self.apps_searchbox.set_text("")
			
			#get launch button icon
	       		self.apps_launch_button.show()
      									
						
 	def ErrorMessage(self, message, searchbox):
 		md = gtk.MessageDialog(self.window,
 					gtk.DIALOG_DESTROY_WITH_PARENT,
 					gtk.MESSAGE_WARNING,
 					gtk.BUTTONS_CLOSE,
 					message)
 		md.run()
 		md.destroy()
 		
 		# Remove text from file_searchbox
 		searchbox.set_text("")
 		
 		
	def on_file_searchbox_activate(self, widget):
		
		self.file_searchbox = self.glade.get_object("file_searchbox")
		
		# getting keyword
		self.keyword_file = self.file_searchbox.get_text()
		print self.keyword_file
				
		# Importing function
		from back_end import search_file as search_file
		
		self.output_list = search_file(self.keyword_file)

		# get file_search_frame from glade
		self.file_search_frame = self.glade.get_object("file_search_frame")
				
		if (self.output_list == None):
			# If no such file found, then warn
			self.message="No File or Folder found by that name"
			self.ErrorMessage(self.message,self.file_searchbox)
											
		elif (self.output_list == 2):
			# Blank Keyword Error
			self.message="Blank Keyword!"
			self.ErrorMessage(self.message,self.file_searchbox)
		else:
			print self.output_list

			#### THE TREE CODE ####
	       		
	       		# Treestore
	       		self.treestore = gtk.TreeStore(str)
			
			for parent in self.output_list:
				piter=self.treestore.append(None, [parent])
			       		
			# TreeView
			self.treeview = gtk.TreeView(self.treestore)
			self.treeview.connect('cursor-changed', self.get_selected_path)
			# Create Treeview column
			self.tvcolumn = gtk.TreeViewColumn('File List')
			
			#add tvcolumn to treeview
			self.treeview.append_column(self.tvcolumn)
			
			# Create a CellRendererText to render data
			self.cell = gtk.CellRendererText()
			
			# Add the cell to tvcolumn and allow it to expand
			self.tvcolumn.pack_start(self.cell, True)
			
			# Set the cell to text attribute to column 0
			self.tvcolumn.add_attribute(self.cell, 'text', 0)
			
			print "duck duck, gtk tree created!"
			
			# adding it to frame
			self.file_search_frame = self.glade.get_object("file_search_frame")
			self.file_search_frame.add(self.treeview)
			self.file_search_frame.show_all()
			
			
	###
	def get_selected_path(self, widget, data=None):
		
		self.manoj=self.treeview.get_selection()
		self.manoj.set_mode(gtk.SELECTION_SINGLE)
		self.var1,self.var2=self.manoj.get_selected()
		self.result=self.var1.get_value(self.var2,0)
		
		self.on_folder_launch_button(self.result)


	def on_folder_launch_button(self, path):
		from back_end import open_path as open_path
		open_path(path)
		
	
	def on_apps_launch_button_clicked(self, widget):
		from back_end import open_app as open_app
		try:
			self.did_app_open=open_app(str(self.output))
			print self.did_app_open
		except:
			print "app not found"
			print self.output
			print list(self.output)
			
						

if __name__=="__main__" :
	front_obj=front_end()
	front_obj.main()
    	gtk.main()
