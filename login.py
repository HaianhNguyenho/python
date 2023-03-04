from tkinter import *
from tkinter import ttk

from tkinter import messagebox

import pandas as pd

def formsp():
    win = Toplevel()
    win.geometry("600x400")
    win.title("Profilecellphone")

    def show():
        ds.delete(0, END)
        df = pd.read_csv('profilecell.csv')
        for i in range(len(df)):
            ds.insert(END, str(df.iloc[i]))

    def dienvo():
        comb = nhap1.get()
        ma = nhap2.get()
        ten = nhap3.get()
        sol = chon.get()
        dong = chon1.get()
        ds.insert(END, f"{comb} {ma} {ten} {sol} {dong}")

    label1 = Label(win, text="Thông tin điện thoại")
    label1.place(x=5, y=5)

    label2 = Label(win, text="Danh sách điện thoại")
    label2.place(x=300, y=5)

    label3 = Label(win, text="Hãng điện thoại")
    slecect = StringVar()
    nhap1 = ttk.Combobox(win, textvariable=slecect, width=10)
    nhap1['values'] = ["Oppo", "Samsung", "Iphone", "Readmi", "Xiaomi", "Nokia", "Lumia"]
    nhap1["state"] = "readonly"
    label3.place(x=5, y=30)
    nhap1.place(x=100, y=30)

    ds = Listbox(win, width=50, height=20)
    ds.place(x=300, y=40)

    label4 = Label(win, text="Mã điện thoại")
    label4.place(x=5, y=60)
    nhap2 = Entry(win, width=10)
    nhap2.place(x=100, y=70)

    label5 = Label(win, text="Tên điện thoại")
    label5.place(x=5, y=100)
    nhap3 = Entry(win, width=10)
    nhap3.place(x=100, y=100)

    label6 = Label(win, text="Màu sắc")
    label6.place(x=5, y=120)

    nut1 = Checkbutton(win, text="Trắng", onvalue=True, offvalue=False)
    nut1.place(x=60, y=130)
    nut2 = Checkbutton(win, text="Đen", onvalue=True, offvalue=False)
    nut2.place(x=120, y=130)

    label7 = Label(win, text="Số lượng")
    label7.place(x=5, y=160)
    chon = Entry(win, width=10)
    chon.place(x=100, y=160)

    label8 = Label(win, text="Đơn giá")
    label8.place(x=5, y=200)
    chon1 = Entry(win, width=10)
    chon1.place(x=100, y=200)

    btn1 = Button(win, text="Thêm", activebackground="green", command=dienvo)
    btn1.place(x=15, y=240)
    btn2 = Button(win, text="Xóa", activebackground="red")
    btn2.place(x=80, y=240)
    btn3 = Button(win, text="Sửa", activebackground="yellow")
    btn3.place(x=160, y=240)

    btn4 = Button(win, text="Cập nhật", activebackground="green", command=show)
    btn4.place(x=5, y=280)
    btn5 = Button(win, text="Hủy", activebackground="yellow")
    btn5.place(x=80, y=280)
    btn6 = Button(win, text="Thoát", activebackground="white", command=win.quit)
    btn6.place(x=160, y=280)


def save_password():
    current_password = current_password_entry.get()
    new_password = new_password_entry.get()
    confirm_password = confirm_password_entry.get()

    if current_password == '' or new_password == '' or confirm_password == '':
        message.set("Vui lòng điền đầy đủ thông tin")
    elif new_password != confirm_password:
        message.set("Mật khẩu mới và xác nhận mật khẩu không giống nhau")
    else:
        # Lưu mật khẩu mới vào cơ sở dữ liệu
        # Code xử lý lưu mật khẩu ở đây
        message.set("Mật khẩu đã được thay đổi thành công")

        # Xóa trống các trường nhập liệu
        current_password_entry.delete(0, END)
        new_password_entry.delete(0, END)
        confirm_password_entry.delete(0, END)

