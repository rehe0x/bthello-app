import tkinter

if __name__ == "__main__":
    top = tkinter.Tk()

    top.minsize(530,380)
    top.maxsize(1000,500)

    label = tkinter.Label(top,text='Hello Gui')
    label.pack()

    li = ['C','python','php','html','SQL','java']
    movie = ['CSS','jQuery','Bootstrap']
    listb = tkinter.Listbox(top)
    listb2 = tkinter.Listbox(top)
    for i in li:
        listb.insert(0,i)
    
    for i in movie:
        listb2.insert(0,i)
    
    listb.pack()
    listb2.pack()
    top.mainloop()