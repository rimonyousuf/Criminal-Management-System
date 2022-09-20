from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox


class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1366x768+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')

        #Variables
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_birth_mark=StringVar()
        self.var_crime_type=StringVar()
        self.var_father_name=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()


        lbl_title=Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM',font=('times new roman',40,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1366,height=70)

        #Logo Image
        img_logo=Image.open(r'G:\Rimon Study\Criminal Management System\img\logo.jpg')
        img_logo=img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=100,y=5,width=60,height=60)

        #Image Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1366,height=130)

        img1=Image.open(r'G:\Rimon Study\Criminal Management System\img\1.jpg')
        img1=img1.resize((455,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=455,height=160)

        #2nd image
        img2=Image.open(r'G:\Rimon Study\Criminal Management System\img\2.jpg')
        img2=img2.resize((455,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=455,y=0,width=455,height=160)

        #3rd image
        img3=Image.open(r'G:\Rimon Study\Criminal Management System\img\3.jpg')
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

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        #Criminal No
        lbl_criminal_no=Label(upper_frame,font=('arial',12,'bold'),text='Crminal No:',bg='white')
        lbl_criminal_no.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_criminal_no=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22,font=('arial',11,'bold'))
        txt_criminal_no.grid(row=0,column=3,padx=2,pady=7)

        #Criminal Name
        lbl_Name=Label(upper_frame,font=('arial',12,'bold'),text='Crminal Name:',bg='white')
        lbl_Name.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_Name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
        txt_Name.grid(row=1,column=1,padx=2,pady=7,sticky=W)

        #Nick Name
        lbl_nickname=Label(upper_frame,font=('arial',12,'bold'),text='Nickname:',bg='white')
        lbl_nickname.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        txt_nickname=ttk.Entry(upper_frame,textvariable=self.var_nickname,width=22,font=('arial',11,'bold'))
        txt_nickname.grid(row=1,column=3,padx=2,pady=7)

        #Arrest Date
        lbl_arrestDate=Label(upper_frame,font=('arial',12,'bold'),text='Arrest Date:',bg='white')
        lbl_arrestDate.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        txt_arrestDate=ttk.Entry(upper_frame,textvariable=self.var_arrest_date,width=22,font=('arial',11,'bold'))
        txt_arrestDate.grid(row=2,column=1,padx=2,pady=7)

        #Date of Crime
        lbl_dateOfCrime=Label(upper_frame,font=('arial',12,'bold'),text='Date of Crime:',bg='white')
        lbl_dateOfCrime.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        txt_dateOfCrime=ttk.Entry(upper_frame,textvariable=self.var_date_of_crime,width=22,font=('arial',11,'bold'))
        txt_dateOfCrime.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        #Address
        lbl_address=Label(upper_frame,font=('arial',12,'bold'),text='Address:',bg='white')
        lbl_address.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold'))
        txt_address.grid(row=3,column=1,padx=2,pady=7)

        #Age
        lbl_age=Label(upper_frame,font=('arial',12,'bold'),text='Age:',bg='white')
        lbl_age.grid(row=3,column=2,padx=2,pady=7,sticky=W)

        txt_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('arial',11,'bold'))
        txt_age.grid(row=3,column=3,padx=2,pady=7)

        #Occupation
        lbl_occupation=Label(upper_frame,font=('arial',12,'bold'),text='Occupation:',bg='white')
        lbl_occupation.grid(row=4,column=0,padx=2,pady=7,sticky=W)

        txt_occupation=ttk.Entry(upper_frame,textvariable=self.var_occupation,width=22,font=('arial',11,'bold'))
        txt_occupation.grid(row=4,column=1,padx=2,pady=7)

        #Birth Mark
        lbl_birthMark=Label(upper_frame,font=('arial',12,'bold'),text='Birth Mark:',bg='white')
        lbl_birthMark.grid(row=4,column=2,padx=2,pady=7,sticky=W)

        txt_birthMark=ttk.Entry(upper_frame,textvariable=self.var_birth_mark,width=22,font=('arial',11,'bold'))
        txt_birthMark.grid(row=4,column=3,padx=2,pady=7,sticky=W)

        #Crime Type
        lbl_crimeType=Label(upper_frame,font=('arial',12,'bold'),text='Crime Type:',bg='white')
        lbl_crimeType.grid(row=0,column=4,padx=2,pady=7,sticky=W)

        txt_crimeType=ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=22,font=('arial',11,'bold'))
        txt_crimeType.grid(row=0,column=5,padx=2,pady=7)

        #Father Name
        lbl_fatherName=Label(upper_frame,font=('arial',12,'bold'),text='Father Name:',bg='white')
        lbl_fatherName.grid(row=1,column=4,padx=2,pady=7,sticky=W)

        txt_fatherName=ttk.Entry(upper_frame,textvariable=self.var_father_name,width=22,font=('arial',11,'bold'))
        txt_fatherName.grid(row=1,column=5,padx=2,pady=7)

        #Radio Button Gender
        radio_frame_gender=Label(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=730,y=83,width=185,height=25)

        lbl_gender=Label(upper_frame,font=('arial',12,'bold'),text='Gender:',bg='white')
        lbl_gender.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=('arial',9,'bold'),bg='white')
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        self.var_gender.set('male')

        female=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Female',value='female',font=('arial',9,'bold'),bg='white')
        female.grid(row=0,column=1,pady=2,padx=5,sticky=W)


        #Radio Button Wanted
        radio_frame_wanted=Label(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=730,y=123,width=185,height=25)

        lbl_wanted=Label(upper_frame,font=('arial',12,'bold'),text='Most Wanted:',bg='white')
        lbl_wanted.grid(row=3,column=4,sticky=W,padx=2,pady=7)

        yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='yes',font=('arial',9,'bold'),bg='white')
        yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        self.var_wanted.set('yes')

        no=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='No',value='no',font=('arial',9,'bold'),bg='white')
        no.grid(row=0,column=1,pady=2,padx=5,sticky=W)

        #Button
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=200,width=628,height=45)

        #Add Button
        btn_add=Button(button_frame,command=self.add_data,text='Record Save',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)

        #Update Button
        btn_update=Button(button_frame,command=self.update_data,text='Update',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)

        #Delete Button
        btn_delete=Button(button_frame,command=self.delete_data,text='Delete',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)

        #Clear Button
        btn_clear=Button(button_frame,command=self.clear_data,text='Clear',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)

        #Background right side 
        img4=Image.open(r'G:\Rimon Study\Criminal Management System\img\4.jpg')
        img4=img4.resize((420,245),Image.ANTIALIAS)
        self.photo4=ImageTk.PhotoImage(img4)

        self.img_4=Label(upper_frame,image=self.photo4)
        self.img_4.place(x=940,y=0,width=420,height=245)






        #Lower Frame
        lower_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Criminal Information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        lower_frame.place(x=10,y=280,width=1320,height=270)

        search_frame=LabelFrame(lower_frame,bd=2,relief=RIDGE,text='Search Criminal Record',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1315,height=60)

        #Search by
        search_by=Label(search_frame,font=('arial',11,'bold'),text='Search by',bg='red',fg='white')
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        #Combo Search Box
        self.var_com_search=StringVar()
        cmbo_bx=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('arial',11,'bold'),width=18,state='readonly')
        cmbo_bx['value']=('Select Option','Case_ID','Criminal_No')
        cmbo_bx.current(0)
        cmbo_bx.grid(row=0,column=1,sticky=W,padx=5)

        #Search Box
        self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_search,width=18,font=('arial',11,'bold'))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        #Search Button
        btn_search=Button(search_frame,command=self.search_data,text='Search',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        #All Button
        btn_all=Button(search_frame,command=self.fetch_data,text='Show All',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        #National Crime Agency
        crime_agency=Label(search_frame,font=('arial',20,'bold'),text='National Crime Agency',bg='white',fg='crimson')
        crime_agency.grid(row=0,column=5,sticky=W,padx=70)

        #Table Frame
        table_frame=Frame(lower_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1315,height=130)

        #Scroll
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=('1','2','3','4','5','6','7','8','9','10','11','12','13','14'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        #Table header
        self.criminal_table.heading('1',text='Case ID')
        self.criminal_table.heading('2',text='Criminal No')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='Nickname')
        self.criminal_table.heading('5',text='Arrest Date')
        self.criminal_table.heading('6',text='Crime Date')
        self.criminal_table.heading('7',text='Address')
        self.criminal_table.heading('8',text='Age')
        self.criminal_table.heading('9',text='Occupation')
        self.criminal_table.heading('10',text='Birth Mark')
        self.criminal_table.heading('11',text='Crime Type')
        self.criminal_table.heading('12',text='Father Name')
        self.criminal_table.heading('13',text='Gender')
        self.criminal_table.heading('14',text='Wanted')

        self.criminal_table['show']='headings'

        self.criminal_table.column('1',width=93)
        self.criminal_table.column('2',width=93)
        self.criminal_table.column('3',width=93)
        self.criminal_table.column('4',width=93)
        self.criminal_table.column('5',width=93)
        self.criminal_table.column('6',width=93)
        self.criminal_table.column('7',width=93)
        self.criminal_table.column('8',width=93)
        self.criminal_table.column('9',width=93)
        self.criminal_table.column('10',width=93)
        self.criminal_table.column('11',width=93)
        self.criminal_table.column('12',width=93)
        self.criminal_table.column('13',width=93)
        self.criminal_table.column('14',width=93)

        self.criminal_table.pack(fill=BOTH,expand=1)

        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()


    #Add Function
    def add_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=sqlite3.connect("G:\Rimon Study\Criminal Management System\Database\CMS.db")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into Criminal('Case_ID','Criminal_No','Criminal_Name','Nickname','Arrest_Date','Date_of_Crime','Address','Age','Occupation','Birth_Mark','Crime_Type','Father_Name','Gender','Most_Wanted')values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                                                                                                           
                                                                                                            self.var_case_id.get(),
                                                                                                            self.var_criminal_no.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_nickname.get(),
                                                                                                            self.var_arrest_date.get(),
                                                                                                            self.var_date_of_crime.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_age.get(),
                                                                                                            self.var_occupation.get(),
                                                                                                            self.var_birth_mark.get(),
                                                                                                            self.var_crime_type.get(),
                                                                                                            self.var_father_name.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_wanted.get()

                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo("Success","Criminal record has benn added")
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}")


    #Fetch Data
    def fetch_data(self):
        conn=sqlite3.connect("G:\Rimon Study\Criminal Management System\Database\CMS.db")
        my_cursor=conn.cursor()
        my_cursor.execute('select * from Criminal')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()


    #Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birth_mark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])


    #Update
    def update_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure update this criminal record")
                if update>0:
                    conn=sqlite3.connect("G:\Rimon Study\Criminal Management System\Database\CMS.db")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update Criminal set Criminal_No=?,Criminal_Name=?,Nickname=?,Arrest_Date=?,Date_of_Crime=?,Address=?,Age=?,Occupation=?,Birth_Mark=?,Crime_Type=?,Father_Name=?,Gender=?,Most_Wanted=? WHERE Case_ID=?" ,(

                                                                                                                                                                                                                                                self.var_criminal_no.get(),
                                                                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                                                                self.var_nickname.get(),
                                                                                                                                                                                                                                                self.var_arrest_date.get(),
                                                                                                                                                                                                                                                self.var_date_of_crime.get(),
                                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                                self.var_age.get(),
                                                                                                                                                                                                                                                self.var_occupation.get(),
                                                                                                                                                                                                                                                self.var_birth_mark.get(),
                                                                                                                                                                                                                                                self.var_crime_type.get(),
                                                                                                                                                                                                                                                self.var_father_name.get(),
                                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                                self.var_wanted.get(),
                                                                                                                                                                                                                                                self.var_case_id.get(),

                                                                                                                                                                                                                                                ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo("Success","Crminal record has been successfully updated")
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}")


    #Delete
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                delete=messagebox.askyesno("Delete","Are you sure delete this criminal record")
                if delete>0:
                    conn=sqlite3.connect("G:\Rimon Study\Criminal Management System\Database\CMS.db")
                    my_cursor=conn.cursor()
                    sql="delete from Criminal where Case_ID=?"
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo("Success","Crminal record has been successfully deleted")
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}")


    #Clear Data
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birth_mark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")


    #Search Data
    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=sqlite3.connect("G:\Rimon Study\Criminal Management System\Database\CMS.db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from Criminal where " +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}")
        





if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()