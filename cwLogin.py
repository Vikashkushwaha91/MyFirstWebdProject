import mysql.connector as sql
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
mycon=sql.connect(host="localhost",user="root",password="9117489743",database="myproject1")
mycur=mycon.cursor()
win=Tk()
unm=StringVar()
eid=StringVar()
pas=StringVar()
def login():
    un=unm.get()
    ei=eid.get()
    pa=pas.get()
    q="select * from users where email='{}' and password='{}'".format(ei,pa)
    mycur.execute(q)
    rec=mycur.fetchall()
    rec=tuple(rec)
    if rec==():
        pass
    else:
        messagebox.showinfo("Login","login sucessfull")
        nw=Tk()
        nw.title("hsm system")
        nw.geometry("650x650")
        nw.resizable(0,0)
        nw.config(background="lightgreen")
        def ndm():
            adwin=Tk()
            adwin.geometry("500x500")
            adwin.title("NEW ADMISSION")
            adwin.resizable(0,0)
            adwin.config(background="pink")
            mycon=sql.connect(host="localhost",user="root",password="9117489743",database="myproject1")
            mycur=mycon.cursor()
            sid=StringVar()
            sna=StringVar()
            phn=StringVar()
            age=StringVar()
            doa=StringVar()
            cou=StringVar()
            def close():
                adwin.destroy()
            def sub():
                s=sid.get()
                n=sna.get()
                p=phn.get()
                a=age.get()
                d=doa.get()
                c=cou.get()
                q="insert into students values('{}','{}','{}','{}','{}','{}')".format(s,n,p,a,d,c)
                mycur.execute(q)
                mycon.commit()
                messagebox.showinfo("ADMISSION","THANKS FOR ADMISSION")
            l1=Label(adwin,text="ADMISSION FORM",bg="white",fg="black",font=("monotype corsiva",28,"bold"))
            l1.pack()
            l2=Label(adwin,text="ST. ID",bg="pink",fg="black",font=("algerian",14,"bold"))
            l2.place(x=40,y=80)
            e1=Entry(adwin,font=("clarity",16,"bold"),bg="white",fg="black",bd=3,textvariable=sid)
            e1.place(x=160,y=80)
            l3=Label(adwin,text="NAME",bg="pink",fg="black",font=("algerian",14,"bold"))
            l3.place(x=40,y=130)
            e2=Entry(adwin,font=("clarity",16,"bold"),bg="white",fg="black",bd=3,textvariable=sna)
            e2.place(x=160,y=130)
            l4=Label(adwin,text="AGE",bg="pink",fg="black",font=("algerian",14,"bold"))
            l4.place(x=40,y=180)
            e3=Entry(adwin,font=("clarity",16,"bold"),bg="white",fg="black",bd=3,textvariable=age)
            e3.place(x=160,y=180)
            l5=Label(adwin,text="DOA",bg="pink",fg="black",font=("algerian",14,"bold"))
            l5.place(x=40,y=230)
            e4=Entry(adwin,font=("clarity",16,"bold"),bg="white",fg="black",bd=3,textvariable=doa)
            e4.place(x=160,y=230)
            l6=Label(adwin,text="PHONE No.",bg="pink",fg="black",font=("algerian",14,"bold"))
            l6.place(x=40,y=280)
            e5=Entry(adwin,font=("clarity",16,"bold"),bg="white",fg="black",bd=3,textvariable=phn)
            e5.place(x=160,y=280)
            l7=Label(adwin,text="COURSE",bg="pink",fg="black",font=("algerian",14,"bold"))
            l7.place(x=40,y=330)
            e6=Entry(adwin,font=("clarity",16,"bold"),bg="white",fg="black",bd=3,textvariable=cou)
            e6.place(x=160,y=330)
            b1=Button(adwin,text="SUBMIT",font=("clarity",14,"bold"),bg="green",fg="black",bd=3,command=sub)
            b1.place(x=160,y=400)
            b2=Button(adwin,text="CANCEL",font=("clarity",14,"bold"),bg="green",fg="black",bd=3,command=close)
            b2.place(x=300,y=400)
        def findr():
            fw=Tk()
            fw.title("FIND")
            fw.geometry("450x450")
            fw.resizable(0,0)
            fw.config(background="lightgreen")
            mycon=sql.connect(host="localhost",user="root",password="9117489743",database="myproject1")
            mycur=mycon.cursor()
            fn=StringVar()
                
            def frc():
                f=fn.get()
                q="select * from student where sid='{}'".format(f)
                mycur.execute(q)
                r=mycur.fetchone()
                mycon.commit()
                if r!="":
                    messagebox.showinfo("RECORD FOUND",r[snam])
                else:
                    messagebox.showinfo("RECORD NOT FOUND","NOT FOUND..!!!")
                    
                    
            l1=Label(fw,text="ENTER SID",bg="lightgreen",fg="black",font=("algerian",14,"bold"))
            l1.place(x=100,y=50)
            e1=Entry(fw,font=("clarity",14,"bold"),bg="white",fg="green",bd=2,textvariable=fn)
            e1.place(x=100,y=100)
            b1=Button(fw,text="FIND R",font=("clarity",14,"bold"),bg="green",fg="black",bd=3,command=frc)
            b1.place(x=200,y=200)
        def upd():
            gw=Tk()
            gw.title("UPDATE")
            gw.geometry("450x450")
            gw.resizable(0,0)
            gw.config(background="lightgreen")
            mycon=sql.connect(host="localhost",user="root",password="9117489743",database="myproject1")
            mycur=mycon.cursor()
            ph=StringVar()
            co=StringVar()
            def ud():
                p=ph.get()
                c=co.get()
                q="update students sphn,course where sid='{}'".format(p,c)
                mycur.execute(q)
                mycon.commit()
            l1=Label(fw,text="phone no.",bg="lightgreen",fg="black",font=("algerian",14,"bold"))
            l1.place(x=100,y=50)
            l2=Label(fw,text="course",bg="lightgreen",fg="black",font=("algerian",14,"bold"))
            l2.place(x=100,y=100)
            e1=Entry(fw,font=("clarity",14,"bold"),bg="white",fg="green",bd=2,textvariable=fn)
            e1.place(x=180,y=10)
            b1=Button(fw,text="update",font=("clarity",14,"bold"),bg="green",fg="black",bd=3,command=ud)
            b1.place(x=200,y=200)
            
        def dlt():
            dw=Tk()
            dw.title("DELETE")
            dw.geometry("450x450")
            dw.resizable(0,0)
            dw.config(background="lightgreen")
            mycon=sql.connect(host="localhost",user="root",password="9117489743",database="myproject1")
            mycur=mycon.cursor()
            dl=StringVar()
            q="select sid from students"
            mycur.execute(q)
            
            
            def dlte():
                mycon=sql.connect(host="localhost",user="root",password="9117489743",database="myproject1")
                mycur=mycon.cursor()
                dle=dl.get()
                q="delete from students where sid='{}'".format(dle)
                mycur.execute(q)
                mycon.commit()
                messagebox.showinfo("DELETED SUCCESFULLY")
            l1=Label(dw,text="ENTER SID",bg="lightgreen",fg="black",font=("algerian",14,"bold"))
            l1.place(x=100,y=50)
            e1=Entry(dw,font=("clarity",14,"bold"),bg="white",fg="green",bd=2,textvariable=dl)
            e1.place(x=100,y=100)
            b1=Button(dw,text="DELETE SID",font=("clarity",14,"bold"),bg="green",fg="black",bd=3,command=dlte)
            b1.place(x=200,y=200)
                
        l1=Label(nw,text="Hubnet Student Management",bg="lightblue",fg="black",font=("monotype corsiva",28,"bold"))
        l1.pack(padx=0,pady=10)
        b1=Button(nw,text="FIND",bg="green",fg="white",bd="5",font=("clarity",14,"bold"),command=findr)
        b1.place(x=400,y=140)
        b2=Button(nw,text="NEW ADMISSION",bg="green",fg="white",bd="5",font=("clarity",14,"bold"),command=ndm)
        b2.place(x=400,y=190)
        b3=Button(nw,text="UPDATE",bg="green",fg="white",bd="5",font=("clarity",14,"bold"),command=upd)
        b3.place(x=400,y=250)
        b4=Button(nw,text="DELETE",bg="green",fg="white",bd="5",font=("clarity",14,"bold"),command=dlt)
        b4.place(x=400,y=310)
        l2=Label(nw,text="2nd floor,J.J.Complex,east boring canal road,opp,bharat petrol pump patna-01,BIHAR",bg="lightgreen",fg="white",font=("clarity",6,"bold"))
        l2.place(x=200,y=600)
        
        
        win.destroy()
