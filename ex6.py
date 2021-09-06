def matrizMenor(m, cofact):
	mat = []
	mat2 = []
	for k, linha in enumerate(m):
		if k != 0:
			mat.append(linha)
	for k, coluna in enumerate(zip(*mat)):
		if k != cofact:
			mat2.append(coluna)
			
	return mat2

def determinant(m):
	s = len(m)
	if s == 2:
		return m[0][0] * m[1][1] - m[0][1] * m[1][0]
	
	return sum((-1) ** cofact * m[0][cofact] * determinant(matrizMenor(m, cofact)) for cofact in range(s))
               
               
if __name__ == '__main__':
    mtx = eval(input())
    print(determinant(mtx))