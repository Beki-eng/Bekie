# 랜덤 함수
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성(난수 생성)
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성성
print(int(random() * 10)) # 0 ~ 10 미만의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성성
# # 이렇게 6번 반복하면 임의의 값 6개를 뽑아서 로또번호 생성 가능

print(randrange(1, 46)) # 1 ~ 45 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 45 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 45 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 45 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 45 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 45 미만의 임의의 값 생성
# # randrange 함수를 사용해서 작성도 가능

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# randint 1 ~ 45 이하로 생성 가능능