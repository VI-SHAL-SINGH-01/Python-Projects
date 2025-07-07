from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from customer import Customer
from login import Login_window
from room import Room
from details import Details
from report import Report




class HotalManagementSystem: 
        
#======================= ADDING DIFFERENT WINDOWS IN ONE FORM  ============================     
        
    def customer(self):
                self.new_window=Toplevel(self.root)
                self.app=Customer(self.new_window)
    def room(self):
                self.new_window=Toplevel(self.root)
                self.app=Room(self.new_window)
    def details(self)       :
            self.new_window=Toplevel(self.root)
            self.app=Details(self.new_window)
    def report(self)       :
            self.new_window=Toplevel(self.root)
            self.app=Report(self.new_window)
    
    def Login_window(self):
                self.new_window=Toplevel(self.root)
                self.app=Login_window(self.new_window)
                          
                
                
 #=============================this file root initalization start form here =============================               
                
    def __init__(self,root):
        self.root=root
        self.root.title("Hotal")
        self.root.geometry("1600x800+0+0")               
      
        
        
        
 #=============header=================================
 
        img1=Image.open(r"c:\Users\visha\OneDrive\Pictures\Saved Pictures\Hotel-Website-Banner-Template-edit-online.png")
        img1=img1.resize((1395,100))
        self.photoimg1=ImageTk.PhotoImage(img1)        
        lblimg=Label(self.root,image=self.photoimg1,bd=3,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1800,height=100) 
 
 #=========================logo=======================================
 
        img2=Image.open(r"c:\Users\visha\OneDrive\Pictures\Saved Pictures\download.png")
        img2=img2.resize((250,100))
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE,)
        lblimg.place(x=0,y=0,width=250,height=100)
 
 
 #======================title====================================
 
        lbl_title=Label(self.root,text="Hotel Management System", font=("times new roman",30,"bold"),bg="black",fg="gold",bd=4 ,relief=RIDGE)
        lbl_title.place(x=0,y=100,width=1800,height=50)
        

#======================= main Frame (it name can be anythings)=======================

        main_frame=Frame(self.root,bd=5,relief=RIDGE,background="blue",bg="green") 
        main_frame.place(x=25,y=150,width=1570,height=750)
        
#======================== Menu ==================================
        
        lbl_menu=Label(main_frame,text="Menu", font=("time new roman ",20,"bold"),bg="black",fg="gold",relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=250,)
        
        



# #===============button frame ========================================
        
        
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=33,width=250,height=235,)
        
        
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.customer ,width=22,font=("times new roman ",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=3)
        
        room_btn=Button(btn_frame,text="Room", command=self.room,width=22,font=("times new roman ",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=3)
        
        
       
        details_btn=Button(btn_frame,text="Details",command=self.details,width=22,font=("times new roman ",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=3) 
        
        Report_btn=Button(btn_frame,text="Report",command=self.report,width=22,font=("times new roman ",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        Report_btn.grid(row=3,column=0,pady=3)
        
        logout_btn=Button(btn_frame,text="Login",command=self.Login_window, width=22,font=("times new roman ",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=3)
       
#===============================Right side image==========================================         
        img3=Image.open(r"c:\Users\visha\OneDrive\Pictures\Saved Pictures\1images.jpg")
        img3=img3.resize((1525,750))
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=250,y=0,width=1315,height=645)
        
#================================== Down images=============================================

        
        img4=Image.open(r"c:\Users\visha\OneDrive\Pictures\Saved Pictures\images (2).jpg")
        img4=img4.resize((255,200))
        self.photoimg4=ImageTk.PhotoImage(img4)        
        lblimg=Label(self.root,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=28,y=423,width=255,height=190)
        
        
        
        img5=Image.open(r"c:\Users\visha\OneDrive\Pictures\Saved Pictures\1images.jpg")
        img5=img5.resize((250,190))
        self.photoimg5=ImageTk.PhotoImage(img5)        
        lblimg=Label(self.root,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg.place(x=28,y=605,width=255,height=190)
        
        
        
        
        
if __name__ =="__main__":
    root=Tk()
    obj=HotalManagementSystem(root)
    root.mainloop()