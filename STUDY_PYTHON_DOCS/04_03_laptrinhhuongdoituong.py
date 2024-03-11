#khai báo lớp HCN
class HCN:
#khai báo thuộc tính chiều dài
    chieu_dai = 0
#khai báo thuộc tính chiều rộng
    chieu_rong = 0
#khai báo phương thức tính diện tích
    def tinh_dien_tich(self):
#Lấy thuộc tính chiều dài * thuộc tính chiều rộng
    
#Trả về kết quả diện tích
        return self.chieu_dai * self.chieu_rong

#Khai báo phương thưc tính chu vi
    def tinh_chu_vi(self):

#Trả về kết quả tính chu vi
        return 2 * (self.chieu_dai + self.chieu_rong)
