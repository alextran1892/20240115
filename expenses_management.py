expenses = [{'item_name': 'cafe', 'cost': 29000, 'date': '17/03/2024'},{'item_name': 'clothes', 'cost': 219000, 'date': '15/03/2024'}]
print('Tổng số khoản chi:', len(expenses))

#Khởi tạo hàm thêm mục chi tiêu gồm 2 tham số:mảng chi tiêu hiện tại + mục chi tiêu mới
def add_item(myTemplist, item):
    myTemplist.append(item)
    print('Tổng số khoản chi sau khi cập nhật:', len(expenses))

#Khởi tạo hàm tìm index của phần tử trong mảng
def find_index_item(myTemplist, item_name):
    result = -1
    length = len(myTemplist)
    for i in range(length):
        if myTemplist[i]['item_name'] == item_name:
            result = i
        return result

#Khởi tạo hàm xóa phần tử khỏi mảng chi tiêu
def remove_item(myTemplist, item_name):
    if find_index_item(myTemplist, item_name) > -1:
        del myTemplist[find_index_item(myTemplist, item_name)]
    else:
        print(item_name + ' ' + 'is not in list')

#In mảng chi tiêu hiện tại + lấy thông tin yêu cầu của người dùng
print('Your expenses: ', expenses)
#In ra các phương thức người dùng có thể chọn
print('What do you want to do? -\n'\
      '1. Add\n'\
      '2. Remove')

#Lấy yêu cầu từ người dùng -> chuyển về kiểu int -> gán giá trị cho biến option
option = int(input('Select option 1 or 2:'))



##Kiểm tra yêu cầu của người dùng và gọi hàm tương ứng
if option == 1:
    #Lấy tên khoản chi từ người dùng -> gán giá trị cho biến name_input
    name_input = input('Item name: ')
    cost_input = int(input('Item cost: '))
    date_input = input('Date: ')
    item = {'item_name':name_input, 'cost':cost_input, 'date':date_input}
    add_item(expenses, item)
    print('Your expenses: ', expenses)
elif option == 2:
    #Lấy tên khoản chi từ người dùng -> gán giá trị cho biến name_input
    name_input = input('Item name: ')
    remove_item(expenses, name_input)
    print('Your expenses: ', expenses)
else:
    print('Invalid input')
