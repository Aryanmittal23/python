from tkinter import*
root=Tk()
root.title('GUI')
root.geometry("400x600")
root.configure(bg='green')
Label(root,text='hello',bg='black').pack()



"""img=PhotoImage(file='mittal.png')
Label(root,image=img ,width='300', height='300').pack()"""
def fun():
    Label(root,text="event is added").pack()
Button(root,text="to create event click here",command=fun).pack()
Label(root,text='enter name').pack()
name=Entry(root)
name.pack()
Label(root,text='enter the num 1').pack()
num1=Entry(root)
num1.pack()
Label(root,text='enter the num 2')
num2=Entry(root)
num2.pack()
def sum():
    Label(root,text=int(num1.get())+int(num2.get())).pack()
Button(root,text="click to get sum",command=sum).pack()

v1=StringVar()
v1.set("click to select")
Option=["monday",'tuesday','wednesday','thursday','friday','saturday','sunady']
OptionMenu(root,v1,*Option).pack()
def fun1():
    Label(root,text=v1.get()).pack()
Button(root,text='show choice',command=fun1).pack()

v=IntVar()
Label(root,text='select your branch').pack()
Radiobutton(root,text='cse',var=v,value=1).pack()
Radiobutton(root,text='ece',var=v,value=2).pack()
Radiobutton(root,text='civil',var=v,value=3).pack()
def fun2():
    Label(root,text=v.get()).pack()
Button(root,text='click',command=fun2).pack()
root.mainloop()
