#khai báo module tkinter
from tkinter import*
from tkinter import ttk

#Tạo cửa sổ chính cho giao diện
root = Tk()

#Thiết lập độ rộng cho giao diện
root.geometry('400x250')
root.configure(bg='gray')
#Đặt điều kiện cho cửa sổ chính
root.title('Bố cục băng Place')

#Bố cục
Label(root, text='Name').place(x = 30, y = 50)
Label(root, text = 'Email').place(x = 30, y = 90)
Label(root, text = 'Password').place(x = 30, y = 130)

Entry(root).place(x = 80, y = 50)
Entry(root).place(x = 80, y = 90)
Entry(root).place(x = 95, y = 130)


#=====Kết thúc phần thân chương trình

#Đưa cửa sổ chính giao diện hiển thị ra màn hình
root.mainloop()