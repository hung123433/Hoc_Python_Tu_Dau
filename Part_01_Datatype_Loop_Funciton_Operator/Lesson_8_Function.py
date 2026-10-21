'''
  Bài 8: Function trong python
  - Cú pháp: 
      def [name] ([Tham_so_truyen_vao]):
        #Code
      (return)
'''
#Hàm không có kiểu trả về
def printHello():
  print('Hello World');


#Hàm có giá trị trả về
def soLonHon(a,b):
  if(a < b):
    return b;
  else:
    return a;
print('So lon nhat trong hai so la: ', soLonHon(20,10));