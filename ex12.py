def search(v,x,j,i):
	m = int((i+j)/2)
	if i > j:
		print(-1)
		return -1
	if v[m] < x:
		i = m + 1
		search(v,x,j,i)
		
	elif v[m] > x:
		j = m - 1
		search(v,x,j,i)
		
	elif v[m] == x:
		print(m)
		return m

if __name__ == '__main__':
    v = eval(input())
    x = int(input())
    search(v,x,len(v)-1,0)