Py Finder V1.0
===========

This is small application designed to run on LXDE to search applications and files on local drive.


Features:
---------
* Its is touch optimized, specially meant for LXDE environment on Aakash devices.
* Integrated with screen keyboard
* Light on RAM (takes up atmost 16mb with on-screen keyboard running)
* Low dependencies


Built Using:
------------

* libgtk 2.24.8+
* PyGTK2.24 
* Glade 3.8.0


Installation:
-------------

1. It is assumed that the system has Python 2.7, Florence keyboard or Onscreen Keyboard.

2. To install dependencies, open terminal, `cd` to current directory, and then type ::

     $ sudo ./dep_install

3. To  install application after installing dependencies, open a new terminal, `cd` to current directory and then type

    $ ./app_install

4. After successful installation, We'll have to add it to lxpanel;

* Right Click lxpanel > Panel settings > Panel Applets
* Click on Add > Application Launchbar > Add
* Once, Application Launchbar is added, then Edit on Application Launchbar > Add Py Finder (which is under Universal Access)

5. That's it! Launch Py Finder by clicking on small icon in lxpanel

6. To uninstall application, open a new terminal, cd to current folder, and run uninstall scripts-
	
    $ ./app_uninstall

7. To uninstall dependencies installed, open a new terminal, cd to current folder, and run uninstall scripts-
	
    $ ./dep_uninstall
    
8. To remove app from lxpanel, right-click on Py Finder icon and click on "delete panel item"


Bugs:
-----

Please report all bugs and errors here on github


License:
--------

Released under GNU GPL(General Public Lience) V2 license.
