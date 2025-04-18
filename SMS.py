from tkinter import *
import time
import ttkthemes 
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas 
# Functionality Part

def Exit():
    result = messagebox.askyesno('Confirm','Do You Want to Exit')
    if result:
        root.destroy()
    else:
        pass

def Export_data():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = studenttable.get_children()
    newlist =[]
    for index in indexing:
        content = studenttable.item(index)
        datalist = content['values']
        newlist.append(datalist)
    
    table = pandas.DataFrame(newlist,columns=['Id','Name','Email','Phone','Address',
                                'Gender','D.O.B','Addmission Year','Course Name'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data Saved Successfully.')

def Field_data(title,button_text,command):
    global idEntry,nameEntry,emailEntry,phoneEntry,addEntry,GenderEntry,dobEntry,addmissionEntry,CourseEntry,Screen,studenttable
    Screen = Toplevel()
    Screen.grab_set()
    Screen.geometry('400x500+50+100')
    Screen.resizable(False,False)
    Screen.title(title)
       

    id = Label(Screen,text="Id",font=('times new roman',14,'bold'))
    id.grid(row=0,column=0,pady=10,sticky=W,padx=10)
    idEntry = Entry(Screen,font=('roman',12,'bold'),width=22)
    idEntry.grid(row=0,column=1)

    name = Label(Screen,text="Name",font=('times new roman',14,'bold'))
    name.grid(row=1,column=0,pady=10,sticky=W,padx=10)
    nameEntry = Entry(Screen,font=('roman',12,'bold'),width=22)
    nameEntry.grid(row=1,column=1)

    E_mail = Label(Screen,text="Email",font=('times new roman',14,'bold'))
    E_mail.grid(row=2,column=0,pady=10,sticky=W,padx=10)
    emailEntry = Entry(Screen,font=('roman',12,'bold'),width=22)
    emailEntry.grid(row=2,column=1)

    phone = Label(Screen,text="Mobile No",font=('times new roman',14,'bold'))
    phone.grid(row=3,column=0,pady=10,sticky=W,padx=10)
    phoneEntry = Entry(Screen,font=('roman',12,'bold'),width=22)
    phoneEntry.grid(row=3,column=1)

    address = Label(Screen,text="Address",font=('times new roman',14,'bold'))
    address.grid(row=4,column=0,pady=10,sticky=W,padx=10)
    addEntry = Entry(Screen,font=('roman',12,'bold'),width=22)
    addEntry.grid(row=4,column=1)

    gender = Label(Screen,text="Gender",font=('times new roman',14,'bold'))
    gender.grid(row=5,column=0,pady=10,sticky=W,padx=10)
    GenderEntry = Entry(Screen,font=('roman',12,'bold'),width=22)
    GenderEntry.grid(row=5,column=1)
    
    dob = Label(Screen,text="D.O.B",font=('times new roman',14,'bold'))
    dob.grid(row=6,column=0,pady=10,sticky=W,padx=10)
    dobEntry = Entry(Screen,font=('roman',12,'bold'),width=22)
    dobEntry.grid(row=6,column=1)

    addmission = Label(Screen,text="Addmission Year",font=('times new roman',14,'bold'))
    addmission.grid(row=7,column=0,pady=10,sticky=W,padx=10)
    addmissionEntry = Entry(Screen,font=('roman',12,'bold'),width=22)
    addmissionEntry.grid(row=7,column=1)
    
    Course = Label(Screen,text="Course Name",font=('times new roman',14,'bold'))
    Course.grid(row=8,column=0,pady=10,sticky=W,padx=10)
    CourseEntry = Entry(Screen,font=('roman',12,'bold'),width=22)
    CourseEntry.grid(row=8,column=1)

    button = ttk.Button(Screen,text=button_text,command=command)
    button.grid(row=9,columnspan=2,pady=10) 
    if title=='Update Student Data':
        index = studenttable.focus()
        print(index)
        content = studenttable.item(index)
        listdata = content['values']
        idEntry.insert(0,listdata[0])
        nameEntry.insert(0,listdata[1])
        emailEntry.insert(0,listdata[2])
        phoneEntry.insert(0,listdata[3])
        addEntry.insert(0,listdata[4])
        GenderEntry.insert(0,listdata[5])
        dobEntry.insert(0,listdata[6])
        addmissionEntry.insert(0,listdata[7])
        CourseEntry.insert(0,listdata[8])
   
def update_data():
    query = 'update student set Name=%s,Email=%s,Phone_No=%s,Address=%s,Gender=%s,D_O_B=%s,Addmission_Year=%s,course_Name=%s where id=%s'
    mycursor.execute(query,(nameEntry.get(),emailEntry.get(),phoneEntry.get(),addEntry.get(),
                    GenderEntry.get(),dobEntry.get(),addmissionEntry.get(),CourseEntry.get(),idEntry.get()))
    conn.commit() 
    messagebox.showinfo('Success',f'Id {idEntry.get()} is Modify',parent=Screen)
    Screen.destroy()
    show_student()

def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for data in fetched_data:
        studenttable.insert('',END,values=data)

def delete_student():
    index = studenttable.focus()
    print(index)
    content = studenttable.item(index)
    content_id = content['values'][0]
    query = 'delete from student where id=%s'
    mycursor.execute(query,content_id)
    conn.commit()
    messagebox.showinfo('Delete',f'Id {content_id} is delete Successfully.')
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for data in fetched_data:
        studenttable.insert('',END,values=data)

def Search_data():
    query = 'select * from student where id=%s or Name=%s or Email=%s or Phone_No=%s or Address=%s or Gender=%s or D_O_B=%s or Addmission_Year=%s or course_Name=%s'
    mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),phoneEntry.get(),addEntry.get(),
                                GenderEntry.get(),dobEntry.get(),addmissionEntry.get(),CourseEntry.get()))
    studenttable.delete(*studenttable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        studenttable.insert('',END,values=data)   
 
def Add_data():
    if idEntry.get()=='' or nameEntry.get()=='' or emailEntry.get()=='' or phoneEntry.get()=='' or addEntry.get()=='' or GenderEntry.get()==''or addmissionEntry.get()=='' or CourseEntry.get()=='' or dobEntry.get()=='':
        messagebox.showerror('Error','All Field be Required',parent=Screen)

    else:
        try:
            query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),phoneEntry.get(),addEntry.get(),
                                GenderEntry.get(),dobEntry.get(),addmissionEntry.get(),CourseEntry.get()))
            conn.commit()
            result = messagebox.askyesno('Confirm','Data Inserted SuccessFully. Do You Won`t Clean it')
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                emailEntry.delete(0,END)
                phoneEntry.delete(0,END)
                addEntry.delete(0,END)
                GenderEntry.delete(0,END)
                dobEntry.delete(0,END)
                addmissionEntry.delete(0,END)
                CourseEntry.delete(0,END)
            else:
                pass
            
        except:
            messagebox.showerror('Error','Id Cannot be repeated')
            return

    query = 'SELECT * FROM student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    print(fetched_data)
    for data in fetched_data:
        listdata = list(data)
        studenttable.insert('',END,values=listdata)

