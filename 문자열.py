# name = '홍길동'

# 데이터 출력시 % 기호 입력방법
name = '승현'

print('안녕하세요. 저의 이름은 %s입니다.'%name)


number = 10000
print('입력하신 금액은 %d원입니다.'%number)

# 문자열 슬라이싱
자유로운_문자열 = '만들었습니다요'
print(len(자유로운_문자열))
print(자유로운_문자열[-1])

#문자열 치환 replace

date = '2024,07,04'
print("바꾸기 전", date)
date = date.replace(',', '-')
print('바꾼 후' , date)

