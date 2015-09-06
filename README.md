# WikiReap

> Note: I have plans to port libWikiReap over to the C programming language from python. It will use the libCurl to fetch webpages and libTidy to parse the webpage. This should result in faster, smaller, and compilable code.

![](https://github.com/bitwisekibbles/wikireap/blob/master/.resources/gui.png "Tk Interface on Mac OS X")

WikiReap is a tool that can be used to turn information from Wiki pages into notes.

## Features

WikiReap is designed to be modular, lightweight, and intuitive. Many of it's features are composed into seperate files. The main implementation of WikiReap is actually just a library called `libWikiReap`. This makes building on top of it especially easy because of the fact that you can call WikiReap functions from any compatable environment including: C Programs, Foreign Function Interfaces, <Language> Bindings, etc.

#### Modular

![](https://github.com/bitwisekibbles/wikireap/blob/master/.resources/flavors.png "WikiReap Flavours")

Built on top of the library are the three major flavors of WikiReap. You can find these as git submodules in the root of this repository. These flavors are: Desktop (GUI and Terminal Application), Mobile (Android and iOS), and Web (PHP Website). 

#### Wrappers

Wrappers are third party programs that are not related to WikiReap's core functionality that are built on top of `libWikiReap`. One of the most notable wrappers is `Paraphrase`. Paraphrase is a seperate program that paraphrases any text piped into `stdin` or paraphrases an article fetched through `libWikiReap`.

#### Lightweight

Since WikiReap is built in C, it uses less resources than a normal program. It is also built with efficiency in mind by conciously spliting the program up into different sections. The core library, `libWikiReap`, is designed to be really efficient and have versitile use.

#### Portable

WikiReap is written using only a few (popular) libraries which have been ported to almost every major platform. `libWikiReap` is built using standard C and should work with most standards-compliant compilers.

#### Expandable

Want to use WikiReap functionality in one of your programs? `#include "libWikiReap.h`. Simple as that.
