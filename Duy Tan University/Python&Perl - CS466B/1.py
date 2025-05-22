n = int(input("Nhập vào một số n: "))
sum = 0
for i in range(n):
	if i % 2 == 0:
		sum += i
print("Vậy tổng số chẵn từ 1 đến n là: ", sum)
