def recursiv(m,n,i):

		
	if m[i] == n[i]:
		print('True')
		
	else:

		i += 1
		if i == (len(a)-1) or i == (len(b)-1):
			print('False')
		else:
			recursiv(m,n,i)
				

if __name__ == '__main__':
	i = 0
	a = eval(input())
	b = eval(input())
	recursiv(a,b,i)