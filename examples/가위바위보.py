# 랜덤 함수를 사용하여 가위바위보 게임을 작성하시오
# 사용자가 입력한 가위, 바위 보 중 하나와 컴퓨터가 랜덤으로 선택한 
# 가위바위보를 비교하여 승패  결정하기
import random
com=random.choice(['가위','바위','보'])
hu=input('무엇을 낼 것인가요?')
print(com)
if com==hu:
    print('비겼다')
    
elif (com=='가위' and hu=='보') or \
    (com=='보' and hu=='바위') or \
    (com=='바위' and hu=='가위'):
        print('졌다')

else:
    print('이겼다')
    