
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

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon

class Button(QPushButton):
    def __init__(self, parent, string, font_color="#fff", 
        color="rgb(52, 152, 219)", hover_color="rgb(54, 145, 206)", outline=False, shadow=""):
        super(Button, self).__init__(parent)

        self.outline = outline
        self.hover = hover_color
        self.shadow = shadow
        self.color = color
        self.font_color = font_color
        self.create_style()
        
        self.setText(string)
        
    def create_style(self):
        if self.outline == True:
            style = """
            QPushButton{
                color: %s;
                font: Arial;
                font-size: 8;
                font-weight: bold;
                background-color: transparent;
                border: 2px solid %s;
             
            }
            QPushButton:hover{
                color: %s;
                font: Arial;
                font-weight: bold;
                font-size: 8;
                background-color: %s;
                
            }
            """ % (self.color, self.color, self.font_color, self.color)
            
        
        elif self.outline == False and self.shadow  != "":
            style = """
            QPushButton{
                color: %s;
                font: Arial;
                font-weight: bold;
                background-color: %s;
                border: 2px solid %s;
                border-bottom: 2px solid %s;
            }
            QPushButton:hover{
                color: %s;
                font: Arial;
                font-size: 8;
                font-weight: bold;
                background-color: %s;
                border-bottom: 2px solid %s;
                
            }

            """ % (self.font_color, self.color, self.color, self.shadow, self.font_color, self.hover, self.shadow)

        elif self.outline == False and self.shadow == "":
                        style = """
            QPushButton{
                color: %s;
                font: Arial;
                font-weight: bold;
                background-color: %s;
                border: 2px solid %s;
            }
            QPushButton:hover{
                color: %s;
                font: Arial;
                font-size: 8;
                font-weight: bold;
                background-color: %s;                
            }

            """ % (self.font_color, self.color, self.color, self.font_color, self.hover)

        self.setStyleSheet(style) 
