from tkinter import *

class CustomFrame(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)       

    def placeInGrid(self,widget,row,column,rowspan=1,columnspan=1):
        if (row<self.numberOfRows and column<self.numberOfColumns):
            widget.place(relx=self.cellWidth*column,rely=self.cellHeight*row,relwidth=self.cellWidth,relheight=self.cellHeight)
        else:
            self.numberOfRows=row+1
            self.numberOfColumns=column+1
            widget.place(relx=self.cellWidth*column,rely=self.cellHeight*row,relwidth=self.cellWidth,relheight=self.cellHeight)

    numberOfRows=1
    numberOfColumns=1
    cellWidth=(1/numberOfColumns)
    cellHeight=(1/numberOfRows)


class GridParameters:
    def __init__(self,widget,row,column,width,height):
        self.master=widget
        self.widgetRow=row
        self.widgetColumn=column
        self.widgetWidth=width
        self.widgetHeight=height

    def getRow(self):
        return self.widgetRow