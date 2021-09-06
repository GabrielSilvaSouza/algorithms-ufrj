def recursiv(m,n,i,j):
	if i == len(m):
		print('True')
		return True
	if m[i] == n[j]:
		i += 1
		j += 1
		recursiv(m,n,i,j)
	else:
		j += 1
		if j == (len(b)-1):
			print('False')
			return False
		else:
			recursiv(m,n,i,j)
				
if __name__ == '__main__':
	a = eval(input())
	b = eval(input())
	recursiv(a,b,0,0)

	
