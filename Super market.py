from tkinter import * 
from tkinter import messagebox
from datetime import datetime

win=Tk()
win.geometry("700x700")
win.title("billing system")

Menus={
 "Apple":50,
 "Banana":90,
 "Cherry":100
 
}
TAX_RATE = 0.07

entries_dict = {}

def calculate():
    total = 0
    print_text.delete("1.0", END)

   
    print_text.insert(END, "========== ABC Supermarket ==========\n\n")
    print_text.insert(END, datetime.now().strftime("%Y-%m-%d %H:%M") + "\n")
    print_text.insert(END, f"{'Item':<15}{'Qty':<10}{'Price':<10}{'Total':<10}\n")
    print_text.insert(END, "-" * 50 + "\n")

    
    for item, price in Menus.items():
        try:
            qty = int(entries_dict[item].get())
        except ValueError:
            qty = 0

        if qty > 0:
            line_total = price * qty
            total += line_total
            print_text.insert(END, f"{item:<15}{qty:<10}{price:<10}{line_total:<10}\n")

    if total == 0:
        messagebox.showinfo("Info", "Please enter at least one quantity")
        return

    tax = total * TAX_RATE
    grand_total = total + tax
    
    
    print_text.insert(END, "-" * 50 + "\n")
    print_text.insert(END, f"Subtotal:      {total:.2f}\n")
    print_text.insert(END, f"Tax (7%):      {tax:.2f}\n")
    print_text.insert(END, f"Total:         {grand_total:.2f}\n")
    print_text.insert(END, "=" * 50 + "\n")
    

def clear():

    for entry in entries_dict.values():
        entry.delete(0,END)
    print_text.delete("1.0",END)




header_label=Label(win,text="ABC supermarket",font="Coolvetica 20",fg="orange")
header_label.pack()

items=Label(win,text="items",font="Arial 15",fg="blue")
items.place(x=100,y=50)

items=Label(win,text="price",font="Arial 15",fg="blue")
items.place(x=300,y=50)

items=Label(win,text="Quantity",font="Arial 15",fg="blue")
items.place(x=490,y=50)

print_text=Text(win,width=81,height=20)
print_text.place(x=30,y=360)

total_button=Button(win,text="Total",font="arial 15",command=calculate)
total_button.place(x=100,y=300)

clear_button=Button(win,text="Clear",font="arial 15",command=clear)
clear_button.place(x=300,y=300)

exit_button=Button(win,text="Exit",font="Arial 15",command=win.destroy)
exit_button.place(x=500,y=300)
y_pos=100
for items,price in Menus.items():
    items_label=Label(win,text=f"{items}",font="arial 15")
    items_label.place(x=100,y=y_pos)
    price_label=Label(win,text=f"{price}",font="Arial 15")
    price_label.place(x=300,y=y_pos)

    entries=Entry(win,width=10,)
    entries.place(x=500,y=y_pos)
    entries_dict[items]=entries

    y_pos+=50


            




win.mainloop()