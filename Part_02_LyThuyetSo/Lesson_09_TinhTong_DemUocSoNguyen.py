#Tính tổng và đếm ước của số nguyên
import math
#Ham co ban
#Độ phức tạp: O(n)
def sum_uocSoNguyen_basic(n):
  sum = 0
  for i in range(1, n + 1):
    if n % i == 0:
      sum += i
  return sum

def cnt_uocSoNguyen_basic(n):
  cnt = 0
  for i in range(1,n+1):
    if n % i == 0:
      cnt += 1
  return cnt

#Hàm nâng cao
#Độ phức tạp: O(sqrt(n))
def sum_uocSoNguyen_advance(n):
  sum = 0
  for i in range(1, math.isqrt(n) + 1):
    if n % i == 0:
      sum += i
      if i != n//i:
        sum += n//i
  return sum

def cnt_uocSoNguyen_advance(n):
  cnt = 0
  for i in range(1, math.isqrt(n)+1):
    if n % i == 0:
      cnt += 1
      if i != n//i:
        cnt += 1
  return cnt
#Chạy thử chương trình
n = int(input('Vui long nhap mot so nguyen: '))
print('Tong uoc cua so nguyen',n,'la:',sum_uocSoNguyen_advance(n))
print('Uoc cua so nguyen',n,'la:',cnt_uocSoNguyen_advance(n))