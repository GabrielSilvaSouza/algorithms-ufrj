def lines(l):
	check = []
	for k in range(0,len(l)-1):
		check.append(sum(l[k]))
	x = check[0]
	for a in check:
		if a != x:
			return 0
	return check[0]
	
def columns(l):
	check = []
	counter = 0
	for k in range(0,len(l)):
		for i in range(0, len(l)):
			counter += l[k][i]
		check.append(counter)
		counter = 0
	x = check[0]
	for a in check:
		if a != x:
			return 0
	return check[0]

def main_diagonal(l):
	counter = 0
	i = 0
	for k in range(0, len(l)):
		counter += l[k][i]
		i += 1
	return counter

def lazy_diagonal(l):
	counter = 0
	i = len(l)-1
	for k in reversed(range(0, len(l))):
		counter += l[k][i]
		i -= 1
	return counter

if __name__ == '__main__':
	l = eval(input())
	if len(l) == 1:
		print('True')
		exit()
	p,q,r,s = lines(l), columns(l), main_diagonal(l), lazy_diagonal(l)
	if p == r == s == q:
		print('True')
	else:
		print('False')