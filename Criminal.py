from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1366x768+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')

        lbl_title=Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM',font=('times new roman',40,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1366,height=70)

        img_logo=Image.open('img/logo.jpg')
        img_logo=img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=100,y=5,width=60,height=60)





if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()