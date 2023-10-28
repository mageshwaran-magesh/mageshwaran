from tkinter import *
import sqlite3
from tkinter import messagebox

conn=sqlite3.connect("C:\\Users\seshu kutty\Desktop\supermarket_management_system\database\store.db")
cur=conn.cursor()

result=cur.execute("select max(id)from inventory")
for i in result:
    id=i[0]

class database:
    def __init__(self,master,*args,**kwargs):

        self.master=master
        self.heading=Label(master,text="Add to the database",font=("arial",40,'bold'),fg='lightGreen')
        self.heading.place(x=400,y=0) 

        self.name_label=Label(master,text="Enter product name", font=("arial",18,'bold'))
        self.name_label.place(x=0,y=80)

        self.name_entry=Entry(master,width=25,font=("arial",18,'bold'))
        self.name_entry.place(x=370,y=80)

        self.stock_label=Label(master,text="Enter stocks", font=("arial",18,'bold'))
        self.stock_label.place(x=0,y=130)

        self.stock_entry=Entry(master,width=25,font=("arial",18,'bold'))
        self.stock_entry.place(x=370,y=130)

        self.cost_price_label=Label(master,text="Enter cost price", font=("arial",18,'bold'))
        self.cost_price_label.place(x=0,y=180)

        self.cost_price_entry=Entry(master,width=25,font=("arial",18,'bold'))
        self.cost_price_entry.place(x=370,y=180)

        self.selling_price_label=Label(master,text="Enter selling price", font=("arial",18,'bold'))
        self.selling_price_label.place(x=0,y=230)

        self.selling_price_entry=Entry(master,width=25,font=("arial",18,'bold'))
        self.selling_price_entry.place(x=370,y=230)

        self.vendor_label=Label(master,text="Enter vendor name", font=("arial",18,'bold'))
        self.vendor_label.place(x=0,y=280)

        self.vendor_entry=Entry(master,width=25,font=("arial",18,'bold'))
        self.vendor_entry.place(x=370,y=280)

        self.vendor_mob_label=Label(master,text="Enter vendor phone Number", font=("arial",18,'bold'))
        self.vendor_mob_label.place(x=0,y=330)

        self.vendor_mob_entry=Entry(master,width=25,font=("arial",18,'bold'))
        self.vendor_mob_entry.place(x=370,y=330)

        self.btn_add=Button(master,text="Add to Database",font=("arial",15,'bold'),width=25,height=2,bg='lightgreen',fg="white",command=self.get_items)
        self.btn_add.place(x=500,y=450)

        self.btn_reset=Button(master,text="Reset",width=15,height=1,font=("arial",15,'bold'),bg="lightgreen",fg="white",command=self.clear_all)
        self.btn_reset.place(x=270,y=460)

        self.text_box=Text(master,width=60,height=20)
        self.text_box.place(x=750,y=70)
        self.text_box.insert(END, "ID has reached upto:"+ str(id))
    
    #function for reset button command
    def clear_all(self, *args, **kwargs):
        num=id+1
        self.name_entry.delete(0, END)
        self.stock_entry.delete(0,END)
        self.cost_price_entry.delete(0,END)
        self.selling_price_entry.delete(0,END)
        self.vendor_entry.delete(0,END)
        self.vendor_mob_entry.delete(0,END)

    #function for add to database command
    def get_items(self,*args,**kwargs):
        #get from entries
        self.name=self.name_entry.get()
        self.stock=self.stock_entry.get()
        self.cost_price=self.cost_price_entry.get()
        self.selling_price=self.selling_price_entry.get()
        self.vendor=self.vendor_entry.get()
        self.vendor_mob=self.vendor_mob_entry.get()

        #dynamic entries 
        self.totalcp=float(self.cost_price)* float(self.stock)
        self.totalsp=float(self.selling_price) * float(self.stock)
        self.assumped_profit=float(self.totalsp - self.totalcp)

        if self.name=='' or self.stock=='' or self.cost_price=="" or self.selling_price=="":
            messagebox.showinfo("Error","please fill the all the entries!")
        else:
            sql="insert into inventory (name,stock,cost_price,selling_price,total_cp,total_sp,assumped_profit,vendor,vendor_mob) values(?,?,?,?,?,?,?,?,?)"
            cur.execute(sql,(self.name,self.stock,self.cost_price,self.selling_price,self.totalcp,self.totalsp,self.assumped_profit,self.vendor,self.vendor_mob))
            conn.commit()
            #textbox insert 
            self.text_box.insert(END,"\n\nInserted" + str(self.name)+" into the database")
            messagebox.showinfo("Success","successfully added to the database")

window=Tk()
my_obj=database(window)        

screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")

window.title("Add to the database")
window.mainloop()