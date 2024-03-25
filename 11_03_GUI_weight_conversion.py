from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x400")
root.configure(bg='gray')
root.title("Weight Convert")

#Hàm chuyển đổi trọng lượng
def convertKg():
    kg = float(kg_input.get())
    gram = round(kg *1000,2)
    result1.config(text=str(gram))
    pound = round(kg * 2.20462,2)
    result2.config(text=str(pound))
    ounce = round(kg * 35.274,2)
    result3.config(text=str(ounce))

kg_input = Entry(root, width=20)

Label(root, text="Enter the weight in Kg").grid(row=0, column=0)
kg_input.grid(row=0, column=1)
Button(root, text="Convert",command=convertKg).grid(row=0, column=2)

Label(root, text="Gram").grid(row=1,column=0)
Label(root, text="Pound").grid(row=1,column=1)
Label(root, text="Ounce").grid(row=1,column=2)

result1 = Label(root,width=10)
result1.grid(row=2,column=0,pady=10, padx=50)

result2 = Label(root,width=10)
result2.grid(row=2,column=1,pady=10, padx=50)

result3 = Label(root,width=10)
result3.grid(row=2,column=2,pady=10, padx=50)

root.mainloop()


