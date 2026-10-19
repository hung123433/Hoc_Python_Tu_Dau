'''
  Bài 3: Toán tử trong python
  1. Toán tử gán
    - Cú pháp: ten_bien = gia_tri
    - Toán tử gán được sử dụng để gán giá trị cho một biến.
  2. Toán tử số học
    +: Cộng.
    -: Trừ.
    *: Nhân.
    /: Chia thập phân.
    //: Chia lấy phần nguyên.
    %: Chia lấy phần dư.
    **: Lũy thừa.
  3. Toán tử so sánh
    - ==: So sánh bằng.
    - !=: So sánh khác.
    - >: So sánh lớn hơn.
    - <: So sánh nhỏ hơn.
    - >=: So sánh lớn hơn hoặc bằng.
    - <=: So sánh nhỏ hơn hoặc bằng.
  4. Toán tử logic
    - AND: Trả về True nếu cả hai biểu thức đều đúng.
    - OR: Trả về True nếu một trong hai biểu thức đúng.
    - NOT: Đảo ngược giá trị của biểu thức.
  5. Toán tử đồng nhất
   - So sánh địa chỉ ô nhớ của biến.
   - Nếu hai cùng trỏ đến một địa chỉ nó trả về true.
   - Ngược lại chả về false.
   - Cú pháp: is, is not.
'''

#Vi du toán tử gán trong python
x = 5
z, y = 10, 15
print(x, y, z)
x ,y = y,x
print('Sau khi hoán đổi giá trị của x và y:', x, y )

#Luỹ thừa
print(2**3) #8

#Toán tử đồng nhất
a = 12
print(a is z)