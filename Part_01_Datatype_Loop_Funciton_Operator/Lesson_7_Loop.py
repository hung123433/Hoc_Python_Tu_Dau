'''
  Bài 7: Vòng lặp
  1. For
    - Trong ngôn ngữ lập trình Python có chút
    khác so với các ngôn ngữ lập trình như
    C/C++, Java,...
    - Thay vì duyệt qua các giá trị số thì Python
    sẽ lặp trên các iterable (list, tuple, string,
    set...). Thứ tự duyệt sẽ theo thứ tự xuất
    hiện trong iterable. 
    => Để thực hiện vòng lặp
    for ta sử dụng built-in function là range().
    - Cú pháp:
      +) Cách 1: for [Tên_biến] in [Tập_hợp_đối_tượng]:
      +) Cách 2: HÀM RANGE()
    - Hàm range() sẽ sinh ra một dãy số -> tạo ra iterable và bạn sẽ sử dụng vòng for để duyệt qua từng số trong dãy đã sinh ra.
    -Cú pháp: range(start, stop, step)
      + start: Giá trị bắt đầu của dãy số (mặc định là 0).
      + stop: Giá trị cuối cùng của dãy số (cận này không được lấy).
      + step: Bước nhảy của dãy số (mặc định là 1).
  2. Break và continue
    - Câu lệnh break dùng để kết thúc vòng lặp ngay lập tức ngay khi gặp break => thực hiện tiếp các khối lệnh bên dưới vòng for => giống C và C++
    LƯU Ý: break thông thường sẽ đi kèm với điều kiệ
    
'''
#For
#Cách 1:
'''
names = ['Hung', 'Yen', 'Nhung', 'Ngan'];
for name in names:
  print('Ten toi la: ', name);
'''

#In số chẵn từ 0->10
#Cách 1:
for i in range(0,10,2):
  print(i, end = ' ');
print('\n');
#Cách 2:
for i in range(0,10):
  if i % 2 == 0:
    print(i, end = ' ');
print('\n');
#Vòng for lồng nhau
for i in range(3):
  for j in range(2):
    print(i,j);