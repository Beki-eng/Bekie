#슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7]) # 컴퓨터는 시작을 0으로 시작, 그렇기에 9는 0번째 자리, 1은 7번째 자리가 됨
print("연 : " + jumin[0:2]) # 0번째부터 2 "직전" 까지 (0, 1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒷자리 : ",jumin[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 뒤에서 7번째부터 끝까지



