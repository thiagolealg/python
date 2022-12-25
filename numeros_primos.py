def is_prime(num):
    if num %2 == 0 and num!=2 or num %3 == 0 and num!=3 or num %5 == 0 and num!=5:
        return False
    else:
        return True


for i in range(1, 100):
	if is_prime(i + 1):
			print(i + 1, end=" ")
