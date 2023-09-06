password = "a123456"
x = 0
while x < 3 :
    enter = input("請輸入密碼")

    if enter == password:
        print("登入成功")
        break
    else :
        if x < 2 :
            print(f"密碼錯誤,還有{2-x}次機會")
        else :
            print("錯誤超過三次,帳戶已鎖定")

    x += 1







