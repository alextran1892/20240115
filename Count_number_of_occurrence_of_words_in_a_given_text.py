
#Khai báo hàm đếm số lần xuất hiện của một từ trong một đoạn văn bản truyền vào
def occurrence_of_word(word):
    word = word.lower()
    count = 0
    for i in text_list:
        if word == i:
            count+=1
    return count


#Khai báo biến Message mang giá trị là văn bản cần đếm

message = input('Enter the text: ')
message2 = message.replace(",","")
message3 = message2.replace(".","")
message4 = message3.replace(":","")
message5 = message4.replace("?","")
message6 = message5.replace("!","")
message7 = message6.replace(";","")
message8 = message7.lower()

text_list = message8.split()
print(text_list)

#Gọi hàm đếm từ và truyền message làm tham số
print(occurrence_of_word(word="Từ"))

