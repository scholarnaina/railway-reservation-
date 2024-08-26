"""import mysql.connector
   conn=mysql.connector.connect(host='localhost',user='root',password='1234')
   mycur=conn.cursor()
   mycur.execute('create database RAILWAY_RESERVATION_SYSTEM')
   conn.close()"""
"""import mysql.connector
   conn=mysql.connector.connect(host='localhost',user='root',password='1234',database='RAILWAY_RESERVATION_SYSTEM')
   mycur=conn.cursor()
   mycur.execute('create table TRAIN3(TRAIN_NO int primary key,TRAIN_NAME VARCHAR(60),FROM_PLACE VARCHAR(60),TO_PLACE VARCHAR(60),STATIONS VARCHAR(150),TRAIN_DATE DATE,TRAIN_TIME TIME,AM_PM VARCHAR(120),CHAIR_CAR INT,SLEEPER INT)')
   qry11="insert into TRAIN3 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
   data11=[(12431,"TVM RAJDHANI EXPRESS","Tiruvananthapuram","New Delhi","Kollam,Kozhikode,Kasargod,Ernakulam,Kannur","23-12-20","12:30:56","PM",500,0)]
   qry12="insert into TRAIN3 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
   data12=[(16301,"VENAD EXPRESS","Shornoor","Tiruvananthapuram","Thrissur,Aluva,Kottayam,Ernakulam,Kollam,Kayamkulam,Tiruvananthapuram","23-12-20","1:30:56","AM",0,40)]
   qry13="insert into TRAIN3 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
   data13=[(15321,"KERALA EXPRESS","Tiruvananthapuraum","Mumbai","Thrissur,Aluva,Kollam,Kasargod,Kozhikode,Ernakulam,Kayamkulam,Tiruvananthapuram","23-12-20","8:30:26","AM",50,0)]
   qry14="insert into TRAIN3 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
   data14=[(12341,"GURUVAYUR EXPRESS","Guruvayur","Chennai","Kollam,Kasargod,Kannur,Palakkad,Dindigal,Kayamkulam","23-12-20","3:30:26","PM",70,0)]
   qry15="insert into TRAIN3 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
   data15=[(10341,"MALABAR EXPRESS","Tiruvananthapuram","Karnataka","Thrissur,Aluva,Kollam,Kasargod,Kozhikode,Ernakulam,Kottayam,Palakkad","23-12-20","12:00:26","AM",0,60)]
   mycur.executemany(qry11,data11)
   mycur.executemany(qry12,data12)
   mycur.executemany(qry13,data13)
   mycur.executemany(qry14,data14)
   mycur.executemany(qry15,data15)
   conn.commit()"""


from tkinter import *
import tkinter as tk
import sys
from tkinter import messagebox
from functools import partial
import random
#first window
w1=tk.Tk()
w1.geometry("1500x700")
w1.title("LOGIN")
w1.configure(bg='#fff')
w1.resizable(False,False)
img = PhotoImage(file='login.png')
Label(w1,image=img,bg='white').place(x=200,y=230)
Option=None
pass_frame=None
bookt=None
tick_frame=None
#variable for entered data
uservalue=tk.StringVar()
passvalue=tk.StringVar()
user2value=tk.StringVar()
pass2value=tk.StringVar()
confpassvalue=tk.StringVar()
emailvalue=tk.StringVar()
name_entry=tk.StringVar()
c_entry=tk.StringVar()
names = []
ages = []
genders = []
#login logic
def login1():
    if uservalue.get()=="" or passvalue.get()=="":
        messagebox.showerror("Error","All fields are required",parent=w1)
        sys.exit()
    
    import mysql.connector as con
    connection=con.connect(host="localhost",user="root",password="1234",database="railway_reservation_system")
    cursor=connection.cursor()
    username=uservalue.get()
    password=passvalue.get()
    query = "SELECT COUNT(*) FROM user WHERE username = %s AND password = %s"
    cursor.execute(query,(username,password))
    result=cursor.fetchone()
    print(result)
    cursor.close()
    connection.close()
    if result:
        column1=result[0]
        if column1==1:
           messagebox.showinfo("Information","Login succesfull",parent=w1)
           login2()
           sys.exit()
        else:
            messagebox.showerror("Error","Invalid credentials",parent=w1)
            sys.exit()

