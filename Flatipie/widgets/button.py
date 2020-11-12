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
from PyQt5.QtGui import QIcon, QColor
from .errors import *

class Button(QPushButton):
    def __init__(self, parent, string, color: QColor,
        font_color=QColor("#fff"), outline=False, shadow=True):
        super(Button, self).__init__(parent)

        self.color = color
        self.hover = self.color.darker(105).name()
        self.font_color = font_color
        self.shadow_color = self.color.darker(115).name()        
        self.outline = outline
        self.shadow = shadow
        
        
        self.create_style()
        
        self.setText(string)
        
    def create_style(self):
      
        if self.outline == True:
            style = f"""
            QPushButton {{
                color: {self.font_color.name()};
                font: Arial;
                font-size: 8;
                font-weight: bold;
                background-color: transparent;
                border: 2px solid {self.color.name()};
             
            }}
            QPushButton:hover{{
                color: {self.font_color.name()};
                font: Arial;
                font-weight: bold;
                font-size: 8;
                background-color: {self.color.name()};
                
            }}
            """ 
            
        
        elif self.outline == False and self.shadow  == False:
            style = f"""
            QPushButton {{
                color: {self.font_color.name()};
                font: Arial;
                font-weight: bold;
                background-color: {self.color.name()};
                border: 2px solid {self.color.name()};
            }}
            QPushButton:hover {{
                color: {self.font_color.name()};
                font: Arial;
                font-size: 8;
                font-weight: bold;
                background-color: {self.color.name()};    
            }}
            """
        elif self.outline == False and self.shadow == True:
            style = f"""
            QPushButton {{
                color: {self.font_color.name()};
                font: Arial;
                font-size: 8;
                font-weight: bold;
                background-color: {self.color.name()};
                padding: 12px;
                border-radius: 4px;
                border-bottom: 4px solid {self.shadow_color};
            }}
            QPushButton:hover {{
                color: {self.font_color.name()};
                font: Arial;
                font-size: 8;
                font-weight: bold;
                background-color: {self.hover};                
            }}
            """
            
        elif self.outline == True and self.shadow == True:
            raise UnknownStyleError("You cannot add shadow while outline is true.")
            
        self.setFixedSize(100, 40)
        self.setStyleSheet(style) 
