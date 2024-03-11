tu_dien = {
    'ten':'Trần Thị Ngọc Ánh',
    'tuoi': '32',
    'can nang':'50'
}
#gọi và in tên cách 1
print(tu_dien['ten'])
#gọi và in tên cách 2
print(tu_dien.get('ten'))
#thêm sở thích
tu_dien_2 = {'so thich':'piano'}
tu_dien.update(tu_dien_2)
#xóa sở thích
tu_dien.pop('so thich')
#thay đổi cân nặng
tu_dien['can nang']='49'
#xóa cân nặng
tu_dien.pop('can nang')
#xóa từ điển
tu_dien.clear()