def openw():  
    w1.lift()

def login2():
    #booking page
    def book_ticket():
        book=tk.Toplevel(w1)
        book.geometry("1500x700")
        book.title("Booking")
        booking_options_frame = tk.Frame(book, bg='white')
        booking_options_frame.place(x=0, y=0, width=1500, height=800)

        from_label = tk.Label(booking_options_frame, text="FROM:", font=("Century Gothic", 20), bg='white')
        from_label.place(x=50, y=50)
        from_entry = tk.Entry(booking_options_frame, font=("Century Gothic", 15), bg='lightgray')
        from_entry.place(x=200, y=50, width=250)

        to_label = tk.Label(booking_options_frame, text="TO:", font=("Century Gothic", 20), bg='white')
        to_label.place(x=50, y=100)
        to_entry = tk.Entry(booking_options_frame, font=("Century Gothic", 15), bg='lightgray')
        to_entry.place(x=200, y=100, width=250)
        
        date_label = tk.Label(booking_options_frame, text="DATE:", font=("Century Gothic", 20), bg='white')
        date_label.place(x=50, y=150)
        date_entry = tk.Entry(booking_options_frame, font=("Century Gothic", 15), bg='lightgray')
        date_entry.place(x=200, y=150, width=250)
        #entering no of passengers
        def book1(train_no):
            bookt=tk.Toplevel(w1)
            bookt.geometry("1500x700")
            bookt.title("Passenger Details")
            global pass_frame
            pass_frame = tk.Frame(bookt, bg='white')
            pass_frame.place(x=0, y=0, width=1500, height=800)
            no_label = tk.Label(pass_frame, text="Number of Passenger", font=("Century Gothic", 20), bg='white')
            no_label.place(x=50,y=50)
            no_entry=tk.Entry(pass_frame,font=("Century Gothic", 15), bg='lightgray')
            no_entry.place(x=50,y=100, width=250)
            buttonno=tk.Button(pass_frame,text="Book",font=("Century Gothic", 20), bg="#0080FF", fg="white",command=lambda: pass1(no_entry.get(), train_no))
            buttonno.place(x=400,y=50,width=150,height=50)
        #entering passenger details
        def pass1(no,train_no):
             global names,genders,ages,tick_frame
             import mysql.connector as con
             connection=con.connect(host="localhost",user="root",password="1234",database="railway_reservation_system")
             cursor=connection.cursor()
             labels=[]
             entry=[]
             print(no)
             num=int(no)
             """qry='CREATE TABLE ticket(ticket_no INT primary key default 0,train_no INT, name varchar(50),age varchar(50),gender varchar(50))'
             cursor.execute(qry)"""
             global pass_frame
             for i in range(num):
                name_label = tk.Label(pass_frame, text="Name of Passenger", font=("Century Gothic", 20), bg='white')
                labels.append(name_label)
                name_entry=tk.Entry(pass_frame,font=("Century Gothic", 15), bg='lightgray')
                entry.append(name_entry)
                age_label = tk.Label(pass_frame, text="Age of Passenger", font=("Century Gothic", 20), bg='white')
                labels.append(age_label)
                age_entry=tk.Entry(pass_frame,font=("Century Gothic", 15), bg='lightgray')
                entry.append(age_entry)
                gender_label = tk.Label(pass_frame, text="Gender", font=("Century Gothic", 20), bg='white')
                labels.append(gender_label)
                gender_entry=tk.Entry(pass_frame,font=("Century Gothic", 15), bg='lightgray')
                entry.append(gender_entry)
                
             for i, label in enumerate(labels):
                           label.place(x=50, y=210+i*70)
             for i, entr in enumerate(entry):
                           entr.place(x=50, y=250+i*70)
             def get_values(entry):
               #insert passenger details into table ticket
               t=[]
               global names, ages, genders,tick_frame,tkno
               tkno=[]
               names = [e.get() for i, e in enumerate(entry) if i % 3 == 0]
               ages = [e.get() for i, e in enumerate(entry) if i % 3 == 1]
               genders = [e.get() for i, e in enumerate(entry) if i % 3 == 2]
               for i in range(num):
                 tkno.append(random.randint(1000,8000))
                 qry8='insert into ticket(ticket_no,train_no,name,age,gender)values(%s,%s,%s,%s,%s)'
                 data8=[tkno[i],train_no,names[i],ages[i],genders[i]]
                 cursor.execute(qry8,data8)
                 connection.commit()
             def ticket(train_no,no):
                 #decrement vacant seats
                 tick=tk.Toplevel(w1)
                 tick.geometry("1500x700")
                 tick.title("Ticket Details")
                 import mysql.connector as con
                 connection=con.connect(host="localhost",user="root",password="1234",database="railway_reservation_system")
                 cursor=connection.cursor()           
                 query3='select sleeper,chair_car  from train3 where train_no=%s'
                 data3=[train_no]
                 cursor.execute(query3,data3)
                 res=cursor.fetchone()
                 
                 num=int(no)
                 if res:
                     res1=res[0]
                     res2=res[1]
                     if res1!=0:
                         ress1=res1-num
                         query4='update train3 set sleeper=%s where train_no=%s'
                         data4=[ress1,train_no]
                         cursor.execute(query4,data4)
                         connection.commit()
                     if res2!=0:
                         ress2=res2-num
                         
                         query5='update train3 set chair_car=%s where train_no=%s'
                         data5=[ress2,train_no]
                         cursor.execute(query5,data5)
                         connection.commit()
                 selected_option = tk.IntVar()
                 global tick_frame
                 tick_frame = tk.Frame(tick, bg='white')
                 tick_frame.place(x=0, y=0, width=1500, height=800)
                 #select AC/NON-AC
                 radio_button1 = tk.Radiobutton(tick_frame,text="AC", variable=selected_option, value=1,command=lambda: ac(num, selected_option.get()))
                 radio_button1.place(x=50, y=50)
                 ac_label = tk.Label(tick_frame, text="AC Ticket Price:400", font=("Century Gothic", 20), bg='white')
                 ac_label.place(x=200, y=50)
                 radio_button2 = tk.Radiobutton(tick_frame,text="Non AC", variable=selected_option, value=2,command=lambda: non(num, selected_option.get()))
                 radio_button2.place(x=50, y=150)
                 nonac_label = tk.Label(tick_frame, text="NON-AC Ticket Price:140", font=("Century Gothic", 20), bg='white')
                 nonac_label.place(x=200, y=150)
             def info():
                     #print ticket
                     global tick_frame
                     t=[]
                     pay_label = tk.Label(tick_frame, text="Payment Successful", font=("Century Gothic", 20), bg='white')
                     pay_label.place(x=50, y=420)
                     for i in range(num):
                       t_label = tk.Label(tick_frame, text=f"Ticket No:{tkno[i]} Train No:{train_no},Name:{names[i]} Age:{ages[i]} Gender:{genders[i]}", font=("Century Gothic", 20), bg='white')
                       t.append(t_label)
                 
                     for i, label in enumerate(t):
                           label.place(x=50, y=500+i*70)
                    
             def ac(num,x):
                  if x==1:
                     global tick_frame
                     ttp=400*num
                     p_label = tk.Label(tick_frame, text=f"Total Amount to pay:{ttp}", font=("Century Gothic", 20), bg='white')
                     p_label.place(x=50, y=250)
                     pay_btn=tk.Button(tick_frame,text="Pay",font=("Century Gothic", 20), bg="#0080FF", fg="white", command=info)
                     pay_btn.place(x=250, y=340, width=150, height=30)
             def non(num,y):
                  if y==2:
                    global tick_frame
                    ttp=140*num
                    p1_label = tk.Label(tick_frame, text=f"Total Amount to pay:{ttp}", font=("Century Gothic", 20), bg='white')
                    p1_label.place(x=50, y=250)
                    pay1_btn=tk.Button(tick_frame,text="Pay",font=("Century Gothic", 20), bg="#0080FF", fg="white", command=info)
                    pay1_btn.place(x=250, y=340, width=150, height=50)
             next_btn=tk.Button(pass_frame,text="Next",font=("Century Gothic", 20), bg="#0080FF", fg="white",command=lambda: [get_values(entry), ticket(train_no, no)])
             next_btn.place(x=450, y=350, width=150, height=50)               
        def search():
          #search the train based on the stations entered
          import mysql.connector as con
          connection=con.connect(host="localhost",user="root",password="1234",database="railway_reservation_system")
          cursor=connection.cursor()
          frompl=from_entry.get()
          topl=to_entry.get()
          date=date_entry.get()
          if date == "2023-12-20":
            query1="select stations,train_no from train3"
            cursor.execute(query1)
            result1=cursor.fetchall()
            labels = []
            buttons=[]
            for row in result1:
             str=row[0]
             tn=row[1]
             
             values=str.split(',')
             i=0
             flag=0
             for value in values:
              
              if frompl==value or flag==1:
                   flag=1
                   if frompl==value:
                      continue
                   if topl==value:
                    query2="select * from train3 where train_no=%s"
                    data2=[tn]
                    cursor.execute(query2,data2)
                    result2=cursor.fetchone()
                    
                    if result2:
                        train_no=result2[0]
                        train_name=result2[1]
                        train_date=result2[5]
                        train_time=result2[6]
                        train_t=result=result2[7]
                        train_c=result2[8]
                        train_s=result2[9]
                        if train_c!=0:
                           label_train_no = tk.Label(booking_options_frame, text=f"Train No: {train_no} Train Name: {train_name} Date: {train_date} Time:{train_time} {train_t} Chair Car-Number of Remaining seats:{train_c}",font=("Century Gothic", 15), bg='white')
                           label_train_no.place(x=50, y=200)
                           labels.append(label_train_no)
                        else:
                           label_train_no = tk.Label(booking_options_frame, text=f"Train No: {train_no} Train Name: {train_name} Date: {train_date} Time:{train_time} {train_t} Sleeper-Number of Remaining seats:{train_s}",font=("Century Gothic", 15), bg='white')
                           label_train_no.place(x=50, y=200)
                           labels.append(label_train_no)


                        button1=tk.Button(booking_options_frame,text="Select",font=("Century Gothic", 20), bg="#0080FF", fg="white",command=partial(book1, train_no))
                        buttons.append(button1)
                        
            for i, label in enumerate(labels):
                           label.place(x=50, y=200 + i * 60)
                           
            for i, button in enumerate(buttons):
                           button.place(x=1350, y=200 + i * 60)
        #search button
        search_btn=tk.Button(booking_options_frame,text="Search",font=("Century Gothic", 20), bg="#0080FF", fg="white",command=search)
        search_btn.place(x=550,y=100,width=150,height=50)
    #cancel logic
    def cancel(tno):
          global t_frame
          import mysql.connector as con
          connection=con.connect(host="localhost",user="root",password="1234",database="railway_reservation_system")
          cursor=connection.cursor()
          qry9='select count(*) from ticket where ticket_no=%s'
          data9=[tno]
          cursor.execute(qry9,data9)
          result=cursor.fetchone()
          if result:
              res=result[0]
              if res==1:
                  qry10='select sleeper,chair_car,tik.train_no from train3 t join ticket tik on t.train_no=tik.train_no where tik.ticket_no=%s'
                  data10=[tno]
                  cursor.execute(qry10,data10)
                  result=cursor.fetchall()
                  res1=result[0]
                  ress1=res1[0]
                  ress2=res1[1]
                  ress3=res1[2]
                  if ress1!=0:
                      up=ress1+1
                      qry11='update train3 set sleeper=%s where train_no=%s'
                      data11=[up,ress3]
                      cursor.execute(qry11,data11)
                      can_label = tk.Label(t_frame, text="Cancellation Successfull.Money will be refunded soon", font=("Century Gothic", 20), bg='white')
                      can_label.place(x=50, y=370)
                  if ress2!=0:
                      up=ress2+1
                      qry12='update train3 set chair_car=%s where train_no=%s'
                      data12=[up,ress3]
                      cursor.execute(qry12,data12)
                      can_label = tk.Label(t_frame, text="Cancellation Successfull.Money will be refunded soon", font=("Century Gothic", 20), bg='white')
                      can_label.place(x=50, y=370)
                  qry13='delete from ticket where ticket_no=%s'
                  data13=[tno]
                  cursor.execute(qry13,data13)
                  connection.commit()
    #cancel page
    def cancel_booking():
                 m=tk.Toplevel(w1)
                 global t_frame
                 m.geometry("1500x700")
                 m.title("Cancel Ticket")
                 t_frame = tk.Frame(m, bg='white')
                 t_frame.place(x=0,y=0, width=1500, height=800)
                 c_label = tk.Label(t_frame, text=f"Enter Ticket No", font=("Century Gothic", 20), bg='white')
                 c_label.place(x=50, y=50)
                 c_entry = tk.Entry(t_frame, font=("Century Gothic", 15), bg='lightgray')
                 c_entry.place(x=50, y=100, width=250)
                 print(c_entry.get())
                 c_btn=tk.Button(t_frame,text="Cancel",font=("Century Gothic", 20), bg="#0080FF",fg="white",command=lambda: cancel(c_entry.get()))
                 c_btn.place(x=50,y=200,width=150,height=30)
