import tkinter as tk
import json as js 
import io
import time
from ftplib import FTP as ft 

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.label = tk.Label(root, text = "Name of program:")
        self.label2 = tk.Label(root, text = "Team Name:")
        self.label3 = tk.Label(root, text = "Server address")
        self.entryBox = tk.Entry(root)
        self.entryBox2 = tk.Entry(root)
        self.entryBox3 = tk.Entry(root)
        self.label.grid(row = 0)
        self.entryBox.grid(column = 1, row = 0)
        self.label2.grid(row = 1)
        self.entryBox2.grid(column = 1, row = 1)
        self.label3.grid(row = 2)
        self.entryBox3.grid(column = 1, row = 2)
        self.button = tk.Button(root, text="Send to Server", command = lambda: [self.sendToServer(self.entryBox.get(), self.entryBox2.get(), self.entryBox3.get()), self.entryBox.delete(0,tk.END), self.entryBox2.delete(0, tk.END), self.entryBox3.delete(0,tk.END)] )
        self.button.grid(column = 1, row = 3)
    
    def sendToServer(self, program, name, address):
        if program[-3:] != '.py':
            program = program + '.py'
        with open(program, "r") as pyFile: 
            programConts = pyFile.read()
        toJson = [name, programConts]
        connectionObj = ft(address)
        connectionObj.login()
        JSONObj = []
        connectionObj.retrbinary('RETR Funcs.json', JSONObj.append)
        PyObj = js.loads(JSONObj[0])
        PyObj.append(toJson)
        toSend = js.dumps(PyObj)
        connectionObj.storbinary('STOR %s.json' % name, io.BytesIO(toSend.encode('utf-8')))
        

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).grid(columnspan=2,rowspan=3)
    root.title("Send to Server Widget")
    root.mainloop()
