from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk




class Customer:
    def __init__(self,root):
        self.root=root
        self.root.title("customer window")
        self.root.geometry("1315x611+280+185")
        
        #======================title====================================
 
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS", font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4 ,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1310,height=50)
        
        
        
 #=========================logo=======================================
        img2=Image.open(r"c:\Users\visha\OneDrive\Pictures\Saved Pictures\download.png")
        img2=img2.resize((345,250))
        #img2=img2.resize((200,30))
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=1,relief=RIDGE)
        lblimg.place(x=0,y=0,width=155,height=50)


#===================label Frame ================================================
       
        LabelFrame=Label(self.root,bd=5,relief=RIDGE)
        LabelFrame.place(x=5,y=55,width=425,height=553)
        
        custLabel=Label(self.root,text="Customer Details",font=("times new roman",9,"bold"))
        custLabel.place(x=10,y=47)
        
#============================ label and entitys  ==================================================

        # customer Refrence NO         
        refrenceNo=Label(LabelFrame,text="Customer Referene" ,bd=2,relief=RIDGE,font=("times new roman",13,"bold"))
        refrenceNo.grid(row=0,column=0,sticky=W,pady=7,padx=5)        
        refEntry=ttk.Entry(LabelFrame,width=2,font=("time new roman",12,"bold"))
        refEntry.grid(row=0,column=0,sticky=N,padx=170,pady=10,ipadx=70)
        
        
        # customer name         
        customerName=Label(LabelFrame,text="Customer Name" ,bd=2,relief=RIDGE,font=("times new roman",13,"bold"))
        customerName.grid(row=1,column=0,sticky=W,pady=10,padx=5)        
        customerNameEntry=ttk.Entry(LabelFrame,width=2,font=("time new roman",12,"bold"))
        customerNameEntry.grid(row=1,column=0,sticky=N,padx=170,pady=7,ipadx=70)
        
        # Mother name        
        motherName=Label(LabelFrame,text="Mother Name" ,bd=2,relief=RIDGE,font=("times new roman",13,"bold"))
        motherName.grid(row=2,column=0,sticky=W,pady=10,padx=5)        
        motherNameEntry=ttk.Entry(LabelFrame,width=2,font=("time new roman",12,"bold"))
        motherNameEntry.grid(row=2,column=0,sticky=N,padx=170,pady=10,ipadx=70)
        
        #gender
        gender=Label(LabelFrame,text="Gender" ,bd=2,relief=RIDGE,font=("times new roman",13,"bold"))
        gender.grid(row=3,column=0,sticky=W,pady=10,padx=5)                
        combo_gender=ttk.Combobox(LabelFrame,font=("times new roman",13,"bold"),width=16,state="readonly")
        combo_gender["value"]=("Male","female","other")
        # combo_gender.current(0)
        combo_gender.grid(row=3,column=0)
        
        #postcode
        postcode=Label(LabelFrame,text="Post Code" ,bd=2,relief=RIDGE,font=("times new roman",13,"bold"))
        postcode.grid(row=4,column=0,sticky=W,pady=10,padx=5)        
        postcodeEntry=ttk.Entry(LabelFrame,width=2,font=("time new roman",12,"bold"))
        postcodeEntry.grid(row=4,column=0,sticky=N,padx=170,pady=7,ipadx=70)
        
        #mobile NO
        mobileNo =Label(LabelFrame,text="Mobile NO." ,bd=2,relief=RIDGE,font=("times new roman",13,"bold"))
        mobileNo.grid(row=5,column=0,sticky=W,pady=10,padx=5)        
        mobileNoEntry=ttk.Entry(LabelFrame,width=2,font=("time new roman",12,"bold"))
        mobileNoEntry.grid(row=5,column=0,sticky=N,padx=170,pady=7,ipadx=70)
        
        #Email
        email =Label(LabelFrame,text="Email Id" ,bd=2,relief=RIDGE,font=("times new roman",13,"bold"))
        email.grid(row=6,column=0,sticky=W,pady=10,padx=5)        
        emailEntry=ttk.Entry(LabelFrame,width=2,font=("time new roman",12,"bold"))
        emailEntry.grid(row=6,column=0,sticky=N,padx=170,pady=7,ipadx=70)
        
        
        #nationlity
        nationality =Label(LabelFrame,text="Nationality" ,bd=2,relief=RIDGE,font=("times new roman",13,"bold"))
        nationality.grid(row=7,column=0,sticky=W,pady=10,padx=5)        
        nationalityEntry=ttk.Entry(LabelFrame,width=2,font=("time new roman",12,"bold"))
        nationalityEntry.grid(row=7,column=0,sticky=N,padx=170,pady=7,ipadx=70)
        
        combo_nationslity=ttk.Combobox(LabelFrame,font=("times new roman",13,"bold"),width=16,state="readonly")
        combo_nationslity["value"]=("Indian","American","Russian","other")
        # combo_nationslity.current(0)
        combo_nationslity.grid(row=7,column=0)
        
        #id proof type
        idProof =Label(LabelFrame,text="Id Proof Type" ,bd=2,relief=RIDGE,font=("times new roman",13,"bold"))
        idProof.grid(row=8,column=0,sticky=W,pady=10,padx=5)        
        combo_idProof=ttk.Combobox(LabelFrame,font=("times new roman",13,"bold"),width=16,state="readonly")
        combo_idProof["value"]=("Adharcard","Driving Licence","Password","other")
        # combo_idProof.current(0)
        combo_idProof.grid(row=8,column=0)
        
        #id NO
        idNo =Label(LabelFrame,text="Id NO." ,bd=2,relief=RIDGE,font=("times new roman",13,"bold"))
        idNo.grid(row=9,column=0,sticky=W,pady=10,padx=5)        
        idNoEntry=ttk.Entry(LabelFrame,width=2,font=("time new roman",12,"bold"))
        idNoEntry.grid(row=9,column=0,sticky=N,padx=170,pady=7,ipadx=70)
        
        #Address
        address =Label(LabelFrame,text="Address" ,bd=2,relief=RIDGE,font=("times new roman",13,"bold"))
        address.grid(row=10,column=0,sticky=W,pady=10,padx=5)        
        addressEntry=ttk.Entry(LabelFrame,width=2,font=("time new roman",12,"bold"))
        addressEntry.grid(row=10,column=0,sticky=N,padx=170,pady=7,ipadx=70)
        
        
