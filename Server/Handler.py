import json as js
import os
def collect():
    files = []
    with open("Server\Data\Funcs.json", 'r+') as file:
        parentList = js.load(file)
        for filename in os.listdir('Server\Data'):
            if filename != 'Funcs.json':
                with open('Server\Data\%s' % filename, 'r') as tempfile:
                    files.append(js.load(tempfile))
                os.remove('Server\Data\%s' % filename)
        modList = parentList
        for i in range(len(files)):
            modList = modList + files[i]
        file.seek(0)
        js.dump(modList, file)