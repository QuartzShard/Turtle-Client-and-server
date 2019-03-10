
import  json
from tkinter import *

def deserialiser(filePath):
    con = open(filePath, "r")
    li = json.loads(con.read())
    con.close()
    return li

def runFunctionFromString(funcString):
    exec(funcString)
    return

fullList = deserialiser("Funcs.json")

root = Tk()
buttons = []
for i in range(len(fullList)):
    add = Button(text=fullList[i][0], command=lambda i=i :runFunctionFromString(fullList[i][1]))
    buttons.append(add)
    buttons[i].pack()

root.mainloop()



