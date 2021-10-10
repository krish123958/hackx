
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Recognition")

        #=======variables========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_std_name=StringVar()
        self.var_section=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()

        img=Image.open("images/header1.jfif")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        img1=Image.open("images/header1.jfif")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        img2=Image.open("images/header1.jfif")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #bg image
        img3=Image.open("images/header1.jfif")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lb1=Label(bg_img,text="STUDENT SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=45,width=1530,height=710)

        #left label
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=5,y=10,width=650,height=710)

        #current course
        current_course = LabelFrame(left_frame,bd=2,relief=RIDGE,text="course informatiom",font=("times new roman",12,"bold"))
        current_course.place(x=-1,y=10,width=648,height=200)
        #department
        dep_label =Label(current_course,text="Select Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_course,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=50,outline=None,state="readonly")
        dep_combo["values"]=("Select Department","CSE","IT","ECE","EEE","mech","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        #course
        course_label =Label(current_course,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=1,column=0,sticky=W)

        course_combo=ttk.Combobox(current_course,textvariable=self.var_course,font=("times new roman",12,"bold"),width=50,outline=None,state="readonly")
        course_combo["values"]=("Select course","Btech")
        course_combo.current(0)
        course_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        #year
        year_label =Label(current_course,text="year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=2,column=0,sticky=W)

        year_combo=ttk.Combobox(current_course,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,outline=None,state="readonly")
        year_combo["values"]=("Select year","1","2","3","4")
        year_combo.current(0)
        year_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)
        #semester
        semester_label =Label(current_course,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=3,column=0,sticky=W)

        semester_combo=ttk.Combobox(current_course,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,outline=None,state="readonly")
        semester_combo["values"]=("Select semester","1","2")
        semester_combo.current(0)
        semester_combo.grid(row=3,column=1,padx=2,pady=10,sticky=W)
        
        #class student informatiom
        student_course = LabelFrame(left_frame,bd=2,relief=RIDGE,text="student informatiom",font=("times new roman",12,"bold"))
        student_course.place(x=-1,y=210,width=648,height=400)
        #student Id
        studentid_label =Label(student_course,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,sticky=W)


        studentID_entry =ttk.Entry(student_course,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        #student name

        studentname_label =Label(student_course,text="StudentName:",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,sticky=W)

        studentname_entry =ttk.Entry(student_course,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #Section

        section_label =Label(student_course,text="Section",font=("times new roman",12,"bold"),bg="white")
        section_label.grid(row=1,column=0,sticky=W)

        section_combo=ttk.Combobox(student_course,textvariable=self.var_section,font=("times new roman",12,"bold"),width=17,outline=None,state="readonly")
        section_combo["values"]=("Select section","A","B","C","D")
        section_combo.current(0)
        section_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Gender
        gender_label =Label(student_course,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=1,column=2,sticky=W)

        gender_combo=ttk.Combobox(student_course,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=17,outline=None,state="readonly")
        gender_combo["values"]=("Select Gender","male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #dob

        dob_label =Label(student_course,text="DOB(DD/MM/YY):",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=0,sticky=W)

        dob_entry =ttk.Entry(student_course,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        #email
        email_label =Label(student_course,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=2,column=2,sticky=W)

        email_entry =ttk.Entry(student_course,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=2,column=3,padx=2,pady=10,sticky=W)

        
        #phone number

        ph_label =Label(student_course,text="PHONE NUMBER:",font=("times new roman",12,"bold"),bg="white")
        ph_label.grid(row=3,column=0,sticky=W)

        ph_entry =ttk.Entry(student_course,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        ph_entry.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        #address

        address_label =Label(student_course,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=3,column=2,sticky=W)

        address_entry =ttk.Entry(student_course,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=3,column=3,padx=2,pady=10,sticky=W)
        
        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(student_course,text="with photo",variable=self.var_radio1,value="YES")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(student_course,variable=self.var_radio1,text="without photo",value="NO")
        radiobtn2.grid(row=6,column=1)

        #buttons at last
        btn_frame=Frame(student_course,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=648,height=35)

        save_btn=Button(btn_frame,width=17,text="Save",command=self.add_data,font=("times new roman",12,"bold"),bg="black",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,width=17,text="update",command=self.update_data,font=("times new roman",12,"bold"),bg="black",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,width=17,text="Delete",command=self.delete_data,font=("times new roman",12,"bold"),bg="black",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,width=17,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),bg="black",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(student_course,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=245,width=648,height=35)


        take_photo=Button(btn_frame1,width=35,text="Take photo sample",command=self.generate_dataset,font=("times new roman",12,"bold"),bg="black",fg="white")
        take_photo.grid(row=0,column=0)

        update_photo=Button(btn_frame1,width=35,text="update photo sample",font=("times new roman",12,"bold"),bg="black",fg="white")
        update_photo.grid(row=0,column=1)
        

        
        #Right label
        right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=700,y=10,width=805,height=710)
         

        #===================search system=====

        search_frame = LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search ",font=("times new roman",12,"bold"))
        search_frame.place(x=-1,y=0,width=800,height=70)


        search_label =Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="white")
        search_label.grid(row=0,column=0,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=20,outline=None,state="readonly")
        search_combo["values"]=("Select","ID","Phone_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        search_entry =ttk.Entry(search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=2,pady=10,sticky=W) 

        search_btn=Button(search_frame,width=20,height=-2,text="Search",font=("times new roman",10,"bold"),bg="black",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(search_frame,width=20,text="Show A11",font=("times new roman",10,"bold"),bg="black",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)


        table_frame = Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=70,width=800,height=500)


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","section","gender","dob","email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)

        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)

        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="semester")
        self.student_table.heading("id",text="Roll_no")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("section",text="Section")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"

        

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("section",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)


        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    #=======function==========  ======================================================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_id.get()=="" : 
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root123",password="18481A05c2@1234567890",database="face")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_id.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_section.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_radio1.get(),))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","students details succesfully saved")
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    #data fetch_data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root123",password="18481A05c2@1234567890",database="face")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if( len(data) != 0):
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,value=i)
            conn.commit()
        conn.close()
#cursor function

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_section.set(data[6])
        self.var_gender.set(data[7])
        self.var_dob.set(data[8])
        self.var_email.set(data[9])
        self.var_phone.set(data[10])
        self.var_address.set(data[11])
        self.var_radio1.set(data[12])
    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_id.get()=="" : 
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:

                update=messagebox.askyesno("Upadate","Do you want to update student details",parent=self.root)  
                if update>0:
                    conn=mysql.connector.connect(host="localhost",user="root123",password="18481A05c2@1234567890",database="face")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,course=%s,year=%s,sem=%s,name=%s,section=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,photo=%s where id=%s",(
                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                            self.var_section.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                            self.var_id.get(),))
                else:
                    if not update:
                        return
                messagebox.showinfo("success","students details updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Errorr",f"Due to:{str(es)}",parent=self.root)
    #delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","student id must required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root123",password="18481A05c2@1234567890",database="face")
                    my_cursor=conn.cursor()
                    my_cursor.execute("delete from student where id=%s",(self.var_id.get(),))
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("deleted","succesfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Errorr",f"Due to:{str(es)}",parent=self.root)   
    #reset
    def reset_data(self):
        self.var_dep.set('Select Department')
        self.var_course.set('Select course')
        self.var_year.set('Select year')
        self.var_semester.set('Select semester')
        self.var_id.set("")
        self.var_std_name.set('')
        self.var_section.set('Select section')
        self.var_gender.set('Select Gender')
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")
    # generate data set
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_id.get()=="" : 
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root123",password="18481A05c2@1234567890",database="face")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                iD=0
                for x in myresult:
                    iD+=1
                my_cursor.execute("update student set Department=%s,course=%s,year=%s,sem=%s,name=%s,section=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,photo=%s where id=%s",(
                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                            self.var_section.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                            self.var_id.get()==iD+1,))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #load predefined
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while(1):
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="Data/user."+str(iD)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
                        cv2.imshow("cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("result","generate data set succesfully")
            except Exception as es:
                messagebox.showerror("Errorr",f"Due to:{str(es)}",parent=self.root)








    











if __name__ =="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()