#second window                
    global option,img
    option = tk.Toplevel(w1)
    option.geometry("1500x700")
    option.title("Railway Reservation")
    booking_frame=tk.Frame(option,bg='white')
    booking_frame.place(x=750,y=130,width=500, height=400)
    img= PhotoImage(file='train.png')
    Label(option,image=img,bg='white').place(x=200,y=230)
    book_btn=tk.Button(booking_frame,text="Book",font=("Century Gothic", 20), bg="#0080FF", fg="white", command=book_ticket)
    book_btn.place(x=50,y=150,width=150, height=50)

    cancel_btn=tk.Button(booking_frame,text="Cancel", font=("Century Gothic", 20), bg="#0080FF", fg="white", command=cancel_booking)
    cancel_btn.place(x=300,y=150,width=150, height=50)
 
 #signup logic
def signup2():
    if(user2value.get()=="" or emailvalue.get()=="" or pass2value.get()=="" or confpassvalue.get()==""):
        messagebox.showerror("Error","All fields are required",parent=w1)
    elif pass2value.get() != confpassvalue.get():
        messagebox.showerror("Error","Password does not match",parent=w1)
        sys.exit()
    else:
        printuser=user2value.get()
        printemail=emailvalue.get()
        printpass=pass2value.get()
    
    #creating conection
    import mysql.connector as con
    connection=con.connect(host="localhost",user="root",password="1234",database="railway_reservation_system")
    cursor=connection.cursor()
    #cursor.execute('create table user(username varchar(50),password varchar(50))')
    username=user2value.get()
    print(username)
    password=pass2value.get()
    print(password)
    print("user2value:", user2value.get())
    print("pass2value:", pass2value.get())
    query = "SELECT COUNT(*) FROM user WHERE username = %s AND password = %s"
    cursor.execute(query,(user2value.get(),pass2value.get()))
    result=cursor.fetchone()
    print(result)
    if result:
         column1=result[0]
         if column1==1:
            messagebox.showerror("Error","User already exists",parent=w1)
            sys.exit()
         else:
            print("hi")
            messagebox.showinfo("Information","Account created",parent=w1)
            qry2='insert into user(username,password)values(%s,%s)'
            data2=[user2value.get(),pass2value.get()]
            cursor.execute(qry2,data2)
            connection.commit()
            login2()
            sys.exit()
