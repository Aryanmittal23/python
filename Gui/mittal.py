from tkinter import*
from tkinter import messagebox
root=Tk()
root.geometry('400x400')
root.configure(bg='yellow')
root.title("Gui")
def msg():
    messagebox.showwarning('alert','top')
Button(root,text='hello',command=msg).pack()
def join(e=0):
    root.destroy()
    import window.py
Button(root,text='hii',command=join).pack()    
root.mainloop()
    
