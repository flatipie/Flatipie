"""
					  Copyright (c) 2020 Flatipie
				This project was created by Flatipie.

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

from PyQt5.QtWidgets import ( QApplication, QWidget, QGridLayout, QDesktopWidget )
from Flatipie.widgets import MaterialButton, Button
from Flatipie import apply_palette, ModernWindow
import random

class MainWindow(QWidget):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.setWindowTitle("flatipie buttons")
    resolution = QDesktopWidget().screenGeometry()
		self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
			(resolution.height() / 2) - (self.frameSize().height() / 2)) 
    
    grid = QGridLayout()
    
    for x in range(5):
      for y in range(5):
        # You can use Material Button aswell also you can change the style to Flat and more in Button.
        # Read more infos at https://github.com/flatipie/flatipie
        
        grid.addWidget(Button("Push me"), x, y)
    
    self.setLayout(grid)
    
 if __name__ == "__main__":
  app = QApplication(sys.argv)
  apply_palette(app)
  window = ModernWindow(MainWindow())
  window.show()
  sys.exit(app)
