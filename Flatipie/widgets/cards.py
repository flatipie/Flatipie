
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

from PyQt5.QtWidgets import QGroupBox, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QPoint

class MaterialCard(QGroupBox):
    clicked = pyqtSignal()
    def __init__(self, parent=None, shadow=True):
        super(MaterialCard, self).__init__(parent)
        self._is_shadow = shadow

    @property
    def is_shadow(self):
        return self._is_shadow

    def enterEvent(self, event):
        if self.is_shadow:
            shadow_effect = QGraphicsDropShadowEffect(
                blurRadius=10, offset=QPoint(0, 0)
            )
            self.setGraphicsEffect(shadow_effect)

    def leaveEvent(self, event):
        if self.is_shadow:
            self.setGraphicsEffect(None)

    def mousePressEvent(self, event):
        self.clicked.emit()

        
