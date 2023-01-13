from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Treeview
import pickle

main = Tk()
main.geometry("1500x800")

def add_exp():
    exp = {
        "date": date_entry.get(),
        "desc": desc_entry.get(),
        "amount": amount_entry.get(),
        "rec": rec_entry.get(),
        "paid": paid_entry.get()
    }
    tree.insert('', END, values=(
        exp["date"],exp["desc"],exp["amount"],exp["rec"],exp["paid"]
    ))

def delete_exp():
    tree.delete(tree.focus())


left_column = Frame(main, bg='#aa3f3f')
right_column = Frame(main,bg='')
left_column_f1 = Frame(left_column, bg='#aa3f3f')
left_column_f2 = Frame(left_column, bg='#aa3f3f')
left_column_f3 = Frame(left_column, bg='#aa3f3f')
left_column_f4 = Frame(left_column, bg='#aa3f3f')
left_column_f5 = Frame(left_column, bg='#aa3f3f')
left_column_f6 = Frame(left_column, bg='#aa3f3f')
right_column_f1 = Frame(right_column, height=60,bg='#7d3d3d')
right_column_f2 = Frame(right_column,bg='red')
################### LABELS
title_label = Label(left_column_f1, text="EXPENSES TRACKER", bg="#683b3b", fg='white',height=2,font='Helvetica 20 bold')
date_label = Label(left_column_f2, text="Date MM-DD-YYYY: ", height=5,bg='#aa3f3f', font='Helvetica 12 bold', fg='white')
desc_label = Label(left_column_f3, text="Description", height=5,bg='#aa3f3f', font='Helvetica 12 bold', fg='white')
amount_label = Label(left_column_f4, text="Amount:", height=5,bg='#aa3f3f', font='Helvetica 12 bold', fg='white')
rec_label = Label(left_column_f5, text="Receiver:", height=5,bg='#aa3f3f', font='Helvetica 12 bold', fg='white')
paid_label = Label(left_column_f6, text="Mode of payment:", height=5,bg='#aa3f3f', font='Helvetica 12 bold', fg='white')
exp_amount = Label(right_column_f1, text="All expenses: 0", width=20,height=2, fg='white', bg='#aa3f3f', font='Helvetica 12 bold').place(x=780, y=10)
################### ENTRIES
date_entry = Entry(left_column_f2)
desc_entry = Entry(left_column_f3)
amount_entry = Entry(left_column_f4)
rec_entry = Entry(left_column_f5)
paid_entry = Entry(left_column_f6)
################### BUTTONS
add_btn = Button(left_column, text="Add expense",width=25,height=2, font='Helvetica 15 bold', bg='brown', fg='white', bd=3, command=add_exp)
delete_btn = Button(right_column_f1, text="Delete Expense", width=14, height=2, font='Helvetica 12 bold', fg="white", bg='brown', command=delete_exp).place(x=10, y=6)
delete_all_exp = Button(right_column_f1, text="Delete All Expenses", width=14, height=2, font='Helvetica 12 bold', fg="white", bg='brown').place(x=200, y=6)
save_exp_as = Button(right_column_f1, text="Save to file", width=14, height=2,font='Helvetica 12 bold', fg="white", bg='brown').place(x=390, y=6)
load_file = Button(right_column_f1, text="Load file", width=14, height=2,font='Helvetica 12 bold', fg="white", bg='brown').place(x=575,y=6)
################# TREE
tree = Treeview(right_column_f2,selectmode=BROWSE ,columns=(1,2,3,4,5))
tree.column("#0", width=0, stretch='no')
tree.column(1, width=150)
tree.column(2, width=200)
tree.column(3, width=200)
tree.column(4, width=200)
tree.column(5, width=200)
tree.heading(1, text="Date")
tree.heading(2, text="Description")
tree.heading(3, text="Amount")
tree.heading(4, text="Receiver")
tree.heading(5, text="Mode of payment")
################# PACK ELEMENTS
left_column.pack(side=LEFT,fill=BOTH)
left_column_f1.pack(fill=X)
left_column_f2.pack(fill=X,padx=70)
left_column_f3.pack(fill=X, padx=70)
left_column_f4.pack(fill=X, padx=70)
left_column_f5.pack(fill=X, padx=70)
left_column_f6.pack(fill=X, padx=70)
right_column.pack(side=RIGHT, fill=BOTH,expand=True)
right_column_f1.pack(fill=X,anchor=N)
right_column_f2.pack(fill=BOTH,expand=True)
title_label.pack(fill=X)
date_label.pack(side=LEFT)
desc_label.pack(side=LEFT)
amount_label.pack(side=LEFT)
rec_label.pack(side=LEFT)
paid_label.pack(side=LEFT)
date_entry.pack(side=RIGHT)
desc_entry.pack(side=RIGHT)
amount_entry.pack(side=RIGHT)
rec_entry.pack(side=RIGHT)
paid_entry.pack(side=RIGHT)
add_btn.pack()
tree.pack(fill=BOTH, expand=True)

main.mainloop()