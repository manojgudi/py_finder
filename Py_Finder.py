#!/usr/bin/env/python
'''
    This is small application designed to run on LXDE to search applications 
    and files on local drive. For more information check out :
    		http://manojgudi.github.io/py_finder/
    Copyright (C) 2012/2013 Manoj Gudi, Pranav Salunke

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''
import UI_GTK

try:
	import elementtree.Elementtree
except:
	print 'Install the depencences in dep_install, Refer readme for more details'

	'''
		This should invoke the UI_GTK.py python program which contains the Front End written in python.
	'''
if __name__=="__main__" :
	front_obj=UI_GTK.front_end()
	front_obj.main()
    	UI_GTK.gtk.main()
	
	'''
		Need to add the constraints
			1). TO check if keyborad is already open...
	'''
