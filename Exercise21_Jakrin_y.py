from tkinter import *
import math

def leftClickButton(event):
    BMI = (float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    labelResult.configure(text=BMI)
    if BMI >= 30:
        x = "อ้วนมาก"
    elif 25<=BMI<=29.9:
        x = "อ้วน"
    elif 23<=BMI<=24.9:
        x = "น้ำหนักเกิน"
    elif 18.6<=BMI<=22.9:
        x = "น้ำหนักปกติ"
    else:
        x = "ผอมเกินไป"
    labelResult.configure(text=x)

MainWindow = Tk()

labelHeight = Label(MainWindow,text="ส่วนสูง (cm)")
labelHeight.grid(row=0,column=0)

textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)

labelWeight = Label(MainWindow,text="น้ำหนัก (kg)")
labelWeight.grid(row=1,column=0)

textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text="คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)

labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)

MainWindow.mainloop()
