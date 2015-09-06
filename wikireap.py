#!/usr/bin/python

from Tkinter import *
from tkMessageBox import *
from bs4 import BeautifulSoup
import requests
import re
import codecs
import textwrap

def validate():
	"""Assert input fields are sufficiently filled"""
	if e1.get() == "":
		showerror("Build Error", "Error: URL Field is empty!")
		return False
	elif e2.get() == "":
		showerror("Build Error", "Error: No Output File Selected!")
		return False
	elif e3.get() == "":
		showerror("Build Error", "No Return Margin Specified")
		return False
	else:
		return True

def fetch(url):
	"""Fetches a given URL from the Internet"""
	try:
		r = requests.get(url)
	except Exception:
		showerror("HTTP Error", "Encountered an Error while trying to retrieve the source...")
		return None
	return r


def parse(page, rm, is_build_html, is_build_latex):
	"""Parses a given Wiki page and formats it correctly"""
	wpage = BeautifulSoup(page.text)

	title = ""
	body = ""

	for i in wpage.find_all('h1'): 					
    		title += "".join(i.findAll(text=True))      

	for i in wpage.find_all('p'):
   		body += "".join(i.findAll(text=True))

	#Remove Annotations
	body = re.sub(r'\[([0-9]*)\]', r'', body) 
	#Ensure Correct .
	body = re.sub(r'[.]', r'. ', body) 
	#Ensure Correct !	 
	body = re.sub(r'[!]', r'! ', body) 
	#Ensure Correct ?	 
	body = re.sub(r'[?]', r'? ', body) 

	if (not is_build_html):
		if int(rm) != -1:
			body = textwrap.dedent(body).strip()          
			body = textwrap.fill(body, width=int(rm))
			if (not is_build_latex):
				title = title.center(int(rm))    
				title += "\n "
	
	return [title,body]	


def build_plaintext():
	if validate() == False:
		return None

	url = e1.get()
	of = e2.get()
	rm = e3.get()

	output = parse(fetch(url),rm, False, False)
	
	try:
		fo = codecs.open(of, 'wb','utf-8')
	except Exception:
		showerror("File Write Error", "Could not write file. Possibly no more space or no permissions for the accessed folder.")
		return None
	fo.write(output[0])
	fo.write(output[1])
	fo.close
	showinfo('Process Completed', 'Wiki Reaped.')

def build_html():
	if validate() == False:
		return None

	url = e1.get()
	of = e2.get()
	rm = e3.get()

	output = parse(fetch(url),rm, True, False)
	try:
		fo = codecs.open(of, 'wb','utf-8')
	except Exception:
		showerror("File Write Error", "Could not write file. Possibly no more space or no permissions for the accessed folder.")
		return None
	fo.write("<html>\n")
	fo.write("\t<head>\n")
	fo.write("\t\t<title>")
	fo.write(output[0].strip())
	fo.write("</title>\n")
	fo.write("\t</head>")
	fo.write("\t<body>\n")
	fo.write("\t\t<center><h1>")
	fo.write(output[0])
	fo.write("</h1></center>\n")
	fo.write("\t\t<hr>\n")
	fo.write("\t\t<p>")
	fo.write(output[1])
	fo.write("</p>\n")
	fo.write("\t</body>\n")
	fo.write("</html>")
	fo.close
	showinfo('Process Completed', 'Wiki Reaped.')

def build_latex():
	if validate() == False:
		return None
	
	url = e1.get()
	of = e2.get()
	rm = e3.get()

	output = parse(fetch(url),rm, False, True)

	try:
		fo = codecs.open(of, 'w','utf-8')
	except Exception:
		showerror("File Write Error", "Could not write file. Possibly no more space or no permissions for the accessed folder.")
		return None
	fo.write("""
	\\documentclass[11pt]{article}
	\\title{\\textbf{""")
	fo.write(output[0].strip())
	fo.write("""}}
	\\date{}
	\\begin{document}
	\\maketitle
	\\begin{verbatim}""")
	fo.write(output[1])
	fo.write("""
	\\end{verbatim}
	\\end{document}""")
	fo.close
	showinfo('Process Completed', 'Wiki Reaped.')


def build_pdf():
	if validate() == False:
		return None
	
	url = e1.get()
	of = e2.get()
	rm = e3.get()

	output = parse(fetch(url),rm, False, True)

	try:
		fo = codecs.open(ofile, 'w','utf-8')
	except Exception:
		showerror("File Write Error", "Could not write file. Possibly no more space or no permissions for the accessed folder.")
		return None
	fo.write("""
	\\documentclass[11pt]{article}
	\\title{\\textbf{""")
	fo.write(output[0].strip())
	fo.write("""}}
	\\date{}
	\\begin{document}
	\\maketitle
	\\begin{verbatim}""")
	fo.write(output[1])
	fo.write("""
	\\end{verbatim}
	\\end{document}""")
	fo.close
	showinfo('Process Completed', 'Wiki Reaped.')
	try:
		call(["pdflatex", options.out])
	except Exception:
		showerror("Build Error", "Latex->PDF is an Experimental Feature and is Platform Dependent (works on GNU/Linux with PDFLatex Package installed). Program not found or an error occured while building.")
		return None


def about_wikireap():
	showinfo('About WikiReap', 'WikiReap is a free and open source wiki \"note-ifier\" licensed under the GPLv3.0 or later. Fork us on Github! http://www.github.com/linearInsanity/WikiReap/')


def about_authors():
	showinfo('Created By...', 'WikiReap was created by Keiran Rowan (affiliated with Chord Development Studios LLC.) as a side project. You can find WikiReap and other softwares alike at my Github: http://www.github.com/linearInsanity/')


if __name__ == '__main__':
	root = Tk()
	menu = Menu(root)

	root.config(menu=menu)
	root.title("WikiReap")
   	root["padx"] = 30
   	root["pady"] = 20 

	filemenu = Menu(menu)
	menu.add_cascade(label="File", menu=filemenu)
	filemenu.add_command(label="Exit", command=root.quit)

	buildmenu = Menu(menu)
	menu.add_cascade(label="Build", menu=buildmenu)
	buildmenu.add_command(label="Plaintext", command=build_plaintext)
	buildmenu.add_command(label="HTML", command=build_html)
	buildmenu.add_command(label="Latex", command=build_latex)
	buildmenu.add_command(label="PDF", command=build_pdf)

	aboutmenu= Menu(menu)
	menu.add_cascade(label="About", menu=aboutmenu)
	aboutmenu.add_command(label="About WikiReap...", command=about_wikireap)
	aboutmenu.add_command(label="Created by...", command=about_authors)
	
	Label(root, text="Source URL").grid(row=0)
	Label(root, text="Output File").grid(row=1)
	Label(root, text="Return Margin").grid(row=2)

	e1 = Entry(root)
	e2 = Entry(root)
	e3 = Entry(root)

	e1.grid(row=0, column=1)
	e2.grid(row=1,column=1)
	e3.grid(row=2,column=1)

	root.mainloop()

	
	
