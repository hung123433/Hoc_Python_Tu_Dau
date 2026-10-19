
'''
  Bài 4: Nhập dữ liệu trong python bằng map function và input function
  1. Hàm input()
   - Hàm input() được sử dụng để nhận dữ liệu từ người dùng.
   - Cú pháp: input("Nhập dữ liệu: ")
   - Chú ý: Hàm input() luôn trả về dữ liệu kiểu string, nếu muốn nhận dữ liệu kiểu khác thì cần ép kiểu dữ liệu.
   - Nhập dữ liệu với hàm input nhiều giá trị trên cùng một dòng:
    +) Bước 1:Nhập các dòng bằng ham input()
    +) Bước 2: Tách các dòng thành các giá trị riêng biệt bằng phương thức split(), cắt chuỗi lưu dưới dạng string.
    +) Bước 3: Ép kiểu dữ liệu cho các giá trị bằng hàm map() và ép kiểu dữ liệu.

'''

#hàm input()
'''
  name = input("Nhập tên của bạn: ")
  print("Tên của bạn là:", name)
  print(type(name))
  age = int(input("Nhập tuổi của bạn: "))
  print("Tuổi của bạn là:", age)
  print(type(age))
  print('------------------------------')
'''

#Nhập dữ liệu trên cùng một dòng
#Bước 1: Nhập các dòng bằng hàm input()
years = input('Nhập 3 năm bất kì: ')
#Bước 2: Tách chuỗi
year = years.split()
print('Các năm bạn vừa nhập là:', year)
print('Kiểu dữ liệu của year là:', type(year))
#Bước 3: Ép kiểu dữ liệu cho các giá trị bằng hàm map() và ép kiểu dữ liệu.
a, b, c = map(int, year)
print('Các năm bạn vừa nhập là:', a, b, c);
print('Kiểu dữ liệu của a, b, c là:', type(a), type(b), type(c))
print('------------------------------')

#Cách viết gộp trên cùng một dòng
x,y,z = map(int, input('Nhập 3 số bất kì: ').split())
print('Các số bạn vừa nhập là:', x, y, z)
print('Tổng 3 số bạn vừa nhập là: ',x+y+z)