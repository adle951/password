password = 'a123456'
result = 4
while result != 1:
	enter = input('請輸入密碼')
	if enter == password:
		result = 1
		print("登入成功")
	else:
		result = result - 1
		count = result -1 
		if count == 0:
			print('登入失敗')
			break
		print('還有%d次機會'%count)
