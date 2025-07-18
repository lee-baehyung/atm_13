# balance : 초기 잔액을 설정하는 변수를 초기화 해주세요 
# 금액은 여러분 마음대로 설정해주세요

# 사용자로부터 atm 기계에 사용 목적에 맞는 기능을 선택 할 수 있도록
# 기능 입력을 받는 기능을 구현해주세요

balance = 10000

#무한루프? while vs for 

# while 조건 :
#     조건 만족 시키는 중

while True:
    num = input("사용하실 기능의 번호를 선택해주세요 (1.입금,  2.출금, 3.입출금내역 영수증보기, 4.종료) : ")

    if num == '4': # 4번 종료 기능
        break

    if num == '1': # 입금 기능 구현 => feat/deposit 브랜치에서 작업
       deposit_amount = int(input('입금할 금액을 입력해주세요: ')) # str:5000 -> int -> int:500
       balance += deposit_amount # balance = balance + deposit_amount
       print(f'입금하신 금액{deposit_amount}원이고, 현재 잔액은 {balance}원 입니다.')
       
    if num == '2':
        pass

    if num == '3':
        pass

print(f'서비스를 종료합니다. 현재 잔액은 {balance}')
