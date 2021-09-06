def n1(mtx):
	return mtx[0][0]

def n2(mtx2):
	return (mtx2[0][0]*mtx2[1][1] - mtx2[0][1]*mtx2[1][0]) 


def n3(mtx3):
	a = mtx3[0][0]*mtx3[1][1]*mtx3[2][2] #AEI
	
	b = mtx3[0][1]*mtx3[1][2]*mtx3[2][0] #BFG
	
	c = mtx3[0][2]*mtx3[1][0]*mtx3[2][1] #CDH
	
	d = mtx3[0][0]*mtx3[1][2]*mtx3[2][1] #AFH
	
	e = mtx3[0][1]*mtx3[1][0]*mtx3[2][2] #BDI
	
	f = mtx3[0][2]*mtx3[1][1]*mtx3[2][0] #CEG
		
	return ((a+b+c)-(d+e+f))

if __name__ == '__main__':
	matriz = eval(input())

	if len(matriz) == 1:
		print(n1(matriz))
	elif len(matriz) == 2:
		print(n2(matriz))
	elif len(matriz) == 3:
		print(n3(matriz))