def change_password():
    # Tạo một cửa sổ mới để thay đổi mật khẩu
    password_screen = Toplevel()
    password_screen.title("Thay đổi mật khẩu")
    password_screen.geometry("350x200")

    global current_password_entry
    global new_password_entry
    global confirm_password_entry
    global message

    current_password_label = Label(password_screen, text="Mật khẩu hiện tại:")
    current_password_label.pack()
    current_password_entry = Entry(password_screen, show="*")
    current_password_entry.pack()

    new_password_label = Label(password_screen, text="Mật khẩu mới:")
    new_password_label.pack()
    new_password_entry = Entry(password_screen, show="*")
    new_password_entry.pack()

    confirm_password_label = Label(password_screen, text="Xác nhận mật khẩu mới:")
    confirm_password_label.pack()
    confirm_password_entry = Entry(password_screen, show="*")
    confirm_password_entry.pack()

    message = StringVar()
    message_label = Label(password_screen, text="", textvariable=message)
    message_label.pack()

    save_button = Button(password_screen, text="Lưu", command=save_password)
    save_button.pack()


def login():

    uname=username.get()
    pwd=password.get()

    if uname=='' or pwd=='':
        message.set("Điền vào ô trống!!!")
    else:
        if uname=="nhom5" and pwd=="123":
            # create a new window and destroy the login screen
            global main_screen
            main_screen = Tk()
            main_screen.title("Hệ thống quản lý cửa hàng bán điện thoại")
            main_screen.geometry("900x500")

            menubar = Menu(main_screen)


            filemenu = Menu(menubar, tearoff=0)
            filemenu.add_command(label="Thay đổi mật khẩu",command=change_password)
            filemenu.add_command(label="Đăng xuất", command=main_screen.quit)

            menubar.add_cascade(label="Tài khoản", menu=filemenu)

            filemenu1 = Menu(menubar, tearoff=0)
            menubar.add_cascade(label="Sản phẩm ", menu=filemenu1)
            filemenu1.add_command(label="Quản lý điện thoại", command=formsp)

            filemenu2 = Menu(menubar, tearoff=0)
            menubar.add_cascade(label="Khách hàng ", menu=filemenu2)
            filemenu2.add_command(label="Quản lý khách hàng")

            filemenu3 = Menu(menubar, tearoff=0)
            menubar.add_cascade(label="Đơn hàng ", menu=filemenu3)
            filemenu3.add_command(label="Quản lý hóa đơn")

            filemenu4 = Menu (menubar, tearoff=0)
            menubar.add_cascade(label="Báo cáo")
            filemenu4.add_command(label="Thống kê")

            main_screen.config(menu=menubar)

            label1 = Label(main_screen, text='Xây dựng cửa hàng quản lý bán điện thoại', font=('Arial,', 18, 'bold'),
                           fg='blue')
            label1.pack()



            # thêm Label vào giao diện người dùng


        else:
            message.set("Sai tên đăng nhập và mật khẩu!!!")


def Loginform():
    global login_screen
    login_screen = Tk()

    login_screen.title("Đăng nhập hệ thống quản lý")
    # setting height and width of screen
    login_screen.geometry("350x200")

    global message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message = StringVar()

    Label(login_screen, width="300", text="Vui lòng nhập thông tin chi tiết bên dưới", bg="brown", fg="white").pack()

    Label(login_screen, text="Username * ").place(x=20, y=40)

    Entry(login_screen, textvariable=username).place(x=90, y=42)

    Label(login_screen, text="Password * ").place(x=20, y=80)

    Entry(login_screen, textvariable=password, show="*").place(x=90, y=82)

    Label(login_screen, text="", textvariable=message).place(x=95, y=100)

    Button(login_screen, text="Login", width=10, height=1, bg="blue", command=login).place(x=105, y=130)

    Button(login_screen, text="Exit", width=10, height=1, bg="red", command=login_screen.destroy).place(x=215, y=130)

    login_screen.mainloop()


Loginform()
