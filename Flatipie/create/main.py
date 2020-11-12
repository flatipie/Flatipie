
"""
                    Copyright (c) 2020 Flatipie
				This project folder was created by Flatipie.

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
try:
	from Flatipie import apply_palette, ModernWindow
except ModuleNotFoundError:
	print("There's an error importing Flatipie. Please re install the module again")

from PyQt5.QtWidgets import QApplication
from src.app import App
import sys

def main():
	
	# First we created a application object for pyqt
	app = QApplication(sys.argv)

	# Then we apply Flatipie style sheet and modern window style for creating modern-looking interfaces.
	# Please note that this is important for creating flatipie style app.
	apply_palette(app)
	window = ModernWindow(App())

	# Next is we show the window then execute the app.
	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()