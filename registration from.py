
from tkinter import *

root = Tk()
root.geometry("500x300")

def getvals():
    print("Your form has been submitted !!")


Label(root, text="Registration From", font="times 15 bold").grid(row=0, column=3)

Name = Label(root, text="Name")
Name.grid(row=1, column=2)
Phone = Label(root, text="Phone")
Phone.grid(row=2, column=2)
Email = Label(root, text="Email")
Email.grid(row=3, column=2)
Gender = Label(root, text="Gender")
Gender.grid(row=4, column=2)
country = Label(root, text="Country")
country.grid(row=5, column=2)
Payment = Label(root, text="Payment_mode")
Payment.grid(row=6, column=2)

Name_value = StringVar()
phone_value = StringVar()
email_value = StringVar()
gender_value = StringVar()
country_value = StringVar()
Payment_value = StringVar()

checkvalue = IntVar()
Name_entry = Entry(root, textvariable=Name_value)
Name_entry.grid(row=1, column=3)
Phone_entry = Entry(root, textvariable=phone_value)
Phone_entry.grid(row=2, column=3)
Email_entry = Entry(root, textvariable=email_value)
Email_entry.grid(row=3, column=3)
Gender_entry = Entry(root, textvariable=gender_value)
Gender_entry.grid(row=4, column=3)
country_entry = Entry(root, textvariable=country_value)
country_entry.grid(row=5, column=3)
Payment_entry = Entry(root, textvariable=Payment_value)
Payment_entry.grid(row=6, column=3)


Check_btn = Checkbutton(root, text="Remember me?", variable=checkvalue)
Check_btn.grid(row=7, column=3)

Button(text = "submit", command=getvals).grid(row=8, column=3)

root.mainloop()



