'''
  Bài 6: Cấu trúc rẽ nhánh
  1. Câu lệnh if
  - Các câu lệnh bên trong if phải thụt so với if.
  - Có nhiều câu lệnh if thì cũng thụt lề như vậy.
  - Cú pháp:
    +) if [điều_kiện]:
      #các câu lệnh
  - Phần [điều_kiện] có thể kết hợp các toán tử logic.
  - Nếu điều kiện đúng thì các câu lệnh bên dưới if được thực thi.
  - Nếu điều kiện sai thì các câu lệnh bên dưới không được thực thi.
  2. Câu lệnh else
  - Cú pháp:
    +) if [điều_kiện]:
        #các câu lệnh
      else:
        #các câu lệnh
  3. Câu lệnh elif
  - Cú pháp:
    +)  if [điều_kiện]:
            #các câu lệnh
        elif [điều_kiện]:
            #các câu lệnh
        else:
            #các câu lệnh
  4. Toán tử 3 ngôi
  - Cú pháp:
    +) variable = True stament if conditon else False stament
          
    
'''

#Ví dụ kiểm tra số n có nằm trong đoạn từ 0 đên 10 ?
'''
  n = int(input('Vui lòng nhập số n:'));
  if(n >= 0) and (n < 10):
    print('Số n có nằm trong đoạn từ 0 đến 10')
'''

#Ví dụ if - else
#Kiểm tra bạn có trên 18 tuổi không
age = int(input('Nhap so tuoi cua ban:'));
if(age >= 18):
  print('Ban da 18 tuoi');
else:
  print('Ban chua du 18 tuoi');

#Toán tử 3 ngôi
a,b = 10,20
c = a if a > b else b
print(c)