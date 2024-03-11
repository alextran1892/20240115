#khai báo module tkinter
from tkinter import*
from tkinter import ttk

#Tạo cửa sổ chính cho giao diện
root = Tk()

#Thiết lập độ rộng cho giao diện
root.geometry('400x250')
root.configure(bg='gray')
#Đặt điều kiện cho cửa sổ chính
root.title('First_program')

#=====Bắt đầu phần thân chương trình

#Tọa text "Hello World!"
Label(root,text='Hello Viet Nam!').pack()
#Tao nút nhấn
ttk.Button(root,text='Cộng').pack()
#Sellect box
ttk.Combobox(root, values=['Mùa Xuân','Mùa Hạ','Mùa Thu','Mùa Đông']).pack()
#Check box
ttk.Checkbutton(root, text='Chọn').pack()
#Ô nhập dữ liệu
ttk.Entry(root).pack()
#Thanh kéo
ttk.Scale(root, from_=0, to=100,orient=HORIZONTAL).pack()

#Ô nhập số
ttk.Spinbox(root,from_=0, to=100).pack()
#Ô nhập nhiều text
Text(root).pack()





#=====Kết thúc phần thân chương trình

#Đưa cửa sổ chính giao diện hiển thị ra màn hình
root.mainloop()



