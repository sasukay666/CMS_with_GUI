from CMS_pkg import *
import tkinter

root = tkinter.Tk()
root.title("Customer Management System")
frm_login = Login_Form.Login_form(master=root)
frm_login.grid(row=0, column=0)

root.mainloop()