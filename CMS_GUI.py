import tkinter
import tkinter.messagebox
from CMS_pkg import *

class Customer_form(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.create_widgets()

    def create_widgets(self):
        self.lbl_id = tkinter.Label(master=self, text="Customer ID", width=16)
        self.lbl_id.grid(row=0, column=0, columnspan=2)
        self.lbl_name = tkinter.Label(master=self, text="Name", width=16)
        self.lbl_name.grid(row=1, column=0, columnspan=2)
        self.lbl_address = tkinter.Label(master=self, text="Address", width=16)
        self.lbl_address.grid(row=2, column=0, columnspan=2)
        self.lbl_mobile_no = tkinter.Label(master=self, text="Mobile No", width=16)
        self.lbl_mobile_no.grid(row=3, column=0, columnspan=2)

        self.var_id = tkinter.IntVar()
        self.txt_id = tkinter.Entry(self, textvariable=self.var_id, width=16)
        self.txt_id.grid(row=0, column=2, columnspan=2)

        self.var_name = tkinter.StringVar()
        self.txt_name = tkinter.Entry(self, textvariable=self.var_name, width=16)
        self.txt_name.grid(row=1, column=2, columnspan=2)

        self.var_address = tkinter.StringVar()
        self.txt_address = tkinter.Entry(self, textvariable=self.var_address, width=16)
        self.txt_address.grid(row=2, column=2, columnspan=2)

        self.var_mobile = tkinter.StringVar()
        self.txt_mobile = tkinter.Entry(self, textvariable=self.var_mobile, width=16)
        self.txt_mobile.grid(row=3, column=2, columnspan=2)

        self.btn_add = tkinter.Button(master=self, text="Add Customer", width=16, command=self.btn_add_click)
        self.btn_add.grid(row=4, column=0)

        self.btn_delete = tkinter.Button(master=self, text="Delete Customer", width=16, command=self.btn_delete_click)
        self.btn_delete.grid(row=4, column=1)

        self.btn_viewall = tkinter.Button(master=self, text="Display All Customer", width=16, command=self.btn_viewall_click)
        self.btn_viewall.grid(row=4, column=2)

        self.lblframe_search = tkinter.LabelFrame(master=self, text="Search Customer")
        self.lblframe_search.grid(row=5, column=1)
        self.var_r1 = tkinter.StringVar()
        self.r1 = tkinter.Radiobutton(master=self.lblframe_search, text="ID", variable=self.var_r1, value='id')
        self.r1.grid(row=0, column=0)
        self.r2 = tkinter.Radiobutton(master=self.lblframe_search, text="Mobile", variable=self.var_r1, value='mobile')
        self.r2.grid(row=1, column=0)
        self.var_r1.set('id')
        self.btn_search = tkinter.Button(master=self.lblframe_search, text="OK", command=self.lblframe_search_click)
        self.btn_search.grid(row=2, column=1)

        self.lblframe_modify = tkinter.LabelFrame(master=self, text="Modify Customer")
        self.lblframe_modify.grid(row=5, column=0)
        self.var_r2 = tkinter.StringVar()
        self.r1 = tkinter.Radiobutton(master=self.lblframe_modify, text="Name", variable=self.var_r2, value='name')
        self.r1.grid(row=0, column=0)
        self.r2 = tkinter.Radiobutton(master=self.lblframe_modify, text="Address", variable=self.var_r2, value='address')
        self.r2.grid(row=1, column=0)
        self.r3 = tkinter.Radiobutton(master=self.lblframe_modify, text="Mobile", variable=self.var_r2, value='mobile')
        self.r3.grid(row=2, column=0)
        self.r4 = tkinter.Radiobutton(master=self.lblframe_modify, text="All Fields", variable=self.var_r2, value='all')
        self.r4.grid(row=3, column=0)
        self.var_r2.set('name')
        self.btn_modify = tkinter.Button(master=self.lblframe_modify, text="OK", command=self.lblframe_modify_click)
        self.btn_modify.grid(row=4, column=1)

        self.btn_clearAll = tkinter.Button(master=self, text="Clear All Fields", command=self.btn_clearAll_click)
        self.btn_clearAll.grid(row=5, column=2)

    def lblframe_search_click(self):
        ch1 = self.var_r1.get()
        if ch1 == 'id':
            try:
                obj = CMS_ops.Customer()
                obj.id = self.var_id.get()
                obj.searchCustomerByID()
                self.var_name.set(obj.name)
                self.var_address.set(obj.address)
                self.var_mobile.set(obj.mobile)
            except:
                tkinter.messagebox.showerror("CMS", "ID not found")

        elif ch1 == 'mobile':
            try:
                obj = CMS_ops.Customer()
                obj.mobile = self.var_mobile.get()
                obj.searchCustomerByMobile()
                self.var_name.set(obj.name)
                self.var_address.set(obj.address)
                self.var_id.set(obj.id)
            except:
                tkinter.messagebox.showerror("CMS", "Mobile Number not found")

    def lblframe_modify_click(self):
        ch2 = self.var_r2.get()

        if ch2 == 'all':
            try:
                if self.var_name.get() != '' and self.var_address.get() != '' and self.var_mobile.get() !='':
                    obj = CMS_ops.Customer()
                    obj.id = self.var_id.get()
                    obj.name = self.var_name.get()
                    obj.address = self.var_address.get()
                    obj.mobile = self.var_mobile.get()
                    obj.updateAll()
                    tkinter.messagebox.showinfo("CMS", "Customer's details updated successfully.")
                else:
                    raise Exception
            except:
                tkinter.messagebox.showerror("CMS", "ID not found.")

        elif ch2 == 'name':
            try:
                if self.var_name.get() != '':
                    obj = CMS_ops.Customer()
                    obj.id = self.var_id.get()
                    obj.name = self.var_name.get()
                    obj.updateCustomerName()
                    tkinter.messagebox.showinfo("CMS", "Customer's name updated successfully.")
                else:
                    raise Exception
            except:
                tkinter.messagebox.showerror("CMS", "ID not found.")

        elif ch2 == 'address':
            try:
                if self.var_address.get() != '':
                    obj = CMS_ops.Customer()
                    obj.id = self.var_id.get()
                    obj.address = self.var_address.get()
                    obj.updateCustomerAddress()
                    tkinter.messagebox.showinfo("CMS", "Customer's address updated successfully.")
                else:
                    raise Exception
            except:
                tkinter.messagebox.showerror("CMS", "ID not found.")

        if ch2 == 'mobile':
            try:
                if self.var_mobile.get() != '':
                    obj = CMS_ops.Customer()
                    obj.id = self.var_id.get()
                    obj.mobile = self.var_mobile.get()
                    obj.updateCustomerMobile()
                    tkinter.messagebox.showinfo("CMS", "Customer's mobile no. updated successfully.")
                else:
                    raise Exception("Please enter mobile no.")
            except Exception as ex:
                tkinter.messagebox.showerror("CMS", ex)

    def btn_delete_click(self):
        try:
            CMS_ops.Customer.deleteCustomer(self.var_id.get())
            tkinter.messagebox.showinfo("CMS", "Customer Deleted Successfully")
        except:
            tkinter.messagebox.showerror("CMS", "No matching ID found")

    def btn_add_click(self):
        if self.var_name.get() != '' and self.var_mobile.get() != '':
            obj = CMS_ops.Customer()
            obj.name = self.var_name.get()
            obj.address = self.var_address.get()
            obj.mobile = self.var_mobile.get()
            obj.addCustomer()
            tkinter.messagebox.showinfo("CMS", "Customer Added Successfully!!")
        else:
            tkinter.messagebox.showerror("CMS", "Name and mobile no. must be entered")

    def btn_viewall_click(self):
        try:
            CMS_ops.Customer.viewAll()

            stre=''
            for e in CMS_ops.Customer.Custlist:
                stre += f"{e.id} {e.name} \t\t {e.address} \t\t {e.mobile}\n"

            if str != '':
                root1 = tkinter.Tk()
                root1.title("Customer List")
                lbl_viewall = tkinter.Label(master=root1, text=stre)
                lbl_viewall.grid(row=0, column=0)
                root1.mainloop()
            else:
                raise Exception
        except:
            tkinter.messagebox.showerror("CMS", "No Records in CMS Database.")

    def btn_clearAll_click(self):
        self.var_id.set(0)
        self.var_name.set('')
        self.var_address.set('')
        self.var_mobile.set('')


if __name__ == '__main__':
    global root
    root = tkinter.Tk()
    root.title("Customer Management System")
    frm_login = Customer_form(master=root)
    frm_login.grid(row=0, column=0)
    root.mainloop()