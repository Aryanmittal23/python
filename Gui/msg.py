from tkinter import*
from tkinter import messagebox
root=Tk()
root.title('msg')
root.configure(bg='yellow')
root.geometry('400x400')
def msg():
    messagebox.showwarning('alert','valid')
Button(root,text='ok',command=msg).pack()    
def join(e=0):
    root.destroy()
    import window.py
root.after('3000',join)

"""v=StringVar()
v.set('click here')
Option=['q','w','e']
OptionMenu(root,v,*Option).pack()
def fun():
    Label(root,text=v.get()).pack()
Button(root,text='click',command=fun).pack()

a=IntVar()
Label(root,text='select branch').pack()
Radiobutton(root,text='ece',variable=a,value=1).pack()
Radiobutton(root,text='cse',variable=a,value=2).pack()
Radiobutton(root,text='civil',variable=a,value=3).pack()
def fun1():
    Label(root,text=a.get()).pack()
Button(root,text='branch',command=fun1).pack()    """
