# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Sat Nov 17 22:07:42 2012
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_pyfinder(object):
    def setupUi(self, pyfinder):
        pyfinder.setObjectName(_fromUtf8("pyfinder"))
        pyfinder.resize(825, 722)
        pyfinder.setMouseTracking(False)
        pyfinder.setFocusPolicy(QtCore.Qt.NoFocus)
        self.py_tabWidget = QtGui.QTabWidget(pyfinder)
        self.py_tabWidget.setGeometry(QtCore.QRect(10, 20, 791, 691))
        self.py_tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.py_tabWidget.setStyleSheet(_fromUtf8(""))
        self.py_tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.py_tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.py_tabWidget.setIconSize(QtCore.QSize(42, 42))
        self.py_tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.py_tabWidget.setMovable(False)
        self.py_tabWidget.setObjectName(_fromUtf8("py_tabWidget"))
        self.app_tab = QtGui.QWidget()
        self.app_tab.setObjectName(_fromUtf8("app_tab"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.app_tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 751, 101))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.Layout_InputSearch = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.Layout_InputSearch.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.Layout_InputSearch.setMargin(0)
        self.Layout_InputSearch.setObjectName(_fromUtf8("Layout_InputSearch"))
        self.app_textbox_search = QtGui.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_textbox_search.sizePolicy().hasHeightForWidth())
        self.app_textbox_search.setSizePolicy(sizePolicy)
        self.app_textbox_search.setMinimumSize(QtCore.QSize(505, 42))
        self.app_textbox_search.setObjectName(_fromUtf8("app_textbox_search"))
        self.Layout_InputSearch.addWidget(self.app_textbox_search)
        self.app_button_search = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.app_button_search.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../graphics/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.app_button_search.setIcon(icon)
        self.app_button_search.setIconSize(QtCore.QSize(42, 42))
        self.app_button_search.setObjectName(_fromUtf8("app_button_search"))
        self.Layout_InputSearch.addWidget(self.app_button_search)
        self.scrollArea_display = QtGui.QScrollArea(self.app_tab)
        self.scrollArea_display.setGeometry(QtCore.QRect(20, 150, 751, 491))
        self.scrollArea_display.setWidgetResizable(True)
        self.scrollArea_display.setObjectName(_fromUtf8("scrollArea_display"))
        self.app_display = QtGui.QWidget()
        self.app_display.setGeometry(QtCore.QRect(0, 0, 749, 489))
        self.app_display.setObjectName(_fromUtf8("app_display"))
        self.gridLayoutWidget = QtGui.QWidget(self.app_display)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 751, 471))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea_display.setWidget(self.app_display)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../graphics/apps.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.py_tabWidget.addTab(self.app_tab, icon1, _fromUtf8(""))
        self.file_tab = QtGui.QWidget()
        self.file_tab.setObjectName(_fromUtf8("file_tab"))
        self.horizontalLayoutWidget_6 = QtGui.QWidget(self.file_tab)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(20, 30, 751, 101))
        self.horizontalLayoutWidget_6.setObjectName(_fromUtf8("horizontalLayoutWidget_6"))
        self.Layout_InputSearch_7 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.Layout_InputSearch_7.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.Layout_InputSearch_7.setMargin(0)
        self.Layout_InputSearch_7.setObjectName(_fromUtf8("Layout_InputSearch_7"))
        self.file_textbox_search = QtGui.QLineEdit(self.horizontalLayoutWidget_6)
        self.file_textbox_search.setMinimumSize(QtCore.QSize(505, 42))
        self.file_textbox_search.setObjectName(_fromUtf8("file_textbox_search"))
        self.Layout_InputSearch_7.addWidget(self.file_textbox_search)
        self.file_button_search = QtGui.QPushButton(self.horizontalLayoutWidget_6)
        self.file_button_search.setIcon(icon)
        self.file_button_search.setIconSize(QtCore.QSize(42, 42))
        self.file_button_search.setObjectName(_fromUtf8("file_button_search"))
        self.Layout_InputSearch_7.addWidget(self.file_button_search)
        self.scrollArea_6 = QtGui.QScrollArea(self.file_tab)
        self.scrollArea_6.setGeometry(QtCore.QRect(20, 150, 751, 491))
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName(_fromUtf8("scrollArea_6"))
        self.file_display = QtGui.QWidget()
        self.file_display.setGeometry(QtCore.QRect(0, 0, 749, 489))
        self.file_display.setObjectName(_fromUtf8("file_display"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.file_display)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 751, 471))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scrollArea_6.setWidget(self.file_display)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../../graphics/files.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.py_tabWidget.addTab(self.file_tab, icon2, _fromUtf8(""))

        self.retranslateUi(pyfinder)
        self.py_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(pyfinder)

    def retranslateUi(self, pyfinder):
        pyfinder.setWindowTitle(QtGui.QApplication.translate("pyfinder", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.app_button_search.setText(QtGui.QApplication.translate("pyfinder", "  Search  ", None, QtGui.QApplication.UnicodeUTF8))
        self.py_tabWidget.setTabText(self.py_tabWidget.indexOf(self.app_tab), QtGui.QApplication.translate("pyfinder", "Apps", None, QtGui.QApplication.UnicodeUTF8))
        self.file_button_search.setText(QtGui.QApplication.translate("pyfinder", "  Search  ", None, QtGui.QApplication.UnicodeUTF8))
        self.py_tabWidget.setTabText(self.py_tabWidget.indexOf(self.file_tab), QtGui.QApplication.translate("pyfinder", "Files", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    pyfinder = QtGui.QDialog()
    ui = Ui_pyfinder()
    ui.setupUi(pyfinder)
    pyfinder.show()
    sys.exit(app.exec_())

