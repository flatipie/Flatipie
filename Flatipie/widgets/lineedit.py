
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

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor


class LineEdit(QLineEdit):
	def __init__(self, parent=None, color: QColor(77, 153, 239), background=True):
		super(LineEdit, self).__init__(parent)
		self.color = color.name()
		self.hover = color.darker(115).name()
		self._color = QColor(207, 207, 207).name()
		
		self.isbackground = background
		
		if self.isbackground == True:
			self.background = QColor(232, 232, 232).name()
		elif self.isbackground == False:
			self.background = "transparent"

		self.create_style()

	def create_style(self):
		
		style = f"""
		QLineEdit {{
			font: 8pt Arial;
			border: none;
			border-top-left-radius: 4px;
			border-top-right-radius: 4px;
			border-bottom: 2px solid {self._color};
			background-color: {self.background};
			selection-background-color: rgba(255, 255, 255, 1);
		}}
		QLineEdit:hover {{
			font: 8pt Arial;
			border: none;
			border-top-left-radius: 4px;
			border-top-right-radius: 4px;
			border-bottom: 2px solid {self.color};
			background-color: {self.background};
			selection-background-color: rgba(255, 255, 255, 1);
		}}
		"""
		
		self.setStyleSheet(style)

	def focusInEvent(self, event):
		super().focusInEvent(event)
		self.setStyleSheet(f"""
		QLineEdit {{
			font: 8pt Arial;
			border: none;
			border-top-left-radius: 4px;
			border-top-right-radius: 4px;
			border-bottom: 2px solid {self.color};
			background-color: {self.background};
			selection-background-color: rgba(255, 255, 255, 1);
		}}
		""")
	def focusOutEvent(self, event):
		super().focusInEvent(event)
		self.setStyleSheet(f"""		
		QLineEdit {{
			font: 8pt Arial;
			border: none;
			border-top-left-radius: 4px;
			border-top-right-radius: 4px;
			border-bottom: 2px solid {self._color};
			background-color: {self.background};
			selection-background-color: rgba(255, 255, 255, 1);
		}}
		""")
