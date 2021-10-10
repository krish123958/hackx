from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Recognition")

        title_lb1=Label(self.root,text="Train your images here",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lb1.place(x=0,y=0,width=1530,height=50)
        b1_1=Button(self.root,text="Click here to train your data",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),bg="Black",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=40)


    def train_classifier(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')#Grey scale image
            imagenp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Train",imagenp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        #======train classifier =================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifer.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","training dataset completed")


        
if __name__ =="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()