from tkinter import *

class Details:
    def __init__(self,root):
         self.root=root
         self.root.title("customer window")
         self.root.geometry("1265x560+285+230")


if __name__ =="__main__":
    root=Tk()
    obj=Details(root)
    root.mainloop()