def Connect_DB():
    def connect():
        global mycursor,conn
        try:
            conn = pymysql.connect(host="localhost",user="root",passwd="Ajinath@8545")
            mycursor = conn.cursor()

        except: 
            messagebox.showerror('Error','Invalid Details.',parent=connectroot)
            return
        
        try:
            query = 'CREATE DATABASE StudentManaSy'
            mycursor.execute(query)
            query = 'use StudentManaSy'
            mycursor.execute(query)
            query = 'create table student(Id int not null PRIMARY KEY, Name varchar(50), Email varchar(50), Phone_No varchar(15), Address varchar(50), Gender varchar(20), D_O_B varchar(30), Addmission_Year varchar(30), course_Name varchar(50))'
            mycursor.execute(query)
        except:
            query = 'use StudentManaSy'
            mycursor.execute(query)
        messagebox.showinfo('Success','Database is Connected Successfully.',parent=connectroot)
        connectroot.destroy()
        addbutton.config(state=NORMAL)
        searchbutton.config(state=NORMAL)
        deletebutton.config(state=NORMAL)
        updatehbutton.config(state=NORMAL)
        showbutton.config(state=NORMAL)
        trfbutton.config(state=NORMAL)
       
    
    connectroot=Toplevel()
    connectroot.grab_set()
    connectroot.geometry('450x200+730+230')
    connectroot.resizable(False,False)
    connectroot.title('Database Connection')

    hostname = Label(connectroot,text='Host Name',font=('Arial',15,'bold'))
    hostname.grid(row=0,column=0,padx=20)
    hostEntry = Entry(connectroot,font=('roman',13,'bold'),bd=2,width=30)
    hostEntry.grid(row=0,column=1,pady=10,padx=5)

    username = Label(connectroot,text='User Name',font=('Arial',15,'bold'))
    username.grid(row=1,column=0,padx=20)
    userEntry = Entry(connectroot,font=('roman',13,'bold'),bd=2,width=30)
    userEntry.grid(row=1,column=1,pady=10,padx=5)

    password = Label(connectroot,text='Password',font=('Arial',15,'bold'))
    password.grid(row=2,column=0,padx=20)
    passEntry = Entry(connectroot,font=('roman',13,'bold'),bd=2,width=30)
    passEntry.grid(row=2,column=1,pady=10,padx=5)

    connectBtn = ttk.Button(connectroot,text='CONNECT',command=connect)
    connectBtn.grid(row=3,columnspan=2,pady=10,padx=50)

