# WikiReap

> Note: I have plans to move WikiReap over to the C programming language from python. It will use the libCurl to fetch webpages and libTidy to parse the webpage. This should result in faster, smaller, and compilable code.

![](https://github.com/bitwisekibbles/wikireap/blob/master/.resources/gui.png "Tk Interface on Mac OS X")

WikiReap is a tool that can be used to turn information from Wiki pages into notes. WikiReap has a graphical user interface and works with all major operating systems. 

## Features

WikiReap is designed to be modular, lightweight, and intuitive. Many of it's features are composed into seperate files. The main implementation of WikiReap is actually just a library called `libWikiReap`. This makes building on top of it especially easy because of the fact that you can call WikiReap functions from any compatable environment including: C Programs, Foreign Function Interfaces, <Language> Bindings, etc.

#### Modular


