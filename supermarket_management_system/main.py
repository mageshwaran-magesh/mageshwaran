from tkinter import *
import sqlite3
from tkinter import messagebox
import datetime
import os
import random

conn=sqlite3.connect("C:\\Users\seshu kutty\Desktop\supermarket_management_system\database\store.db")
cur=conn.cursor()

#date
date=datetime.datetime.now().date()

#temperary variabe to store the data
products_list=[]
products_price=[]
products_quantity=[]
products_id=[]

#list labels
labels_list=[]

class application:
    def __init__(self,master,*args,**kwargs):
        self.master=master

        #frames
        self.left_frame=Frame(master,width=750,height=750,bg="lightblue")
        self.left_frame.pack(side=LEFT)

        self.right_frame=Frame(master,width=600,height=750,bg="white")
        self.right_frame.pack(side=RIGHT)

        #components
        self.heading=Label(self.left_frame,text="Welcome to the store",font=("arial",40,"bold"),bg="lightblue")
        self.heading.place(x=0,y=0)

        self.date_label=Label(self.right_frame,text="Today's date:"+ str(date),font=("arial",14,"bold"),bg="white",fg="black")
        self.date_label.place(x=0,y=0)

        #right frame table invoice
        self.product_label=Label(self.right_frame,text="products",font=("arial",18,"bold"),bg="white",fg="black")
        self.product_label.place(x=0,y=40)

        self.quantity_label=Label(self.right_frame,text="Quantity",font=("arial",18,"bold"),bg="white",fg="black")
        self.quantity_label.place(x=200,y=40)

        self.amount_label=Label(self.right_frame,text="Amount",font=("arial",18,"bold"),bg="white",fg="black")
        self.amount_label.place(x=400,y=40)

        #left frame label
        self.id_label=Label(self.left_frame,text="Enter product's Id",font=("arial",18,"bold"),bg="lightblue",fg="black")
        self.id_label.place(x=0,y=65)

        self.id_entry=Entry(self.left_frame,width=25,font=("arial",18,"bold"),bg="white")
        self.id_entry.place(x=240,y=68)
        self.id_entry.focus()

        self.btn_search=Button(self.left_frame,text="Search",width=10,font=("arial",18,"bold"),bg="orange",fg="black",command=self.show)
        self.btn_search.place(x=450,y=120)

        #show the products name and price when click id
        self.product_name=Label(self.left_frame,text="",font=("arial",18,"bold"),bg="lightblue",fg="black")
        self.product_name.place(x=0,y=200)

        self.product_price=Label(self.left_frame,text="",font=("arial",18,"bold"),bg="lightblue",fg="black")
        self.product_price.place(x=0,y=240)

    #function for search button
    def show(self,*args,**kwargs):
        self.get_id=self.id_entry.get()
        #get the information product name and price when click the id
        query="select * from inventory where id=?"
        result=cur.execute(query, (self.get_id, ))
        for self.i in result:
            self.get_id=self.i[0]
            self.get_name=self.i[1]
            self.get_price=self.i[4]
            self.get_stock=self.i[2]
        self.product_name.configure(text="Product's Name: " + str(self.get_name))
        self.product_price.configure(text="Price: Rs." + str(self.get_price))

        #create the quantity label
        self.qty_label=Label(self.left_frame,text="Quantity",font=("arial",18,"bold"),bg="lightblue")
        self.qty_label.place(x=0,y=295)

        self.qty_entry=Entry(self.left_frame,width=25,font=("arial",18,"bold"),bg="white")
        self.qty_entry.place(x=120,y=300)
        self.qty_entry.focus()

        #create the discount label
        self.discount_label=Label(self.left_frame,text="Discount",font=("arial",18,"bold"),bg="lightblue")
        self.discount_label.place(x=0,y=350)

        self.discount_entry=Entry(self.left_frame,width=25,font=("arial",18,"bold"),bg="white")
        self.discount_entry.place(x=120,y=355)
        self.discount_entry.insert(END,0)

        #create label for total right frame
        self.total_amt_label=Label(self.right_frame,text="",font=("arial",23,"bold"),bg="white",fg="black")
        self.total_amt_label.place(x=0,y=550)

        #create add to card button
        self.add_to_card_btn=Button(self.left_frame,text="Add to cart",width=15,height=2,font=("arial",10,"bold"),bg="orange",command=self.add_items)
        self.add_to_card_btn.place(x=450,y=400)

        #create generate bill and change
        self.change_label=Label(self.left_frame,text="Given amount",font=("arial",18,"bold"),bg="lightblue")
        self.change_label.place(x=0,y=450)

        self.change_entry=Entry(self.left_frame,width=20,font=("arial",18,"bold"),bg="white")
        self.change_entry.place(x=180,y=450)

        #create button for change button and calculate button
        self.change_btn=Button(self.left_frame,text="Calculate",width=10,height=2,font=("arial",10,"bold"),bg="orange",command=self.change_func)
        self.change_btn.place(x=450,y=500)

        self.bill_btn=Button(self.left_frame,text="Generate Bill",width=20,height=2,font=("arial",15,"bold"),bg="green",command=self.generate_bill)
        self.bill_btn.place(x=0,y=550)

    
    #function for add to cart buton
    def add_items(self,*args,**kwargs):
        #get the quantity value from database
        self.quantity_value=int(self.qty_entry.get())

        if self.quantity_value > int(self.get_stock):
            messagebox.showerror("Error","Out of the stock in inventory!")
        else:
            #calculate the price 
            self.final_price=(float(self.quantity_value) * float(self.get_price)) -(float(self.discount_entry.get()))
            products_list.append(self.get_name)
            products_price.append(self.final_price)
            products_quantity.append(self.quantity_value)
            products_id.append(self.get_id)

            #to print the bill and calculate the amount
            self.index_y=100
            self.count=0
            for i in products_list:
                self.name=Label(self.right_frame,text=str(products_list[self.count]),font=("arial",18,"bold"),bg="white",fg="black")
                self.name.place(x=0,y=self.index_y)
                labels_list.append(self.name)

                self.quantity=Label(self.right_frame,text=str(products_quantity[self.count]),font=("arial",18,"bold"),bg="white",fg="black")
                self.quantity.place(x=300,y=self.index_y)
                labels_list.append(self.quantity)

                self.costprice=Label(self.right_frame,text=str(products_price[self.count]),font=("arial",18,"bold"),bg="white",fg="black")
                self.costprice.place(x=500,y=self.index_y)
                labels_list.append(self.costprice)

                self.index_y+=30
                self.count+=1

                #total configure
                self.total_amt_label.configure(text="Total: Rs." + str(sum(products_price)))

                #delete  after inserted
                self.qty_label.place_forget()
                self.qty_entry.place_forget()
                self.discount_label.place_forget()
                self.discount_entry.place_forget()
                self.product_name.configure(text="")
                self.product_price.configure(text="")
                self.add_to_card_btn.destroy()
                

                #autofocus on id
                self.id_entry.focus()
                self.id_entry.delete(0,END)


    #function for change button
    def change_func(self,*args,**kwargs):
        #get the amount given by customer and give the balance amount
        self.given_amount=float(self.change_entry.get())
        self.total=float(sum(products_price))

        self.balance=self.given_amount - self.total

        #label for balance
        self.balance_amt_label=Label(self.left_frame,text="Balance amount: Rs." + str(self.balance),font=("arial",18,"bold"),bg="lightblue",fg="black")
        self.balance_amt_label.place(x=0,y=500)

    #function for bill button
    def generate_bill(self,*args,**kwargs):

        #-------------------------------------------------------------------------------------------
        #create the bill before update the database
        directory="C:/Users/seshu kutty/Desktop/supermarket_management_system/invoice_bill/" + str(date)

        if os.path.exists(directory):
            os.makedirs(directory)

        #templates the bill
        store_name="\t\t\t\twelcome to the store\n"
        store_address="\t\t\t\t\t\t\t2,aaa road\n"
        phone="\t\t\t\t\t\t\t1234567890\n"
        dt="\t\t\t\t\t\t\t" + str(date)

        table_header="\n\n\t\t\t------------------------------------------\n\t\t\tS.No\tproducts\tquantity\t\tamount\n\t\t\t------------------------------------------"
        final= store_name + store_address + phone + dt + "\n" + table_header

        #open a file  to write to 
        file_name=str(directory) + str(random.randrange(5000,10000)) + ".rtf"
        f=open(file_name, "w")
        f.write(final)

        # to print the bill
        r=1
        i=0
        for x in products_list:
            f.write("\n\t\t\t" + str(r) +"\t" + str(products_list[i] + ".........")[:10] +"\t\t" + str(products_quantity[i]) + "\t\t" + str(products_price[i]))
            i +=1
            r +=1

        f.write("\n\n\t\t\t\t\t\t\t Total: Rs." + str(sum(products_price)))
        f.write("\n\n\t\t\t\t\tThank you visit again!")
        f.close()

    # -------------------------------------------------------------
        # to decrease the stock
        self.x = 0

        query="select * from inventory where id=?"
        result=cur.execute(query,(products_id[self.x], ))

        for i in products_list:
            for j in result:
                self.old_stock=j[2]
            self.new_stock= int(self.old_stock) - int(products_quantity[self.x])

            #update the stock
            sql="UPDATE inventory SET stock=? WHERE id=?"
            cur.execute(sql, (self.new_stock, products_id[self.x]))
            conn.commit()
            
            #insert into the trasaction 
            sql2="INSERT INTO `transaction` (products_name, quantity, amount, date) VALUES (?, ?, ?, ?)"
            cur.execute(sql2, (products_list[self.x], products_quantity[self.x], products_price[self.x], date))
            conn.commit()

            self.x += 1
        for a in labels_list:
            a.destroy()
        

        del(products_id[:])
        del(products_list[:])
        del(products_quantity[:])
        del(products_price[:])

        self.total_amt_label.configure(text="")
        self.change_label.configure(text="")
        self.change_entry.delete(0,END)
        self.id_entry.focus()
            
        
        messagebox.showinfo("generate bill","done")


window=Tk()
my_obj=application(window)

screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")
window.mainloop()