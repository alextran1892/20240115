#khai báo module tkinter
from tkinter import*
from tkinter import ttk

#Tạo cửa sổ chính cho giao diện
root = Tk()

#Thiết lập độ rộng cho giao diện
root.geometry('400x250')
root.configure(bg='silver')
#Đặt điều kiện cho cửa sổ chính
root.title('Widget Caculator')

#Tạo ô input
nhapso = Entry(root,width=50)
nhapso.grid(row=0, columnspan=4,pady=10, padx=50)

#Tạo các phím bấm
# Button(root,width=4, height=2,text='1').grid(row=1,column=0)
# Button(root,width=4, height=2,text='2').grid(row=1,column=1)
# Button(root,width=4, height=2,text='3').grid(row=1,column=2)
# Button(root,width=4, height=2,text='+').grid(row=1,column=3)

# Button(root,width=4, height=2,text='4').grid(row=2,column=0)
# Button(root,width=4, height=2,text='5').grid(row=2,column=1)
# Button(root,width=4, height=2,text='6').grid(row=2,column=2)
# Button(root,width=4, height=2,text='-').grid(row=2,column=3)

# Button(root,width=4, height=2,text='7').grid(row=3,column=0)
# Button(root,width=4, height=2,text='8').grid(row=3,column=1)
# Button(root,width=4, height=2,text='9').grid(row=3,column=2)
# Button(root,width=4, height=2,text='*').grid(row=3,column=3)

# Button(root,width=4, height=2,text='0').grid(row=4,column=0)
# Button(root,width=4, height=2,text='Clear').grid(row=4,column=1)
# Button(root,width=4, height=2,text='=').grid(row=4,column=2)
# Button(root,width=4, height=2,text='/').grid(row=4,column=3)

# Button(root,width=4, height=2,text='.').grid(row=5,column=0)

#Hàm xử lý khi nhấn vào các phím 0,1,2,3,4,5,6,7,8,9,+,-,*,/,dấu chấm
def onPress(number):
    # print(number)
    #Thêm dữ liệu vào vị trí sau cùng trong ô input
    nhapso.insert('end',number)

#Hàm xử lý khi nhấn phím =
def onEqual():
    # print('Xử lý')
    # Lấy giá trị trong ô input
    value = nhapso.get()
    # Xử lý biểu thức bằng hàm eval có sẵn trong Python. Hàm lấy toàn bộ biểu thức ->thực hiện tính toán -> Cho ra kết quả
    result = eval(value)
    # Xóa dữ liệu nhập vào và hiển thị nội dung kết quả
    nhapso.delete(0,'end')
    nhapso.insert('end',result)
    

#Hàm xử lý khi nhấn phím Clear
def onClear():
    # print('Xử lý')
    #Xóa toàn bộ ô input
    nhapso.delete(0,'end')
#Cập nhật lại sự kiện cho các phím 0,1,2,3,4,5,6,7,8,9,+,-,*,/,dấu chấm
Button(root,width=4, height=2, text='1',command=lambda:onPress('1')).grid(row=1,column=0,pady=2)
Button(root,width=4, height=2, text='2',command=lambda:onPress('2')).grid(row=1,column=1,pady=2)
Button(root,width=4, height=2, text='3',command=lambda:onPress('3')).grid(row=1,column=2,pady=2)
Button(root,width=4, height=2, text='+',command=lambda:onPress('+')).grid(row=1,column=3,pady=2)

Button(root,width=4, height=2, text='4',command=lambda:onPress('4')).grid(row=2,column=0,pady=2)
Button(root,width=4, height=2, text='5',command=lambda:onPress('5')).grid(row=2,column=1,pady=2)
Button(root,width=4, height=2, text='6',command=lambda:onPress('6')).grid(row=2,column=2,pady=2)
Button(root,width=4, height=2, text='-',command=lambda:onPress('-')).grid(row=2,column=3,pady=2)

Button(root,width=4, height=2, text='7',command=lambda:onPress('7')).grid(row=3,column=0,pady=2)
Button(root,width=4, height=2, text='8',command=lambda:onPress('8')).grid(row=3,column=1,pady=2)
Button(root,width=4, height=2, text='9',command=lambda:onPress('9')).grid(row=3,column=2,pady=2)
Button(root,width=4, height=2, text='*',command=lambda:onPress('*')).grid(row=3,column=3,pady=2)

Button(root,width=4, height=2, text='0',command=lambda:onPress('0')).grid(row=4,column=0,pady=2)
Button(root,width=4, height=2, text='/',command=lambda:onPress('/')).grid(row=4,column=3,pady=2)
Button(root,width=4, height=2, text='.',command=lambda:onPress('.')).grid(row=5,column=0)
#Cập nhật lại sự kiện cho phím =
Button(root, width=4, height=2, text="Clear", command=onClear).grid(row=4, column=1,pady=2)

#Cập nhật lại sự kiện cho phím Clear
Button(root, width=4, height=2, text="=", command=onEqual).grid(row=4, column=2,pady=2)
root.mainloop()