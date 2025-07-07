from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Admin Login")
        self.root.geometry("1265x560+285+230")
        
        
        # image set code start here 
        
        bag=Image.open(r"c:\Users\visha\OneDrive\Pictures\project images\gif images\hotal.jpg")
        bag=bag.resize((1550,1000) )
        
        self.bg =ImageTk.PhotoImage(bag)
        lbl_bg =Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,height=1000,width=1550)
        
        
        
        
        #=====================for window frmae  code start here========================
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1=Image.open(r"C:\Users\visha\OneDrive\Pictures\img1.png")
        img1=img1.resize((100,100) )
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Admin Login",font=("tiems new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)
    
    
    #=============== fields of form start from here =============================
    
        
        #========= for username  label and input box ===================
        
        username=lbl=Label(frame,text="Username",font=('times new roman',15,"bold"),fg="white",bg="black")
        username.place(x=65,y=155)
        
        # self.txtuser=Entry(frame,font=("times new roman",15,"bold"))
        # self.txtuser.place(x=40,y=180,width=270)
        
        # if we want entery just like google fill then
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=38,y=180,width=270)
        
        #========= for Password label  and input box  ==============================
        
        
        password=lbl=Label(frame,text="Password",font=('times new roman',15,"bold"),fg="white",bg="black")
        password.place(x=65,y=225)
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
        #=========icon images for username  ==========
        
        
        img2=Image.open(r"C:\Users\visha\OneDrive\Pictures\img1.png")
        img2=img2.resize((25,25) )
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=20,height=25)
        
        #=========icon images for Password ==========
        
        img3=Image.open(r"C:\Users\visha\OneDrive\Pictures\img1.png")
        img3=img3.resize((25,25) )
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=390,width=20,height=25)
        
    
    
#============== buttons are start from here=========================

#=============login button=================
        
        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),fg="white",bg="red", command=self.login,relief=RIDGE,borderwidth=0, activebackground="red",activeforeground="white")
        loginbtn.place(x=90,y=300,width=150,height=35)
        
        
        
                #=============== REGISTATION BUTTON ==================   
        
        
        registationbtn=Button(frame,text="Register",font=("times new roman",10,"bold"),fg="white",relief=RIDGE, borderwidth=0,bg="black" ,activebackground="black",activeforeground="white")
        registationbtn.place(x=10,y=370,width=150,height=35)
        
        
#======================= fORGOT PASSWORD BUTTON ============================
                
                
        forgotPasswordbtn=Button(frame,text="Forgot Password",font=("times new roman",10,"bold"),relief=RIDGE,borderwidth=0,fg="white",bg="black" ,activebackground="black",activeforeground="white")
        forgotPasswordbtn.place(x=180,y=370,width=150,height=35)



#========================= validate and Authantaction ================================
        
        
    def login(self):
            if(self.txtuser.get()=="" or self.txtpass.get()==""):
                messagebox.showerror("error","all fields are required")
            else:
                messagebox.showinfo("success","Valid Inputs")             
        
if __name__=="__main__":
    root=Tk()
    app=Login_window(root)
    root.mainloop() 