#signup page

def signup1():
    sign=tk.Toplevel(w1)
    sign.geometry("1500x700")
    sign.title("New Window")
    f=tk.PhotoImage("background.jpg")
    background_label=tk.Label(w1,image=f)
    background_label.place(x=1000,y=1500,relwidth=1,relheight=1)
    frame_input2=tk.Frame(sign,bg="skyblue")
    frame_input2.place(x=320,y=130,height=500,width=630)

    label1=tk.Label(frame_input2,text="Register Here",font=("impact",32,"bold"),fg="blue",bg="white")
    label1.place(x=175,y=20)

    global user2value
    global pass2value
    global emailvalue
    global confpassvalue

    #username entry
    user2=tk.Label(frame_input2,text="USERNAME",font=("Impact",20),fg="white",bg="orangered")
    user2.place(x=30,y=95)
    uentry2=tk.Entry(frame_input2,font=("Times New Roman",15),bg="lightgray",textvariable=user2value)
    uentry2.place(x=30,y=145,width=270,height=35)

    #password entry
    pass2=tk.Label(frame_input2,text="PASSWORD",font=("Impact",20),bg="orangered",fg="white")
    pass2.place(x=30,y=195)
    passentry2=tk.Entry(frame_input2,font=("time new roman",15),bg="lightgray",textvariable=pass2value)
    passentry2.place(x=30,y=245,width=270,height=35)

    #email
    email=tk.Label(frame_input2,text="EMAIL",font=("Impact",20),bg="orangered",fg="white")
    email.place(x=330,y=95)
    emailentry=tk.Entry(frame_input2,font=("times new roman",15),bg="lightgray",textvariable=emailvalue)
    emailentry.place(x=330,y=145,width=270,height=35)

    #confirm password
    confpass=tk.Label(frame_input2,text="CONFIRM PASSWORD",font=("Impact",20),bg="orangered",fg="white")
    confpass.place(x=330,y=195)
    confpassentry=tk.Entry(frame_input2,font=("times new roman",15),bg="lightgray",textvariable=confpassvalue)
    confpassentry.place(x=330,y=245,width=270,height=35)

    #singup button
    btns=tk.Button(frame_input2,text="SIGN UP",font=("Century Gothic",18),fg="white",bg="orangered",command=signup2)
    btns.place(x=50,y=340)

    #if already registered
    rego=tk.Button(frame_input2,command=openw,text="Already registered? Login",cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=30,height=1)
    rego.place(x=270,y=340)
    w1.mainloop()

