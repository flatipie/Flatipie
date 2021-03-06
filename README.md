<h1 align="center">
     <br>
     <img src="https://github.com/flatipie/Flatipie/blob/main/.resources/flatipie.png" alt="Flatipie">
</h1>

<h4 align="center">An open source framework for building desktop application..</h4>

<p align="center">
    <a href="https://github.com/zenqii">
    <img src="https://img.shields.io/github/followers/zenqii?label=Follow&logo=github&style=flat-square"
         alt="GitHub">
     <a href="https://discord.com/invite/SyZeeahz7E">
    <img src="https://img.shields.io/discord/776701754619985950?label=Discord&logo=discord&style=flat-square"
         alt="Discord">
    <a href="https://twitter.com/flatipieqt">
    <img src=https://img.shields.io/twitter/follow/flatipieqt?color=%235087F4&label=Twitter&logo=twitter&style=flat-square
         alt="Twitter">
     <a href="#License">
     <img src=https://img.shields.io/github/license/flatipie/Flatipie?color=5087F4&label=License&style=flat-square
          alt="License">
</p>

<p align="center">
  <a href="#about">About</a> | 
  <a href="#installation">Installation</a> | 
  <a href="#usage">Usage</a> | 
  <a href="#features">Features</a> | 
  <a href="#author">Author</a> | 
  <a href="#contributors">Contributors</a> |
  <a href="#help">Help</a> | 
  <a href="#license">License</a>
</p>

## About
> Flatipie is now an unmaintained project. I'll continue developing this if I have encouraged to do so.

**Flatipie** *is an **open source framework use for deploying**, **building** and **creating desktop applications**. It was created to build modern qt project easily and reliable.*

**Flatipie** was originally **developed** to build <u>desktop application </u>easily using [PyQt5](https://pypi.org/project/pyqt5) that also uses it's original stylesheet for creating *modern application*.

| <img src="https://github.com/flatipie/Flatipie/blob/main/.resources/vector.jpg" width="512"> |
|:-------------------------------------------------------------------------:|

## Installation

---
```
$ pip install flatipie
```

## Usage

---

> You can check out the main [documentation](https://www.github.com/flatipie/Flatipie)

To create your first project, just kindly execute **create** command after you installed Flatipie and fill out any requirements used for packaging the project

```
$ flatipie create
```

You can **run** file that contains *package.json* just execute this following **command**

```
$ flatipie run
```

After you finish creating your app, you can easily build **executable** file for it with the following **command**. Make sure it contains package.json

```
$ flatipie build
```

| [Learn More](https://www.github.com/flatipie/flatipie) |
|:------------------------------------------------------:|

## Features

---

We also added alot of **widgets**/**features** for creating modern applications. Here are the list of widgets we customize

**Button**

```py
"""
Following args for the button:

    Button(parent, string: str, color: QColor, font_color: QColor, outline: bool, shadow: bool)

You don't need to provide stylesheet for it, just pass in the arguments
in order to achieve your style.

"""
button = Button(self, "Get Started")
button.clicked.connect(lambda: print("Navigation"))

# Material Style

button = MaterialButton(self, QColor(77, 153, 239))
button.clicked.connect(lambda: print("Material Button"))

```
**LineEdit**

```python
"""
LineEdits have 2 style, the first one is with background and second has no background
It's arguments is same as QLineEdit:
     LineEdit(parent, color: QColor, background: bool)
"""
line = LineEdit(self, color=QColor(77, 153, 239), background=True)

```

**Clickable cards**

```python
"""
Clickable cards are similar to groupbox with clicking signals
and more effect. 

To connect clicked signals you may use this
"""
cards = MaterialCard(self, shadow=True)
cards.clicked.connect(lambda: print("Navigation"))
```

**Sidebar**

```python
"""
The sidebar is based on QTabWidget.
"""


sidebar = Sidebar(self)
sidebar.addTab(QWidget(), QIcon("icon.png"))
```

---

For more<u> information</u> about custom **widgets** and samples, kindly proceed in this *link*

| [Learn More](https://www.github.com/flatipie/flatipie) |
|:------------------------------------------------------:|

## Help

---

Having **troubles** or *issues* regarding to this <u>topic</u>? Join our **discord server** and chat with others! You can also follow me on **twitter**

<a href="https://discord.com/invite/SyZeeahz7E">
<img src="https://img.shields.io/discord/776701754619985950?label=Discord&logo=discord&style=flat-square"
    alt="Discord">
<a href="https://twitter.com/flatipieqt">
<img src=https://img.shields.io/twitter/follow/flatipieqt?color=%235087F4&label=Twitter&logo=twitter&style=flat-square
    alt="Twitter">

## Author

---

**Flatipie** was *created* and *maintained* in **9th day of November, 2020**.

| ![](https://www.github.com/flatipie.png?size=50) | ![](https://github.com/zenqii.png?size=50) |
|:------------------------------------------------:| ------------------------------------------- |
| [flatipie](https://www.github.com/flatipie)      | [Zenqi](https://www.github.com/zenqii)     |

## Contributors

---
![](https://www.github.com/zenqii.png?size=50)


## License

---

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
