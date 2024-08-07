from tkinter import *
import os
 
current_directory = os.path.dirname(os.path.realpath(__file__))
apelsinfile = current_directory + r"\apelsin.png"
backspacefile = current_directory + r"\backspace.png"
swapfile = current_directory + r"\swap.png"

root = Tk()
root.geometry("250x250")
root.title("smart thing")
root.resizable(height=False, width=False)

frame = Frame(root)
frame.place(relwidth=1,relheight=1)

output = Label(frame, justify="right", text="", background="white", font=("Arial", 20), anchor="e")
output.place(relx=0,rely=0.05,relwidth=1,relheight=0.2)
output1 = Label(frame, justify="right", text="", background="white", font=("Arial", 10), anchor="e")
output1.place(relx=0,rely=0,relwidth=0.95,relheight=0.05)
argument = Label(frame, justify="right", text="", background="white", font=("Arial", 10), anchor="e")
argument.place(relx=0.95,rely=0,relwidth=0.05,relheight=0.05)

apelsinpng = PhotoImage(file = apelsinfile)
apelsinimage = apelsinpng.subsample(15, 15) 
apelsin = Label(frame, image = apelsinimage, background="white")
apelsin.place(relx=-0.2,rely=0,relwidth=0.5,relheight=0.3)

def clear():
    output.config(text="")
    output1.config(text="")
    argument.config(text="")
def eql():
    v = 0
    str1 = output1.cget("text")
    str2 = output.cget("text")
    argum = argument.cget("text")
    if str2 == "" or str1 == "" or str2 == "-":
        return
    num1 = float(str1)
    num2 = float(str2)

    if argum == "%":
        result = num1 % num2
        if result.is_integer():
            result = int(result)
        output1.config(text="")
        argument.config(text="")
        output.config(text=str(result))
    elif argum == "/":
        result = num1 / num2
        if result.is_integer():
            result = int(result)
        output1.config(text="")
        argument.config(text="")
        output.config(text=str(result))
    elif argum == "*":
        result = num1 * num2
        if result.is_integer():
            result = int(result)
        output1.config(text="")
        argument.config(text="")
        output.config(text=str(result))
    elif argum == "-":
        result = num1 - num2
        if result.is_integer():
            result = int(result)
        output1.config(text="")
        argument.config(text="")
        output.config(text=str(result))
    elif argum == "+":
        result = num1 + num2
        if result.is_integer():
            result = int(result)
        output1.config(text="")
        argument.config(text="")
        output.config(text=str(result))
def backs():
    v = 0
    newtext = ""
    text = output.cget("text")
    for i in text:
        if v == len(text) - 1:
            output.config(text=newtext)
        newtext = newtext + text[v]
        v = v + 1
def swap():
    text = output.cget("text")
    newtext = ""
    if text.find("-") > -1:
        for i in text:
            if i != "-":
                newtext = newtext + i
        output.config(text=newtext)
    else:
        output.config(text="-"+text)

def but1():
    if output.cget("text") == "" or output.cget("text") == "-" or argument.cget("text") != "":
        return
    output1.config(text=output.cget("text"))
    argument.config(text="%")
    output.config(text="")
def but2():
    if output.cget("text") == "" or output.cget("text") == "-" or argument.cget("text") != "":
        return
    output1.config(text=output.cget("text"))
    argument.config(text="/")
    output.config(text="")
def but3():
    output.config(text=output.cget("text")+"7")
def but4():
    output.config(text=output.cget("text")+"8")
def but5():
    output.config(text=output.cget("text")+"9")
def but6():
    if output.cget("text") == "" or output.cget("text") == "-" or argument.cget("text") != "":
        return
    output1.config(text=output.cget("text"))
    argument.config(text="*")
    output.config(text="")
def but7():
    output.config(text=output.cget("text")+"4")
def but8():
    output.config(text=output.cget("text")+"5")
def but9():
    output.config(text=output.cget("text")+"6")
def but10():
    if output.cget("text") == "":
        output.config(text=output.cget("text")+"-")
    elif output.cget("text") == "-":
        return
    else:
        if output.cget("text") == "" or output.cget("text") == "-" or argument.cget("text") != "":
            return
        output1.config(text=output.cget("text"))
        argument.config(text="-")
        output.config(text="")
def but11():
    output.config(text=output.cget("text")+"1")
def but12():
    output.config(text=output.cget("text")+"2")
def but13():
    output.config(text=output.cget("text")+"3")
