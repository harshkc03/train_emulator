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

def placeGridConfigure(self,rows,columns,relWidthPadding,root):
        root.update()
        self.yPad=(((root.winfo_width())/(root.winfo_height()))*relWidthPadding)
        self.xPad=relWidthPadding
        self.rowHeight=(1/rows)-(2*self.yPad)
        self.columnWidth=(1/columns)-(2*self.xPad)

def placeInGrid(self,root,row,column,rowspan=1,columnspan=1):
        root.place(relx=column*(self.columnWidth+2*self.xPad)+self.xPad,
                                rely=row*(self.rowHeight+2*self.yPad)+self.yPad,
                                relwidth=self.columnWidth*columnspan+2*(columnspan-1)*self.xPad,
                                relheight=self.rowHeight*rowspan+2*(rowspan-1)*self.yPad)

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def convert_int(number,decimals) :
    return str(number).zfill(decimals)

def rectCoord(self,canvas,relx,rely,relheight,relwidth):
    canvas.update()
    x1=relx*canvas.winfo_width()
    y1=rely*canvas.winfo_height()

    x2=(relx+relwidth)*canvas.winfo_width()
    y2=(rely+relheight)*canvas.winfo_height()

    return (x1,y1,x2,y2)

def returnCoord(self,canvas,relx,rely):
    canvas.update()
    x1=relx*canvas.winfo_width()
    y1=rely*canvas.winfo_height()

    return (x1,y1)

defaultFont="Calibri 20"
# yellow="#ECCC11"
# red="#ff5252"
blue="#52ffff"
# blue="#2332F6"
green="#54CC11"
red="#DA4040"
white="#FFFFFF"
pink="#FF69B4"