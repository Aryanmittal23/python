from tkinter import*
root=Tk()
root.title('GUI')
root.geometry("400x600")
root.configure(bg='green')
Label(root,text='hello',bg='black').grid(row=0,column=1)
def fun():
    Label(root,text="click here").grid(row=1, column=1)
    root.destroy()
def join(e=0):
    root.destroy()
    import window.py
    
    
root.after(3000,join )
