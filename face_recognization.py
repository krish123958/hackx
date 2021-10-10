from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Recognition")

        title_lb1=Label(self.root,text="Face recognition",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lb1.place(x=0,y=0,width=1530,height=50)

        img=Image.open("images/face-detection.jpg")
        img=img.resize((600,500),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=500,y=100,width=600,height=500)

        b1_1=Button(self.root,text="Click here to detect",command=self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),bg="Black",fg="white")
        b1_1.place(x=500,y=680,width=600,height=40)
    def face_recog(self):
        def draw_boundary(img,classifier,scalefactor,minNeighbors,color,text,clf):
            grey_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(grey_image,scalefactor,minNeighbors)

            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)
                id,predict=clf.predict(grey_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",user="root123",password="18481A05c2@1234567890",database="face")
                my_cursor=conn.cursor()

                my_cursor.execute("select name from student where id="+str(id))
                n=my_cursor.fetchall()
                

                my_cursor.execute("select Department from student where id="+str(id))
                d=my_cursor.fetchall()
                

                my_cursor.execute("select section from student where id="+str(id))
                se=my_cursor.fetchall()


                if confidence >77:
                    cv2.putText(img,f"Name:{id}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"section:{se}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,h]
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifer.xml")

        video_cap=cv2.VideoCapture(0)

        while(1):
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome to face recoginazation",img)

            if cv2.waitKey(1)==3:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ =="__main__":
    root=Tk()
    obj=recognition(root)
    root.mainloop()
