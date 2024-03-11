from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x250")
root.configure(bg='gray')
root.title("Chương trình máy tính")
#Khai báo hàm xử lý
def addNumbers():
    num1 =int(so_thu_nhat.get())
    num2 =int(so_thu_hai.get())
    result = num1 + num2
    ket_qua.config(text='Kết quả:' + str(result))

#======= BẮT ĐẦU PHẦN THÂN CHƯƠNG TRÌNH
Label(root, text = "Số thứ nhất").grid(row = 0, column = 0)
#Cập nhật ô input 1
so_thu_nhat = Entry(root)
so_thu_nhat.grid(row = 0, column = 1)

Label(root, text = "Số thứ hai").grid(row = 1, column = 0)
#Cập nhật ô input 2
so_thu_hai = Entry(root)
so_thu_hai.grid(row = 1, column = 1)

Button(root, text = "Tính", command=addNumbers).grid(row = 2, column = 0)
#Cập nhật lại label kết quả
ket_qua = Label(root,text="Kết quả")
ket_qua.grid(row = 2, column = 1)
#======= BẮT ĐẦU PHẦN THÂN CHƯƠNG TRÌNH

root.mainloop()