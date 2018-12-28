import random

ans = random.randint(1, 100)

while True:
    x = int(input('請猜一ㄍ數字: '))
    if x == ans:
        print('終於猜對了!')
        break
    elif x > ans:
        print('比答案大喔！')
    else:
        print('比答案小喔！')