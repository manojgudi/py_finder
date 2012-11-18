from PyQt4 import QtCore, QtGui
from py_menu_ui import Ui_pyfinder

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    pyfinder = QtGui.QDialog()
    ui = Ui_pyfinder()
    ui.setupUi(pyfinder)
    pyfinder.show()
    sys.exit(app.exec_())
