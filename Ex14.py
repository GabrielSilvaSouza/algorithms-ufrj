class Matrix:

    def __init__(self,v):
        self.matrix = v

    def __add__(self,other):
        resmtx = [ [ self.matrix[i][j] + other.matrix[i][j] for j in range(0,len(self.matrix)) ] for i in range(0, len(self.matrix))]
        return resmtx

    def __sub__(self, other):
        resmtx = [ [ self.matrix[i][j] - other.matrix[i][j] for j in range(0,len(self.matrix)) ] for i in range(0, len(self.matrix))]
        return resmtx

    def __mul__(self, other):
        resmtx = []
        for ii in range(0, len(self.matrix)):
            resmtx.append([0 for x in range(len(other.matrix[0]))])
        for n in range(0, len(self.matrix)):
            for m in range(0, len(other.matrix[0])): 
                for k in range(0, len(other.matrix)):
                    resmtx[n][m] = resmtx[n][m] + self.matrix[n][k]*other.matrix[k][m]
        return resmtx

    def __repr__(self):
        return repr(self.resmtx)


def turn_into_matrix(the_string):
        line, column = int(the_string[1]), int(the_string[3])
        bracket_1, bracket_2 = the_string.index('['), the_string.index(']') 
        vector = eval(the_string[bracket_1 : bracket_2+1]) 
        n = iter( [t for t in range(0,len(vector))] )
        vector  = [ [ vector[next(n)] for x in range(0, column) ] for i in range(0, line) ]
        return vector

if __name__ == '__main__':
    the_string = input()

    if ')+(' in the_string:
        the_string = the_string.split('+')
        a = Matrix(turn_into_matrix(the_string[0]))
        b = Matrix(turn_into_matrix(the_string[1]))
        print(a+b)
    
    elif ')-(' in the_string:
        the_string = the_string.split('-')
        a = Matrix(turn_into_matrix(the_string[0]))
        b = Matrix(turn_into_matrix(the_string[1]))
        print(a-b)

    elif ')*(' in the_string:
        the_string = the_string.split('*')
        a = Matrix(turn_into_matrix(the_string[0]))
        b = Matrix(turn_into_matrix(the_string[1]))
        print(a*b)

    

