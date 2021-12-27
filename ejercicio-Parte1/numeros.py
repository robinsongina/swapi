for i in range(101):
	print(i, end=" ")
	if i%2 == 0:
		print("buzz", end=" ")
	if i%5 == 0:
		print("bazz", end=" ")
	print("")