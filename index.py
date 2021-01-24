from tkinter import *
from tkinter import ttk, messagebox as msg
import os
import datetime

main_win = Tk()
main_win.geometry("900x600")


def isunique(name):
    if f"{name}.txt" in files:
        print("hello")
        return False
    else:
        print("no")
        return True
style=

def add():
    main_win.title("Note Taker")
    add_win = Toplevel(main_win)
    add_win.geometry("900x600")

    def done():
        if name_val.get():
            if isunique(name_val.get()):
                current = str(datetime.datetime.now())
                tree.insert("", END, values=(1, name_val.get(), desc_val.get(), current[:11], current[11:19]))
                with open(f"{name_val.get()}.txt", "w") as file:
                    file.write(f"Date/Time : {current[:19]}\n{desc_val.get()}  \n\n{tex.get('0.0', END)}")
                    file.close()
                add_win.destroy()
            else:
                msg.showwarning("Already Exists", "Note with this name already exists!")
        else:
            msg.showwarning("Empty credential!", "Please Fill the name Entry")

    Label(add_win, text="Name", font="None 17").place(x=100, y=50)
    Label(add_win, text="Description", font="None 17").place(x=100, y=100)
    Label(add_win, text="Note", font="None 17").place(x=100, y=200)

    name_val = StringVar()
    desc_val = StringVar()
    Entry(add_win, textvariable=name_val, font="None 17", width=15).place(x=250, y=50)
    Entry(add_win, textvariable=desc_val, font="None 17", width=25).place(x=250, y=100)
    tex = Text(add_win, font="None 12", width=55, height=20)
    tex.place(x=250, y=200)

    Button(add_win, text="Done", font="None 17", command=done).place(x=800, y=200)
    add_win.mainloop()


def delete(event):
    ask = msg.askyesno("Confirmation", "Are you sure you want to delete?")
    if ask:
        selec = tree.selection()
        os.remove(f"{tree.item(selec)['values'][1]}.txt")
        tree.delete(selec)


def edit():
    edit_win = Toplevel(main_win)
    edit_win.geometry("900x600")

    def done():
        if isunique(name_val.get()):
            current = str(datetime.datetime.now())
            tree.item(tree.selection(), text="",
                      values=(1, name_val.get(), desc_val.get(), current[:11], current[11:19]))
            edit_win.destroy()
        else:
            msg.showwarning("Already Exists", "Note with this name already exists!")

    Label(edit_win, text="Name", font="None 17").place(x=100, y=50)
    Label(edit_win, text="Description", font="None 17").place(x=100, y=100)
    Label(edit_win, text="Note", font="None 17").place(x=100, y=200)

    name_val = StringVar()
    desc_val = StringVar()
    Entry(edit_win, textvariable=name_val, font="None 17", width=15).place(x=250, y=50)
    Entry(edit_win, textvariable=desc_val, font="None 17", width=25).place(x=250, y=100)
    tex = Text(edit_win, font="None 12", width=55, height=20)
    tex.place(x=250, y=200)

    Button(edit_win, text="Done", font="None 17", command=done).place(x=800, y=200)
    items = tree.item(tree.selection())["values"]
    name_val.set(items[1])
    desc_val.set(items[2])
    with open(f"{items[1]}.txt") as file:
        file.readline()
        note = file.read()
        tex.insert("0.0", note)

    edit_win.mainloop()


tree = ttk.Treeview(main_win, columns=(1, 2, 3, 4, 5), show="headings", height=600)
tree.column(1, width=50)
tree.column(2, width=150)
tree.column(3, width=200)
tree.column(4, width=150)
tree.column(5, width=150)
tree.heading(1, text="S.No.")
tree.heading(2, text="Name")
tree.heading(3, text="Description")
tree.heading(4, text="Date of Creation")
tree.heading(5, text="Time of Creation")
tree.pack()

new_but = Button(main_win, text="Add", command=add, font="None 17").place(x=350, y=550)
edit_but = Button(main_win, text="Edit", font="None 17", command=edit).place(x=450, y=550)
del_but = Button(main_win, text="Delete", font="None 17", command=lambda: delete("a")).place(x=550, y=550)

files = os.listdir(os.getcwd())
for i in files:
    if ".txt" in i:
        name = i[:-4]
        with open(i) as file:
            date_time = file.readline()
            date = date_time[12:22]
            timen = date_time[23:31]
            desc = file.readline()
            file.close()
        tree.insert("", END, values=(1, name, desc, date, timen))

tree.bind("<Delete>", delete)
print(files)
main_win.mainloop()
