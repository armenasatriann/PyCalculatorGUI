import tkinter as tk
root = tk.Tk()
def insertElement(symbol):
    entry.insert(tk.END, symbol)
def entryClear():
        entry.delete(0, tk.END)
'''
def Calculate():
    text = entry.get()
    result = eval(text)
    entryClear()
    entry.insert(0, result)
'''
def Calculate():
    text = entry.get()
    result = 0
    if '+' in text:
        splitted = text.split('+')
        first = float(splitted[0])
        second = float(splitted[1])
        result = first + second
    elif '-' in text:
        splitted = text.split('-')
        first = float(splitted[0])
        second = float(splitted[1])
        result = first - second
    elif '*' in text:
        splitted = text.split('*')
        first = float(splitted[0])
        second = float(splitted[1])
        result = first * second
    elif '/' in text:
        splitted = text.split('/')
        first = float(splitted[0])
        second = float(splitted[1])
        if second == 0:
            entryClear()
            entry.insert(0, "Eval Error")
            return
        result = first / second
    entryClear()
    entry.insert(0,result)
def deleteSymbol():
        text = entry.get()
        if text:
            entry.delete(len(text) - 1,tk.END)
root.title("Calculator")
root.geometry("300x410")
root.iconphoto(True, tk.PhotoImage(file=r'C:\Users\armen\Desktop\Uni\Homework\Python\Calculator\Content\Icon.png'))
root.resizable(False,False)
entry = tk.Entry(root,width=150,font=("Roboto",20),bg="#F2F3F4",borderwidth=0, highlightthickness=0)
entry.place(x=0,y=0)
button = tk.Button(text="1",bg="#525252",fg="White",borderwidth=0, highlightthickness=0,command=lambda:insertElement(1))
button.place(x=0,y=38,width=75,height=75)
button = tk.Button(text="2",bg="#525252",fg="White",borderwidth=0, highlightthickness=0,command=lambda:insertElement(2))
button.place(x=75,y=38,width=75,height=75)
button = tk.Button(text="3",bg="#525252",fg="White",borderwidth=0, highlightthickness=0,command=lambda:insertElement(3))
button.place(x=150,y=38,width=75,height=75)
button = tk.Button(text="CE",bg="#2E2E2E",fg="White",borderwidth=0, highlightthickness=0,command=lambda:entryClear())
button.place(x=225,y=38,width=75,height=75)
button = tk.Button(text="4",bg="#525252",fg="White",borderwidth=0, highlightthickness=0,command=lambda:insertElement(4))
button.place(x=0,y=113,width=75,height=75)
button = tk.Button(text="5",bg="#525252",fg="White",borderwidth=0, highlightthickness=0,command=lambda:insertElement(5))
button.place(x=75,y=113,width=75,height=75)
button = tk.Button(text="6",bg="#525252",fg="White",borderwidth=0, highlightthickness=0,command=lambda:insertElement(6))
button.place(x=150,y=113,width=75,height=75)
button = tk.Button(text="+",bg="#2E2E2E",fg="White",borderwidth=0, highlightthickness=0,command=lambda:insertElement("+"))
button.place(x=225,y=113,width=75,height=75)
button = tk.Button(text="7",bg="#525252",fg="White",borderwidth=0, highlightthickness=0,command=lambda:insertElement(7))
button.place(x=0,y=188,width=75,height=75)
button = tk.Button(text="8",bg="#525252",fg="White",borderwidth=0, highlightthickness=0,command=lambda:insertElement(8))
button.place(x=75,y=188,width=75,height=75)
button = tk.Button(text="9",bg="#525252",fg="White",borderwidth=0, highlightthickness=0,command=lambda:insertElement(9))
button.place(x=150,y=188,width=75,height=75)
button = tk.Button(text="-",bg="#2E2E2E",fg="White",borderwidth=0, highlightthickness=0,command=lambda:insertElement("-"))
button.place(x=225,y=188,width=75,height=75)
button = tk.Button(text="0",bg="#525252",fg="White",borderwidth=0, highlightthickness=0,command=lambda:insertElement(0))
button.place(x=0,y=263,width=150,height=75)
button = tk.Button(text="*",bg="#2E2E2E",fg="White",borderwidth=0, highlightthickness=0,command=lambda:insertElement("*"))
button.place(x=150,y=263,width=75,height=75)
button = tk.Button(text='=',bg="#E67E22",fg="White",borderwidth=0, highlightthickness=0,command=lambda:Calculate())
button.place(x=225,y=263,width=75,height=150)
button = tk.Button(text='␡',bg="#2E2E2E",fg="White",borderwidth=0, highlightthickness=0,command=lambda:deleteSymbol())
button.place(x=0,y=338,width=75,height=75)
button = tk.Button(text='.',bg="#2E2E2E",fg="White",borderwidth=0, highlightthickness=0,command=lambda:insertElement('.'))
button.place(x=75,y=338,width=75,height=75)
button = tk.Button(text="/",bg="#2E2E2E",fg="White",borderwidth=0, highlightthickness=0,command=lambda:insertElement("/"))
button.place(x=150,y=338,width=75,height=75)
root.mainloop()