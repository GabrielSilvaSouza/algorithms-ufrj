def size_number(number):
	number = str(number)
	number = list(number)
	counter = 0
	for i in number:
		counter += 1
	return counter
		
		
def inverter(number):
	number = str(number)
	number = list(number)
	number.reverse()
	number = [str(n) for n in number]
	number = int(''.join(number))
	return number

if __name__ == '__main__':
	number = int(input())
	a = size_number(number)
	b = inverter(number)
	l = []
	l.append(a)
	l.append(b)
	print(tuple(l))