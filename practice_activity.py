from tkinter import *
from PIL import ImageTk , Image
from tkinter import filedialog
import os
root = Tk()
root.configure(background="#adf8da")
root.minsize(652 , 653)
root.maxsize(652 , 653)

open_img = ImageTk.PhotoImage(Image.open ("open.png"))
save_img = ImageTk.PhotoImage(Image.open ("save.png"))
exit_img = ImageTk.PhotoImage(Image.open ("exit.jpg"))

label_file_name = Label(root, text="File Name")
label_file_name.place(relx=0.38,rely=0.05,anchor= CENTER)

input_file_name = Entry(root,foreground="red")
input_file_name.place(relx=0.57,rely=0.05, anchor= CENTER)

my_text = Text(root,height=35.50,width=80,background="#fae4ba",foreground="blue")
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)

name = ""

def Open_File():
    global name
    my_text.delete(1.0 , END)
    input_file_name.delete(0 , END)
    text_file = filedialog.askopenfilename(title = "Open Text File " , filetypes = (("Text Files" , "*.txt") , ))
    
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    input_file_name.insert(END,formated_name)
    root.title(formated_name)
    text_file = open(name , 'r')
    paragraph = text_file.read()
    my_text.insert(END , paragraph)
    text_file.close()

def save():
    input_name = input_file_name.get()
    file = open(input_name + ".txt" , "w")
    data = my_text.get("1.0" , END)
    print(data)
    file.write(data)
    input_file_name.delete(0 , END)
    my_text.delete(1.0 , END)
    messagebox.showinfo("Update" , "Success")

def closeWindow():
    
    root.destroy()

open_button=Button(root,image=open_img,text="Open File",command=Open_File)
open_button.place(relx=0.05,rely=0.05,anchor=CENTER)

save_button=Button(root,image=save_img,text="Save",command=save)
save_button.place(relx=0.12,rely=0.05,anchor=CENTER)

exit_button=Button(root,image=exit_img,text="Exit",command=closeWindow)
exit_button.place(relx=0.19,rely=0.05,anchor=CENTER)

root.mainloop()

