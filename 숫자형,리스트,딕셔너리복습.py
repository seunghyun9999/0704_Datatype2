num_1 = 1
num_2 = '2'

number = [0,1,2,3,4,5,6,7,8,9]

# 수열 만드는 함수는 range
# 나열해주는 함수는 list
r = list(range(10))
print(r)

t = list(range(0,10,2))
# (시작, 끝, 증가치)

# append 리스트에 요소 추가하는 함수
r.append(13)
print(r)

# remove 삭제하는 함수
r.remove(3)
print(r)


dic= {'전승현' : 26, '홍길동': 30}
print(dic['전승현'])
#키 찾는법
print(dic.keys())

if 1==1 : print('집에 가자')