import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
  
name_var = tk.StringVar()
street_var = tk.StringVar()
town_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
author_var = tk.StringVar()

font=("calibre",10, "bold")
 
def submit():
    name = name_var.get()
    phone = phone_var.get()
     
    print(f"{name} {phone}")

def clear():
    name_var.set("")
    street_var.set("")
    town_var.set("")
    phone_var.set("")
    email_var.set("")
    author_var.set("")


name_label = tk.Label(root, text = "Homeowner(s)' Name")
name_entry = tk.Entry(root, textvariable = name_var)

street_label = tk.Label(root, text = "Homeowner(s)' Street")
street_entry = tk.Entry(root, textvariable = street_var)

town_label = tk.Label(root, text = "Homeowner(s)' Town")
town_entry = tk.Entry(root, textvariable = town_var)

phone_label = tk.Label(root, text = "Homeowner(s)' Phone")
phone_entry = tk.Entry(root, textvariable = phone_var)

email_label = tk.Label(root, text = "Homeowner(s)' Email")
email_entry = tk.Entry(root, textvariable = email_var)

clr_btn = tk.Button(root,text = "Clear", command = clear)
sub_btn = tk.Button(root,text = "Submit", command = submit)
  
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)

street_label.grid(row=1,column=0)
street_entry.grid(row=1,column=1)

town_label.grid(row=2,column=0)
town_entry.grid(row=2,column=1)

phone_label.grid(row=3,column=0)
phone_entry.grid(row=3,column=1)

email_label.grid(row=4,column=0)
email_entry.grid(row=4,column=1)

clr_btn.grid(row=5,column=1)
sub_btn.grid(row=5,column=1)
  
root.mainloop()