def deciToHex(digit):
	dictHex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10:'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
	reste = 0
	resultat = ''
	while(digit != 0):
		resultat += dictHex.get(digit % 16)
		digit = digit // 16
	return "0b" + resultat[::-1]

def hexToDeci(num):
	dictToDeci = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A':10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
	resultat = 0
	num = num[::-1]
	for i in range(len(num)):
		resultat += dictToDeci.get(num[i])*16**i
	return resultat

def deciToHexRecur(x, resultat = '', dictHex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10:'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}):
	if x == 0: return "0x" + resultat[::-1]
	else: return deciToHexRecur(x//16, resultat + dictHex.get(x%16))

print(deciToHex(4791))
print(deciToHexRecur(4791))
print(hexToDeci("12B7"))
