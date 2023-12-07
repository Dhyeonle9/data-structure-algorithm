# 함수
def add_data(friend):
    # 1단계 빈칸추가
    katok.append(None)
    klen = len(katok)
    # 2단계 마지막칸에 대입
    katok[klen-1] = friend

def insert_data(position, friend):
    # 1단계 빈칸추가
    katok.append(None)
    klen = len(katok)
    # 자리이동 (반복)
    for i in range(klen-1, position, -1): 
        katok[i] = katok[i-1]
        katok[i-1] = None
    # 빈칸에 대입
    katok[position] = friend

def del_data(position):
    # 1단계 지우기
    katok[position] = None
    klen = len(katok)
    for i in range(position+1, klen):
        katok[i-1] = katok[i]
        katok[i] = None
    del katok[klen-1]


# 변수
katok = []

# 메인
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')

print(katok)

add_data('모모')
print(katok)

insert_data(3, '미나')
print(katok)

del_data(4)
print(katok)