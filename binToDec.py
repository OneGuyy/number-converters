def binToDeci(num):
	for i in str(num):
		if(i != "0" and i != "1"):
			print("Ce n'est pas un nombre binaire !")
			return None
	if (num <= 0):
		return 0
	else:
		numString = list(str(num))
		count = 0
		result = 0
		for i in reversed(numString):
			if(i == "1"):
				result += 2**count
			count += 1
		return result
			

#toConvert = int(input("Nombre à convertir : "))
print(convert(10))