def but14():
    if output.cget("text") == "" or output.cget("text") == "-" or argument.cget("text") != "":
        return
    output1.config(text=output.cget("text"))
    argument.config(text="+")
    output.config(text="")
def but15():
    output.config(text=output.cget("text")+"0")
def but16():
    text = output.cget("text")
    if text != "" and text != "-" and text.find(".") == -1:
       output.config(text=text+".")

C = Button(frame, text="C", font=("Arial", 15),background="#d4fcec", command=clear)
C.place(relx=0,rely=0.25,relwidth=0.25,relheight=0.15)

photo1 = PhotoImage(file = backspacefile) 
photoimage1 = photo1.subsample(20, 20) 
backspace = Button(frame, image = photoimage1,background="#d4fcec", command=backs)
backspace.place(relx=0.25,rely=0.25,relwidth=0.25,relheight=0.15)

button1 = Button(frame, text="%", font=("Arial", 15),background="#d4fcec", command=but1)
button1.place(relx=0.5,rely=0.25,relwidth=0.25,relheight=0.15)
button2 = Button(frame, text="/", font=("Arial", 15),background="#d4fcec", command=but2)
button2.place(relx=0.75,rely=0.25,relwidth=0.25,relheight=0.15)

button3 = Button(frame, text="7", font=("Arial", 15),background="#d4fcec", command=but3)
button3.place(relx=0,rely=0.4,relwidth=0.25,relheight=0.15)
button4 = Button(frame, text="8", font=("Arial", 15),background="#d4fcec", command=but4)
button4.place(relx=0.25,rely=0.4,relwidth=0.25,relheight=0.15)
button5 = Button(frame, text="9", font=("Arial", 15),background="#d4fcec", command=but5)
button5.place(relx=0.5,rely=0.4,relwidth=0.25,relheight=0.15)
button6 = Button(frame, text="*", font=("Arial", 15),background="#d4fcec", command=but6)
button6.place(relx=0.75,rely=0.4,relwidth=0.25,relheight=0.15)

button7 = Button(frame, text="4", font=("Arial", 15),background="#d4fcec", command=but7)
button7.place(relx=0,rely=0.55,relwidth=0.25,relheight=0.15)
button8 = Button(frame, text="5", font=("Arial", 15),background="#d4fcec", command=but8)
button8.place(relx=0.25,rely=0.55,relwidth=0.25,relheight=0.15)
button9 = Button(frame, text="6", font=("Arial", 15),background="#d4fcec", command=but9)
button9.place(relx=0.5,rely=0.55,relwidth=0.25,relheight=0.15)
button10 = Button(frame, text="-", font=("Arial", 15),background="#d4fcec", command=but10)
button10.place(relx=0.75,rely=0.55,relwidth=0.25,relheight=0.15)

button11 = Button(frame, text="1", font=("Arial", 15),background="#d4fcec", command=but11)
button11.place(relx=0,rely=0.7,relwidth=0.25,relheight=0.15)
button12 = Button(frame, text="2", font=("Arial", 15),background="#d4fcec", command=but12)
button12.place(relx=0.25,rely=0.7,relwidth=0.25,relheight=0.15)
button13 = Button(frame, text="3", font=("Arial", 15),background="#d4fcec", command=but13)
button13.place(relx=0.5,rely=0.7,relwidth=0.25,relheight=0.15)
button14 = Button(frame, text="+", font=("Arial", 15),background="#d4fcec", command=but14)
button14.place(relx=0.75,rely=0.7,relwidth=0.25,relheight=0.15)

button15 = Button(frame, text="0", font=("Arial", 15),background="#d4fcec", command=but15)
button15.place(relx=0.25,rely=0.85,relwidth=0.25,relheight=0.15)
button16 = Button(frame, text=".", font=("Arial", 15),background="#d4fcec", command=but16)
button16.place(relx=0.5,rely=0.85,relwidth=0.25,relheight=0.15)
button17 = Button(frame, text="=", font=("Arial", 15),background="#9cffd7", command=eql)
button17.place(relx=0.75,rely=0.85,relwidth=0.25,relheight=0.15)

photo2 = PhotoImage(file = swapfile) 
photoimage2 = photo2.subsample(30, 30) 
swap = Button(frame, image = photoimage2,background="#d4fcec", command=swap)
swap.place(relx=0,rely=0.85,relwidth=0.25,relheight=0.15)

root.mainloop()