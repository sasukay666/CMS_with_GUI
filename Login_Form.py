import tkinter.messagebox
from CMS_pkg import *

class Login_form(tkinter.Frame):
    mstcpy = ''
    def __init__(self, master=None):
        super().__init__(master=master)
        Login_form.mstcpy = master
        self.create_widget()

    def create_widget(self):
        self.user_name = tkinter.Label(master=self, text='UserName: ', width=10)
        self.user_name.grid(row=0,column=0)
        self.password = tkinter.Label(master=self, text='Password: ', width=10)
        self.password.grid(row=1,column=0)

        self.var_user_name = tkinter.StringVar()
        self.txt_user_name = tkinter.Entry(master=self, textvariable=self.var_user_name)
        self.txt_user_name.grid(row=0,column=1)

        self.var_password = tkinter.StringVar()
        self.txt_password = tkinter.Entry(master=self, show='*', textvariable=self.var_password)
        self.txt_password.grid(row=1, column=1)

        self.btn_login = tkinter.Button(master=self, text='Login', command=self.btn_login_click)
        self.btn_login.grid(row=2, column=1)

    def btn_login_click(self):
        '''from GUI takes username and password and
        then logs in with those credetials.
        Then, if the connection with the db is successful,
        it draws the frame of CMS if the user'''
        try:
            user = self.var_user_name.get()
            password = self.var_password.get()
            host = 'localhost'
            CMS_ops.Customer.login(host, user, password)

            cms_gui = CMS_GUI.Customer_form(master=Login_form.mstcpy)
            cms_gui.grid(row=0, column=0)

        except Exception:
            tkinter.messagebox.showerror("ERROR", "Wrong Input. Please try again!!")

if __name__ == '__main__':
    global root
    root = tkinter.Tk()
    root.title("Customer Management System")
    frm_login = Login_form(master=root)
    frm_login.grid(row=0, column=0)
    root.mainloop()