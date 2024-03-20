prod_db = {
1001: {"prod_name" : "laptop", "cat" : "office"},
1002: {"prod_name" : "screen", "cat" : "office"},      
1003: {"prod_name" : "Key board", "cat" : "office"},
1004: {"prod_name" : "mouse", "cat" : "office"}   
}

#Khái báo hàm lấy thông tin sản phẩm bằng id sản phẩm
def get_prod_info(prod_id):
        if prod_id in prod_db:
            return prod_db[prod_id]
        
#Khai báo hàm cập nhật thông tin sản phẩm
def add_prob_db(prod_db, prod_id):
    prod_db[prod_id] = {}
    prod_db[prod_id]["prod_name"] = prod_name
    prod_db[prod_id]["cat"] = cat

#In ra danh sách sản phẩm hiện tại
print('Real time products database:', prod_db)
#Khởi tạo vòng lặp
while True:
    #In ra màn hình các lựa chọn người dùng có thể thực hiện
    print('What do you want to do?: -\n'\
          '1. Add product \n'\
            '2. Update product database \n'\
                '3. Delete product in database \n'\
                    '4. Exit \n'\
                        '5. Other option')
    #Khai báo biến option, mang giá trị phương thức quản lý mà người dùng muốn thực hiện
    option = int(input('Select option 1 / 2 / 3 / 4 / 5:'))

    #Kiểm tra giá trị của biến option và thực hiện các hàm theo đúng giá trị đó
    if option == 1: #Thêm sản phẩm vào data
         prod_id = int(input('Enter Product Id please: '))
         if get_prod_info(prod_id):
              print(prod_id, "existed")
         else:
              prod_name = input("Enter product's name please: ")
              cat = input("Enter the category of product please: ")
              add_prob_db(prod_db,prod_id)
    elif option == 2: #Cập nhật sản phẩm vào data
         prod_id = int(input('Enter Product Id please: '))
         if get_prod_info(prod_id):
              prod_name = input("Enter product's name please: ")
              cat = input("Enter the category of product please: ")
              add_prob_db(prod_db,prod_id)
         else:
              print(prod_id, "does not exist")
    elif option == 3: #Xóa sản phẩm
         prod_id = int(input('Enter Product Id please: '))
         if get_prod_info(prod_id):
              del prod_db[prod_id]
              print('Delete successed')
         else:
              print(prod_id, "does not exist")
    elif option == 4:
         break
    else:
         print('Please follow instruction entering 1/2/3/4 for your choice')

#In ra danh sách sản phẩm sau khi quản lý
print(prod_db)
