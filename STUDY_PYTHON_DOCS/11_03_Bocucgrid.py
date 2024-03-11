#khai báo module tkinter
from tkinter import*
from tkinter import ttk

#Tạo cửa sổ chính cho giao diện
root = Tk()

#Thiết lập độ rộng cho giao diện
root.geometry('400x250')
root.configure(bg='gray')
#Đặt điều kiện cho cửa sổ chính
root.title('Bố cục băng Grid')

#Bố cục
Label(root, text='Tài khoản').grid(row = 5, column = 5)
Entry(root).grid(row = 5, column = 6)
Label(root, text = 'Mật khẩu').grid(row = 6, column= 5)
Entry(root).grid(row = 6, column = 6)
Button(root, text = 'Đăng nhập').grid(row = 7, column = 5)

#=====Kết thúc phần thân chương trình

#Đưa cửa sổ chính giao diện hiển thị ra màn hình
root.mainloop()