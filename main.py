from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import student
from train import Train
import os
from face_recognization import recognition
class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Recognition")

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

        title_lb1=Label(bg_img,text="FACE RECOGNITION SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1530,height=45)
        #button 1
        img4=Image.open("images/header1.jfif")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=400,y=100,width=220,height=220)


        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="Blue",fg="red")
        b1_1.place(x=400,y=300,width=220,height=40)


        #button 2
        img5=Image.open("images/header1.jfif")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.train_data)
        b1.place(x=800,y=100,width=220,height=220)


        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="Blue",fg="red")
        b1_1.place(x=800,y=300,width=220,height=40)

        #button 3
        img6=Image.open("images/header1.jfif")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=400,width=220,height=220)


        b1_1=Button(bg_img,text="photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="Blue",fg="red")
        b1_1.place(x=400,y=600,width=220,height=40)


        #button 4
        img7=Image.open("images/header1.jfif")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,command=self.face_rec,cursor="hand2")
        b1.place(x=800,y=400,width=220,height=220)


        b1_1=Button(bg_img,text="face detect",command=self.face_rec,cursor="hand2",font=("times new roman",15,"bold"),bg="Blue",fg="red")
        b1_1.place(x=800,y=600,width=220,height=40)

        #button 5
        img11=Image.open("images/header1.jfif")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1200,y=200,width=220,height=220)


        b1_1=Button(bg_img,text="Attandance",cursor="hand2",font=("times new roman",15,"bold"),bg="Blue",fg="red")
        b1_1.place(x=1200,y=400,width=220,height=40)


        #======functions============================================================
    def open_img(self):
        os.startfile("Data")
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)   
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=recognition(self.new_window) 





      


if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()