def main():
    global uservalue
    global passvalue

    #creating first frame
    frame_input=tk.Frame(w1,bg='white')
    frame_input.place(x=750,y=130,height=500,width=400)
    #login page
    tk.Label(text="LOGIN",font=("Century Gothic BOLD",30),fg="#2F4F4F",bg="white",borderwidth=0,relief=tk.RIDGE).place(x=810,y=150)
    tk.Label(text="USERNAME",font=("Century Gothic BOLD",15),fg="#2F4F4F",bg="white",borderwidth=0,relief=tk.RIDGE).place(x=770,y=230)
    tk.Label(text="PASSWORD",font=("Century Gothic BOLD",15),fg="#2F4F4F",bg="white",borderwidth=0,relief=tk.RIDGE).place(x=770,y=340)
     
    userentry=tk.Entry(w1,font=("Sans Sherif",20),fg="black",bg="darkgray",textvariable=uservalue)
    passwordentry=tk.Entry(w1,font=("Sans Sherif",20),fg="black",background="darkgrey",textvariable=passvalue)
    userentry.place(x=770,y=260)
    passwordentry.place(x=770,y=370)

    #login button
    btn1=tk.Button(frame_input,text="Login",font=("Centtury Gothic",22),bg="#0080FF",fg="white",command=login1)
    btn1.place(x=45,y=340)
    tk.Label(text="Don't have an account?",font=("Century Gothic BOLD",15),fg="#2F4F4F",bg="white",borderwidth=0,relief=tk.RIDGE).place(x=770,y=525)
    btn2=tk.Button(frame_input,text="Sign Up",cursor="hand2",bd=0,font=("Century Gothic",15),bg="white",fg="#0080FF",command=signup1)
    btn2.place(x=255,y=390)
    w1.mainloop()
main()