#================= button layouts start from here ===========================================
        
        btn_frame=Frame(LabelFrame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=500,height=40,width=415)
        
        
        buttonAdd=Button(btn_frame,text="Add",cursor="hand1",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        button1=buttonAdd.grid(row=0,column=0,padx=1)
       
        
        buttonUpdate=Button(btn_frame,text="Add",cursor="hand1",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        buttonUpdate=buttonUpdate.grid(row=0,column=1,padx=2)
        
        buttonDelete=Button(btn_frame,text="Add",cursor="hand1",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        buttonDelete=buttonDelete.grid(row=0,column=2,padx=2)
        
        buttonReset=Button(btn_frame,text="Add",cursor="hand1",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        buttonReset=buttonReset.grid(row=0,column=3,padx=1)
        

#=========================== table frame ===========================================width=> 1315-425=890
       
        
        tabel_frame=Label(self.root,bd=5,relief=RIDGE,font=("arial",12,"bold"),pady=20)
        tabel_frame.place(x=425,y=47,width=881,height=563,)
        
        tabel_title=Label(self.root,text="View Details and Search History",font=("arial",14,"bold"),bg="black",fg="white")
        tabel_title.place(x=780,y=35)        
        
        
        lblSearch=Label(tabel_frame,font=("arial",12,"bold"),text="Search By",bg="red",fg="white")
        lblSearch.grid(row=0,column=0,sticky=W,pady=20)
        
        combo_Search=ttk.Combobox(tabel_frame,font=("times new roman",13,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Mobile","Refrence")
        combo_Search.grid(row=0,column=1,padx=20)
        
        SearchEntry=ttk.Entry(tabel_frame,width=2,font=("time new roman",12,"bold"))
        SearchEntry.grid(row=0,column=3,sticky=N,ipadx=100,pady=20)
        
        buttonSearch=Button(tabel_frame,text="Add",cursor="hand1",font=("arial",11,"bold"),bg="green",fg="white",width=10)
        buttonSearch=buttonSearch.grid(row=0,column=4,padx=5)
        
        buttonShowAll=Button(tabel_frame,text="Add",cursor="hand1",font=("arial",11,"bold"),bg="green",fg="white",width=10)
        buttonShowAll=buttonShowAll.grid(row=0,column=5,padx=5)
        
#=========================================== show data tables=============================================

        details_Tabel=Label(tabel_frame,bd=5,relief=RIDGE,font=("arial",12,"bold"),pady=20)
        details_Tabel.place(x=0,y=48,width=860,height=460,)   
        
        
        
        scroll_x=ttk.Scrollbar(details_Tabel,orient=HORIZONTAL)   
        scroll_y=ttk.Scrollbar(details_Tabel,orient=VERTICAL)
        
        self.Cust_Details_Table=ttk.Treeview(details_Tabel,columns=("Ref","Name","Mother","Gender","PostCode","Mobile","Email","Nationality","Id Proof","IdNo","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)
        
        self.Cust_Details_Table.heading("Ref",text="Ref")
        self.Cust_Details_Table.heading("Name",text="Name")
        self.Cust_Details_Table.heading("Mother",text="Mother")
        self.Cust_Details_Table.heading("Gender",text="Gender")
        self.Cust_Details_Table.heading("PostCode",text="PostCode")
        self.Cust_Details_Table.heading("Mobile",text="Mobile")
        self.Cust_Details_Table.heading("Email",text="Email")
        self.Cust_Details_Table.heading("Nationality",text="Nationality")
        self.Cust_Details_Table.heading("Id Proof",text="IdProof")
        self.Cust_Details_Table.heading("IdNo",text="Id No")
        self.Cust_Details_Table.heading("Address",text="Address")
        
        
        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column("Ref",width=100)
        self.Cust_Details_Table.column("Name",width=100)
        self.Cust_Details_Table.column("Mother",width=100)
        self.Cust_Details_Table.column("Gender",width=100)
        self.Cust_Details_Table.column("PostCode",width=100)
        self.Cust_Details_Table.column("Mobile",width=100)
        self.Cust_Details_Table.column("Email",width=100)
        self.Cust_Details_Table.column("Nationality",width=100)
        self.Cust_Details_Table.column("Id Proof",width=100)
        self.Cust_Details_Table.column("IdNo",width=100)
        
        
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        
        




        
        
if __name__=="__main__":
    root=Tk()
    obj=Customer(root)
    root.mainloop()
        