'''
  Bài 2: Biến và kiểu dữ liệu trong Python
  1. Biến
    - Biến trong python là một tên đại diện cho một giá trị. Biến được sử dụng để lưu trữ dữ liệu trong bộ nhớ.
    - Muốn biết kiểu dữ liệu của biến dùng: type(ten_bien).
    - Trong python không cần khai báo kiểu dữ liệu của biến, python sẽ tự động  xác định kiểu dữ liệu của biến dựa trên giá trị được gán cho biến đó.
  2. Kiểu dữ liệu
  a) Kiểu dữ liệu số
  a1) Kiểu số nguyên (integer - int)
    - Là kiểu dữ liệu biểu diễn các số nguyên, không có phần thập phân.
    - Số nguyên int không giới hạn về giá trị, có thể là số dương, số âm hoặc số 0, nó có thể lưu giá trị nguyên rất lớn.
    - Số nguyên thường ở dạng cơ số 10, nhưng cũng có thể ở dạng cơ số 2, 8 hoặc 16.
  a2) Kiểu số thực (float)
    - Là kiểu dữ liệu biểu diễn các số thực, có phần thập phân.
    - Số thực float có thể lưu giá trị rất lớn hoặc rất nhỏ, nhưng không chính xác tuyệt đối.
    - In ra độ chính xác sau dấu phẩy:
    vd: a = 5.5562424;
      Có 3 cách:
        +) Cách 1: print('%.2f' % a) => Nên dùng
        +) Cách 2: print(round(a,2))
        +) Cách 3: print('{:.2f}'.format(a)) => Nên dùng
  a3) Kiểu số phức (complex)
    - Là kiểu dữ liệu biểu diễn các số phức, có phần thực và phần ảo.
    - Số phức complex có thể lưu giá trị rất lớn hoặc rất nhỏ, nhưng không chính xác tuyệt đối.
    - Cú pháp khai báo số phức: z = a + bj, trong đó a là phần thực, b là phần ảo và j là đơn vị ảo.
      +) Ví dụ: z = 2 + 3j
    - Cách đọc phần thực và phần ảo của số phức:
      +) z.real: đọc phần thực của số phức z => Trả về kiểu dữ liệu float
      +) z.imag: đọc phần ảo của số phức z => Trả về kiểu dữ liệu float
    - Tính module của số phức: abs(z) => Trả về kiểu dữ liệu float
  
    a4) Kiểu dữ liệu boolean (bool)
    - Là kiểu dữ liệu biểu diễn giá trị đúng hoặc sai.
    - Các giá trị true trong python là xâu khác rông, các số khác 0.

  b) Kiểu dữ liệu xâu (string - str)
    - Là kiểu dữ liệu biểu diễn các chuỗi ký tự.
    - Chuỗi ký tự trong python được đặt trong dấu nháy đơn hoặc nháy kép.
    - Chuỗi ký tự trong python có thể chứa các ký tự đặc biệt như: \n, \t, \\, \', \", ...
    - Một số phương thức xử lý chuỗi trong python:
      +) len(str): trả về độ dài của chuỗi str
      +) str.upper(): chuyển chuỗi str thành chữ hoa
      +) str.lower(): chuyển chuỗi str thành chữ thường
      +) str.strip(): loại bỏ khoảng trắng ở đầu và cuối chuỗi str
      +) str.replace(old, new): thay thế tất cả các ký tự old bằng new trong chuỗi str
      +) str.split(sep): tách chuỗi str thành một danh sách các chuỗi con dựa trên ký tự phân tách sep
      +) sep.join(list): nối các chuỗi con trong danh sách list thành một chuỗi duy nhất, các chuỗi con được phân tách bởi ký tự sep.
  c) Ép kiểu dữ liệu trong python
    - Là quá trình chuyển đổi kiểu dữ liệu của một giá trị sang kiểu dữ liệu khác.
    - Cú pháp ép kiểu dữ liệu: ten_bien = kieu_du_lieu(mot_gia_tri)
'''

#Khai báo biến và gán giá trị cho biến
x = 5
y = 5.5
name = "Hung"
print(x,y,name)
print('------------------------------')

#Làm tròn số trong python
a = 5.5562424
#Cách 1:
print('%.2f' % a)
#Cách 2:
print(round(a,2))
#Cách 3:
print('{:.2f}'.format(a))
print('------------------------------')

#Khai báo số phức trong python
z = 2 + 3j
print(z)
print('Phần thực của z:', z.real)
print('Phần ảo của z:', z.imag)
print('Module của z:{:.2f}'.format(abs(z)))
print('------------------------------')

#Kieu du lieu boolean trong python
x = 100
print(bool(x)) #True
y = 0
print(bool(y)) #False
z = ""
print(bool(z)) #False
print('------------------------------')

#Kiểu dữ liệu string trong python
name = "Hung"
print('Tôi tên là:', name)
print('Kiểu dữ liệu là:', type(name))
print('------------------------------')

#Ép kiểu dữ liệu trong python
b = 10
print('Trước khi ép kiểu:', type(b))
c = str(b)
print('Sau khi ép kiểu:', type(c))