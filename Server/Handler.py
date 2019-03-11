import json as js
import os
def collect():
    files = []
    with open("Data\Funcs.json", 'r+') as file:
        parentList = js.load(file)
        for filename in os.listdir('Data'):
            if filename != 'Funcs.json':
                with open('Data\%s' % filename, 'r') as tempfile:
                    files.append(js.load(tempfile))
                os.remove('Data\%s' % filename)
        modList = parentList
        for i in range(len(files)):
            modList = modList + files[i]
        file.seek(0)
        js.dump(modList, file)
        file.truncate()

def prune():
    with open("Data\Funcs.json", 'r+') as file:
        funcs = js.load(file)
        curPos = 0
        length = len(funcs)-1
        while curPos < length:
            for j in range(len(funcs)):
                if curPos != j:
                    if funcs[curPos][0] == funcs[j][0]:
                        del funcs[curPos]
                        break
            length = len(funcs)-1
            curPos += 1
        file.seek(0)            
        js.dump(funcs, file)  
        file.truncate()