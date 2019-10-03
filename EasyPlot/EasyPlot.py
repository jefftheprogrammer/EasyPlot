# EasyPlot
# By Mihai Stefan Merlas
# Allows user to easily make plots
# v2.0
#############################
# header
# var name
# units
import matplotlib.pyplot as plt
import xlrd as excel

class DataFromFile():
    def __init__(self):
        self.filename = None
        
    @staticmethod
    def find_file(self):# loads file
        self.filename = input("enter filename")
        wb = excel.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        return sheet

    
        

class Graph:
    def __init__(self, data_x, data_y, x_label, y_label):
        self.data_x = data_x# data is inputted into the self.data var
        self.data_y = data_y
        self.x_label = x_label
        self.y_label = y_label

    @staticmethod
    def choose_marker():
        print(""" .:point
,:pixel
o:circle
v:triangle down
^:triangle up
<:triangle left
>:triangle right
1:tri down
2:tri up
3:tri left
4:tri right
p:plus (thick)
+:plus
X:X (thick)
x:X
D:diamond (thick)
d:diamond
|:vertical line
_:horizontal line
""")
    def scatterPlot(self):
        Graph.choose_marker()
        plt.plot(self.data_x, self.data_y, 'ro')
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.show()

g = Graph([1,2,3,4],[2,4,6,8],'x','y')
g.scatterPlot()
