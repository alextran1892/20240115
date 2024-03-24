class student_list:
    global stud_db
    global stud_full_name
    global stud_date_of_birth
    global stud_birth_place
    global stud_major
    stud_db = {
    1001: {"stud_full_name" : "Trần Thị Ngọc Ánh", "stud_date_of_birth" : "01/08/1992", "stud_birth_place" : "Quảng Trị", "stud_major" : "Data Analyst"},
    1002: {"stud_full_name" : "Trần Thị Ngọc Ánh", "stud_date_of_birth" : "01/08/1992", "stud_birth_place" : "Quảng Trị", "stud_major" : "Data Analyst"},      
    1003: {"stud_full_name" : "Trần Thị Ngọc Ánh", "stud_date_of_birth" : "01/08/1992", "stud_birth_place" : "Quảng Trị", "stud_major" : "Data Analyst"},
    1004: {"stud_full_name" : "Trần Thị Ngọc Ánh", "stud_date_of_birth" : "01/08/1992", "stud_birth_place" : "Quảng Trị", "stud_major" : "Data Analyst"}
    }
    
    def stud_management(self):
            #Khái báo hàm lấy thông tin sản phẩm bằng id sinh viên
        def get_stud_info(stud_id):
                if stud_id in stud_db:
                    return stud_db[stud_id]
                
        #Khai báo hàm cập nhật thông tin sinh viên
        def add_stud_db(stud_db, stud_id):
            stud_db[stud_id] = {}
            stud_db[stud_id]["stud_full_name"] = stud_full_name
            stud_db[stud_id]["stud_date_of_birth"] = stud_date_of_birth
            stud_db[stud_id]["stud_birth_place"] = stud_birth_place
            stud_db[stud_id]["stud_major"] = stud_major

        #In ra danh sách sinh viên hiện tại
        print('Real time studucts database:', stud_db)
        #Khởi tạo vòng lặp
        while True:
            #In ra màn hình các lựa chọn người dùng có thể thực hiện
            print('What do you want to do?: -\n'\
                '1. Add studuct \n'\
                    '2. Update studuct database \n'\
                        '3. Delete studuct in database \n'\
                            '4. Exit \n'\
                                '5. Other option')
            #Khai báo biến option, mang giá trị phương thức quản lý mà người dùng muốn thực hiện
            option = int(input('Select option 1 / 2 / 3 / 4:'))

            #Kiểm tra giá trị của biến option và thực hiện các hàm theo đúng giá trị đó
            if option == 1: #Thêm sinh viên vào data
                stud_id = int(input('Enter studuct Id please: '))
                if get_stud_info(stud_id):
                    print(stud_id, "existed")
                else:
                    stud_full_name = input("Enter student's full name please: ")
                    stud_date_of_birth = input("Enter student's date of birth please: ")
                    stud_birth_place = input("Enter student's birth place please: ")
                    stud_major = input("Enter student's major please: ")
                    add_stud_db(stud_db,stud_id)
            elif option == 2: #Cập nhật sinh viên vào data
                stud_id = int(input('Enter studuct Id please: '))
                if get_stud_info(stud_id):
                    stud_full_name = input("Enter student's full name please: ")
                    stud_date_of_birth = input("Enter student's date of birth please: ")
                    stud_birth_place = input("Enter student's birth place please: ")
                    stud_major = input("Enter student's major please: ")
                    add_stud_db(stud_db,stud_id)
                else:
                    print(stud_id, "does not exist")
            elif option == 3: #Xóa sinh viên
                stud_id = int(input('Enter studuct Id please: '))
                if get_stud_info(stud_id):
                    del stud_db[stud_id]
                    print('Delete successed')
                else:
                    print(stud_id, "does not exist")
            elif option == 4:
                break
            else:
                print('Please follow instruction entering 1/2/3/4 for your choice')

        #In ra danh sách sinh viên sau khi quản lý
        print(stud_db)

c = student_list()
c.stud_management()