def signup():
    u=unm.get()
    e=eid.get()
    p=pas.get()
    q="insert into users values('{}','{}','{}')".format(u,e,p)
    mycur.execute(q)
    mycon.commit()
    messagebox.showinfo("SAVED","SIGNUP SUCESSFULL")
def fpas():
    n=unm.get()
    i=eid.get()
    w=pas.get()
    q="update users set password='{}' where emailid='{}'".format(w,i)
    mycur.execute(q)
    mycon.commit()
    messagebox.showinfo("update","Password Updated")
    
win.title("LOGIN SYSTEM")
win.geometry("600x600")
win.resizable(0,0)
win.config(background="navyblue")
l1=Label(win,text="Hubnet Login System",bg="navyblue",fg="white",font=("monotype corsiva",26,"bold"))
l1.pack(padx=0,pady=6)
image=Image.open("c:\\users\\vikash\\downloads\\hubnet image.png")
imm=image.resize((50,50))
img=ImageTk.PhotoImage(imm)
l2=Label(win,image=img)
l2.pack()
l3=Label(win,text="USERNAME ",bg="navyblue",fg="white",font=("algerian",18,"bold"))
l3.place(x=220,y=140)
l4=Label(win,text="EMAILID",bg="navyblue",fg="white",font=("algerian",18,"bold"))
l4.place(x=230,y=220)
l5=Label(win,text="PASSWORD",bg="navyblue",fg="white",font=("algerian",18,"bold"))
l5.place(x=230,y=285)
e1=Entry(win,font=("clarity",16,"bold"),bg="white",fg="black",bd=2,textvariable=unm)
e1.place(x=160,y=180)
e2=Entry(win,font=("clarity",16,"bold"),bg="white",fg="black",bd=2,textvariable=eid)
e2.place(x=160,y=250)
e3=Entry(win,font=("clarity",16,"bold"),bg="white",fg="black",bd=2,textvariable=pas)
e3.place(x=160,y=320)
b1=Button(win,text="login",bg="darkgreen",fg="white",bd=6,command=login)
b1.place(x=120,y=400)
b2=Button(win,text="signup",bg="darkgreen",fg="white",bd=6,command=signup)
b2.place(x=240,y=400)
b3=Button(win,text="forgot password",bg="darkgreen",fg="white",bd=6,command=fpas)
b3.place(x=380,y=400)
l6=Label(win,text="2nd floor,J.J.Complex,east boring canal road,opp. bharat petrol pump patna-01, BIHAR",bg="navyblue",fg="white",font=("clarity",6,"bold"))
l6.place(x=120,y=550)
l7=Label(win,text="+91-7091499201,+91-9334179627",bg="navyblue",fg="white",font=("clarity",7,"bold"))
l7.place(x=200,y=562)
l8=Label(win,text="email : https:\\www.hubnettech.net",bg="navyblue",fg="white",font=("clarity",7,"bold"))
l8.place(x=200,y=575)
l9=Label(win,text="copy 2023 all rights reserved by hubnet",bg="navyblue",fg="white",font=("clarity",6,"bold"))
l9.place(x=450,y=580)

win.mainloop()
