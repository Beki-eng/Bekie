#연산자

print(1+1) # 2
print(3 + 4) # 7
print(3 * 5) # 15
print(3 ** 3) # 3^3 27
print(15 / 3) # 5
print(14 % 3) # 2, 나누기 구하기
print(14 // 3) # 4, 몫 구하기

print(3 == 3) # True
print(3 >= 4) # False
print(5 > 2) # True
print(3 + 4 >= 9) # False
print(3 >= 2 * 2) # False
print(5 == 2 + 3) # True
print(2 + 3 == 5) # True

print(1 != 3) #True, != 는 같지 않다 라는 뜻
print(not(1 != 3)) #False

print((3 > 0) and (3 < 5)) # True, End 게이트
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True, Or 게이트
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False