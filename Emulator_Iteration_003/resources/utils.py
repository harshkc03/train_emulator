def gridConfigure(rows,columns,root):
        root.update()
        for x in range(rows):
            root.rowconfigure(x,weight=1,minsize=(root.winfo_height()/rows))
        for x in range(columns):
            root.columnconfigure(x,weight=1,minsize=(root.winfo_width()/columns))

def getKey(val,myDict):
        for key,value in myDict.items():
            if val==value :
                return key


defaultFont="Calibri 15"