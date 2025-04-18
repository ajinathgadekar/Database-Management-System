from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
def login():
    if userEntry.get()=='' or passEntry.get()=='':
        messagebox.showerror('Error','Field cannot be Empty')
    elif userEntry.get()=='Ajinath' and passEntry.get()=='1234':
        messagebox.showinfo('Success','Welcome')
        root.destroy()
        import SMS  
    else:
        messagebox.showerror('Error','Please Enter Creadetials')

root = Tk()

root.geometry('1280x700+0+0')
root.title('Login Stystem For Student')

root.resizable(False,False)
backIm = ImageTk.PhotoImage(file="hiring.jpg")

bg = Label(root, image=backIm)
bg.place(x=0,y=0)

loginFrame = Frame(root)
loginFrame.place(x=500, y=150)

logoIm = PhotoImage(file='student.png')
logo = Label(loginFrame, image=logoIm)
logo.grid(row=0,column=0,columnspan=2,pady=7,padx=5)

userIm = PhotoImage(file='username.png')
username = Label(loginFrame,image=userIm,text='Username',compound=LEFT,
                 font=('times new roman',14,'bold'))
username.grid(row=1,column=0,pady=7,padx=5)

userEntry = Entry(loginFrame,font=('times new roman',14,'bold'),bd=3)
userEntry.grid(row=1,column=1,pady=7,padx=5)

userpass = PhotoImage(file='padlock.png')
password = Label(loginFrame,image=userpass,text='Password',compound=LEFT,
                 font=('times new roman',14,'bold'))
password.grid(row=2,column=0,pady=7,padx=5)

passEntry = Entry(loginFrame,font=('times new roman',14,'bold'),bd=3)
passEntry.grid(row=2,column=1,pady=7,padx=5)

loginbtn = Button(loginFrame,text='Login',font=('times new roman',13,'bold'),width=15 ,fg='black',
bg='cornflowerblue', activebackground='cornflowerblue', cursor='hand2',command=login)
loginbtn.grid(row=3,column=1,pady=7)

root.mainloop()
