import turtle
import  json
from tkinter import *
import Handler as fix

class Mainapplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        
        

    def deserialiser(filePath):
        fix.collect()
        con = open(filePath, "r")
        li = json.loads(con.read())
        con.close()
        return li

    def runFunctionFromString(funcString):
        exec(funcString)
        return

    def addbuttons(self):
        for widget in self.winfo_children(root):
            widget.destroy()
        funcList = self.deserialiser("Data\Funcs.json")
        buttons = []
        for i in range(len(funcList)):
            add = Button(text=funcList[i][0], command=lambda i=i :self.runFunctionFromString(funcList[i][1]))
            buttons.append(add)
            buttons[i].pack()
        refresh = Button(text='refresh', command=lambda:self.addbuttons(self)).pack()
        


if __name__ == "__main__":
    root = Tk()
    Mainapplication(root).pack(fill="both", expand=True)
    Mainapplication.addbuttons(Mainapplication)
    root.title("Server")
    root.mainloop()

