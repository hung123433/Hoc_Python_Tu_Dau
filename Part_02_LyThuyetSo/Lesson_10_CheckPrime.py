#Kiểm tra số nguyên tố
import math
#Cơ bản
#Độ phức tạp:O(n)
def basic_checkPrime(n):
  for i in range(2,n):
    if n % i == 0:
      return False
  return True

#Hàm nâng cao
#Độ phức tạp: O(sqrt(n))
def advance_checkPrime(n):
  if n < 2:
    return False
  for i in range(2,math.isqrt(n)+1):
    if n % i == 0:
      return False
  return True  
#Hàm main
n = int(input('Nhập số nguyên n: '))
if advance_checkPrime(n):
  print('Đây là số nguyên tố')
else:
  print('Đây không phải là số nguyên tố')