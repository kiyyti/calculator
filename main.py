from pdf2image import convert_from_path
from tkinter import *
from tkinter import messagebox

def pdf2img():
    try:
        imges = comvert_from_path(str(e1.get()))
        for img in images:d
            img.save("")
    except:
        result = "ไม่เจอ pdf ไฟล์"
        messagebox.showinfo("Result", result)
    else:
        result = "แปลงไฟล์เสร็จสิ้น"
        messagebox.showinfo("Result", result)

master = TK()
lebel(master, text="File Location").grid(row=0,sticky=W)

e1 = Entry(master)
e1.grid(row=0, column=1)

b = Button(master, text="convert", command=pdf2img)
b.grid(row=0, column=2,columnspan=2,rowspan=2,padx=5,pady=5)

mainloop()