
import  json
from tkinter import *

class Mainapplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        

    def deserialiser(filePath):
        con = open(filePath, "r")
        li = json.loads(con.read())
        con.close()
        return li

    def runFunctionFromString(funcString):
        exec(funcString)
        return

    def addbuttons(self):
        funcList = self.deserialiser("Funcs.json")
        buttons = []
        for i in range(len(funcList)):
            add = Button(text=funcList[i][0], command=lambda i=i :self.runFunctionFromString(funcList[i][1]))
            buttons.append(add)
            buttons[i].pack()


if __name__ == "__main__":
    root = Tk()
    Mainapplication(root).pack(fill="both", expand=True)
    Mainapplication.addbuttons(Mainapplication)
    root.title("Server")
    root.mainloop()

