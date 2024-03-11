#khai báo module tkinter
from tkinter import*
from tkinter import ttk

#Tạo cửa sổ chính cho giao diện
root = Tk()

#Thiết lập độ rộng cho giao diện
root.geometry('400x250')
root.configure(bg='gray')
#Đặt điều kiện cho cửa sổ chính
root.title('pack')

#Bố cục
Button (root, text = "Red", fg = "red").pack(side = LEFT)
Button (root, text = "Black", fg = "black").pack(side = RIGHT)
Button (root, text = "Blue", fg = "blue").pack(side = TOP)
Button (root, text = "Green", fg = "green").pack(side = BOTTOM)

#=====Kết thúc phần thân chương trình

#Đưa cửa sổ chính giao diện hiển thị ra màn hình
root.mainloop()