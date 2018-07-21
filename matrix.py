import random
from copy import deepcopy
class Matrix:
    def __init__(self, nrows, ncols):
        self.row=nrows
        self.col=ncols
        self.t=[[random.randint(0,9) for j in range(self.col)]for i in range(self.row)]

    def add(self, m):
        """return a new Matrix object after summation"""
        if self.row==m.row and self.col==m.col:
            C=Matrix(m.row, m.col)
            for i in range(self.row):
                for j in range(self.col):
                    C.t[i][j]=self.t[i][j]+m.t[i][j]
            return C
        else:
            return None

    def sub(self, m):
        """return a new Matrix object after substraction"""
        if self.row==m.row and self.col==m.col:
            C=Matrix(m.row, m.col)
            for i in range(m.row):
                for j in range(m.col):
                    C.t[i][j]=self.t[i][j]-m.t[i][j]
            return C
        else:
            return None
 
    def mul(self, m):
        """return a new Matrix object after multiplication"""
        if self.col==m.row:
            C=Matrix(self.row, m.col)
            for i in range(self.row):
                for j in range(m.col):
                    C.t[i][j] = 0
                    for k in range(self.col):
                        C.t[i][j] += self.t[i][k] * m.t[k][j]
            return C
        else:
            return None
    
    def transpose(self):
        """return a new Matrix object after transpose"""
        result=Matrix(self.col, self.row)
        for i in range(self.row):
            for j in range(self.col):
                result.t[j][i]=self.t[i][j]
        return result
    
    def display(self):
        """Display the content in the matrix"""
        for i in range(self.row):
            for j in range(self.col):
                 print("%4d" % self.t[i][j], end=' ')
            print()
               
while True:
    try:              
        a_row=int(input("Enter A matrix's rows: "))
        a_col=int(input("Enter A matrix's cols: "))
        b_row=int(input("Enter B matrix's rows: "))
        b_col=int(input("Enter B matrix's cols: "))
        if a_row==b_row and a_col==b_row:
            break
        else:
            print("="*30)
            print("A與B的col相等、A與B的row相等，才能跳出程式喔～")
    finally:
        A=Matrix(a_row,a_col)
        B=Matrix(b_row,b_col)
        result=Matrix(a_row,b_col)
        print("Matrix A")
        A.display()
        print("Matrix B")
        B.display()

        print("==============A+B=============")
        if A.add(B)==None:
            print("Matrix'size should be in the same size")
            pass
        else:
            A.add(B).display()

        print("==============A-B==============")
        if A.sub(B)==None:
            print("Matrix'size should be in the same size")
            pass
        else:
            A.sub(B).display()

        print("=============A*B==============")
        if A.mul(B)==None:
            print("AB矩陣相乘:A的cols需與B的rows相等")
            pass
        else:
            A.mul(B).display()
            result = A.mul(B)

        print("=====the transpose of A*B=====")
        if A.mul(B)==None:
            print("A*B已出錯，無法產生transpose of A*B")
            pass
        else:
            result.transpose().display()