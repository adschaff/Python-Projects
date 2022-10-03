import tkinter as tk
from tkinter import *
import webbrowser
import os




class ParentWindow(Frame): #creates the frame ands tyling of my generator
    def __init__(self, master): 
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.name_label = tk.Label(root, text = 'Enter custom text or click the Default HTML page button', width=40)
        self.name_label.grid(row=1,column=0)
        self.name_entry = tk.Entry(root,width=30, bg="black")
        self.name_entry.grid(row=1,column=1)
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10, 10) , pady=(10,10), row=2, column=0)
        self.btn = Button(self.master, text="Custom Text", width=30, height=2, command=self.customHTML)
        self.btn.grid(padx=(10, 10) , pady=(10,10), row=2, column=1)

    def defaultHTML(self): #First function for the default HTML template
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open('file://' + os.path.realpath('index.html')) #While this command does not match the original -- this is mac specific

    def customHTML(self): #Second function for the custom HTML template
        user_text = self.name_entry.get()
        htmlcode = "<html>\n<body>\n<h1>" + user_text +"</h1>\n</body>\n</html>"
        f = open("index.html", "w")
        f.write(htmlcode)
        f.close()
        webbrowser.open('file://' + os.path.realpath('index.html'))
        
    


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
