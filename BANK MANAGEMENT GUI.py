'''make withdraw and deposit function.
make statement button.
stop to add duplicates.
add date and time of entry.
'''
from tkinter import*
from tkinter import ttk#for combo box
import sqlite3
from tkinter import messagebox as m
import datetime
    
    
class management:
    def __init__(self,root):
        self.root=root
        self.root.title("BANK MANAGEMENT SYSTEM")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="BANK MANAGEMENT SYSTEM",bd=10,relief=GROOVE,font=("times new roman",30,"bold"),bg='black',fg='white')
        title.pack(side=TOP,fill=X)

        self.Account=StringVar()
        self.name=StringVar()
        self.accno=StringVar()
        self.iniamt=IntVar()
        self.acctype=StringVar()
        self.date=StringVar()
        self.balance=IntVar()
        self.current=IntVar()
        self.withdraw=IntVar()
        


        def exit():
            qexit=m.askquestion("Quit System","Do You Want To Quit ?")
            if qexit == 'yes':
                root.destroy()
            else :
                m.showinfo('Return','You Will Now Return To The Application Screen')


        def add_account():
            con = sqlite3.connect('stem.db')
            cur=con.cursor()
            cur.execute("insert into Accounts (Account_No,Name,Type,InitialAmt,Date)values(?,?,?,?,?)",[                self.accno.get()
                                                                                                                        ,self.name.get()
                                                                                                                        ,self.acctype.get()
                                                                                                                        ,self.iniamt.get()
                                                                                                                        ,self.date.get()
                                                                                                                    
                                                                                                                        ])
            con.commit()
            con.close()
            fetch_data()
            clear()
            m.showinfo("Success","Record Added!!")


        def mdelete():
            if m.askyesno('Delete','This will permanently delete the record from the database.\nAre you sure?'):
                con = sqlite3.connect('stem.db')
                cur=con.cursor()
                cur.execute('Delete from Accounts where Account_No=?',(self.Account.get(),))
                con.commit()
                con.close()
                fetch_data()
                clear()
                m.showinfo("Success","Record Deleted!!")
            else:
                pass


        def delete_data():
            if self.Account.get()=="":
                m.showerror("ERROR","ACCOUNT NUMBER IS REQUIRED")
            else:
                mdelete()


        def search_data():
            if self.Account.get()=='':
                m.showerror("Error","ACCOUNT NUMBER IS REQUIRED")
            else:
                con = sqlite3.connect('stem.db')
                cur=con.cursor()
                cur.execute("select * from Accounts where Account_No = ?",(self.Account.get(),))
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.Student_table.delete(*self.Student_table.get_children())
                    for row in rows:
                        self.Student_table.insert('',END,values=row)
                    con.commit()
                con.close()
                

        def clear():
            self.name.set("")
            self.accno.set("")
            self.iniamt.set("")
            self.acctype.set("")
            self.date.set("")
            self.Account.set("")
            self.withdraw.set("")


        def get_cursor(ev):
            cursor_row=self.Student_table.focus()
            contents=self.Student_table.item(cursor_row)
            row=contents['values']
            self.accno.set(row[0])
            self.name.set(row[1])
            self.iniamt.set(row[2])
            self.acctype.set(row[3])
            self.date.set(row[4])
            

        def fetch_data():
            con = sqlite3.connect('stem.db')
            cur=con.cursor()
            cur.execute("select * from Accounts")
            rows=cur.fetchall()
            if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('',END,values=row)
                con.commit()
            con.close()


        def balance():
            con = sqlite3.connect('stem.db')
            cur=con.cursor()
            cur.execute("select Account_No, Balance from Accounts where Account_No = ?",(self.Account.get(),))
            rows=cur.fetchall()
            if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('',END,values=row)
                con.commit()
            con.close()
            
            
        def withdrawl():
            con = sqlite3.connect('stem.db')
            cur=con.cursor()
            balance()
            p=0
            withdraw_amt = self.withdraw.get()
            p = (self.balance.get() - withdraw_amt) # amount after withdraw
            cur.execute("UPDATE Accounts SET Balance=? WHERE Account_No = ? ",(p,self.Account.get(),))
            clear()
            fetch_data()
            con.commit()
            con.close()
            
            

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg='black')
        Manage_Frame.place(x=0,y=100,width=450,height=660)

        m1_title=Label(Manage_Frame,text="Manage Account",bg="black",fg="white",font=("times new roman",20,"bold"))
        m1_title.grid(row=0,columnspan=2,pady=20)

        lbl_Acc=Label(Manage_Frame,text="Account NO.",bg="black",fg="white",font=("times new roman",12,"bold"))
        lbl_Acc.grid(row=1,column=0,pady=10,padx=20,sticky='w')
        
        txt_Acc=Entry(Manage_Frame,textvariable=self.accno,font=("cambria",15),bd=5,relief=GROOVE)
        txt_Acc.grid(row=1,column=1,pady=10,padx=5,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name",bg="black",fg="white",font=("times new roman",12,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky='w')
        
        txt_name=Entry(Manage_Frame,textvariable=self.name,font=("cambria",15),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=5,sticky="w")

        lbl_iniamt=Label(Manage_Frame,text="Initial Amt",bg="black",fg="white",font=("times new roman",12,"bold"))
        lbl_iniamt.grid(row=3,column=0,pady=10,padx=20,sticky='w')
        
        txt_iniamt=Entry(Manage_Frame,textvariable=self.iniamt,font=("cambria",15),bd=5,relief=GROOVE)
        txt_iniamt.grid(row=3,column=1,pady=10,padx=5,sticky="w")

        lbl_type=Label(Manage_Frame,text="Type",bg="black",fg="white",font=("times new roman",12,"bold"))
        lbl_type.grid(row=4,column=0,pady=10,padx=20,sticky='w')
        
        combo_type=ttk.Combobox(Manage_Frame,textvariable=self.acctype,font=("cambria",15),state='readonly')
        combo_type['values']=('Current','Savings')
        combo_type.grid(row=4,column=1,pady=10,padx=5)
        
        lbl_date=Label(Manage_Frame,text="Date",bg="black",fg="white",font=("times new roman",12,"bold"))
        lbl_date.grid(row=5,column=0,pady=10,padx=20,sticky='w')
        
        txt_date=Entry(Manage_Frame,textvariable=self.date,font=("cambria",15),bd=5,relief=GROOVE)
        txt_date.grid(row=5,column=1,pady=10,padx=5,sticky="w")

    
        lbl_withdraw=Label(Manage_Frame,text="Amt To Wthdrw/Dpst",bg="black",fg="white",font=("times new roman",12,"bold"))
        lbl_withdraw.grid(row=6,column=0,pady=10,padx=20,sticky='w')
        
        txt_withdraw=Entry(Manage_Frame,textvariable=self.withdraw,font=("cambria",15),bd=5,relief=GROOVE)
        txt_withdraw.grid(row=6,column=1,pady=10,padx=5,sticky="w")


        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg='black')
        btn_Frame.place(x=15,y=500,width=420)

        addbtn=Button(btn_Frame,text="Add",width=10,command=add_account).grid(row=0,column=0,padx=10,pady=10)
        withdrawlbtn=Button(btn_Frame,text="Withdraw",width=10,command=withdrawl).grid(row=0,column=1,padx=10,pady=10)
        depositbtn=Button(btn_Frame,text="Deposit",width=10).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",width=10,command=clear).grid(row=0,column=3,padx=10,pady=10)



        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Detail_Frame.place(x=450,y=100,width=1200,height=690)

        m_title=Label(Detail_Frame,text="Customer Help",bg="black",fg="white",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)
        
        lbl_search=Label(Detail_Frame,text="Search By:",bg="black",fg="white",font=("times new roman",15,"bold"))
        lbl_search.grid(row=1,column=0,pady=10,padx=5,sticky='w')

        lbl_ACC=Label(Detail_Frame,text="Account Number =>",bg="black",fg="white",font=("times new roman",14,"bold"))
        lbl_ACC.grid(row=1,column=1,pady=10,padx=5,sticky='w')

        
        txt_search=Entry(Detail_Frame,width=25,textvariable=self.Account,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=1,column=2,pady=10,padx=5,sticky="w")

        delbtn=Button(Detail_Frame,text="Delete",width=10,pady=5,command=delete_data).grid(row=1,column=3,padx=10,pady=10)
        stmbtn=Button(Detail_Frame,text="Check Balance",width=10,pady=5,command=balance).grid(row=1,column=4,padx=10,pady=10)
        upbtn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=fetch_data).grid(row=1,column=5,padx=10,pady=10)
        exitbtn=Button(Detail_Frame,text="EXIT",width=10,pady=5,command=exit).grid(row=1,column=6,padx=10,pady=10)


        Tabel_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg='black')
        Tabel_Frame.place(x=20,y=110,width=800,height=450)

        
        scroll_x=Scrollbar(Tabel_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Tabel_Frame,orient=VERTICAL)

        self.Student_table=ttk.Treeview(Tabel_Frame,columns=('Account',"Name","Initial","Type","Date","Balance"))
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("Account",text="Account NO.")
        self.Student_table.heading("Balance",text="Balance")
        self.Student_table.heading("Initial",text="Initial Amt")
        self.Student_table.heading("Type",text="Type")
        self.Student_table.heading("Date",text="Date")
        self.Student_table.heading("Name",text="Name")
        self.Student_table['show']='headings'
        self.Student_table.column("Account",width=120)
        self.Student_table.column("Balance",width=50)
        self.Student_table.column("Initial",width=100)
        self.Student_table.column("Type",width=50)
        self.Student_table.column("Date",width=50)
        self.Student_table.column("Name",width=130)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",get_cursor)
        fetch_data()



root=Tk()
ob=management(root)
root.mainloop()
        
