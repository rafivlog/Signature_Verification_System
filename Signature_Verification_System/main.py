import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter import *
import cv2
from numpy import result_type
from signature import match
import csv

# Mach Threshold
THRESHOLD = 80
path="demo.png"
name="Demo"
def load_user_name():
    found=False
    global path
    demo_dataset=dataset
    for row in demo_dataset:
        print(userid_data.get(),row[0]) 
        if(row[0] == userid_data.get()):
            found=True
            path=row[3]
            name=row[1]
            print(row[1])
            break
    if(found==False):
        messagebox.showerror("Failure: User Not Found","User Not Found!!")
    else:
        username_label = tk.Label(root, text="User Name : "+name, font=10)
        username_label.place(x=10, y=180)
    return

def browsefunc(ent):
    filename = askopenfilename(filetypes=([
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg"),
    ]))
    ent.delete(0, tk.END)
    ent.insert(tk.END, filename)
    print(filename)  # add this

def checkSimilarity(window, path1, path2):
    result = match(path1=path1, path2=path2)
    if(result <= THRESHOLD):
        messagebox.showerror("Failure: Signatures Do Not Match","Signatures Do Not Match")
        pass
    else:
        messagebox.showinfo("Success: Signatures Match","Signatures are "+str(result)+f" % similar!!")
    return True

dataset= csv.reader(open('D:\Signature-Matching\database\IP_Dataset.csv','r'))

root = tk.Tk()
root.title("Signature Verification")
root.geometry("500x500") 

label = tk.Label(root, text="Signature Verification System", font=10)
label.place(x=120, y=50)

userid_label = tk.Label(root, text="User_ID : ", font=10)
userid_label.place(x=10, y=120)

userid_data = StringVar()
userid_textbox = tk.Entry(root,textvariable=userid_data ,font=('Arial',15))

userid_textbox.place(x=150, y=120,height=27,width=230)
search_user = tk.Button(root,command=lambda:load_user_name(), text="Search", font=10)

search_user.place(x=400,y=110)
image2_path_entry = tk.Entry(root, font=10)

image2_path_entry.place(x=150, y=240)
img2_message = tk.Label(root, text="Signature 2", font=10)

img2_message.place(x=10, y=240)
img2_browse_button = tk.Button(root, text="Browse", font=10, command=lambda: browsefunc(ent=image2_path_entry))
img2_browse_button.place(x=400, y=230)

compare_button = tk.Button(root, text="Compare", font=10, command=lambda: checkSimilarity(window=root,path1=path,path2=image2_path_entry.get(),))
compare_button.place(x=200, y=320)
root.mainloop()
