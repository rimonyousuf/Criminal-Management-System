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

        #Logo Image
        img_logo=Image.open('img/logo.jpg')
        img_logo=img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=100,y=5,width=60,height=60)

        #Image Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1366,height=130)

        img1=Image.open('img/1.jpg')
        img1=img1.resize((455,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=455,height=160)

        #2nd image
        img2=Image.open('img/2.jpg')
        img2=img2.resize((455,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=455,y=0,width=455,height=160)

        #3rd image
        img3=Image.open('img/3.jpg')
        img3=img3.resize((456,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=910,y=0,width=455,height=160)

        #Main Frame
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=200,width=1340,height=560)

        #Upper Frame
        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Criminal Information',font=('times new roman',11,'bold'),fg='red',bg='white')
        upper_frame.place(x=10,y=10,width=1320,height=270)

        #Labels Entry

        #Case ID
        caseid=Label(upper_frame,text='Case ID:',font=('arial',11,'bold'),bg='white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        #Criminal No
        lbl_criminal_no=Label(upper_frame,font=('arial',12,'bold'),text='Crminal No:',bg='white')
        lbl_criminal_no.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_criminal_no=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_criminal_no.grid(row=0,column=3,padx=2,pady=7)

        #Criminal Name
        lbl_Name=Label(upper_frame,font=('arial',12,'bold'),text='Crminal Name:',bg='white')
        lbl_Name.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_Name=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_Name.grid(row=1,column=1,padx=2,pady=7,sticky=W)

        #Nick Name
        lbl_nickname=Label(upper_frame,font=('arial',12,'bold'),text='Nickname:',bg='white')
        lbl_nickname.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        txt_nickname=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_nickname.grid(row=1,column=3,padx=2,pady=7)

        #Arrest Date
        lbl_arrestDate=Label(upper_frame,font=('arial',12,'bold'),text='Arrest Date:',bg='white')
        lbl_arrestDate.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        txt_arrestDate=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_arrestDate.grid(row=2,column=1,padx=2,pady=7)

        #Date of Crime
        lbl_dateOfCrime=Label(upper_frame,font=('arial',12,'bold'),text='Date of Crime:',bg='white')
        lbl_dateOfCrime.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        txt_dateOfCrime=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_dateOfCrime.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        #Address
        lbl_address=Label(upper_frame,font=('arial',12,'bold'),text='Address:',bg='white')
        lbl_address.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        txt_address=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_address.grid(row=3,column=1,padx=2,pady=7)

        #Age
        lbl_age=Label(upper_frame,font=('arial',12,'bold'),text='Age:',bg='white')
        lbl_age.grid(row=3,column=2,padx=2,pady=7,sticky=W)

        txt_age=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_age.grid(row=3,column=3,padx=2,pady=7)

        #Occupation
        lbl_occupation=Label(upper_frame,font=('arial',12,'bold'),text='Occupation:',bg='white')
        lbl_occupation.grid(row=4,column=0,padx=2,pady=7,sticky=W)

        txt_occupation=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_occupation.grid(row=4,column=1,padx=2,pady=7)

        #Birth Mark
        lbl_birthMark=Label(upper_frame,font=('arial',12,'bold'),text='Birth Mark:',bg='white')
        lbl_birthMark.grid(row=4,column=2,padx=2,pady=7,sticky=W)

        txt_birthMark=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_birthMark.grid(row=4,column=3,padx=2,pady=7,sticky=W)

        #Crime Type
        lbl_crimeType=Label(upper_frame,font=('arial',12,'bold'),text='Crime Type:',bg='white')
        lbl_crimeType.grid(row=0,column=4,padx=2,pady=7,sticky=W)

        txt_crimeType=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_crimeType.grid(row=0,column=5,padx=2,pady=7)

        #Father Name
        lbl_fatherName=Label(upper_frame,font=('arial',12,'bold'),text='Father Name:',bg='white')
        lbl_fatherName.grid(row=1,column=4,padx=2,pady=7,sticky=W)

        txt_fatherName=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_fatherName.grid(row=1,column=5,padx=2,pady=7)






        #Lower Frame
        lower_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Criminal Information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        lower_frame.place(x=10,y=280,width=1320,height=270)

        search_frame=LabelFrame(lower_frame,bd=2,relief=RIDGE,text='Search Criminal Record',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1315,height=60)





if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()
