import random

from copy import deepcopy

class Matrix :
    
    def __init__(self, nrows, ncols):
        self.matrix = []
        self.nrows = nrows
        self.ncols = ncols

        for a in range (1, nrows+1) :
            for b in range (1, ncols+1) :
                integer = random.randint(0, 9)
                self.matrix.append(str(integer))
        
    def add(self, m):
        i = 0
        self.new_matrix_add = []

        while i < nrows * ncols :
            self.matrix2 = [int(i) for i in self.matrix]
            m = [int(i) for i in m]
            _add = self.matrix2[i] + m[i]
            self.new_matrix_add.append(str(_add))
            i = i + 1

        print ('-------- A + B --------')

        if self.nrows != nrows :
            print ('Error')
        elif self.ncols != ncols :
            print ('Error')
        elif self.ncols == ncols and self.nrows == nrows :
            for c in range (0, nrows) :
                for d in range (0, ncols) :
                    if 0 <= int(self.new_matrix_add[ncols * c + d]) < 10 :
                        print (str('   '), self.new_matrix_add[ncols * c + d], end = ' ')
                    elif 10 <= int(self.new_matrix_add[ncols * c + d]) < 100 :
                        print (str('  '), self.new_matrix_add[ncols * c + d], end = ' ')
                    elif 10 <= int(self.new_matrix_add[ncols * c + d]) < 100 :
                        print (str(' '), self.new_matrix_add[ncols * c + d], end = ' ')
                print ('')

    def sub(self, m):
        j = 0
        self.new_matrix_sub = []
        while j < nrows * ncols :
            self.matrix3 = [int(j) for j in self.matrix]
            m = [int(j) for j in m]
            _sub = self.matrix3[j] - m[j]
            self.new_matrix_sub.append(str(_sub))
            j = j + 1
        
        print ('-------- A - B --------')

        if self.nrows != nrows :
            print ('Error')
        elif self.ncols != ncols :
            print ('Error')
        elif self.ncols == ncols and self.nrows == nrows :
            for c in range (0, nrows) :
                for d in range (0, ncols) :
                    if -99 <= int(self.new_matrix_sub[ncols * c + d]) < -9 :
                        print (str(' '), self.new_matrix_sub[ncols * c + d], end = ' ')
                    elif -9 <= int(self.new_matrix_sub[ncols * c + d]) < 0 :
                        print (str('  '), self.new_matrix_sub[ncols * c + d], end = ' ')
                    elif 0 <= int(self.new_matrix_sub[ncols * c + d]) < 10 :
                        print (str('   '), self.new_matrix_sub[ncols * c + d], end = ' ')
                    elif 10 <= int(self.new_matrix_add[ncols * c + d]) < 100 :
                        print (str('  '), self.new_matrix_sub[ncols * c + d], end = ' ')
                    elif 10 <= int(self.new_matrix_add[ncols * c + d]) < 100 :
                        print (str(' '), self.new_matrix_sub[ncols * c + d], end = ' ')
                print ('')

    def mul(self, m):
        A = 0
        self.new_matrix_mul = []
        for n in range (0, ncols) :
            k = 0
            for l in range (0, ncols) :
                for k in range (0, nrows) :
                    self.matrix4 = [int(k) for k in self.matrix]
                    m = [int(k) for k in m]
                    _mul = self.matrix4[k + n * nrows] * m[k * ncols + l]
                    A = A + _mul
                
                self.new_matrix_mul.append(A)
                A = 0

        print ('-------- A * B --------')

        if len(self.new_matrix_mul) == ncols ** 2 :
            for c in range (0, ncols) :
                for d in range (0, ncols) :
                    if 0 <= self.new_matrix_mul[ncols * c + d] < 10 :
                        print (str('   ') + str(self.new_matrix_mul[ncols * c + d]) , end = ' ')
                    elif self.new_matrix_mul[ncols * c + d] < 100 :
                        print (str('  ') + str(self.new_matrix_mul[ncols * c + d]) , end = ' ')
                    elif self.new_matrix_mul[ncols * c + d] >= 100 :
                        print (str(' ') + str(self.new_matrix_mul[ncols * c + d]), end = ' ')
                print ('')
       
    def transpose(self):
        i = 0
        self.new_matrix_transpose = []
        for p in range (0, ncols) :
            for o in range (0, ncols * ncols) :
                if o % ncols == p and o % (ncols+1) != 0 :
                    self.new_matrix_transpose.append(self.new_matrix_mul[o])

        for o in range (0, ncols * ncols) :
            if o % (ncols+1) == 0 :
                self.new_matrix_transpose.insert((o), self.new_matrix_mul[o])
                i = i + 1
        
        print ('---- the transpose of A * B ----')

        if len(self.new_matrix_transpose) == ncols ** 2 :
            for c in range (0, ncols) :
                for d in range (0, ncols) :
                    if 0 <= self.new_matrix_transpose[ncols * c + d] < 10 :
                        print (str('  '), str(self.new_matrix_transpose[ncols * c + d]), end = ' ')
                    if 10 <= self.new_matrix_transpose[ncols * c + d] < 100 :
                        print (str(' '), str(self.new_matrix_transpose[ncols * c + d]), end = ' ')
                    elif self.new_matrix_transpose[ncols * c + d] >= 100 :
                        print (str(''), str(self.new_matrix_transpose[ncols * c + d]), end = ' ')
                print ('')

    def display(self):
        """Display the content in the matrix"""
            
        print ('Matrix ',  ' (', self.nrows, ',', self.ncols, ')')

        for c in range (0, self.nrows) :
            for d in range (0, self.ncols) :
                print (self.matrix[self.ncols * c + d], end = ' ')
            print ('')
        
nrows = int(input ('Enter A matrix rows = '))
ncols = int(input ('Enter A matrix cols = '))
A = Matrix(nrows, ncols)
A.display()
nrows = int(input ('Enter B matrix rows = '))
ncols = int(input ('Enter B matrix cols = '))
B = Matrix(nrows, ncols)
B.display()
A.add(B.matrix)
A.sub(B.matrix)
A.mul(B.matrix)
A.transpose()