count = 0
text = ''
def slider():
    global text,count
    if count==len(s):
        count = 0
        text = ''
    text = text+s[count]
    Sliderlabel.config(text=text)
    count+=1
    Sliderlabel.after(300,slider)

def clock():
    date = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%H:%M:%S')
    datetime.config(text=f'    Date: {date}\nTime: {currenttime}')
    datetime.after(1000,clock)
    
root = ttkthemes.ThemedTk() #Creating Window in the Screen Using Tkinter Package

root.get_themes()

root.set_theme('radiance') #Creation Theme And Font in the this page Using package

root.geometry('1280x700+0+0')       # Set the height % width And Padding Using Geometry function
root.resizable(False,False)         # set fix value for screen 
root.title('Student Management System')    #Creating title of this page

datetime = Label(root,font=('times new roman',16,'bold'))   # creating clock in today datetime function
datetime.place(x=5,y=5)
clock()

s="Student Management System"   # Heading of the page
Sliderlabel = Label(root,text=s,font=('Arial',24,'italic bold'),width=35)           #set label value and font sixe etc.
Sliderlabel.place(x=210,y=5)                                    #used to place method to insert the content i =n screen.
slider()

connectBtn = ttk.Button(root,text='Connect Database',command=Connect_DB) #Connect To database cmd
connectBtn.place(x=1050,y=15)

leftFrame = Frame(root,bg="white")            #This is the frame context.
leftFrame.place(x=10,y=70,width=300,height=550)

logoIm = PhotoImage(file='student1.png')        #set the background image in the screen.
logolabel = Label(leftFrame,image=logoIm)
logolabel.grid(row=0,column=0,pady=10,padx=105)

addbutton = ttk.Button(leftFrame,text='Add Data',width=19,state=DISABLED,command=lambda :Field_data('Adding Student Data','ADD DATA',Add_data))
addbutton.grid(row=1,column=0,pady=15)

searchbutton = ttk.Button(leftFrame,text='Search Data',width=19,state=DISABLED,command=lambda :Field_data('Search Student Data','SEARCH',Search_data))
searchbutton.grid(row=2,column=0,pady=15)

deletebutton = ttk.Button(leftFrame,text='Delete Data',width=19,state=DISABLED,command=delete_student)
deletebutton.grid(row=3,column=0,pady=15)

updatehbutton = ttk.Button(leftFrame,text='Update Data',width=19,state=DISABLED,command=lambda :Field_data('Update Student Data','UPDATE',update_data))
updatehbutton.grid(row=4,column=0,pady=15)

showbutton = ttk.Button(leftFrame,text='Show Data',width=19,state=DISABLED,command=show_student)
showbutton.grid(row=5,column=0,pady=15)

trfbutton = ttk.Button(leftFrame,text='Export Data',width=19,state=DISABLED,command=Export_data)
trfbutton.grid(row=6,column=0,pady=15)


Exitbutton = ttk.Button(leftFrame,text='Exit',width=15,command=Exit)
Exitbutton.grid(row=7,column=0,pady=15)

rightFrame = Frame(root,bg="white")                 # Create Frame 2.
rightFrame.place(x=330,y=70,width=930,height=600)

ScrollbarX = Scrollbar(rightFrame,orient=HORIZONTAL)  #this is the scrollbar using up-down & left right Scroll
ScrollbarY = Scrollbar(rightFrame,orient=VERTICAL)


studenttable = ttk.Treeview(rightFrame,columns=('Id','Name','Email','Mobile No','Address','Gender','D.O.B',
                                 'Addmission Year','Course Name'),xscrollcommand=ScrollbarX.set
                                ,yscrollcommand=ScrollbarY.set)

ScrollbarX.config(command=studenttable.xview)
ScrollbarY.config(command=studenttable.yview)

ScrollbarX.pack(side=BOTTOM,fill=X)
ScrollbarY.pack(side=RIGHT,fill=Y)

studenttable.pack(fill=BOTH,expand=1)

studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Email',text='Email')
studenttable.heading('Mobile No',text='Mobile No')
studenttable.heading('Address',text='Address')       # Set the Heading of the this scrollbar.
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Addmission Year',text='Addmission Year')
studenttable.heading('Course Name',text='Course Name')

studenttable.column('Id',width=80,anchor=CENTER)
studenttable.column('Name',width=300)
studenttable.column('Email',width=300)
studenttable.column('Mobile No',width=200,anchor=CENTER)
studenttable.column('Address',width=300)
studenttable.column('Gender',width=150)         #Set the column of the this frame
studenttable.column('D.O.B',width=150)
studenttable.column('Addmission Year',width=200)
studenttable.column('Course Name',width=200)

style = ttk.Style()
style.configure('Treeview', rowheight=30,font=('Arial',12,'bold'),foreground='Black')
style.configure('Treeview.Heading',font=('Arial',14),foreground='Black')

studenttable.config(show='headings')

root.mainloop()