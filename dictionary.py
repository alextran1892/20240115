Eng_Vn_dictionary = {
"hello":"Xin chào",
"good bye":"Tạm biệt",
"yellow":"màu vàng",
"blue":"màu xanh dương"
}

#Khai báo hàm tìm và in ra từ sau khi được dịch
def translate_eng_to_vn(input_word):
    for item in Eng_Vn_dictionary:
        if input_word == item:
            return Eng_Vn_dictionary[item]
        
        

#Khai báo biến input_word, mang giá trị là từ cần dịch mà người dùng nhập vào
input_word = input("Enter Eng word: ")

#Gọi hàm tìm từ cần dịch
translated_word = translate_eng_to_vn(input_word)

#In ra kết quả
if translated_word:
    print(translated_word)
else:
    print("This word is not available in this dictionary")
