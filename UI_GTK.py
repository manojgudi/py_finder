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
		
		# Set environment path
		import os
		path="/opt/py_finder/"
		os.chdir(path)
		
		#Set glade file
		self.gladefile = "./UI_GTK.glade"
		self.glade = gtk.Builder()
		self.glade.add_from_file(self.gladefile)
		
		self.window=self.glade.get_object("window1")
		self.window.show_all()
		self.window.connect("destroy",self.main_quit)
		self.open_kybd()
		
		# Grab Notebook object
		self.notebook = self.glade.get_object("notebook")
		
		# I found this useless and repeated code, do you require this pps ? please delete and commit later if no
		#self.dic = {"on_apps_searchbox_activate" : self.on_apps_searchbox_activate, "gtk_main_quit" : gtk.main_quit }
		
		## dic start
		self.dic = {
		"on_apps_searchbox_activate" : self.on_apps_searchbox_activate,
		"gtk_main_quit" : self.main_quit, 
		"on_apps_search_button_clicked" : self.on_apps_searchbox_activate,
		"on_file_searchbox_activate" : self.on_file_searchbox_activate,
		"on_file_search_button_clicked" : self.on_file_searchbox_activate,
		"on_notebook_switch_page" : self.on_notebook_focus_tab,
		"on_quit_button_clicked" : self.on_quit_button_clicked,
		"on_quit_wo_onboard_clicked" : self.on_quit_wo_onboard_clicked
		}
		## End of dic
		self.glade.connect_signals(self.dic)
		
        def open_kybd(self):
                try:
                        sp.Popen("florence")
                        print "started florence onscreen keyboard"
                except:
                	print "florence not found"
                	
                	# Try for onboard if florence is not found
                	try: 
                		sp.Popen("onboard")
                	except:
                		print "onboard not found"

	def main_quit(self,widget):
		"""
			Predefined callback.
			Equivalent to self.quit()
			I want my ram free of any infections after fucking with GTK....;)
		"""                    
		try:
			print "Killing florence and/or onboard"
			sp.Popen(["pkill", "florence"])
			sp.Popen(["pkill", "onboard"])
		except:
			print "cannot kill virtual keyboard instance since no such app started"			
		gtk.main_quit()
                
	def main(self):		
	# Insert any code just before apps goes into gtk.main()
		print 'main()'


        def on_apps_searchbox_activate(self,widget):
       		print "apps_searchbox working"
       		self.apps_searchbox=self.glade.get_object("apps_searchbox")
       		self.keyword=self.apps_searchbox.get_text()
       		print self.keyword
		
		# Importing functions
		from back_end import app_search as app_search
		self.output, self.output_full_path = app_search(self.keyword)		

		# Get frame
		self.apps_result_frame = self.glade.get_object("apps_result_frame")				
		
		
		if (self.output==0):
			# Error condition
			message="blank keyword!"
			self.ErrorMessage(message, self.apps_searchbox)
			

		elif (self.output==1):
			# Error condition
			message="No such application found"
			self.ErrorMessage(message, self.apps_searchbox)

		else:   
			### Application Found:
			
			# If Frame already contains iconview, then remove it
			try:
				self.apps_result_frame.remove(self.apps_search_iconview)
			except: pass
							
			# make new liststore
			self.apps_search_liststore = gtk.ListStore(str, gtk.gdk.Pixbuf)
			
			# Find icon 
			self.icon="/usr/share/icons/hicolor/48x48/apps/"+self.output[0]+".png"
			self.default_icon="graphics/default_apps.png"
			
			# Set pixbuf
			try:
				self.apps_search_pixbuf = gtk.gdk.pixbuf_new_from_file(self.icon)
			except:
				# If icon not found, then use defaults
				self.apps_search_pixbuf = gtk.gdk.pixbuf_new_from_file(self.default_icon)
			
			# Append to model
			for i in self.output:
				self.apps_search_liststore.append([i,self.apps_search_pixbuf])
			
			
			# Make icon view
			self.apps_search_iconview = gtk.IconView(self.apps_search_liststore)
			
			# Icon view settings
			self.apps_search_iconview.set_text_column(0)
			self.apps_search_iconview.set_pixbuf_column(1)
			#self.apps_search_iconview.set_orientation(gtk.ORIENTATION_VERTICAL)
			#self.apps_search_iconview.set_selection_mode(gtk.SELECTION_SINGLE)
			
			# connecter, when selection changed, call on_activate, and pass it apps_searchbox
			self.apps_search_iconview.connect('selection_changed', self.on_activate, self.apps_searchbox, self.output_full_path)
			
			# iconview set columns
			self.apps_search_iconview.set_columns(2)
			
			# Add iconview to frame	
			self.apps_result_frame.add(self.apps_search_iconview)
			print "added iconview to frame"
			self.apps_result_frame.show_all()
			
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
 		
	def on_activate(self, widget, searchbox, output_list):

		print "item selected "
		# Clear searchbox
		searchbox.set_text("")
		
		# When nothing is selected
		try:
			self.item = self.apps_search_iconview.get_selected_items()[0][0]
			
			# self.output will be a path to desktop file like /usr/share/application/firefox.desktop
			self.output=output_list[self.item]
		except:
			print "No item selected"
			self.item = ""
			
		if self.item != "" :
			# open app		
			from back_end import open_app as open_app
			self.did_app_open=open_app(self.output)
			
			if self.did_app_open == 1001:
				self.ErrorMessage("Couldn't Open Application",searchbox)
			else:
				print "App opened successfully..."
      	
 		
 		
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
				
		if (self.output_list == []):
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
			
			#Clear existing widget from file_search_frame
			try:
				self.file_search_frame.remove(self.treeview)
			except:
				# Do nothing if found error => there is no widget in frame
				pass
				       		
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
			
			print "gtk tree created!"
			
			# adding it to frame
			self.file_search_frame = self.glade.get_object("file_search_frame")
			self.file_search_frame.add(self.treeview)
			self.file_search_frame.show_all()
			
			
	def get_selected_path(self, widget, data=None):
		## To get selected path from gtk widget, note that we use a connector above displaying treeview
		
		self.treeview_instance=self.treeview.get_selection()
		self.treeview_instance.set_mode(gtk.SELECTION_SINGLE)
		
		# get_selected returns 2 variables in tuples
		self.var1,self.var2=self.treeview_instance.get_selected()
		self.result=self.var1.get_value(self.var2,0)

		# When clicked, launch this function
		self.on_folder_launch(self.result)


	def on_folder_launch(self, path):
		from back_end import open_path as open_path
		open_path(path)
		
	
	def on_notebook_focus_tab(self, notebook, page, page_num):
		# If user opens third page [0, 1, 2]
		if page_num == 2:
			self.recent_search_frame_activate()
			
	def recent_search_frame_activate(self):
		# Called for third page only	
		# try block which removes the scrolled window if its already present
		try:
			self.recent_search_apps_scrolledwindow.remove(self.recent_search_apps_treeview)
		except:
			pass
		
		try:
			self.recent_search_files_scrolledwindow.remove(self.recent_search_files_treeview)
		except:
			pass

				
		print "this is third page"
		
		from back_end import recent_search_r as recent_search_r

		self.recent_search_apps_list = recent_search_r(1)
		self.recent_search_files_list = recent_search_r(2)
		
		###############################################
		####  Treestore FOR apps_list
	       	self.recent_search_apps_treestore = gtk.TreeStore(str)
			
		for parent in self.recent_search_apps_list:
			piter=self.recent_search_apps_treestore.append(None, [parent])
		       		
		# TreeView
		self.recent_search_apps_treeview = gtk.TreeView(self.recent_search_apps_treestore)
		self.recent_search_apps_treeview.connect('cursor-changed', self.take_to_page0)
		
		# Create Treeview column
		self.recent_search_apps_tvcolumn = gtk.TreeViewColumn('Recent 5 searches')

		#add tvcolumn to treeview
		self.recent_search_apps_treeview.append_column(self.recent_search_apps_tvcolumn)
			
		# Create a CellRendererText to render data
		self.recent_search_apps_cell = gtk.CellRendererText()
			
		# Add the cell to tvcolumn and allow it to expand
		self.recent_search_apps_tvcolumn.pack_start(self.recent_search_apps_cell, True)
			
		# Set the cell to text attribute to column 0
		self.recent_search_apps_tvcolumn.add_attribute(self.recent_search_apps_cell, 'text', 0)
			
		print "apps tree created!"
			
		# adding it to apps_scrolledwindow
		self.recent_search_apps_scrolledwindow = self.glade.get_object("recent_search_apps_scrolledwindow")
		self.recent_search_apps_scrolledwindow.add(self.recent_search_apps_treeview)
		self.recent_search_apps_scrolledwindow.show_all()
		#####
		
		###########################################################		
		
		#### TreeStore FOR files_list
		
	       	self.recent_search_files_treestore = gtk.TreeStore(str)
			
		for parent in self.recent_search_files_list:
			piter=self.recent_search_files_treestore.append(None, [parent])
		       		
		# TreeView
		self.recent_search_files_treeview = gtk.TreeView(self.recent_search_files_treestore)
		self.recent_search_files_treeview.connect('cursor-changed', self.take_to_page1)
		
		# Create Treeview column
		self.recent_search_files_tvcolumn = gtk.TreeViewColumn('Recent 5 searches')

		#add tvcolumn to treeview
		self.recent_search_files_treeview.append_column(self.recent_search_files_tvcolumn)
			
		# Create a CellRendererText to render data
		self.recent_search_files_cell = gtk.CellRendererText()
			
		# Add the cell to tvcolumn and allow it to expand
		self.recent_search_files_tvcolumn.pack_start(self.recent_search_files_cell, True)
			
		# Set the cell to text attribute to column 0
		self.recent_search_files_tvcolumn.add_attribute(self.recent_search_files_cell, 'text', 0)
			
		print "files tree created!"
			
		# adding it to files_scrolledwindow
		self.recent_search_files_scrolledwindow = self.glade.get_object("recent_search_files_scrolledwindow")
		self.recent_search_files_scrolledwindow.add(self.recent_search_files_treeview)
		self.recent_search_files_scrolledwindow.show_all()
		#####
			
	
	# When clicked on recent_search_apps_element / similar to get_selected_path
	def take_to_page0(self,widget,data=None):
		self.recent_search_apps_treeview_instance=self.recent_search_apps_treeview.get_selection()
		self.recent_search_apps_treeview_instance.set_mode(gtk.SELECTION_SINGLE)
		
		# get_selected returns 2 variables in tuples
		self.var1,self.var2 = self.recent_search_apps_treeview_instance.get_selected()
		
		# Initially both variables are None, so
		if (self.var2 == None):
			return self.var1[0][0]
			
		self.result = self.var1.get_value(self.var2,0)
		
		# self.result is keyword which user clicked
		
		# When clicked, launch take user to page 0
		self.notebook.set_current_page(0)
		# get searchbox and set its text value to self.result/keyword
       		self.apps_searchbox=self.glade.get_object("apps_searchbox")
       		self.apps_searchbox.set_text(self.result)				

	def take_to_page1(self, widget, data=None):

		self.recent_search_files_treeview_instance=self.recent_search_files_treeview.get_selection()
		self.recent_search_files_treeview_instance.set_mode(gtk.SELECTION_SINGLE)
		
		# get_selected returns 2 variables in tuples
		self.var1,self.var2 = self.recent_search_files_treeview_instance.get_selected()

		# Initially both variables are None, so
		if (self.var2 == None):
			return self.var1[0][0]

		self.result = self.var1.get_value(self.var2,0)
		
		# self.result is keyword which user clicked
		
		# When clicked, launch take user to page 1
		self.notebook.set_current_page(1)
		# get searchbox and set its text value to self.result/keyword
       		self.files_searchbox=self.glade.get_object("file_searchbox")
       		self.files_searchbox.set_text(self.result)				

	def on_quit_button_clicked(self, widget):
		### Quit whole application and onboard/florence instance
		self.main_quit(widget)

		
	def on_quit_wo_onboard_clicked(self, widget):
		### Quit Only instance
		gtk.main_quit()

