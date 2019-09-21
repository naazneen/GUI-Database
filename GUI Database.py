from tkinter import *
from functools import partial

class SQLqueries():

    def sqlfun(s):
        print("sql function used:",s)

class Application(SQLqueries,Frame):
    
    def showenter(self):
        self.frameview.grid_remove()
        self.frameenter.grid(row=1,column=0,columnspan = 2)

    def showview(self):
        self.frameenter.grid_remove()
        self.frameview.grid(row=1,column=0,columnspan = 2)

    def createWidgets(self):
        self.enterbutton = Button(self,text = "Enter",command = self.showenter)
        self.viewbutton = Button(self,text = "View",command = self.showview)
        self.enterbutton.grid(row = 0,column = 0)
        self.viewbutton.grid(row = 0,column = 1)
        
        self.frameenter = Frame(self)
        self.frameenter.grid(row=1,column=0,columnspan = 2)

        self.frameview = Frame(self)
        self.frameview.grid(row=1,column=0,columnspan = 2)

        self.namelabel = Label(self.frameenter,text = "Name")
        self.namelabel.grid(row = 0,column = 0)
        
        self.namebox = Entry(self.frameenter,text = "")
        self.namebox.grid(row = 0,column = 1)

        self.classlabel = Label(self.frameenter,text = "Class")
        self.classlabel.grid(row = 1,column = 0)

        self.submit = Button(self.frameenter,text = "Submit",command = partial(SQLqueries.sqlfun,"arg"))
        self.submit.grid(row = 3,column = 0,columnspan = 2)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
 
