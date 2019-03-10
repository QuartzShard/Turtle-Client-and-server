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

for i in fullList:
    Button(text=i[0], command=lambda:runFunctionFromString(i[1]) ).pack()

root.mainloop()

