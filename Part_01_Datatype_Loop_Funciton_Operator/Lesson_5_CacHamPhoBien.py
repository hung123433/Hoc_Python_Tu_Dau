'''
  Bài 5: Các hàm phổ biến trong python
    - Để sử dụng các hàm toán học trong python, cần import thư viện math.
      +) import math: import toàn bộ thư viện math
      +) from math import *: import toàn bộ thư viện math
  1. Các hàm toán học phổ biến trong python
    - sqrt(x): trả về căn bậc hai của x => Trả về kiểu số thực (float).
    - isqrt(x): Tính căn bậc 2 của x và trả về kết quả là số nguyên (int).
    - pow(x,y): Hàm luỹ thừa x^y, trả về kiểu số thực.
    - ceil: Hàm làm tròn số nguyên gần nhất => Lấy phần nguyên.
    - floor: Hàm làm tròn xuống.
    - factorial(x): Hàm giải thừa số => x!
    - fabs(x): Tính trị tuyệt đối của x => trả về số thực
    - abs(x): Trị tuyệt đối của x => Trả về số nguyên (Hàm có sẵn không cần dùng thư viện)
    - round(n): Hàm làm tròn n (có sẵn trong hệ thống).
    - max(): Trả về giá trị lớn nhất giữa nhiều só (có sẵn trong hệ thống).
    - min(): Trả về giá trị nhỏ nhất giữa nhiều số (có sẵn trong hệ thống).
    - sum(): Tính tổng các số (có sẵn trong hệ thống).
'''

#Import toàn bộ thư viện math
import math
#from math import *

#Các hàm toán học phổ biến trong python
#Hàm tính căn bậc hai
x = 25
print('Căn bậc hai của 25 là:', math.sqrt(x))
print('Kiểu dữ liệu:', type(math.sqrt(x)))
print('-------------------------------')

#Hàm tính căn bậc 2 trả về là số nguyên
print('Căn bậc 2 của 25 là:', math.isqrt(x))
print('Kiểu dữ liệu:', type(math.isqrt(x)))
print('--------------------------------')

#Hàm luỹ thừa
print('2 mũ 3:', math.pow(2,3),type(math.pow(2,3)))
print('2 mũ 3:', 2**3)
print('--------------------------------')

#Hàm làm tròn số nguyên gần nhất
print('Số nguyên gần nhất của 2.4 là:', math.ceil(2.4));
print('Số nguyên gần nhất của 3.7 là:', math.ceil(3.7));
print('---------------------------------')

#Hàm làm tròn xuống
print('Số nguyên gần nhất của 2.4 là:', math.floor(2.4));
print('Số nguyên gần nhất của 3.7 là:', math.floor(3.7));
print('---------------------------------')

#Hàm giải thừa số
print('Thừa số của 3! là:', math.factorial(3));
print('---------------------------------')

#Hàm trị tuyệt đối
print('Trị tuyệt đối của -20 là:', math.fabs(-20), 'Kiểu dữ liệu:', type(math.fabs(-20)));
print('Trị tuyệt đối của -20 là:', abs(-20), 'Kiểu dữ liệu:', type(abs(-20)));
print('---------------------------------')

#Hàm làm tròn
print('Giá trị của 2.5 khi làm tròn:',round(2.5),'Kiểu dữ liệu:',type(round(2.5)))
print('Giá trị của 3.7 khi làm tròn:', round(3.7),'Kiểu dữ liệu:',type(round(3.7)))
print('---------------------------------')

#Hàm tìm giá trị lớn nhất, nhỏ nhất, tính tổng nhiều số
print('Giá trị lớn nhất:', max(1, 4, 6, 7, 3))
print('Giá trị nhỏ nhất:', min(1,4,7,3))
print('Tổng các số:', sum([1,4,7,3]))