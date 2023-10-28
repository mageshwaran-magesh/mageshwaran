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
        self.heading=Label(master,text="update the database",font=("arial",40,'bold'),fg='lightGreen')
        self.heading.place(x=400,y=0) 

        #lable for id and entry
        self.id_label=Label(master,text="Enter ID",font=("arial",18,'bold'))
        self.id_label.place(x=0,y=80)

        self.id_entry=Entry(master,font=("arial",18,'bold'),width=10)
        self.id_entry.place(x=370,y=80)

        self.btn_search=Button(master,text="Search",width=15,height=2,bg="lightgreen",fg="white",command=self.search)
        self.btn_search.place(x=550,y=75)


        #labels and entries
        self.name_label=Label(master,text="Enter product name", font=("arial",18,'bold'))
        self.name_label.place(x=0,y=130)

        self.name_entry=Entry(master,width=25,font=("arial",18,'bold'))
        self.name_entry.place(x=370,y=130)

        self.stock_label=Label(master,text="Enter stocks", font=("arial",18,'bold'))
        self.stock_label.place(x=0,y=180)

        self.stock_entry=Entry(master,width=25,font=("arial",18,'bold'))
        self.stock_entry.place(x=370,y=180)

        self.cost_price_label=Label(master,text="Enter cost price", font=("arial",18,'bold'))
        self.cost_price_label.place(x=0,y=230)

        self.cost_price_entry=Entry(master,width=25,font=("arial",18,'bold'))
        self.cost_price_entry.place(x=370,y=230)

        self.selling_price_label=Label(master,text="Enter selling price", font=("arial",18,'bold'))
        self.selling_price_label.place(x=0,y=280)

        self.selling_price_entry=Entry(master,width=25,font=("arial",18,'bold'))
        self.selling_price_entry.place(x=370,y=280)

        self.vendor_label=Label(master,text="Enter vendor name", font=("arial",18,'bold'))
        self.vendor_label.place(x=0,y=330)

        self.vendor_entry=Entry(master,width=25,font=("arial",18,'bold'))
        self.vendor_entry.place(x=370,y=330)

        self.vendor_mob_label=Label(master,text="Enter vendor phone Number", font=("arial",18,'bold'))
        self.vendor_mob_label.place(x=0,y=380)

        self.vendor_mob_entry=Entry(master,width=25,font=("arial",18,'bold'))
        self.vendor_mob_entry.place(x=370,y=380)

        self.btn_add=Button(master,text="update Database",font=("arial",15,'bold'),width=25,height=2,bg='lightgreen',fg="white" ,command=self.update)
        self.btn_add.place(x=500,y=450)


        self.text_box=Text(master,width=60,height=20)
        self.text_box.place(x=750,y=70)
        self.text_box.insert(END, "ID has reached upto:"+ str(id))

    #function for search button
    def search(self,*args,**kwars):
        sql="select * from inventory where id=?"
        result=cur.execute(sql,(self.id_entry.get()))
        for i in result:
            self.n1=i[1] #name
            self.n2=i[2] #stock
            self.n3=i[3] #cost_price
            self.n4=i[4] #selling_price
            self.n5=i[5] #total_cp
            self.n6=i[6] #total_sp
            self.n7=i[7] #assumped_profit
            self.n8=i[8] #vendor
            self.n9=i[9] #vendor_mob
        conn.commit()

        #insert into update entries  to update
        #name entry to update
        self.name_entry.delete(0,END)
        self.name_entry.insert(0,str(self.n1))

        #stock entry to update
        self.stock_entry.delete(0,END)
        self.stock_entry.insert(0,str(self.n2))

        #cost_price entry to update
        self.cost_price_entry.delete(0,END)
        self.cost_price_entry.insert(0,str(self.n3))

        #selling_price entry to update
        self.selling_price_entry.delete(0,END)
        self.selling_price_entry.insert(0,str(self.n4))

        #vendor entry to update
        self.vendor_entry.delete(0,END)
        self.vendor_entry.insert(0,str(self.n8))

        #vendor_mob entry to update
        self.vendor_mob_entry.delete(0,END)
        self.vendor_mob_entry.insert(0,str(self.n9))

    #function for update 
    def update(self,*args,**kwargs):
    #get update all values
        self.u1=self.name_entry.get()
        self.u2=self.stock_entry.get()
        self.u3=self.cost_price_entry.get()
        self.u4=self.selling_price_entry.get()
        self.u5=float(self.u3)* float(self.u2)
        self.u6=float(self.u4) * float(self.u2)
        self.u7=float(self.u6 - self.u5)
        self.u8=self.vendor_entry.get()
        self.u9=self.vendor_mob_entry.get()
        

        query="update inventory set name=?,stock=?,cost_price=?,selling_price=?,total_cp=?,total_sp=?,assumped_profit=?,vendor=?,vendor_mob=? where id=?"
        cur.execute(query,(self.u1,self.u2,self.u3,self.u4,self.u5,self.u6,self.u7,self.u8,self.u9,self.id_entry.get()))
        conn.commit()
        messagebox.showinfo("Success","updated successfully")



window=Tk()
my_obj=database(window)        

screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")

window.title("update the database")
window.mainloop()        