"""
					Copyright (c) 2020 Flatipie

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""



from PyQt5.QtGui import QPalette, QColor
from os.path import join, dirname, abspath
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QMetaObject, pyqtSignal, pyqtSlot, QEvent, QFile, QTextStream
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QToolButton,
							QLabel, QSizePolicy, QDesktopWidget)
import sys
import PyQt5
import qtpy
from . import resources

#QT_VERSION = tuple(int(v) for v in qtpy.QT_VERSION.split('.'))
#print(QT_VERSION)
QT_VERSION = (5, 15, 1)


_raw_data = QFile(":/stylesheet/style.qss")
_raw_data.open(QFile.ReadOnly | QFile.Text)
_ts = QTextStream(_raw_data)
app_stylesheet = _ts.readAll()

def _apply_base_theme(app):
	""" Apply base theme to the application.

		Args:
			app (QApplication): QApplication instance.
	"""

	if QT_VERSION < (5,):
		app.setStyle('plastique')
	else:
		app.setStyle('Fusion')

	
	app.setStyleSheet(app_stylesheet)


def apply_palette(app):
	""" Apply Light Theme to the Qt application instance.

		Args:
			app (QApplication): QApplication instance.
	"""

	palette = QPalette()

	# base
	palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
	palette.setColor(QPalette.Button, QColor(240, 240, 240))
	palette.setColor(QPalette.Light, QColor(180, 180, 180))
	palette.setColor(QPalette.Midlight, QColor(200, 200, 200))
	palette.setColor(QPalette.Dark, QColor(225, 225, 225))
	palette.setColor(QPalette.Text, QColor(0, 0, 0))
	palette.setColor(QPalette.BrightText, QColor(0, 0, 0))
	palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
	palette.setColor(QPalette.Base, QColor(237, 237, 237))
	palette.setColor(QPalette.Window, QColor(240, 240, 240))
	palette.setColor(QPalette.Shadow, QColor(20, 20, 20))
	palette.setColor(QPalette.Highlight, QColor(76, 163, 224))
	palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
	palette.setColor(QPalette.Link, QColor(0, 162, 232))
	palette.setColor(QPalette.AlternateBase, QColor(225, 225, 225))
	palette.setColor(QPalette.ToolTipBase, QColor(240, 240, 240))
	palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))

	# disabled
	palette.setColor(QPalette.Disabled, QPalette.WindowText,
						 QColor(115, 115, 115))
	palette.setColor(QPalette.Disabled, QPalette.Text,
						 QColor(115, 115, 115))
	palette.setColor(QPalette.Disabled, QPalette.ButtonText,
						 QColor(115, 115, 115))
	palette.setColor(QPalette.Disabled, QPalette.Highlight,
						 QColor(190, 190, 190))
	palette.setColor(QPalette.Disabled, QPalette.HighlightedText,
						 QColor(115, 115, 115))

	app.setPalette(palette)

	_apply_base_theme(app)
	




#_FL_STYLESHEET = join(dirname(abspath(__file__)), 'resources/frameless.qss')
""" str: Frameless window stylesheet. """
raw_data = QFile(":/stylesheet/frameless.qss")
raw_data.open(QFile.ReadOnly | QFile.Text)
ts = QTextStream(raw_data)
window_stylesheet = ts.readAll()

class WindowDragger(QWidget):
	""" Window dragger.

		Args:
			window (QWidget): Associated window.
			parent (QWidget, optional): Parent widget.
	"""

	doubleClicked = pyqtSignal()

	def __init__(self, window, parent=None):
		QWidget.__init__(self, parent)

		self._window = window
		self._mousePressed = False

	def mousePressEvent(self, event):
		self._mousePressed = True
		self._mousePos = event.globalPos()
		self._windowPos = self._window.pos()

	def mouseMoveEvent(self, event):
		if self._mousePressed:
			self._window.move(self._windowPos +
							  (event.globalPos() - self._mousePos))

	def mouseReleaseEvent(self, event):
		self._mousePressed = False

	def mouseDoubleClickEvent(self, event):
		self.doubleClicked.emit()


class ModernWindow(QWidget):
	""" Modern window.

		Args:
			w (QWidget): Main widget.
			parent (QWidget, optional): Parent widget.
	"""

	def __init__(self, w, parent=None):
		QWidget.__init__(self, parent)

		self._w = w
		self.setupUi()

		contentLayout = QHBoxLayout()
		contentLayout.setContentsMargins(0, 0, 0, 0)
		contentLayout.addWidget(w)

		self.windowContent.setLayout(contentLayout)

		self.setWindowTitle(w.windowTitle())
		self.setGeometry(w.geometry())

		# Adding attribute to clean up the parent window when the child is closed
		self._w.setAttribute(Qt.WA_DeleteOnClose, True)
		self._w.destroyed.connect(self.__child_was_closed)

	def setupUi(self):
		# create title bar, content
		self.vboxWindow = QVBoxLayout(self)
		self.vboxWindow.setContentsMargins(0, 0, 0, 0)

		self.windowFrame = QWidget(self)
		self.windowFrame.setObjectName('windowFrame')

		self.vboxFrame = QVBoxLayout(self.windowFrame)
		self.vboxFrame.setContentsMargins(0, 0, 0, 0)

		self.titleBar = WindowDragger(self, self.windowFrame)
		self.titleBar.setObjectName('titleBar')
		self.titleBar.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,
												QSizePolicy.Fixed))

		self.hboxTitle = QHBoxLayout(self.titleBar)
		self.hboxTitle.setContentsMargins(0, 0, 0, 0)
		self.hboxTitle.setSpacing(0)

		self.lblTitle = QLabel('Title')
		self.lblTitle.setObjectName('lblTitle')
		self.lblTitle.setAlignment(Qt.AlignCenter)

		spButtons = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

		self.btnMinimize = QToolButton(self.titleBar)
		self.btnMinimize.setObjectName('btnMinimize')
		self.btnMinimize.setSizePolicy(spButtons)

		self.btnRestore = QToolButton(self.titleBar)
		self.btnRestore.setObjectName('btnRestore')
		self.btnRestore.setSizePolicy(spButtons)
		self.btnRestore.setVisible(False)

		self.btnMaximize = QToolButton(self.titleBar)
		self.btnMaximize.setObjectName('btnMaximize')
		self.btnMaximize.setSizePolicy(spButtons)

		self.btnClose = QToolButton(self.titleBar)
		self.btnClose.setObjectName('btnClose')
		self.btnClose.setSizePolicy(spButtons)

		self.vboxFrame.addWidget(self.titleBar)

		self.windowContent = QWidget(self.windowFrame)
		self.vboxFrame.addWidget(self.windowContent)

		self.vboxWindow.addWidget(self.windowFrame)

		if sys.platform == "darwin":
			self.hboxTitle.addWidget(self.btnClose)
			self.hboxTitle.addWidget(self.btnMinimize)
			self.hboxTitle.addWidget(self.btnRestore)
			self.hboxTitle.addWidget(self.btnMaximize)
			self.hboxTitle.addWidget(self.lblTitle)
		else:
			self.hboxTitle.addWidget(self.lblTitle)
			self.hboxTitle.addWidget(self.btnMinimize)
			self.hboxTitle.addWidget(self.btnRestore)
			self.hboxTitle.addWidget(self.btnMaximize)
			self.hboxTitle.addWidget(self.btnClose)

		# set window flags
		self.setWindowFlags(
				Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)

		if QT_VERSION >= (5,):
			self.setAttribute(Qt.WA_TranslucentBackground)

		# set stylesheet
	 
		self.setStyleSheet(window_stylesheet)

		# automatically connect slots
		QMetaObject.connectSlotsByName(self)

	def __child_was_closed(self):
		self._w = None  # The child was deleted, remove the reference to it and close the parent window
		self.close()

	def closeEvent(self, event):
		if not self._w:
			event.accept()
		else:
			self._w.close()
			event.setAccepted(self._w.isHidden())



	def setWindowTitle(self, title):
		""" Set window title.

			Args:
				title (str): Title.
		"""

		super(ModernWindow, self).setWindowTitle(title)
		self.lblTitle.setText(title)

	@pyqtSlot()
	def on_btnMinimize_clicked(self):
		self.setWindowState(Qt.WindowMinimized)

	@pyqtSlot()
	def on_btnRestore_clicked(self):
		self.btnRestore.setVisible(False)
		self.btnMaximize.setVisible(True)

		self.setWindowState(Qt.WindowNoState)

	@pyqtSlot()
	def on_btnMaximize_clicked(self):
		self.btnRestore.setVisible(True)
		self.btnMaximize.setVisible(False)

		self.setWindowState(Qt.WindowMaximized)

	@pyqtSlot()
	def on_btnClose_clicked(self):
		self.close()

	@pyqtSlot()
	def on_titleBar_doubleClicked(self):
		if self.btnMaximize.isVisible():
			self.on_btnMaximize_clicked()
		else:
			self.on_btnRestore_clicked()

